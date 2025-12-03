[INFO] [1764789984.472472]: Pausing the particle filter.
Picking up tray...
[INFO] [1764790006.700456]: Pausing the particle filter.
Dropping off tray...
[INFO] [1764790016.348819]: Resuming the particle filter.
Detected can Y-position: [-0.02910603 -0.02910603 -0.02910603 -0.03492724 -0.03492724 -0.03201663
 -0.03492724 -0.03492724 -0.03201663 -0.02910603]
Traceback (most recent call last):
  File "/home/qh229/homework_ws/devel/lib/arm_final_project/airport", line 15, in <module>
    exec(compile(fh.read(), python_script, 'exec'), context)
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 141, in <module>
    if can_position + 0.04 < 0.4:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()