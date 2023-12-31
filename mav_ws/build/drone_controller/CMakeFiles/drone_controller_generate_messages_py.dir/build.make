# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/giovanni/mav_ws/src/drone_controller

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/giovanni/mav_ws/build/drone_controller

# Utility rule file for drone_controller_generate_messages_py.

# Include the progress variables for this target.
include CMakeFiles/drone_controller_generate_messages_py.dir/progress.make

CMakeFiles/drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_TakeOff.py
CMakeFiles/drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_Land.py
CMakeFiles/drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py
CMakeFiles/drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoHome.py
CMakeFiles/drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py


/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_TakeOff.py: /opt/ros/noetic/lib/genpy/gensrv_py.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_TakeOff.py: /home/giovanni/mav_ws/src/drone_controller/srv/TakeOff.srv
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating Python code from SRV drone_controller/TakeOff"
	catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/genpy/cmake/../../../lib/genpy/gensrv_py.py /home/giovanni/mav_ws/src/drone_controller/srv/TakeOff.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv

/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_Land.py: /opt/ros/noetic/lib/genpy/gensrv_py.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_Land.py: /home/giovanni/mav_ws/src/drone_controller/srv/Land.srv
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating Python code from SRV drone_controller/Land"
	catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/genpy/cmake/../../../lib/genpy/gensrv_py.py /home/giovanni/mav_ws/src/drone_controller/srv/Land.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv

/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /opt/ros/noetic/lib/genpy/gensrv_py.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /home/giovanni/mav_ws/src/drone_controller/srv/GoToPoint.srv
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /opt/ros/noetic/share/geometry_msgs/msg/PoseStamped.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /opt/ros/noetic/share/std_msgs/msg/Header.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /opt/ros/noetic/share/geometry_msgs/msg/Point.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /opt/ros/noetic/share/geometry_msgs/msg/Quaternion.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py: /opt/ros/noetic/share/geometry_msgs/msg/Pose.msg
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating Python code from SRV drone_controller/GoToPoint"
	catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/genpy/cmake/../../../lib/genpy/gensrv_py.py /home/giovanni/mav_ws/src/drone_controller/srv/GoToPoint.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv

/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoHome.py: /opt/ros/noetic/lib/genpy/gensrv_py.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoHome.py: /home/giovanni/mav_ws/src/drone_controller/srv/GoHome.srv
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Generating Python code from SRV drone_controller/GoHome"
	catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/genpy/cmake/../../../lib/genpy/gensrv_py.py /home/giovanni/mav_ws/src/drone_controller/srv/GoHome.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv

/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py: /opt/ros/noetic/lib/genpy/genmsg_py.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_TakeOff.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_Land.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py
/home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoHome.py
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Generating Python srv __init__.py for drone_controller"
	catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/genpy/cmake/../../../lib/genpy/genmsg_py.py -o /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv --initpy

drone_controller_generate_messages_py: CMakeFiles/drone_controller_generate_messages_py
drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_TakeOff.py
drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_Land.py
drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoToPoint.py
drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/_GoHome.py
drone_controller_generate_messages_py: /home/giovanni/mav_ws/devel/.private/drone_controller/lib/python3/dist-packages/drone_controller/srv/__init__.py
drone_controller_generate_messages_py: CMakeFiles/drone_controller_generate_messages_py.dir/build.make

.PHONY : drone_controller_generate_messages_py

# Rule to build all files generated by this target.
CMakeFiles/drone_controller_generate_messages_py.dir/build: drone_controller_generate_messages_py

.PHONY : CMakeFiles/drone_controller_generate_messages_py.dir/build

CMakeFiles/drone_controller_generate_messages_py.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/drone_controller_generate_messages_py.dir/cmake_clean.cmake
.PHONY : CMakeFiles/drone_controller_generate_messages_py.dir/clean

CMakeFiles/drone_controller_generate_messages_py.dir/depend:
	cd /home/giovanni/mav_ws/build/drone_controller && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/giovanni/mav_ws/src/drone_controller /home/giovanni/mav_ws/src/drone_controller /home/giovanni/mav_ws/build/drone_controller /home/giovanni/mav_ws/build/drone_controller /home/giovanni/mav_ws/build/drone_controller/CMakeFiles/drone_controller_generate_messages_py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/drone_controller_generate_messages_py.dir/depend

