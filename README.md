# gazebo_tools

## Description

This is a ros package that summarizes gazebo-related nodes.



## Contents

### scripts/gazebo_tf_publisher.py

This node publish model pose as tf using gazebo information. It requires to running gazebo.

#### Subscribe

- gazebo model topic : gazebo_msgs/ModelStates

#### Broadcast

- tf



### launch/gazebo_tf_publisher.launch

This launch file launches `gazebo_tf_publisher.py`.

#### Parameters

- model_name : gazebo model name*
- base_frame_id : frame_id of model
- global_frame_id : frame_id of global coordinates

*You can get gazebo model name from `/gazebo/model_states` topic, for example following.

```
rostopic echo /gazebo/model_states
```



## Usage

```
roslaunch gazebo_tools gazebo_tf_publisher.launch model_name:="robot" base_frame_id:="/robot" global_frame_id:="/map"
```
