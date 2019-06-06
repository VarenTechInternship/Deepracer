def reward_function(params):

    
    # initialization
    import math
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    speed = params['speed']

    reward = 1.0 # make sure that thos value is a FLOAT

    if closest_waypoints[1] + 1 < len(waypoints):
    
        # fetches the 3 closest waypoints
        w1 = waypoints[closest_waypoints[0]]
        w2 = waypoints[closest_waypoints[1]]
        w3 = waypoints[closest_waypoints[1] + 1]
    
        # calculates waypoint vectors
        
        u = [w2[0] - w1[0], w2[1] - w1[1]]
        v = [w3[0] - w2[0], w3[1] - w2[1]]
    
        # calculates vectors lengths then computes dot product
        # to derive angle between them --> now we have the magnitude of the 'curve'
        ulen = ((u[0]**2) + (u[1]**2)) ** (1/2)
        vlen = ((v[0]**2) + (v[1]**2)) ** (1/2)
        udotprodv = (u[0]*v[0]) + (u[1]*v[1])
    
        # calculates the magnitude angle between waypoint vectors
        curve = math.degrees(math.acos(udotprodv/(ulen*vlen))) # amazing
        if curve>180 and curve<=360: curve -= 180 # compensates for angles over 180 degrees
    
        # This ratios the curve range to the reward range
        # and determines how closely the preferred speed aligns with the curve
    
        # range parameters
        curveMin = 135
        curveMax = 180
        speedMin = 0.8
        speedMax = 4.0
        rewardAmnt = 2.0 # rewards and punishes from 0.0-2.0
        curvePercent = (curveMax-curve/curveMax-curveMin)
        speedPercent = (speedMax-speed/speedMax-speedMin)
    
        
        if curvePercent<speedPercent: 
            ratio1 = curvePercent / speedPercent
        elif speedPercent<curvePercent:
            ratio1 = speedPercent / curvePercent
        else: ratio1 = 0
    
        reward = float((ratio1)*(rewardAmnt)-1)
    
    return reward