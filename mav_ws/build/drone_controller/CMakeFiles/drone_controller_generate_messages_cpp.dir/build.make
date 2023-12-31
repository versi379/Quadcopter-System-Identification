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

# Utility rule file for drone_controller_generate_messages_cpp.

# Include the progress variables for this target.
include CMakeFiles/drone_controller_generate_messages_cpp.dir/progress.make

CMakeFiles/drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/TakeOff.h
CMakeFiles/drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/Land.h
CMakeFiles/drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h
CMakeFiles/drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoHome.h


/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/TakeOff.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/TakeOff.h: /home/giovanni/mav_ws/src/drone_controller/srv/TakeOff.srv
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/TakeOff.h: /opt/ros/noetic/share/gencpp/msg.h.template
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/TakeOff.h: /opt/ros/noetic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from drone_controller/TakeOff.srv"
	cd /home/giovanni/mav_ws/src/drone_controller && /home/giovanni/mav_ws/build/drone_controller/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/giovanni/mav_ws/src/drone_controller/srv/TakeOff.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller -e /opt/ros/noetic/share/gencpp/cmake/..

/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/Land.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/Land.h: /home/giovanni/mav_ws/src/drone_controller/srv/Land.srv
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/Land.h: /opt/ros/noetic/share/gencpp/msg.h.template
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/Land.h: /opt/ros/noetic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating C++ code from drone_controller/Land.srv"
	cd /home/giovanni/mav_ws/src/drone_controller && /home/giovanni/mav_ws/build/drone_controller/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/giovanni/mav_ws/src/drone_controller/srv/Land.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller -e /opt/ros/noetic/share/gencpp/cmake/..

/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /home/giovanni/mav_ws/src/drone_controller/srv/GoToPoint.srv
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/geometry_msgs/msg/PoseStamped.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/std_msgs/msg/Header.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/geometry_msgs/msg/Point.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/geometry_msgs/msg/Quaternion.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/geometry_msgs/msg/Pose.msg
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/gencpp/msg.h.template
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h: /opt/ros/noetic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating C++ code from drone_controller/GoToPoint.srv"
	cd /home/giovanni/mav_ws/src/drone_controller && /home/giovanni/mav_ws/build/drone_controller/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/giovanni/mav_ws/src/drone_controller/srv/GoToPoint.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller -e /opt/ros/noetic/share/gencpp/cmake/..

/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoHome.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoHome.h: /home/giovanni/mav_ws/src/drone_controller/srv/GoHome.srv
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoHome.h: /opt/ros/noetic/share/gencpp/msg.h.template
/home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoHome.h: /opt/ros/noetic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/giovanni/mav_ws/build/drone_controller/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Generating C++ code from drone_controller/GoHome.srv"
	cd /home/giovanni/mav_ws/src/drone_controller && /home/giovanni/mav_ws/build/drone_controller/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/giovanni/mav_ws/src/drone_controller/srv/GoHome.srv -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -p drone_controller -o /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller -e /opt/ros/noetic/share/gencpp/cmake/..

drone_controller_generate_messages_cpp: CMakeFiles/drone_controller_generate_messages_cpp
drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/TakeOff.h
drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/Land.h
drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoToPoint.h
drone_controller_generate_messages_cpp: /home/giovanni/mav_ws/devel/.private/drone_controller/include/drone_controller/GoHome.h
drone_controller_generate_messages_cpp: CMakeFiles/drone_controller_generate_messages_cpp.dir/build.make

.PHONY : drone_controller_generate_messages_cpp

# Rule to build all files generated by this target.
CMakeFiles/drone_controller_generate_messages_cpp.dir/build: drone_controller_generate_messages_cpp

.PHONY : CMakeFiles/drone_controller_generate_messages_cpp.dir/build

CMakeFiles/drone_controller_generate_messages_cpp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/drone_controller_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/drone_controller_generate_messages_cpp.dir/clean

CMakeFiles/drone_controller_generate_messages_cpp.dir/depend:
	cd /home/giovanni/mav_ws/build/drone_controller && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/giovanni/mav_ws/src/drone_controller /home/giovanni/mav_ws/src/drone_controller /home/giovanni/mav_ws/build/drone_controller /home/giovanni/mav_ws/build/drone_controller /home/giovanni/mav_ws/build/drone_controller/CMakeFiles/drone_controller_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/drone_controller_generate_messages_cpp.dir/depend

