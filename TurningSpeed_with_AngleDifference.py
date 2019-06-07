
def reward_function(params):

    # initialization
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']
    head = params['heading']

    reward1 = 1e-3
    reward2 = 1e-3
    #reward3 = 1e-3

    # Multi_feature_reinforcement

    # TURNING SPEED 

    # fetches the 3 closest waypoints 
    w1 = waypoints[closest_waypoints[0]]
    w2 = waypoints[closest_waypoints[1]]
    w3 = waypoints[(closest_waypoints[1] + 1) % len(waypoints)]
    
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

    reward1 = float((ratio1)*(rewardAmnt)) 

    # ANGLE DIFFERENCE 

    '''
    Calculates the difference between the car's heading and the ideal heading based on the two
    closest waypoints. Either punishes or rewards the car based on the difference.
    '''

    # Calculate the direction of the center line based on the closest waypoint
    # and the waypoint 3 after that

    w1 = waypoints[closest_waypoints[0]]
    w2 = waypoints[(closest_waypoints[0] + 2) % len(waypoints)]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    dir1 = math.atan2(w2[1] - w1[1], w2[0] - w1[0]) 

    # Convert to degree
    dir1 = math.degrees(dir1)


    # Calculate the difference between the track direction and the heading direction of the car
    diff1 = abs(dir1 - head)

    if diff1 > 180:
        diff1 = 360 - diff1

    # Calculate reinforcement reward/punishment
    reward2 = (90 - diff1) / 90  # Range of -1 to 1

    total_reward = reward1 + reward2

    if total_reward<-1.6: total_reward = -4.0
    elif total_reward>1.6: total_reward = 4.0


    return(total_reward)
    


