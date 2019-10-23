# bar-boy

This repository contains the source code for a remote controlled drink machine that was built by a friend and I. It consists mainly of a circuit of solenoid valves being controlled by a Raspberry Pi with added functionality with an LCD screen, a pair of distance sensors, and a LED puck light. The main code running this system is a Node.js webserver connected to a HTTP tunnel that calls a multithreaded python3 scripts to triggers various valves and pour fluids into containers. In addition there are a handful of utility scripts that use a link shortener and a LCD screen to display the IP address of the Pi for easier remote SSH access and a shortened version of the tunnel link for convenience.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

If you want to recreate the system we've designed, you'll want to read the full electronics writeup (COMING SOON) and have the following on your Raspberry Pi:

-Python3
-Node.js
-pip3
-npm
-some kind of shell that can run bash scripts

Make sure you have all of these packages installed.

-request
```
npm i request
```
-pythonShell
```
npm i python-shell
```
-express
```
npm i express
```
-RPi.GPIO
```
pip3 install RPi.GPIO
```
-RPLCD
```
pip3 install RPLCD
```
-bitly_api
```
Go to https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/ and follow the tutorial
```

### Installing

To get this system up and runnning you'll want to first read the electronics guide (COMING SOON).

Then once you have the frame constructed and electronics hooked up, clone this repo and navigate to the /bar-boy directory and run:
```
bash start.sh
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
