#!/bin/bash


killall -9 node
killall -9 ngrok

node drinkServer.js&

ngrok http 3000







