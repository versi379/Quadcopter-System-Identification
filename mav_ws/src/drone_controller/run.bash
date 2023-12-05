#!/bin/bash

source /opt/ros/noetic/setup.bash
source /catkin_ws/devel/setup.bash

roslaunch drone_controller drone_controller_no_gui.launch
