def reward_function(params):
    '''
    Calculates the difference between the car's heading and the ideal heading based on the two
    closest waypoints. Either punishes or rewards the car based on the difference.
    '''

    import math

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    head = params['heading']

    # Initialize the reward with typical value 
    reward = 1.0

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
    reward = (90 - diff1) / 90  # Range of -1 to 1
    
    return reward
