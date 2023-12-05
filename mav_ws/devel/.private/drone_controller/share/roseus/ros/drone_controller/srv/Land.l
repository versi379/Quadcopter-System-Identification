;; Auto-generated. Do not edit!


(when (boundp 'drone_controller::Land)
  (if (not (find-package "DRONE_CONTROLLER"))
    (make-package "DRONE_CONTROLLER"))
  (shadow 'Land (find-package "DRONE_CONTROLLER")))
(unless (find-package "DRONE_CONTROLLER::LAND")
  (make-package "DRONE_CONTROLLER::LAND"))
(unless (find-package "DRONE_CONTROLLER::LANDREQUEST")
  (make-package "DRONE_CONTROLLER::LANDREQUEST"))
(unless (find-package "DRONE_CONTROLLER::LANDRESPONSE")
  (make-package "DRONE_CONTROLLER::LANDRESPONSE"))

(in-package "ROS")





(defclass drone_controller::LandRequest
  :super ros::object
  :slots (_data ))

(defmethod drone_controller::LandRequest
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

(defclass drone_controller::LandResponse
  :super ros::object
  :slots (_ack ))

(defmethod drone_controller::LandResponse
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

(defclass drone_controller::Land
  :super ros::object
  :slots ())

(setf (get drone_controller::Land :md5sum-) "cbb2fae3170f584c2b25f43322fecf10")
(setf (get drone_controller::Land :datatype-) "drone_controller/Land")
(setf (get drone_controller::Land :request) drone_controller::LandRequest)
(setf (get drone_controller::Land :response) drone_controller::LandResponse)

(defmethod drone_controller::LandRequest
  (:response () (instance drone_controller::LandResponse :init)))

(setf (get drone_controller::LandRequest :md5sum-) "cbb2fae3170f584c2b25f43322fecf10")
(setf (get drone_controller::LandRequest :datatype-) "drone_controller/LandRequest")
(setf (get drone_controller::LandRequest :definition-)
      "int8 data    		# integer with a flag
---
bool ack 			# acknowledged information
")

(setf (get drone_controller::LandResponse :md5sum-) "cbb2fae3170f584c2b25f43322fecf10")
(setf (get drone_controller::LandResponse :datatype-) "drone_controller/LandResponse")
(setf (get drone_controller::LandResponse :definition-)
      "int8 data    		# integer with a flag
---
bool ack 			# acknowledged information
")



(provide :drone_controller/Land "cbb2fae3170f584c2b25f43322fecf10")


