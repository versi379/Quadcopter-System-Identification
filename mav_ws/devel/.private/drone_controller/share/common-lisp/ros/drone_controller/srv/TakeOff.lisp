; Auto-generated. Do not edit!


(cl:in-package drone_controller-srv)


;//! \htmlinclude TakeOff-request.msg.html

(cl:defclass <TakeOff-request> (roslisp-msg-protocol:ros-message)
  ((altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0))
)

(cl:defclass TakeOff-request (<TakeOff-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TakeOff-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TakeOff-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<TakeOff-request> is deprecated: use drone_controller-srv:TakeOff-request instead.")))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <TakeOff-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:altitude-val is deprecated.  Use drone_controller-srv:altitude instead.")
  (altitude m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TakeOff-request>) ostream)
  "Serializes a message object of type '<TakeOff-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'altitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TakeOff-request>) istream)
  "Deserializes a message object of type '<TakeOff-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TakeOff-request>)))
  "Returns string type for a service object of type '<TakeOff-request>"
  "drone_controller/TakeOffRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TakeOff-request)))
  "Returns string type for a service object of type 'TakeOff-request"
  "drone_controller/TakeOffRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TakeOff-request>)))
  "Returns md5sum for a message object of type '<TakeOff-request>"
  "e548720c10b5dd4b7a5994bbd3ec2c39")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TakeOff-request)))
  "Returns md5sum for a message object of type 'TakeOff-request"
  "e548720c10b5dd4b7a5994bbd3ec2c39")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TakeOff-request>)))
  "Returns full string definition for message of type '<TakeOff-request>"
  (cl:format cl:nil "float32 altitude    		# altitude to take off the drone~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TakeOff-request)))
  "Returns full string definition for message of type 'TakeOff-request"
  (cl:format cl:nil "float32 altitude    		# altitude to take off the drone~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TakeOff-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TakeOff-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TakeOff-request
    (cl:cons ':altitude (altitude msg))
))
;//! \htmlinclude TakeOff-response.msg.html

(cl:defclass <TakeOff-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass TakeOff-response (<TakeOff-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TakeOff-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TakeOff-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<TakeOff-response> is deprecated: use drone_controller-srv:TakeOff-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <TakeOff-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:ack-val is deprecated.  Use drone_controller-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TakeOff-response>) ostream)
  "Serializes a message object of type '<TakeOff-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TakeOff-response>) istream)
  "Deserializes a message object of type '<TakeOff-response>"
    (cl:setf (cl:slot-value msg 'ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TakeOff-response>)))
  "Returns string type for a service object of type '<TakeOff-response>"
  "drone_controller/TakeOffResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TakeOff-response)))
  "Returns string type for a service object of type 'TakeOff-response"
  "drone_controller/TakeOffResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TakeOff-response>)))
  "Returns md5sum for a message object of type '<TakeOff-response>"
  "e548720c10b5dd4b7a5994bbd3ec2c39")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TakeOff-response)))
  "Returns md5sum for a message object of type 'TakeOff-response"
  "e548720c10b5dd4b7a5994bbd3ec2c39")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TakeOff-response>)))
  "Returns full string definition for message of type '<TakeOff-response>"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TakeOff-response)))
  "Returns full string definition for message of type 'TakeOff-response"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TakeOff-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TakeOff-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TakeOff-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TakeOff)))
  'TakeOff-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TakeOff)))
  'TakeOff-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TakeOff)))
  "Returns string type for a service object of type '<TakeOff>"
  "drone_controller/TakeOff")