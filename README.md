# bar-boy

This repository contains the source code for a remote controlled drink machine that was built by a friend and I. It consists mainly of a circuit of solenoid valves being controlled by a Raspberry Pi with added functionality with an LCD screen, a pair of distance sensors, and a LED puck light. 

The main code running this system is a Node.js webserver connected to a HTTP tunnel that calls a multithreaded python3 scripts to triggers various valves and pour fluids into containers. In addition there are a handful of utility scripts that use a link shortener and a LCD screen to display the IP address of the Pi for easier remote SSH access and a shortened version of the tunnel link for convenience.

## Using bar-boy

Once you have completed the setup as described below (Prerequisites, Installing, and Deployment) here's how you get the most out of bar-boy.

Webpages:

**<your_shortened_link>/pour** : bar-boy's default mode. On this page you can choose from a list of recipes (built-in or yours) and make it pour the drink of your choice.

**<your_shortened_link>/shot** : bar-boy's more **EXTREME** mode. Allows you to order a drink containing a variable amount of shots. Use at your own risk.

**<your_shortened_link>/admin** : Allows bar-boy's user to manipulate valves individually to pour custom creations.

**Create your own recipes!** : Since bar-boy can dispense any kind of fluids, you can create your own recipes. Consult the /recipes folder to see examples of the format we use with our .csv recipes and update select.html accordingly to add your new recipe(s) to the option menu on the /pour page.


### Prerequisites

If you want to recreate the system we've designed, you'll want to read the full electronics writeup (COMING SOON) and have the following on your Raspberry Pi:

-Python3
-Node.js
-pip3
-npm
-some kind of shell that can run bash scripts

Make sure you have all of these packages installed.
**request**
```
npm i request
```
**pythonShell**
```
npm i python-shell
```
**express**
```
npm i express
```
**ngrok**
```
npm i ngrok
```
**RPi.GPIO**
```
pip3 install RPi.GPIO
```
**RPLCD**
```
pip3 install RPLCD
```
**bitly_api**
```
Go to https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/ and follow the tutorial
```

### Installing

To get this system up and runnning you'll want to first read the electronics guide (COMING SOON). Once you've done that, clone the repo and make sure you have all the prerequisites installed.


## Deployment

Once you have the frame constructed and electronics hooked up, clone this repo and navigate to the /bar-boy directory and run:
```
bash start.sh
```
You should see an ngrok tunnel listening on port 3000 start followed by a Node.js server followed by the LCD display showing the device's IP on line 1 and a bit.ly shortened version of the ngrok link. When you shut it down after you're doing you may encounter a 
```
panic: runtime error: slice bounds out of range
```
error. If this error appears, just close that terminal window and start a new one.

## Built With

* Node.js
* Python3
* HTML/CSS
* [Ngrok](ngrok.com)
* [Bit.ly API](dev.bitly.com)

## Authors

* **Drew Ehrlich** - *Software Developer* - [deehrlic](https://github.com/deehrlic)

* **Corey DuVal** - *Electronics Developer* - [coreyduval](https://github.com/coreyduval)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Special Thanks To:

* **Nick Adair** - *Lead Construction Assistant/Toolmaster*
* **Justin Hinman** - *Construction Assistant/Tester*
* **Steaven Ballesteros** - *Construction Assistant/Tester*





**GOVERNMENT WARNING: (1) According to the Surgeon General, women should not drink alcoholic beverages during pregnancy because of the risk of birth defects. (2) Consumption of alcoholic beverages impairs your ability to drive a car or operate machinery, and may cause health problems**

By using bar-boy, you are consenting to the following statement:

I am voluntarily participating in the use of this device. I understand that there are risks associated with my participation in using this device, such as physical and/or psychological injury, pain, suffering, illness, disfigurement, temporary or permanent disability, death or economic loss. These injuries or outcomes may arise from my own or other’s actions, inactions, or negligence, or the condition of the use or location of this device. Nonetheless, I assume all risks of my participation in the implementation and use of this device, whether known or unknown to me, and any events incidental to the use of this device.

Please drink responsibly.


