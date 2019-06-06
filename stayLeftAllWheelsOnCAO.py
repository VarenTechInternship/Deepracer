 # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    #stay to the left side of the track always
    #track is counterclockwise
    #punish wheels off the track; reward is left of center

    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']

    position = ((track_width/2.0) - distance_from_center) / (track_width/2.0)

    if all_wheels_on_track: #when it is on the track it measures percent it is from the center
    	if is_left_of_center:
    		if position >= 0.5 and position <=1.0:
    			reward = position * track_width
    		elif position < 0.5 and position >= 0.10:
		    	reward = 0.5 * position * track_width
	    	else:
	    		reward = -1 * track_width
    	else:
	    	if position >= 0.5 and position <=1.0:
		    	reward = -0.2 * position * track_width
	    	elif position < 0.5 and position >= 0.15:
	    		reward = -0.5 * position * track_width
	    	else:
		    	reward = -1 * track_width
		
    else:
    	reward *= -1.5
    
    
    return float(reward)