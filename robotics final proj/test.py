from interbotix_xs_modules.arm import InterbotixManipulatorXS
import math
import rospy
import numpy as np
import modern_robotics as mr
from interbotix_xs_sdk.msg import *
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from interbotix_common_modules import angle_manipulation as ang
from interbotix_xs_modules import mr_descriptions as mrd
from interbotix_xs_modules.core import InterbotixRobotXSCore
from interbotix_xs_modules.gripper import InterbotixGripperXSInterface
# This script commands some arbitrary positions to the arm joints
#
# To get started, open a terminal and type...
# 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250s'
# Then change to this directory and type 'python joint_position_control.py'

def main():
    # joint_positions = [-1.0, 0.5 , 0.5, 0, -0.5, 1.57]
    bot = InterbotixManipulatorXS("wx250s", "arm", "gripper")
    joint_states = [bot.arm.core.joint_states.position[bot.arm.core.js_index_map[name]] for name in bot.arm.group_info.joint_names]
    print(joint_states)

if __name__=='__main__':
    main()