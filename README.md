# Singapore Bus Stop Arrival Timing (Micropython Version)

The code in this repository makes use of Land Transport Authority's (LTA) DataMall Dynamic API to call the bus arrival times for a specified bus stop.

To make calls with the DataMall API, you will need to sign up to use the service.

For this version of the code, it is intended to be used on devices such as:

* ESP32/ESP8266
* Raspberry Pi Pico
* Arduino Boards capable of Micropython
* Pyboard
* and more

As for the Python version of the code, please refer [here](https://github.com/TwelfthDoctor1/BusSvcTesting).

### Requirements

The following libraries will be required to run the code:
* [micropython-urequests](https://pypi.org/project/micropython-urequests/)
* [python_lcd](https://github.com/dhylands/python_lcd)

For physical parts:
* A LCD screen (this project uses 20 by 4 I2C LCD screen)
* An Arduino RP2040 Connect (any other boards with networking functionality will work but changes to the code would be required)
* Board chassis with wiring to connect to the LCD, Board and to two buttons for controls (buttons connect to GPIO 25 and 15 respectively)

### Before running the Code

Before running the code, you would need to get the API KEY and the Bus Timings Request URL from DataMall, and place them onto the Credentials.py file (you will need to create on your own)

To set the bus stops you want to see, set the BUS_STOP list with a list of bus stop codes that you want to see. (example below)

`BUS_STOP = [77009, 77191, 77011, 65191, 65199]`

As for networking credentials, you will need to set the SSID and password in TimeHandling.py (may be shifted at a later time).

### When running the Code

When running, the device will connect to the internet to:
* Get the time
* Get the Bus Stop Timing Data

The device would then display the bus stop timing for the first bus stop in the list (index 0) on the first bus service in that bus stop. After 5 seconds to the next bus service in that bus stop. Once the last service is shown for 5 seconds, it will return to the first bus service in the same bus stop. Note that it will not update the timing until called.

For controls:
* To switch the bus stops, press and hold on button 2.
* To refresh arrival data, press and hold on both buttons 1 and 2. Data will be updated after the last bus service timing.
* To switch between functions, press button 1.

### Extra Features

To switch from the bus stop to these extra features, use button to switch between them.

For this features, they include:
* Time Display
* Temperature (soon?)

#### Time

Currently the time only supports display on 12 hour display. This time and date comes from the NTP server through the NTP protocol and its saved onto the RTC of the board for arrival comparison and time display.
