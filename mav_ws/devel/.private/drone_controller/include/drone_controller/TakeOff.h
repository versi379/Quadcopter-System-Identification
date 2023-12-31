// Generated by gencpp from file drone_controller/TakeOff.msg
// DO NOT EDIT!


#ifndef DRONE_CONTROLLER_MESSAGE_TAKEOFF_H
#define DRONE_CONTROLLER_MESSAGE_TAKEOFF_H

#include <ros/service_traits.h>


#include <drone_controller/TakeOffRequest.h>
#include <drone_controller/TakeOffResponse.h>


namespace drone_controller
{

struct TakeOff
{

typedef TakeOffRequest Request;
typedef TakeOffResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TakeOff
} // namespace drone_controller


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::drone_controller::TakeOff > {
  static const char* value()
  {
    return "e548720c10b5dd4b7a5994bbd3ec2c39";
  }

  static const char* value(const ::drone_controller::TakeOff&) { return value(); }
};

template<>
struct DataType< ::drone_controller::TakeOff > {
  static const char* value()
  {
    return "drone_controller/TakeOff";
  }

  static const char* value(const ::drone_controller::TakeOff&) { return value(); }
};


// service_traits::MD5Sum< ::drone_controller::TakeOffRequest> should match
// service_traits::MD5Sum< ::drone_controller::TakeOff >
template<>
struct MD5Sum< ::drone_controller::TakeOffRequest>
{
  static const char* value()
  {
    return MD5Sum< ::drone_controller::TakeOff >::value();
  }
  static const char* value(const ::drone_controller::TakeOffRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::drone_controller::TakeOffRequest> should match
// service_traits::DataType< ::drone_controller::TakeOff >
template<>
struct DataType< ::drone_controller::TakeOffRequest>
{
  static const char* value()
  {
    return DataType< ::drone_controller::TakeOff >::value();
  }
  static const char* value(const ::drone_controller::TakeOffRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::drone_controller::TakeOffResponse> should match
// service_traits::MD5Sum< ::drone_controller::TakeOff >
template<>
struct MD5Sum< ::drone_controller::TakeOffResponse>
{
  static const char* value()
  {
    return MD5Sum< ::drone_controller::TakeOff >::value();
  }
  static const char* value(const ::drone_controller::TakeOffResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::drone_controller::TakeOffResponse> should match
// service_traits::DataType< ::drone_controller::TakeOff >
template<>
struct DataType< ::drone_controller::TakeOffResponse>
{
  static const char* value()
  {
    return DataType< ::drone_controller::TakeOff >::value();
  }
  static const char* value(const ::drone_controller::TakeOffResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DRONE_CONTROLLER_MESSAGE_TAKEOFF_H
