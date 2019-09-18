# What is this project?

This is a Iridium Modem (9602/9603) emulator to make it possible to test your own software again a "Virtual" Iridium device and it connection.

This application is written in Python language uses pyserial to implement a serial communications interface. The emulator matches the behavior of the Iridium 9602 modem which is available from NAL Research and Rock7Mobile (as Rockblock). The emulator will respond to at commands to write data, execute short-burst data (SBD) sessions, and most of the other functions supported by the 9602 serial interface.


# What's the use?

If you want to develop an application on a PC or an embedded device it will to talk to an Iridium modem, you can use this for initial prototyping and testing. This can potentially save quite some cost on Iridium service charges. Also you can already create an application without already buying the real Iridium Modem (9602/9603) hardware.

# How do I get this software?

In your Unix shell of choice:
```
 $ git clone https://github.com/jmalsbury/virtual_iridium
 $ cd virtual_iridium/python
 $ python Iridium9602.py -d /dev/ttyUSB0 -u youraccount@gmail.com -p your_password -i imap.gmail.com -o smtp.gmail.com -r your_iridium_test_account@gmail.com -m EMAIL
```

The specified serial device, in the example above: ttyUSB0 , should connect to the external device that you are developing your Iridium communications app on. You can also use a virtual serial port (like a pair of SOCAT TTYs), to connect to another application on the same PC.

To see all options, execute
```
$ python Iridium9602.py --help

Usage: Iridium9602.py [options]

Options:
  -h, --help                            show this help message and exit
  -d DEV, --dev=DEV                     tty dev(ex. '/dev/ttyUSB0'
  -p PASSWD, --passwd=PASSWD            Password
  -u USER, --user=USER                  E-mail account username
  -r USER, --recipient=USER             Destination e-mail address.
  -i IN_SRV, --in_srv=IN_SRV            Incoming e-mail server url
  -o OUT_SRV, --out_srv=OUT_SRV         Outging e-mail server
  --mo_ip=MO_IP                         Mobile-originated DirectIP server IP address
  --mo_port=MO_PORT                     Mobile-originated DirectIP server Port
  --mt_port=MT_PORT                     Mobile-terminated DirectIP server Port
  -m MODE, --mode=MODE                  Mode: EMAIL,HTTP_POST,IP,NONE
  -e MODE, --imei=MODE                  IMEI for this modem
  -s HTTP_SRV, --http_srv=HTTP_SRV      Server path to post to in HTTP mode
```

# Fork info

The author seems to have deleted the original repository, but there are several forks that have preserved this incredibly useful piece of software. It had not been updated since 6 years ago and has plenty of TODOs in the code.

This fork includes HTTP POST functionality, which was listed as a TODO in the original code. It allows for testing devices that use the Rock7 HTTP API for feeding their SBD messages into a web server. Be advised: it is not compatible with Python 3, needs Python 2.7 to work correctly.

Thanks to the original autor J.Malsbury.

