Name:
NetID: 

What we should know about your submission:

## Q2.4: Tracking behavior (10 points)
### Why does the end-effector orientation not match the target orientation? How could we modify the controller to also track the target orientation?
The desired velocity only seeks to track the desired position, not the desired orientation. The orientation part of the error is ignored in the control law, so the end-effector does not attempt to align its orientation with that of the target.

We would need to use the orientation Jacobian (which maps angular velocities to changes in orientation) and include the orientation error in the control law. This would involve computing the orientation error (e.g., using quaternions or rotation matrices) and then applying a similar proportional control strategy to minimize this error, in addition to the position error.

### Describe the behavior of the arm for different values of `Kp`. In particular, describe what happens when `Kp` is very small (e.g., `Kp=0.1`) and when `Kp` is large (e.g., `Kp=50.0`).
When `Kp` is very small (e.g., `Kp=0.1`), the arm moves very slowly and may not reach the target position in a reasonable time. The low gain results in a weak response to the position error, causing the arm to be sluggish and unresponsive.

When `Kp` is large (e.g., `Kp=50.0`), the arm responds quickly to position errors and can reach the target position more rapidly. However, a very high gain can cause jitters and, ultimately, destabilize this simple kinematic sim.