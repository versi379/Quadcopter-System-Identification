// Generated by gencpp from file drone_controller/GoToPoint.msg
// DO NOT EDIT!


#ifndef DRONE_CONTROLLER_MESSAGE_GOTOPOINT_H
#define DRONE_CONTROLLER_MESSAGE_GOTOPOINT_H

#include <ros/service_traits.h>


#include <drone_controller/GoToPointRequest.h>
#include <drone_controller/GoToPointResponse.h>


namespace drone_controller
{

struct GoToPoint
{

typedef GoToPointRequest Request;
typedef GoToPointResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GoToPoint
} // namespace drone_controller


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::drone_controller::GoToPoint > {
  static const char* value()
  {
    return "92c8a5b2a2eede8ea83a1f79297fcf35";
  }

  static const char* value(const ::drone_controller::GoToPoint&) { return value(); }
};

template<>
struct DataType< ::drone_controller::GoToPoint > {
  static const char* value()
  {
    return "drone_controller/GoToPoint";
  }

  static const char* value(const ::drone_controller::GoToPoint&) { return value(); }
};


// service_traits::MD5Sum< ::drone_controller::GoToPointRequest> should match
// service_traits::MD5Sum< ::drone_controller::GoToPoint >
template<>
struct MD5Sum< ::drone_controller::GoToPointRequest>
{
  static const char* value()
  {
    return MD5Sum< ::drone_controller::GoToPoint >::value();
  }
  static const char* value(const ::drone_controller::GoToPointRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::drone_controller::GoToPointRequest> should match
// service_traits::DataType< ::drone_controller::GoToPoint >
template<>
struct DataType< ::drone_controller::GoToPointRequest>
{
  static const char* value()
  {
    return DataType< ::drone_controller::GoToPoint >::value();
  }
  static const char* value(const ::drone_controller::GoToPointRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::drone_controller::GoToPointResponse> should match
// service_traits::MD5Sum< ::drone_controller::GoToPoint >
template<>
struct MD5Sum< ::drone_controller::GoToPointResponse>
{
  static const char* value()
  {
    return MD5Sum< ::drone_controller::GoToPoint >::value();
  }
  static const char* value(const ::drone_controller::GoToPointResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::drone_controller::GoToPointResponse> should match
// service_traits::DataType< ::drone_controller::GoToPoint >
template<>
struct DataType< ::drone_controller::GoToPointResponse>
{
  static const char* value()
  {
    return DataType< ::drone_controller::GoToPoint >::value();
  }
  static const char* value(const ::drone_controller::GoToPointResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DRONE_CONTROLLER_MESSAGE_GOTOPOINT_H