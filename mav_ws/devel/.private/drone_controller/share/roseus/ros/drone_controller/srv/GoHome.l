;; Auto-generated. Do not edit!


(when (boundp 'drone_controller::GoHome)
  (if (not (find-package "DRONE_CONTROLLER"))
    (make-package "DRONE_CONTROLLER"))
  (shadow 'GoHome (find-package "DRONE_CONTROLLER")))
(unless (find-package "DRONE_CONTROLLER::GOHOME")
  (make-package "DRONE_CONTROLLER::GOHOME"))
(unless (find-package "DRONE_CONTROLLER::GOHOMEREQUEST")
  (make-package "DRONE_CONTROLLER::GOHOMEREQUEST"))
(unless (find-package "DRONE_CONTROLLER::GOHOMERESPONSE")
  (make-package "DRONE_CONTROLLER::GOHOMERESPONSE"))

(in-package "ROS")





(defclass drone_controller::GoHomeRequest
  :super ros::object
  :slots (_data ))

(defmethod drone_controller::GoHomeRequest
  (:init
   (&key
    ((:data __data) 0)
    )
   (send-super :init)
   (setq _data (round __data))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; int8 _data
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _data
       (write-byte _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _data
     (setq _data (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _data 127) (setq _data (- _data 256)))
   ;;
   self)
  )

(defclass drone_controller::GoHomeResponse
  :super ros::object
  :slots (_ack ))

(defmethod drone_controller::GoHomeResponse
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

(defclass drone_controller::GoHome
  :super ros::object
  :slots ())

(setf (get drone_controller::GoHome :md5sum-) "cbb2fae3170f584c2b25f43322fecf10")
(setf (get drone_controller::GoHome :datatype-) "drone_controller/GoHome")
(setf (get drone_controller::GoHome :request) drone_controller::GoHomeRequest)
(setf (get drone_controller::GoHome :response) drone_controller::GoHomeResponse)

(defmethod drone_controller::GoHomeRequest
  (:response () (instance drone_controller::GoHomeResponse :init)))

(setf (get drone_controller::GoHomeRequest :md5sum-) "cbb2fae3170f584c2b25f43322fecf10")
(setf (get drone_controller::GoHomeRequest :datatype-) "drone_controller/GoHomeRequest")
(setf (get drone_controller::GoHomeRequest :definition-)
      "int8 data    		# integer with a flag
---
bool ack 			# acknowledged information
")

(setf (get drone_controller::GoHomeResponse :md5sum-) "cbb2fae3170f584c2b25f43322fecf10")
(setf (get drone_controller::GoHomeResponse :datatype-) "drone_controller/GoHomeResponse")
(setf (get drone_controller::GoHomeResponse :definition-)
      "int8 data    		# integer with a flag
---
bool ack 			# acknowledged information
")



(provide :drone_controller/GoHome "cbb2fae3170f584c2b25f43322fecf10")


