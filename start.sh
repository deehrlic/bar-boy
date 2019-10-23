#!/bin/bash

killall -9 node


node drinkServer.js&

ngrok http 3000&

sleep 2

curl --ipv4 http://127.0.0.1:4040/api/tunnels > url.py

sleep 2

python3 geturl.py

python3 lcd.py
