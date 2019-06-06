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

    # Calculate the direction of the center line based on the closest waypoints
    w1 = waypoints[closest_waypoints[0]]
    w2 = waypoints[closest_waypoints[1]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    dir1 = math.atan2(w2[1] - w1[1], w2[0] - w1[0])
    # Convert to degree
    dir1 = math.degrees(dir1)

    # Calculate the difference between the track direction and the heading direction of the car
    diff1 = abs(dir1 - head)
    if diff1 > 180:
        diff1 = 360 - diff1

    # Calculate reinforcement reward/punishment
    reward1 = (180-diff)/150
    return reward1
