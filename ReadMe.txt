Deepracer ReadMe.txt

Reward Function: So far, we've determined 3 features to reinforce for thd deepracer model; Angle difference, turning speed, and turning side.
The idea is that each feature calculates it's own reinforcement value (*reward/punishment*) based on prefered behaviors --> then the values from each 
section are added together makeup the total reinforcement. 

Reinforcement Value: The range of values for each feature is from [0.0 - 2.0] 
For the total addition, this makes 0.0 the least and 6.0 the most (for now with three features)

Angle Diff: 

Turning Speed: 

Turning Side: 

