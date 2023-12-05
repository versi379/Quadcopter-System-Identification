// Generated by gencpp from file drone_controller/TakeOffRequest.msg
// DO NOT EDIT!


#ifndef DRONE_CONTROLLER_MESSAGE_TAKEOFFREQUEST_H
#define DRONE_CONTROLLER_MESSAGE_TAKEOFFREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace drone_controller
{
template <class ContainerAllocator>
struct TakeOffRequest_
{
  typedef TakeOffRequest_<ContainerAllocator> Type;

  TakeOffRequest_()
    : altitude(0.0)  {
    }
  TakeOffRequest_(const ContainerAllocator& _alloc)
    : altitude(0.0)  {
  (void)_alloc;
    }



   typedef float _altitude_type;
  _altitude_type altitude;





  typedef boost::shared_ptr< ::drone_controller::TakeOffRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::drone_controller::TakeOffRequest_<ContainerAllocator> const> ConstPtr;

}; // struct TakeOffRequest_

typedef ::drone_controller::TakeOffRequest_<std::allocator<void> > TakeOffRequest;

typedef boost::shared_ptr< ::drone_controller::TakeOffRequest > TakeOffRequestPtr;
typedef boost::shared_ptr< ::drone_controller::TakeOffRequest const> TakeOffRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::drone_controller::TakeOffRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::drone_controller::TakeOffRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::drone_controller::TakeOffRequest_<ContainerAllocator1> & lhs, const ::drone_controller::TakeOffRequest_<ContainerAllocator2> & rhs)
{
  return lhs.altitude == rhs.altitude;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::drone_controller::TakeOffRequest_<ContainerAllocator1> & lhs, const ::drone_controller::TakeOffRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace drone_controller

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drone_controller::TakeOffRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::drone_controller::TakeOffRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drone_controller::TakeOffRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6e65a95f8aa933dff5e33d16e05a9392";
  }

  static const char* value(const ::drone_controller::TakeOffRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6e65a95f8aa933dfULL;
  static const uint64_t static_value2 = 0xf5e33d16e05a9392ULL;
};

template<class ContainerAllocator>
struct DataType< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "drone_controller/TakeOffRequest";
  }

  static const char* value(const ::drone_controller::TakeOffRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 altitude    		# altitude to take off the drone\n"
;
  }

  static const char* value(const ::drone_controller::TakeOffRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.altitude);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TakeOffRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::drone_controller::TakeOffRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::drone_controller::TakeOffRequest_<ContainerAllocator>& v)
  {
    s << indent << "altitude: ";
    Printer<float>::stream(s, indent + "  ", v.altitude);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DRONE_CONTROLLER_MESSAGE_TAKEOFFREQUEST_H