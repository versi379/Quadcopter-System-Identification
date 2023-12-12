;; Auto-generated. Do not edit!


(when (boundp 'drone_controller::GoToPoint)
  (if (not (find-package "DRONE_CONTROLLER"))
    (make-package "DRONE_CONTROLLER"))
  (shadow 'GoToPoint (find-package "DRONE_CONTROLLER")))
(unless (find-package "DRONE_CONTROLLER::GOTOPOINT")
  (make-package "DRONE_CONTROLLER::GOTOPOINT"))
(unless (find-package "DRONE_CONTROLLER::GOTOPOINTREQUEST")
  (make-package "DRONE_CONTROLLER::GOTOPOINTREQUEST"))
(unless (find-package "DRONE_CONTROLLER::GOTOPOINTRESPONSE")
  (make-package "DRONE_CONTROLLER::GOTOPOINTRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass drone_controller::GoToPointRequest
  :super ros::object
  :slots (_pose ))

(defmethod drone_controller::GoToPointRequest
  (:init
   (&key
    ((:pose __pose) (instance geometry_msgs::PoseStamped :init))
    )
   (send-super :init)
   (setq _pose __pose)
   self)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/PoseStamped _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/PoseStamped _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/PoseStamped _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(defclass drone_controller::GoToPointResponse
  :super ros::object
  :slots (_ack ))

(defmethod drone_controller::GoToPointResponse
  (:init
   (&key
    ((:ack __ack) nil)
    )
   (send-super :init)
   (setq _ack __ack)
   self)
  (:ack
   (&optional (__ack :null))
   (if (not (eq __ack :null)) (setq _ack __ack)) _ack)
  (:serialization-length
   ()
   (+
    ;; bool _ack
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _ack
       (if _ack (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _ack
     (setq _ack (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass drone_controller::GoToPoint
  :super ros::object
  :slots ())

(setf (get drone_controller::GoToPoint :md5sum-) "92c8a5b2a2eede8ea83a1f79297fcf35")
(setf (get drone_controller::GoToPoint :datatype-) "drone_controller/GoToPoint")
(setf (get drone_controller::GoToPoint :request) drone_controller::GoToPointRequest)
(setf (get drone_controller::GoToPoint :response) drone_controller::GoToPointResponse)

(defmethod drone_controller::GoToPointRequest
  (:response () (instance drone_controller::GoToPointResponse :init)))

(setf (get drone_controller::GoToPointRequest :md5sum-) "92c8a5b2a2eede8ea83a1f79297fcf35")
(setf (get drone_controller::GoToPointRequest :datatype-) "drone_controller/GoToPointRequest")
(setf (get drone_controller::GoToPointRequest :definition-)
      "geometry_msgs/PoseStamped pose    		# Position of the goal

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
---
bool ack 			# acknowledged information
")

(setf (get drone_controller::GoToPointResponse :md5sum-) "92c8a5b2a2eede8ea83a1f79297fcf35")
(setf (get drone_controller::GoToPointResponse :datatype-) "drone_controller/GoToPointResponse")
(setf (get drone_controller::GoToPointResponse :definition-)
      "geometry_msgs/PoseStamped pose    		# Position of the goal

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
---
bool ack 			# acknowledged information
")



(provide :drone_controller/GoToPoint "92c8a5b2a2eede8ea83a1f79297fcf35")


