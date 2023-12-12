
"use strict";

let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let PositionTarget = require('./PositionTarget.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let StatusText = require('./StatusText.js');
let LogEntry = require('./LogEntry.js');
let FileEntry = require('./FileEntry.js');
let ParamValue = require('./ParamValue.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let HomePosition = require('./HomePosition.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let LandingTarget = require('./LandingTarget.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let Mavlink = require('./Mavlink.js');
let VFR_HUD = require('./VFR_HUD.js');
let WaypointList = require('./WaypointList.js');
let GPSRTK = require('./GPSRTK.js');
let RadioStatus = require('./RadioStatus.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let Tunnel = require('./Tunnel.js');
let State = require('./State.js');
let ManualControl = require('./ManualControl.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let HilGPS = require('./HilGPS.js');
let RTCM = require('./RTCM.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let Altitude = require('./Altitude.js');
let ESCInfo = require('./ESCInfo.js');
let RTKBaseline = require('./RTKBaseline.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let ESCStatus = require('./ESCStatus.js');
let Thrust = require('./Thrust.js');
let GPSINPUT = require('./GPSINPUT.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let RCIn = require('./RCIn.js');
let Waypoint = require('./Waypoint.js');
let RCOut = require('./RCOut.js');
let BatteryStatus = require('./BatteryStatus.js');
let WaypointReached = require('./WaypointReached.js');
let LogData = require('./LogData.js');
let Trajectory = require('./Trajectory.js');
let Vibration = require('./Vibration.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let ExtendedState = require('./ExtendedState.js');
let MountControl = require('./MountControl.js');
let DebugValue = require('./DebugValue.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let Param = require('./Param.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let ActuatorControl = require('./ActuatorControl.js');
let GPSRAW = require('./GPSRAW.js');
let CellularStatus = require('./CellularStatus.js');
let TerrainReport = require('./TerrainReport.js');
let CommandCode = require('./CommandCode.js');
let HilControls = require('./HilControls.js');
let VehicleInfo = require('./VehicleInfo.js');
let HilSensor = require('./HilSensor.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');

module.exports = {
  ESCTelemetryItem: ESCTelemetryItem,
  PositionTarget: PositionTarget,
  MagnetometerReporter: MagnetometerReporter,
  CameraImageCaptured: CameraImageCaptured,
  GlobalPositionTarget: GlobalPositionTarget,
  StatusText: StatusText,
  LogEntry: LogEntry,
  FileEntry: FileEntry,
  ParamValue: ParamValue,
  CamIMUStamp: CamIMUStamp,
  HomePosition: HomePosition,
  NavControllerOutput: NavControllerOutput,
  LandingTarget: LandingTarget,
  OverrideRCIn: OverrideRCIn,
  ESCInfoItem: ESCInfoItem,
  Mavlink: Mavlink,
  VFR_HUD: VFR_HUD,
  WaypointList: WaypointList,
  GPSRTK: GPSRTK,
  RadioStatus: RadioStatus,
  OpticalFlowRad: OpticalFlowRad,
  CompanionProcessStatus: CompanionProcessStatus,
  Tunnel: Tunnel,
  State: State,
  ManualControl: ManualControl,
  WheelOdomStamped: WheelOdomStamped,
  HilGPS: HilGPS,
  RTCM: RTCM,
  OnboardComputerStatus: OnboardComputerStatus,
  Altitude: Altitude,
  ESCInfo: ESCInfo,
  RTKBaseline: RTKBaseline,
  TimesyncStatus: TimesyncStatus,
  ESCStatus: ESCStatus,
  Thrust: Thrust,
  GPSINPUT: GPSINPUT,
  HilActuatorControls: HilActuatorControls,
  ADSBVehicle: ADSBVehicle,
  RCIn: RCIn,
  Waypoint: Waypoint,
  RCOut: RCOut,
  BatteryStatus: BatteryStatus,
  WaypointReached: WaypointReached,
  LogData: LogData,
  Trajectory: Trajectory,
  Vibration: Vibration,
  ESCTelemetry: ESCTelemetry,
  EstimatorStatus: EstimatorStatus,
  ExtendedState: ExtendedState,
  MountControl: MountControl,
  DebugValue: DebugValue,
  PlayTuneV2: PlayTuneV2,
  ESCStatusItem: ESCStatusItem,
  Param: Param,
  AttitudeTarget: AttitudeTarget,
  ActuatorControl: ActuatorControl,
  GPSRAW: GPSRAW,
  CellularStatus: CellularStatus,
  TerrainReport: TerrainReport,
  CommandCode: CommandCode,
  HilControls: HilControls,
  VehicleInfo: VehicleInfo,
  HilSensor: HilSensor,
  HilStateQuaternion: HilStateQuaternion,
};
