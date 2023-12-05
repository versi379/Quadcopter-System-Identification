FROM ros:noetic

RUN apt update && \
    apt install -y python3-pip ros-noetic-mavros ros-noetic-tf ros-noetic-tf2-geometry-msgs  && \
    ./opt/ros/noetic/lib/mavros/install_geographiclib_datasets.sh

WORKDIR /catkin_ws/src/drone_controller
COPY ./ ./
WORKDIR /catkin_ws

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && catkin_make"

WORKDIR /launch_scripts
COPY ./run.bash ./

RUN ["chmod", "+x", "/launch_scripts/run.bash"]
RUN ["chmod", "+x", "/catkin_ws/src/drone_controller/src/controller.py"]
ENTRYPOINT ["/launch_scripts/run.bash"]

