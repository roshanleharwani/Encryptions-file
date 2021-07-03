#!/bin/bash/
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode managed
sudo ifconfig wlan0 up
echo "Managed  Mode Enabled"

