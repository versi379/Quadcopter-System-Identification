; Auto-generated. Do not edit!


(cl:in-package drone_controller-srv)


;//! \htmlinclude GoToPoint-request.msg.html

(cl:defclass <GoToPoint-request> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass GoToPoint-request (<GoToPoint-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoToPoint-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoToPoint-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<GoToPoint-request> is deprecated: use drone_controller-srv:GoToPoint-request instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <GoToPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:pose-val is deprecated.  Use drone_controller-srv:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoToPoint-request>) ostream)
  "Serializes a message object of type '<GoToPoint-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoToPoint-request>) istream)
  "Deserializes a message object of type '<GoToPoint-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoToPoint-request>)))
  "Returns string type for a service object of type '<GoToPoint-request>"
  "drone_controller/GoToPointRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoToPoint-request)))
  "Returns string type for a service object of type 'GoToPoint-request"
  "drone_controller/GoToPointRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoToPoint-request>)))
  "Returns md5sum for a message object of type '<GoToPoint-request>"
  "92c8a5b2a2eede8ea83a1f79297fcf35")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoToPoint-request)))
  "Returns md5sum for a message object of type 'GoToPoint-request"
  "92c8a5b2a2eede8ea83a1f79297fcf35")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoToPoint-request>)))
  "Returns full string definition for message of type '<GoToPoint-request>"
  (cl:format cl:nil "geometry_msgs/PoseStamped pose    		# Position of the goal~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoToPoint-request)))
  "Returns full string definition for message of type 'GoToPoint-request"
  (cl:format cl:nil "geometry_msgs/PoseStamped pose    		# Position of the goal~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoToPoint-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoToPoint-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GoToPoint-request
    (cl:cons ':pose (pose msg))
))
;//! \htmlinclude GoToPoint-response.msg.html

(cl:defclass <GoToPoint-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GoToPoint-response (<GoToPoint-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoToPoint-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoToPoint-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<GoToPoint-response> is deprecated: use drone_controller-srv:GoToPoint-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <GoToPoint-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:ack-val is deprecated.  Use drone_controller-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoToPoint-response>) ostream)
  "Serializes a message object of type '<GoToPoint-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoToPoint-response>) istream)
  "Deserializes a message object of type '<GoToPoint-response>"
    (cl:setf (cl:slot-value msg 'ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoToPoint-response>)))
  "Returns string type for a service object of type '<GoToPoint-response>"
  "drone_controller/GoToPointResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoToPoint-response)))
  "Returns string type for a service object of type 'GoToPoint-response"
  "drone_controller/GoToPointResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoToPoint-response>)))
  "Returns md5sum for a message object of type '<GoToPoint-response>"
  "92c8a5b2a2eede8ea83a1f79297fcf35")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoToPoint-response)))
  "Returns md5sum for a message object of type 'GoToPoint-response"
  "92c8a5b2a2eede8ea83a1f79297fcf35")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoToPoint-response>)))
  "Returns full string definition for message of type '<GoToPoint-response>"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoToPoint-response)))
  "Returns full string definition for message of type 'GoToPoint-response"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoToPoint-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoToPoint-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GoToPoint-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GoToPoint)))
  'GoToPoint-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GoToPoint)))
  'GoToPoint-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoToPoint)))
  "Returns string type for a service object of type '<GoToPoint>"
  "drone_controller/GoToPoint")