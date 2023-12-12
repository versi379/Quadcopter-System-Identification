; Auto-generated. Do not edit!


(cl:in-package drone_controller-srv)


;//! \htmlinclude Land-request.msg.html

(cl:defclass <Land-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Land-request (<Land-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Land-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Land-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<Land-request> is deprecated: use drone_controller-srv:Land-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <Land-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:data-val is deprecated.  Use drone_controller-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Land-request>) ostream)
  "Serializes a message object of type '<Land-request>"
  (cl:let* ((signed (cl:slot-value msg 'data)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Land-request>) istream)
  "Deserializes a message object of type '<Land-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Land-request>)))
  "Returns string type for a service object of type '<Land-request>"
  "drone_controller/LandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Land-request)))
  "Returns string type for a service object of type 'Land-request"
  "drone_controller/LandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Land-request>)))
  "Returns md5sum for a message object of type '<Land-request>"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Land-request)))
  "Returns md5sum for a message object of type 'Land-request"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Land-request>)))
  "Returns full string definition for message of type '<Land-request>"
  (cl:format cl:nil "int8 data    		# integer with a flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Land-request)))
  "Returns full string definition for message of type 'Land-request"
  (cl:format cl:nil "int8 data    		# integer with a flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Land-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Land-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Land-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude Land-response.msg.html

(cl:defclass <Land-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Land-response (<Land-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Land-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Land-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name drone_controller-srv:<Land-response> is deprecated: use drone_controller-srv:Land-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <Land-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader drone_controller-srv:ack-val is deprecated.  Use drone_controller-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Land-response>) ostream)
  "Serializes a message object of type '<Land-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Land-response>) istream)
  "Deserializes a message object of type '<Land-response>"
    (cl:setf (cl:slot-value msg 'ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Land-response>)))
  "Returns string type for a service object of type '<Land-response>"
  "drone_controller/LandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Land-response)))
  "Returns string type for a service object of type 'Land-response"
  "drone_controller/LandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Land-response>)))
  "Returns md5sum for a message object of type '<Land-response>"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Land-response)))
  "Returns md5sum for a message object of type 'Land-response"
  "cbb2fae3170f584c2b25f43322fecf10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Land-response>)))
  "Returns full string definition for message of type '<Land-response>"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Land-response)))
  "Returns full string definition for message of type 'Land-response"
  (cl:format cl:nil "bool ack 			# acknowledged information~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Land-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Land-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Land-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Land)))
  'Land-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Land)))
  'Land-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Land)))
  "Returns string type for a service object of type '<Land>"
  "drone_controller/Land")