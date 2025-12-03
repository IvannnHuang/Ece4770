[INFO] [1764789331.591584]: Pausing the particle filter.
Picking up tray...
Traceback (most recent call last):
  File "/home/qh229/homework_ws/devel/lib/arm_final_project/airport", line 15, in <module>
    exec(compile(fh.read(), python_script, 'exec'), context)
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 124, in <module>
    airport.plan_and_execute("pickup_tray")
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 95, in plan_and_execute
    self.bot.arm.core.robot_write_trajectory("group", "arm", "position", raw_traj)
  File "/home/qh229/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/src/interbotix_xs_modules/core.py", line 141, in robot_write_trajectory
    for key, value in point.items():
AttributeError: 'tuple' object has no attribute 'items'