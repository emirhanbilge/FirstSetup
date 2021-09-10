#!/bin/bash

cd /home/pi/Desktop/EbbScripts/Network/ 
sudo chmod +x resetNetwork.sh
sudo ./resetNetwork.sh


if $1 
then
	#parametre yok
	echo "DHCP"
	#echo "dhcp olacak hiçbir şey yapılmayacak"
	
else
	#parametre var
	echo "STATIC IP "
	chmod u+x netSet.sh
	sudo ./netSet.sh $1 $2 $3
fi

cd /home/pi/Desktop/EbbScripts/Network/ 
sudo chmod +x modbusCrontabCreate.sh
sudo ./modbusCrontabCreate.sh
