## Purpose

This code exists to mock the API of an EMU M-Bus Center.

It is intended to be used to test [the Home Assistant Integration](https://github.com/redlukas/emu_mbus_center) built to read from the API of  a Center.
Since the tester don't necessarily have access to all the various sensors, this mocker was built.

I would have loved to use flask for the application, but the M-Bus center does a socket hang up when you query it for a sensor ID that does not exist and this behaviour had to be replicated, so i am using the socketserver library.

## Usage

The official way to run this code is to use the provided compose file and to just `docker compose up` it. This is mainly because the web server needs to run on port 80 (because I am not expanding the Integration to query a different port just for testing) and since this is a privileged port and you cant (shouldn't) `sudo uv run` docker is the way to go.

## Contributing

### Adding a new sensor

Whenever we want to add a new sensor to the integration, it should also be added here. The checklist is as follows:

1. Add the response JSON in the devices folder. Follow the nomenclature from the integration.
2. Add the filename to the `VALID_IDS` dict in `server_with_sockets.py`. The key should be the index of the device in `custom_components/emu_m_bus_center/device_types` of the integration when sorted lexicographically.
3. In the saved response JSON
   1. set `Device.Id` to id from `VALID_IDS`
   2. set `Device.Name` to the pretty name of the sensor
   3. set `Device.Site` to "MySite"
   4. set `Device.CostUnit` to "MyCostUnit"
   5. set `Device.ValueDescs[x].DeviceId` to id from `VALID_IDS`