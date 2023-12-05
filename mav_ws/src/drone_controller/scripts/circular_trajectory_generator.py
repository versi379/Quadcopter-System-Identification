#! /usr/bin/env python3
import rospy
import tf2_ros as tf2
import numpy as np
from geometry_msgs.msg import PoseStamped

if __name__ == "__main__":
    rospy.init_node("trajectory_generator", anonymous=False)
    global_name = "/drone_controller"

    # Tf
    world_frame = rospy.get_param("{}/world_frame".format(global_name))
    drone_frame = rospy.get_param("{}/drone_frame".format(global_name))
    tf_buffer = tf2.Buffer()
    tf_listener = tf2.TransformListener(tf_buffer)

    # Publisher
    trajectory_publisher = rospy.Publisher("/move_base_simple/goal".format(global_name), PoseStamped, queue_size=1)

    fs = 15
    dt = 1 / fs
    rate = rospy.Rate(fs)

    # Circular Trajecotry Parameters
    phi = (np.pi / 2)
    a = 0.2
    tc = 6
    t = 0

    # Init
    try:
        transform = tf_buffer.lookup_transform(world_frame, drone_frame, rospy.Time(0), rospy.Duration(5))
    except tf2.LookupException:
        print("ERROR: No transformation between {} and {}. Cannot initialize the node. Exiting...".format(
            drone_frame, world_frame))
        exit(-1)

    init_pose = np.array([transform.transform.translation.x,
                          transform.transform.translation.y,
                          transform.transform.translation.z])

    while not rospy.is_shutdown():
        # Set point
        set_point_x = a * np.cos(2 * np.pi * (1 / tc) * t + phi) - a * np.cos(phi) + init_pose[0]
        set_point_y = a * np.sin(2 * np.pi * (1 / tc) * t + phi) - a * np.sin(phi) + init_pose[1]
        set_point_z = init_pose[2]

        msg = PoseStamped()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = world_frame
        msg.pose.position.x = set_point_x
        msg.pose.position.y = set_point_y
        msg.pose.position.z = set_point_z
        msg.pose.orientation.w = 1

        trajectory_publisher.publish(msg)

        t += dt

        rate.sleep()
