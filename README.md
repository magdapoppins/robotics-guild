# Robotics Guild Codebase

## Getting started
1. Download the latest ev3dev image and flash the SD card, see tutorial in: https://www.ev3dev.org/docs/getting-started/
2. Install requirements: `pip3 install python-ev3dev2`
3. If you don't already have it, install the EV3DEV device browser plugin to your VS Code.
4. Connect the ev3dev with your VS Code via USB.
5. From the sidebar find ev3dev device browser and connect to the EV3 brick.

## Ports
Outputs = Port.A, Port.B.... etc.  
Inputs = Port.S1, Port.S2... etc.

## Run
When robot is connected with USB, select Debug tab and select "Download and run", which is configured in `.vscode/launch.json`-file. Then press play-button and main file will be downloaded and executed on a connected robot.