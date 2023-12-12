
"use strict";

let FileRead = require('./FileRead.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let CommandLong = require('./CommandLong.js')
let WaypointClear = require('./WaypointClear.js')
let FileList = require('./FileList.js')
let CommandInt = require('./CommandInt.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let StreamRate = require('./StreamRate.js')
let FileWrite = require('./FileWrite.js')
let MessageInterval = require('./MessageInterval.js')
let FileMakeDir = require('./FileMakeDir.js')
let ParamPush = require('./ParamPush.js')
let WaypointPush = require('./WaypointPush.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let CommandTOL = require('./CommandTOL.js')
let SetMavFrame = require('./SetMavFrame.js')
let CommandHome = require('./CommandHome.js')
let FileClose = require('./FileClose.js')
let LogRequestList = require('./LogRequestList.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let MountConfigure = require('./MountConfigure.js')
let ParamGet = require('./ParamGet.js')
let FileTruncate = require('./FileTruncate.js')
let CommandBool = require('./CommandBool.js')
let CommandAck = require('./CommandAck.js')
let FileChecksum = require('./FileChecksum.js')
let LogRequestData = require('./LogRequestData.js')
let FileOpen = require('./FileOpen.js')
let ParamSet = require('./ParamSet.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let SetMode = require('./SetMode.js')
let FileRemove = require('./FileRemove.js')
let WaypointPull = require('./WaypointPull.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let FileRename = require('./FileRename.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let ParamPull = require('./ParamPull.js')

module.exports = {
  FileRead: FileRead,
  CommandTriggerInterval: CommandTriggerInterval,
  CommandLong: CommandLong,
  WaypointClear: WaypointClear,
  FileList: FileList,
  CommandInt: CommandInt,
  VehicleInfoGet: VehicleInfoGet,
  StreamRate: StreamRate,
  FileWrite: FileWrite,
  MessageInterval: MessageInterval,
  FileMakeDir: FileMakeDir,
  ParamPush: ParamPush,
  WaypointPush: WaypointPush,
  CommandTriggerControl: CommandTriggerControl,
  CommandTOL: CommandTOL,
  SetMavFrame: SetMavFrame,
  CommandHome: CommandHome,
  FileClose: FileClose,
  LogRequestList: LogRequestList,
  WaypointSetCurrent: WaypointSetCurrent,
  MountConfigure: MountConfigure,
  ParamGet: ParamGet,
  FileTruncate: FileTruncate,
  CommandBool: CommandBool,
  CommandAck: CommandAck,
  FileChecksum: FileChecksum,
  LogRequestData: LogRequestData,
  FileOpen: FileOpen,
  ParamSet: ParamSet,
  FileRemoveDir: FileRemoveDir,
  SetMode: SetMode,
  FileRemove: FileRemove,
  WaypointPull: WaypointPull,
  CommandVtolTransition: CommandVtolTransition,
  FileRename: FileRename,
  LogRequestEnd: LogRequestEnd,
  ParamPull: ParamPull,
};
