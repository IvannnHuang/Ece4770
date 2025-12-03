Traceback (most recent call last):
  File "/home/qh229/homework_ws/devel/lib/arm_final_project/airport", line 15, in <module>
    exec(compile(fh.read(), python_script, 'exec'), context)
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 128, in <module>
    airport.plan_and_execute("pickup_tray")
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 99, in plan_and_execute
    self.bot.arm.core.robot_write_trajectory("group", "arm", "position", raw_traj)
  File "/home/qh229/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/src/interbotix_xs_modules/core.py", line 147, in robot_write_trajectory
    traj_point.time_from_start = rospy.Duration.from_sec(key)
  File "/opt/ros/noetic/lib/python3/dist-packages/genpy/rostime.py", line 86, in from_sec
    secs = int(float_secs)
ValueError: invalid literal for int() with base 10: 'time'