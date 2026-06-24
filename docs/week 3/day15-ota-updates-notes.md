Today, I'll learn how to update firmware via an OTA server.

So, OTA, or over-the-air, is a system that updates software or firmware. Updates are performed by uploading it to an OTA server, and any software or firmware connected to the OTA server. If there's update information for the software/firmware, it will be updated without a cable connection because OTA runs on the server side. Therefore, when updating, we'll update using the network.

The server side will have the software or firmware equipped with a hash and digital signature. When updating a device, the device will first verify it to identify whether the software or firmware is genuine from the developer. If not, the update will fail. If it is, the update will be executed on the device side.
