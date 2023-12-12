;; Auto-generated. Do not edit!


(when (boundp 'drone_controller::TakeOff)
  (if (not (find-package "DRONE_CONTROLLER"))
    (make-package "DRONE_CONTROLLER"))
  (shadow 'TakeOff (find-package "DRONE_CONTROLLER")))
(unless (find-package "DRONE_CONTROLLER::TAKEOFF")
  (make-package "DRONE_CONTROLLER::TAKEOFF"))
(unless (find-package "DRONE_CONTROLLER::TAKEOFFREQUEST")
  (make-package "DRONE_CONTROLLER::TAKEOFFREQUEST"))
(unless (find-package "DRONE_CONTROLLER::TAKEOFFRESPONSE")
  (make-package "DRONE_CONTROLLER::TAKEOFFRESPONSE"))

(in-package "ROS")





(defclass drone_controller::TakeOffRequest
  :super ros::object
  :slots (_altitude ))

(defmethod drone_controller::TakeOffRequest
  (:init
   (&key
    ((:altitude __altitude) 0.0)
    )
   (send-super :init)
   (setq _altitude (float __altitude))
   self)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:serialization-length
   ()
   (+
    ;; float32 _altitude
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _altitude
     (setq _altitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass drone_controller::TakeOffResponse
  :super ros::object
  :slots (_ack ))

(defmethod drone_controller::TakeOffResponse
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

(defclass drone_controller::TakeOff
  :super ros::object
  :slots ())

(setf (get drone_controller::TakeOff :md5sum-) "e548720c10b5dd4b7a5994bbd3ec2c39")
(setf (get drone_controller::TakeOff :datatype-) "drone_controller/TakeOff")
(setf (get drone_controller::TakeOff :request) drone_controller::TakeOffRequest)
(setf (get drone_controller::TakeOff :response) drone_controller::TakeOffResponse)

(defmethod drone_controller::TakeOffRequest
  (:response () (instance drone_controller::TakeOffResponse :init)))

(setf (get drone_controller::TakeOffRequest :md5sum-) "e548720c10b5dd4b7a5994bbd3ec2c39")
(setf (get drone_controller::TakeOffRequest :datatype-) "drone_controller/TakeOffRequest")
(setf (get drone_controller::TakeOffRequest :definition-)
      "float32 altitude    		# altitude to take off the drone
---
bool ack 			# acknowledged information
")

(setf (get drone_controller::TakeOffResponse :md5sum-) "e548720c10b5dd4b7a5994bbd3ec2c39")
(setf (get drone_controller::TakeOffResponse :datatype-) "drone_controller/TakeOffResponse")
(setf (get drone_controller::TakeOffResponse :definition-)
      "float32 altitude    		# altitude to take off the drone
---
bool ack 			# acknowledged information
")



(provide :drone_controller/TakeOff "e548720c10b5dd4b7a5994bbd3ec2c39")


