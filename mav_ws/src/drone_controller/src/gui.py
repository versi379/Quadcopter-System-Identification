#! /usr/bin/env python3
import rospy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.config import Config
from drone_controller.srv import TakeOff, Land, GoToPoint, GoHome
from geometry_msgs.msg import PoseStamped
from tf import transformations
import math
import rospkg
import os
import signal


class DroneApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        signal.signal(signal.SIGINT, self.handler_sigint)

        # GUI Properties
        rospack = rospkg.RosPack()
        package_path = rospack.get_path('drone_controller')
        self.screen = Builder.load_file("drone_gui.kv")
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '400')
        Config.write()

        # Services
        global_name = "/drone_controller"
        self.take_off_service = rospy.ServiceProxy("{}/take_off".format(global_name), TakeOff)
        self.land_service = rospy.ServiceProxy("{}/land".format(global_name), Land)
        self.go_home_service = rospy.ServiceProxy("{}/go_home".format(global_name), GoHome)
        self.go_to_point_service = rospy.ServiceProxy("{}/go_to_point".format(global_name), GoToPoint)

    def handler_sigint(self, signum, frame):
        self.stop()

    def build(self):
        return self.screen

    def take_off(self, *args):
        try:
            altitude = float(self.screen.ids.take_off_text.text)
        except ValueError:
            self.screen.ids.log_label.text = "You must insert a float Value in the 'Take Off Meters' field."
            return

        try:
            result = self.take_off_service.call(altitude=altitude)
        except rospy.service.ServiceException as e:
            self.screen.ids.log_label.text = str(e)
            print(str(e))
            return

        ack = result.ack
        self.screen.ids.log_label.text = str(ack)

        if ack:
            self.screen.ids.take_off_button.md_bg_color = 1, 0, 0, 1
            self.screen.ids.land_button.md_bg_color = 0, 1, 0, 1
            self.screen.ids.go_home_button.md_bg_color = 0, 1, 0, 1
            self.screen.ids.go_to_point_button.md_bg_color = 0, 1, 0, 1

    def go_home(self, *args):
        try:
            result = self.go_home_service.call(data=0)
        except rospy.service.ServiceException as e:
            self.screen.ids.log_label.text = str(e)
            print(str(e))
            return

        ack = result.ack
        self.screen.ids.log_label.text = str(ack)

    def land(self, *args):
        try:
            result = self.land_service.call(data=0)
        except rospy.service.ServiceException as e:
            self.screen.ids.log_label.text = str(e)
            print(str(e))
            return

        ack = result.ack
        self.screen.ids.log_label.text = str(ack)

        if ack:
            self.screen.ids.take_off_button.md_bg_color = 0, 1, 0, 1
            self.screen.ids.land_button.md_bg_color = 1, 0, 0, 1
            self.screen.ids.go_home_button.md_bg_color = 1, 0, 0, 1
            self.screen.ids.go_to_point_button.md_bg_color = 1, 0, 0, 1

    def go_to_point(self, *args):
        frame = self.screen.ids.go_to_point_frame_text.text
        try:
            x = float(self.screen.ids.go_to_point_x_text.text)
            y = float(self.screen.ids.go_to_point_y_text.text)
            z = float(self.screen.ids.go_to_point_z_text.text)
            yaw = float(self.screen.ids.go_to_point_yaw_text.text)
        except ValueError:
            self.screen.ids.log_label.text = "You must insert a float Value in the 'X' 'Y' 'Z' 'YAW' fields."
            return

        data = PoseStamped()
        data.header.stamp = rospy.Time.now()
        data.header.frame_id = frame

        data.pose.position.x = x
        data.pose.position.y = y
        data.pose.position.z = z
        qx, qy, qz, qw = transformations.quaternion_from_euler(0, 0, math.radians(yaw))

        data.pose.orientation.x = qx
        data.pose.orientation.y = qy
        data.pose.orientation.z = qz
        data.pose.orientation.w = qw

        try:
            result = self.go_to_point_service.call(pose=data)
        except rospy.service.ServiceException as e:
            self.screen.ids.log_label.text = str(e)
            print(str(e))
            return

        ack = result.ack
        self.screen.ids.log_label.text = str(ack)


if __name__ == "__main__":
    rospy.init_node("simple_gui", anonymous=False)
    drone_app = DroneApp()
    drone_app.run()
