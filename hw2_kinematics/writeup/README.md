# Homework 2: 
Q1.1 

derivation for xt and yt:

![xtyt_derivation](xtyt_derivation.jpg)

Q1.3 

matching output in Figure 2:

![rollout_plot](rollout_plot.png)

Q1.5 

With parameter vel_std: 0.05; alpha_std: 0.10; x_std: 0.012; y_std: 0.012; theta_std: 0.05, I successfully generated similar output plot in Figure 3 and 4.
Question: Why does the motion model produce more particles within 10 cm of the deterministic model prediction in Figure 3 than in Figure 4?

Figure 3 corresponds to a small steering angle (α ≈ 0.34 rad) and shorter duration (Δt = 0.1 s). Because the car travels almost straight and for a short time, small perturbations in control inputs (v,α) cause only minor deviations. Both action noise and model noise have limited time to accumulate, so nearly all particles remain close to the deterministic trajectory — producing a tight cluster where almost 100 % of the samples lie within 10 cm of the mean.

![model_para_1](model_para_1.png)


Figure 4, on the other hand, uses a larger steering angle (α = 0.4 rad) and longer duration (Δt = 0.5 s). Here, small differences in α translate to noticeably different turning radii, so each particle follows a slightly different arc. Over time, these curvature differences amplify, spreading particles along a banana-shaped curve. As a result, fewer particles remain close to the deterministic prediction — only ~18 % fall within 10 cm of the mean.


![model_para_2](model_para_2.png)


Q2.4

1. The end-effector orientation does not match because the controller tracks position only using the 3x6 position Jacobian J_pos. No rotational error is commanded, so orientation is free in the null space. To track orientation, add a rotational term (quaternion error) and solve with the 6x6 geometric Jacobian: q_dot = J_geo [v_des_G; w_des_G].

2. With small Kp the arm moves slowly, lags the figure-8 movement pattern, and can show steady-state position error. With large Kp the arm reacts quickly, reducing lag, but it tends to overshoot and oscillate; joint rates can saturate and the solution becomes sensitive near singularities. 