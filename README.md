# SecureCRTNetworkAutomation
Python_SecureCRT_NetworkAutomation

Author: Kedharnath E (goudkedharnath@gmail.com)

Language: Python

Devices supported : Cisco Switches, Routers ,WLCS

Q. Why do we need this script?

This Script will help us to take the Pre changes logs and also creates the running configuration on the flash and helps with the Outage link. These all can be done at time with the single click. Which make easy for Move Add Change Deletes and Test and Turn Ups request.  

 
Q. What does this script do?

This script will run the list of show commands on the router or switch or WLC and also it will save the running configuration on the flash with the current date Helps us with the OUTAGE link to raise a scheduled outage


Q .How to use it?
Step 1: Please save the file in a folder 
Open secure CRT(script only works on secure crt)

Step 2: Login to any of the device and get in to enable mode.
Note: Before you run the script make sure log are captured  
Step 3: Go to scripts tab-> Select Run- Chose the file.
You will be prompted with below dialog box
Please chose the devices name
Note this only works for Cisco  
Where 
r=Router
s=Switch 
w=WLC
In the above example we have selected r for router.
Once you select the option .You will be prompted to select option to save the backup to the flash here y= yes and n= no.

If you wish to raise a  scheduled outage ticket. Please select y 
This is only for MRS. 

You will be prompted with below screen click okay
If you have selected to raise a ticket then you will be promoted with web browser
Please login and raise the outage ticket accordingly.
