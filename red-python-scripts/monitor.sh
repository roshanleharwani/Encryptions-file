#!/bin/bash/
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode Monitor
sudo ifconfig wlan0 up
echo "Monitor Mode Enabled"
