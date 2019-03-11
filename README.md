# raspberrypibased-switch-control
#process to install 
connect relay board as shown in circuit diagram (can be also use two way switch for batter response)
this project need same network in all device for working or u can bye private ip for work from anywhere
for running web page copy this folder to the raspberry pi board,s home folder or where you want to copy
after copy that folder open this folder in terminal

#process in terminal 
cd "folder where those file are copied"
export FLASK_APP=main.py
flask run --host 0.0.0.0


now you can control switch by open browser and go to 127.0.0.0:5000 addres (this is for rpi's browser for other device refer below step) rpi's default browser can be operate by vnc viewer 
and for other devices connect in same network and type rpi board ip for ex(192.168.43.253:5000) connect as per your ip



#note for active low circuit GPIO.LOW is on state and GPIO.HIGH is off state 
#for active high circuit GPIO.HIGH is on state and GPIO.LOW is off state  for more details refer wikipedia/active low circuit
