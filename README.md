# bar-boy

this repository contains the source code for a remote controlled drink machine that was built by deehrlic and cduval with a raspberry pi

bar-boy's backend has recently been upgraded and now runs on Python with a Flask server directing traffic and uses get requests to communicate between the server and client. This differs from previous builds and allows literally anything with an internet connection running on the same network an ability to easily interface with it since the server and client are no longer dependent on each other.

**[IMAGE HERE](https://raw.githubusercontent.com/deehrlic/bar-boy/master/BarBoyPortrait.JPG)**

**SEE /BARBOI.PDF IN THIS DIRECTORY FOR A TECHNICAL WRITEUP**

## Using bar-boy

Assuming you've recreated our hardware build, all you need to do is make sure all devices intended to connect to the bar-boy and run 
```
python3 api.py
```
on your Pi and 
```
python3 client.py
```
if you're using our included client. Since our setup is modeled off of an API, you can interface with bar-boy by sending a get request to 
```
http://pi's-ip-addr:port#/api/route?drink=drink-name
```
to trigger whatever drink you sent to pour. All service to the bar-boy itself is routed through the LOCAL IP address of the Pi running it so take note of that.


### Prerequisites

Python3 and these non built-in libraries:

-flask

-requests

-csv

-Rpi.GPIO



## Built With

* Python3
* HTML/CSS

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

---------------------------------------------------------------------------------------------------------------------------------------

**GOVERNMENT WARNING: (1) According to the Surgeon General, women should not drink alcoholic beverages during pregnancy because of the risk of birth defects. (2) Consumption of alcoholic beverages impairs your ability to drive a car or operate machinery, and may cause health problems**

By using bar-boy, you are consenting to the following statement:

I am voluntarily participating in the use of this device. I understand that there are risks associated with my participation in using this device, such as physical and/or psychological injury, pain, suffering, illness, disfigurement, temporary or permanent disability, death or economic loss. These injuries or outcomes may arise from my own or other’s actions, inactions, or negligence, or the condition of the use or location of this device. Nonetheless, I assume all risks of my participation in the implementation and use of this device, whether known or unknown to me, and any events incidental to the use of this device.

Please drink responsibly.


