#!/usr/bin/env python

from __future__ import print_function
import time
import rospy
import rospkg
import numpy as np
from planning.roadmap import Roadmap
from planning.problems import JointSpace
from arm_final_project.init_env import Env
from planning.samplers import ArmRandomSampler
from arm_controller.pid_controller import PIDController
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_xs_sdk.msg import *
from arm_state_estimation.tracker import CylinderTracker
from planning.search import ASTARPlanner
from planning.problems import JointSpace
from planning.samplers import ArmRandomSampler
from planning.roadmap import Roadmap
from arm_final_project.planning_context import Widowx250ArmPlanning

class Airport(object):
    def __init__(self):
        extents = np.array([[-3.14, 3.14], [-1.88, 1.99], [-2.15, 1.61], [-3.14, 3.14], [-1.75, 2.15], [-3.14, 3.14]])
        sampler = ArmRandomSampler(extents = extents)
        rospack = rospkg.RosPack()
        map_path = rospack.get_path('arm_final_project')
        problem = JointSpace()
        self.planning_context = Widowx250ArmPlanning()
        self.rm = Roadmap(problem, sampler, 20000, connection_radius=2.5, saveto=map_path+"/map/roadmap_joint_space_final_new_env.pkl")
        self.astar_planner = ASTARPlanner(self.rm)
        self.bot = InterbotixManipulatorXS("wx250s", "arm", "gripper")
        self.pid_controller = PIDController(self.bot)
        self.ct = CylinderTracker()
        self.AIRPORT_POS_DICT = self.planning_context.AIRPORT_POS_DICT

    def extract_plan(self, vpath):
        plan = []
        for i in vpath:
            plan.append(self.rm.vertices[i])
        return np.array(plan)

    def plan_and_execute(self, goal_name, detected_goal=None):
        '''
        Input:
            goal_name (string): 
                key value in AIRPORT_POS_DICT
        '''
        goal = np.array(self.AIRPORT_POS_DICT[goal_name], dtype=float)
        if goal_name.split('_')[0] == "pickup" and detected_goal is not None:
            goal[1] = detected_goal

        ### BEGIN SOLUTION

        # ---- 1. Compute IK → q_goal (first 6 joints)
        q_goal_full = self.planning_context.compute_ik(goal)
        if q_goal_full is None:
            print("[ERROR] IK failed for goal:", goal_name)
            return
        q_goal = np.asarray(q_goal_full[:6], dtype=float).reshape(6)

        # ---- 2. Get current joint values
        try:
            q_start = np.asarray(self.pid_controller.get_current_joints()[:6],
                                 dtype=float).reshape(6)
        except:
            q_start = np.asarray(self.pid_controller.current_position[:6],
                                 dtype=float).reshape(6)

        # ---- 3. Insert start node
        start_id = self.rm.add_node(q_start, is_start=True)

        # ---- 4. Insert goal node
        goal_id = self.rm.add_node(q_goal, is_start=False)

        ### END SOLUTION

        vpath, _ = self.astar_planner.Plan(start_id, goal_id)
        plan = self.extract_plan(vpath)

        #### BEGIN SOLUTION, let the pid_controller execute the plan ####

        # Interbotix expects: raw_traj = [ {time: [positions]}, ... ]
        raw_traj = []
        t = 0.0
        dt = 2.0   # seconds per waypoint (you can reduce later)

        for q in plan:
            t += dt
            q_list = [float(val) for val in q]  # must be a flat list of floats
            raw_traj.append({ t: q_list })      # dict: {time : [positions]}
        #### END SOLUTION ####

        self.bot.arm.core.robot_write_trajectory("group", "arm", "position", raw_traj)
        t = list(raw_traj[-1].keys())[0]
        time.sleep(t)

        if goal_name.split('_')[0] == "dropoff":
            rospy.set_param('object', 'none')
            self.planning_context.publish_dummy_marker()
        if goal_name.split('_')[0] == "pickup":
            rospy.set_param('object', goal_name.split('_')[1])
            airport.ct.pause_pf()
        return 

if __name__ == "__main__":
    try:
        print("")
        print("----------------------------------------------------------")
        print("Welcome to Corneller Airport, Time: 5/07/2051")
        print("----------------------------------------------------------")
        print("Press Ctrl-D to exit at any time")
        print("")
        print("Initialize Security Robot... ...")
        airport = Airport()
        airport.ct.pause_pf()
        
        env = Env(0.1, shape="tray")
        env.publish_obj()

        ###### BEGIN SOLUTION, PICKUP and DROPOFF TRAY #######
        print("Picking up tray...")
        airport.plan_and_execute("pickup_tray")

        print("Dropping off tray...")
        airport.plan_and_execute("dropoff_tray")
        ###### END SOLUTION #######
  
        airport.planning_context.publish_tray_marker()

        airport.ct.resume_pf()
        env = Env(-0.04, shape="can")
        env.publish_obj()

        time.sleep(1)
        ##### BEGIN SOLUTION, get y value of the position of the can from the particle filter####
        can_position = airport.planning_context.package_location_y
        print("Detected can Y-position:", can_position)
        ##### END SOLUTION #####

        if can_position + 0.04 < 0.4:
            ###### BEGIN SOLUTION, PICKUP CAN #######
            print("can localization success, particle filter accurate.")           
            airport.plan_and_execute("pickup_can", detected_goal=can_position)
            airport.plan_and_execute("dropoff_can")
            ###### END SOLUTION #######
        else:
            print("can localization failed, particle filter inaccurate.")
            exit(1)

  
        time.sleep(1)
        airport.ct.resume_pf()
        env = Env(-0.086, shape="wallet")
        env.publish_obj()

        time.sleep(1)
        ##### BEGIN SOLUTION, get y value of the position of the wallet from the particle filter####
        #### Hint: the y value is stored in  airport.planning_context.package_location_y
        wallet_position = airport.planning_context.package_location_y
        print("Detected wallet Y-position:", wallet_position)
        ###### END SOLUTION #######

        if wallet_position + 0.086 < 0.4:
            ###### BEGIN SOLUTION, PICKUP WALLET #######
            print("wallet localization success, particle filter accurate.")           
            airport.plan_and_execute("pickup_wallet", detected_goal=wallet_position)
            airport.plan_and_execute("dropoff_wallet")
            ###### END SOLUTION #######
        else:
            print("wallet localization failed, particle filter inaccurate.")
            exit(1)

    except rospy.ROSInterruptException:
        exit(1)
    except KeyboardInterrupt:
        exit(1)