# 41150-Rover-Project



For Reference:


| Device        | Identifier           | Code Name  |
| ------------- |:-------------:| -----:|
| Pi    | 156-13 N3 W | Frank |
| Gryoscope  | BNO055  |  Phil |
| Pi | AP      |    Al |



# Run process
Files on AP are in: \projects\django-rpi\mysite\
Files on ROVER are in: \ROVER_project\
Confirm Django settings.py contains AP IP as an ALLOWED HOST
1. `sudo motion` on ROVER
1. `sudo pigpiod` on ROVER
1. `python server_ap.py 123.1.1.1` on AP with AP IP as argument
1. `python server_rover.py 10.0.0.2` on ROVER with ROVER IP as argument
1. `python manage.py runserver 123.1.1.1:8000` on AP with AP IP as argument with port 8000
1. Launch `http://123.1.1.1:8000` in internet browser on a laptop

_Ensure all previous code is running before continuing_

1. `python datasend_rover.py 123.1.1.1` on ROVER with AP IP as argument
1. Run command sending script (to be completed)
