from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
turn(1)
distance=20
for n in range(0, distance):
    move()
    
 turn(1)
distance=10
for n in range(0, distance):
    move()   