; Auto-generated. Do not edit!


(cl:in-package drone_controller-srv)


;//! \htmlinclude GoHome-request.msg.html

(cl:defclass <GoHome-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:fixnum
    :initform 0))
)

(cl:defclass GoHome-request (<GoHome-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoHome-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoHome-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<GoHome-request> is deprecated: use drone_controller-srv:GoHome-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <GoHome-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:data-val is deprecated.  Use drone_controller-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoHome-request>) ostream)
  "Serializes a message object of type '<GoHome-request>"
  (cl:let* ((signed (cl:slot-value msg 'data)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoHome-request>) istream)
  "Deserializes a message object of type '<GoHome-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoHome-request>)))
  "Returns string type for a service object of type '<GoHome-request>"
  "drone_controller/GoHomeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoHome-request)))
  "Returns string type for a service object of type 'GoHome-request"
  "drone_controller/GoHomeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoHome-request>)))
  "Returns md5sum for a message object of type '<GoHome-request>"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoHome-request)))
  "Returns md5sum for a message object of type 'GoHome-request"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoHome-request>)))
  "Returns full string definition for message of type '<GoHome-request>"
  (cl:format cl:nil "int8 data    		# integer with a flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoHome-request)))
  "Returns full string definition for message of type 'GoHome-request"
  (cl:format cl:nil "int8 data    		# integer with a flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoHome-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoHome-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GoHome-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude GoHome-response.msg.html

(cl:defclass <GoHome-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GoHome-response (<GoHome-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoHome-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoHome-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<GoHome-response> is deprecated: use drone_controller-srv:GoHome-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <GoHome-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:ack-val is deprecated.  Use drone_controller-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoHome-response>) ostream)
  "Serializes a message object of type '<GoHome-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoHome-response>) istream)
  "Deserializes a message object of type '<GoHome-response>"
    (cl:setf (cl:slot-value msg 'ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoHome-response>)))
  "Returns string type for a service object of type '<GoHome-response>"
  "drone_controller/GoHomeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoHome-response)))
  "Returns string type for a service object of type 'GoHome-response"
  "drone_controller/GoHomeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoHome-response>)))
  "Returns md5sum for a message object of type '<GoHome-response>"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoHome-response)))
  "Returns md5sum for a message object of type 'GoHome-response"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoHome-response>)))
  "Returns full string definition for message of type '<GoHome-response>"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoHome-response)))
  "Returns full string definition for message of type 'GoHome-response"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoHome-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoHome-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GoHome-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GoHome)))
  'GoHome-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GoHome)))
  'GoHome-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoHome)))
  "Returns string type for a service object of type '<GoHome>"
  "drone_controller/GoHome")