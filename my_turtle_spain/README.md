# my_turtle_spain
Turtlebot differential drive robot simulation in rviz. Turtlebot receives command velocity, computes inverse kinematics and publish wheel rotation. 

### System Setup
MacPro
Parallels VM running ROS Kinetic on Ubunutu 16.04.


### Compilation and Testing

To stage Turtlebot run:
```
$ roslaunch turtlebot_stage turtlebot_in_stage.launch
```
To use ```rosrun ``` place the code below in your ``` .bashrc ```
```
$ source ~/catkin_ws/devel/setup.bash
```
catkin_ws is your ROS workspace.

I used  ```demo ``` to move turtlebot in ```rviz``` without running  ``` Move_Turtle ```

### Run Move_Turtle

To move the turtle forward run:
```
$ rosrun my_turtle_spain Listen_Turtle.py
```

### Run Listen_Turtle
```
rosrun my_turtle_spain Move_Turtle.py
```

### Observations
- Publishers and subscribers can be used as a convienent way of sending messages on topics relevant to behavior and telemetry of the robot.
