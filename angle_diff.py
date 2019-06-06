def reward_function(params):

    ###############################################################################
    '''
    Example of using waypoints and heading to make the car in the right direction
    '''

    import math

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    head = params['heading']

    # Initialize the reward with typical value
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    w1 = waypoints[closest_waypoints[0]]
    w2 = waypoints[closest_waypoints[1]]
    w3 = waypoints[closest_waypoints[1] + 1]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    dir1 = math.atan2(w2[1] - w1[1], w2[0] - w1[0])
    # Convert to degree
    dir1 = math.degrees(dir1)
    # Calculate the difference between the track direction and the heading direction of the car
    diff1 = abs(dir1 - head)

     # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    dir2 = math.atan2(w2[1] - w3[1], w2[0] - w3[0])
    # Convert to degree
    dir2 = math.degrees(track_direction)
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff2 = abs(track_direction2 - track_direction)

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return reward
