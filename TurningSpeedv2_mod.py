def reward_function(params):

    
    # initialization
    import math
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    speed = params['speed']
    reward = 1.0

    if closest_waypoints[1] + 1 < len(waypoints):
    
        # fetches the 3 closest waypoints
        w1 = waypoints[closest_waypoints[0]]
        w2 = waypoints[closest_waypoints[1]]
        w3 = waypoints[closest_waypoints[1] + 1]
    
        waypoint_vec1_angle = math.atan2(w2[1] - w1[1], w2[0] - w1[0]) 
        waypoint_vec2_angle = math.atan2(w3[1] - w2[1], w3[0] - w2[0]) 
        # Convert to degree
        waypoint_vec1_angle = math.degrees(waypoint_vec1_angle)
        waypoint_vec2_angle = math.degrees(waypoint_vec2_angle)

        turn_angle = (180-waypoint_vec2_angle) + waypoint_vec1_angle
        if (turn_angle>180) and (turn_angle<=360): turn_angle = 360 - turn_angle

        # now we ratio the curve range to the reward range
        # determines how close the preferred speed aligns with the curve
        turnMin = 135
        turnMax = 180
        speedMin = 0.8
        speedMax = 4.0
        rewardAmnt = 2.0
        turnPercent = (turnMax-turn_angle/turnMax-turnMin)
        speedPercent = (speedMax-speed/speedMax-speedMin)
    
        if turnPercent<speedPercent: 
            ratio1 = turnPercent / speedPercent
        elif speedPercent<turnPercent:
            ratio1 = speedPercent / turnPercent
        else: ratio1 = 1
    
        reward = float((ratio1)*(rewardAmnt))
    
    return reward