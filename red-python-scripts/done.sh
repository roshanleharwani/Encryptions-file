sudo apt-get install linux-headers-`uname -r`
sudo apt-get install linux-headers-5.10.0-kali6-amd64

sudo apt install dkms
sudo rmmod r8188eu.ko
git clone https://github.com/aircrack-ng/rtl8188eus
cd rtl8188eus
sudo -i
echo "blacklist r8188eu" > "/etc/modprobe.d/realtek.conf"
exit
