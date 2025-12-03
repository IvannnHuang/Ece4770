Traceback (most recent call last):
  File "/opt/ros/noetic/lib/python3/dist-packages/rospy/topics.py", line 882, in publish
    self.impl.publish(data)
  File "/opt/ros/noetic/lib/python3/dist-packages/rospy/topics.py", line 1066, in publish
    serialize_message(b, self.seq, message)
  File "/opt/ros/noetic/lib/python3/dist-packages/rospy/msg.py", line 152, in serialize_message
    msg.serialize(b)
  File "/home/qh229/interbotix_ws/devel/lib/python3/dist-packages/interbotix_xs_sdk/msg/_JointTrajectoryCommand.py", line 151, in serialize
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
  File "/opt/ros/noetic/lib/python3/dist-packages/genpy/message.py", line 393, in _check_types
    check_type(n, t, getattr(self, n))
  File "/opt/ros/noetic/lib/python3/dist-packages/genpy/message.py", line 324, in check_type
    check_type('%s.%s' % (field_name, n), t, getattr(field_val, n))
  File "/opt/ros/noetic/lib/python3/dist-packages/genpy/message.py", line 314, in check_type
    check_type(field_name + '[]', base_type, v)
  File "/opt/ros/noetic/lib/python3/dist-packages/genpy/message.py", line 324, in check_type
    check_type('%s.%s' % (field_name, n), t, getattr(field_val, n))
  File "/opt/ros/noetic/lib/python3/dist-packages/genpy/message.py", line 312, in check_type
    raise SerializationError('field %s must be a list or tuple type' % field_name)
genpy.message.SerializationError: field traj.points[].positions must be a list or tuple type

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/qh229/homework_ws/devel/lib/arm_final_project/airport", line 15, in <module>
    exec(compile(fh.read(), python_script, 'exec'), context)
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 125, in <module>
    airport.plan_and_execute("pickup_tray")
  File "/home/qh229/homework_ws/src/final_projects-main/arm_final_project/scripts/airport", line 96, in plan_and_execute
    self.bot.arm.core.robot_write_trajectory("group", "arm", "position", raw_traj)
  File "/home/qh229/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/src/interbotix_xs_modules/core.py", line 150, in robot_write_trajectory
    self.pub_traj.publish(msg)
  File "/opt/ros/noetic/lib/python3/dist-packages/rospy/topics.py", line 886, in publish
    raise ROSSerializationException(str(e))
rospy.exceptions.ROSSerializationException: field traj.points[].positions must be a list or tuple type