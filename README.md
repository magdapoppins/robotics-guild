# Robotics Guild Codebase

## Getting started
1. Download the latest ev3dev image and flash the SD card, see tutorial in: https://www.ev3dev.org/docs/getting-started/
2. Install requirements: `pip3 install python-ev3dev2`
3. If you don't already have it, install the EV3DEV device browser plugin to your VS Code.
4. Connect the ev3dev with your VS Code via USB or Bluetooth.
  - Bluetooth: From the brick select `Wireless and Networks` > `Bluetooth` and select `Powered` and then `Start scan` and select your computer from the list and pair. Then accept from your computer and from the brick. Note that you have to select `Connect to different device` from your VS Code ev3dev device browser if you had connected the brick before with USB.
5. From the sidebar find ev3dev device browser and connect to the EV3 brick.

## Ports
Outputs = Port.A, Port.B.... etc.  
Inputs = Port.S1, Port.S2... etc.

## Run
When robot is connected with USB, select Debug tab and select "Download and run", which is configured in `.vscode/launch.json`-file. Then press play-button and main file will be downloaded and executed on a connected robot.

## Remote control for your robot
Download Commander App from App store or Google play. Turn bluetooth on from the brick. Open commander app and select `New custom robot` and press play button. Connect to the brick with Bluetooth. Then `+` to add some motors you want. Then press `x` from top left corner and when your ready to roll, then press small red wrench 🔧 button from bottom right corner and all is set for controlling your robot.

## Troubleshooting
Sometimes the cables are not properly connected or are broken. This can result in a message like `ev3dev2 Device not found (OutputA)`. Try re-connecting the cable.

## Very simple robot building example

If you just want to build a simple robot and get quickly to coding, here's a simple example.

![Robo back](robo/robo1.png)
![Robo small wheel](robo/robo2.png)
![Robo motors front](robo/robo3.png)