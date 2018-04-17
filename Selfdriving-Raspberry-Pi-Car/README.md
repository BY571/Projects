# Raspberry Pi Car 

<img src="https://github.com/BY571/Raspberry-Pi-Car/blob/master/Images/Car1.JPG" width="600" height="800">


## Hardware Setup

- [Raspberry Pi 3](http://amzn.to/2Cxu0vY)
- [HBridge L298n](http://amzn.to/2lxheqh)
- [5V Power Supply for the Raspberry](http://amzn.to/2ClpPql)
- [9V Power Supply for the DC Motors](http://amzn.to/2zXq9W7)
- [4 x female-to-female Jumper](http://amzn.to/2CA3KBj)
- [2 x male-to-female Jumper](http://amzn.to/2CA3KBj)
- [Hummer H2 or any other RC-Car](http://amzn.to/2lwzks9)

[//]: # (Image References)

[image1]: ./Images/Schaltplan.jpg 
[image2]: ./Images/Final_car.JPG 
[image3]: ./Images/pi3_gpio.png 
[image4]: ./Images/translated.png "Translated"
[image5]: ./Images/Car1.JPG "Warped"
[image6]: ./Images/zoom.png "Zoomed"
[image7]: ./Images/augmenting.png "Augmenting"


#### Electronic Schematic

![image1]

## Setup the Raspberry Pi





### Connect to your PC via SSH


### First Test
Connect all power supplies - Raspberry Pi and H-Bridge. Open a terminal on your PC.
Login to your Raspberry Pi via `ssh pi@ your-IP-address` . Clone this repository by: `git clone https://github.com/BY571/Raspberry-Pi-Car`.
Via terminal, enter the directory where you cloned the repository on your Rapsberry Pi.</b>


### Testing User Control via Keyboard

Enter `python keyboard_control.py` in your terminal at Raspberry-Pi-Car directory.</b>
Controlling keys:
- w = forward
- s = reverse
- a = left
- d = right 
- q = forward+left
- e = forward+right
- y = reverse+left
- x = reverse+right
- p = Stop 

### Controlling via XBOX Controller:
Enter `sudo python controls.py` in your terminal at `Raspberry-Pi-Car` directory-</b>

