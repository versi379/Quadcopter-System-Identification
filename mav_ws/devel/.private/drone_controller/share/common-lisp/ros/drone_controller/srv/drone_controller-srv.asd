
(cl:in-package :asdf)

(defsystem "drone_controller-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "GoHome" :depends-on ("_package_GoHome"))
    (:file "_package_GoHome" :depends-on ("_package"))
    (:file "GoToPoint" :depends-on ("_package_GoToPoint"))
    (:file "_package_GoToPoint" :depends-on ("_package"))
    (:file "Land" :depends-on ("_package_Land"))
    (:file "_package_Land" :depends-on ("_package"))
    (:file "TakeOff" :depends-on ("_package_TakeOff"))
    (:file "_package_TakeOff" :depends-on ("_package"))
  ))