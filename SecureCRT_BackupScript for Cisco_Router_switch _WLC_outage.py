# $language = "python"
# $interface = "1.0"
	
from datetime import datetime
from datetime import timedelta

import webbrowser
#Written by : kedharnath E
#goudkedharnath@gmail.com 

def Main():

	
	
	
	optHostname=""
	crt.Screen.Synchronous = False  
	x=datetime.today().strftime('%Y-%m-%d')
	x=str(x)
	Result=""
	OUT=""
	# Go to outageticket.com 
	optHostname=crt.Dialog.Prompt('Enter a Device Type to take the backup.\n\nPlease Run the script in enable mode only \n\n r=Router \n \n s=Switch \n \n w=Wirless Controller \n', 'Enter Hostname', optHostname)
	Result=crt.Dialog.Prompt('Do you want to save the backup to the flash \n\n y=Yes \n\n n=No \n\n', 'Enter Your Option', Result)
	OUT=crt.Dialog.Prompt('Do you want to Raise a OUTAGE Ticket ? \n\n y=Yes \n\n n=No \n\n', 'Enter Your Option', OUT)
			
	if optHostname=="r" :
		
		
		
		
			crt.Dialog.MessageBox("Router Backup Starts" )
			crt.Screen.Send("ter len 0\n" + chr(13))
			crt.Screen.Send("who\n" + chr(13))
			crt.Screen.Send("sh clock\n" + chr(13))
			crt.Screen.Send("sh ip int brief | i up\n" + chr(13))
			crt.Screen.Send("sh ip int brief | e unassign\n" + chr(13))
			crt.Screen.Send("sh int des\n" + chr(13))
			crt.Screen.Send("sh int status\n" + chr(13))
			crt.Screen.Send("sh int status err-dis\n" + chr(13))
			crt.Screen.Send("sh int | i error\n" + chr(13))
			crt.Screen.Send("sh int | i CRC\n" + chr(13))
			crt.Screen.Send("sh int\n" + chr(13))
			crt.Screen.Send("sh ip arp\n" + chr(13))
			crt.Screen.Send("sh cdp nei\n" + chr(13))
			crt.Screen.Send("sh mac address\n" + chr(13))
			crt.Screen.Send("sh standby brief\n" + chr(13))
			crt.Screen.Send("sh vrrp brief\n" + chr(13))
			crt.Screen.Send("sh ip route summary\n" + chr(13))
			crt.Screen.Send("sh ip protocol\n" + chr(13))
			crt.Screen.Send("sh ip ospf nei\n" + chr(13))
			crt.Screen.Send("sh ip ospf int brief\n" + chr(13))
			crt.Screen.Send("sh ip ospf database\n" + chr(13))
			crt.Screen.Send("sh ip ospf\n" + chr(13))
			crt.Screen.Send("sh ip bgp summ\n" + chr(13))
			crt.Screen.Send("sh ip bgp nei\n" + chr(13))
			crt.Screen.Send("sh ip bgp all\n" + chr(13))
			crt.Screen.Send("sh ip bgp\n" + chr(13))
			crt.Screen.Send("sh ip route\n" + chr(13))
			crt.Screen.Send("sh runn\n" + chr(13))
			crt.Screen.Send("sh log\n" + chr(13))
			crt.Screen.Send("sh version\n" + chr(13))
			crt.Screen.Send("sh module\n" + chr(13))
			crt.Screen.Send("sh invent\n" + chr(13))
			crt.Screen.Send("sh environment\n" + chr(13))
			crt.Screen.Send("sh  boot\n" + chr(13))
			crt.Screen.Send("sh run | i boot\n" + chr(13))
			crt.Screen.Send("dir\n" + chr(13))
			crt.Screen.Send("dir all\n" + chr(13))
			crt.Screen.Send("show policy-map interface brief\n" + chr(13))
			crt.Screen.Send("sh int | in error\n" + chr(13))
			crt.Screen.Send("sh int | in line|count|error\n" + chr(13))
			crt.Screen.Send("sh run | sec ip prefix-list\n" + chr(13))
			crt.Screen.Send("ter len 50\n" + chr(13))
			
			if Result== "y" :
			
				crt.Dialog.MessageBox("Warning:  !! You will be prompted to save the config to the Flash at the end of the script !! \n\n !! Please press enter if you want to save the config to the Flash or press Ctrl+C !!\n\n " )
				crt.Screen.Send("copy running-config flash:config_"+ x +".old")
					
			
			else:
			
				crt.Screen.Send("!! router backup end!!\n" + chr(13))
			
			
			
				
	elif optHostname =="s" :
		
			crt.Screen.Send("en\n" + chr(13))
	
			crt.Dialog.MessageBox("Switch Backup Starts" )
			crt.Screen.Send("ter len 0\n" + chr(13))
			
			crt.Screen.Send("who\n" + chr(13))
			crt.Screen.Send("sh clock\n" + chr(13))
			crt.Screen.Send("ter len 0\n" + chr(13))
			crt.Screen.Send("sh ip int brief | i up\n" + chr(13))
			crt.Screen.Send("sh ip int brief | e unassign\n" + chr(13))
			crt.Screen.Send("sh int des\n" + chr(13))
			crt.Screen.Send("sh int status\n" + chr(13))
			crt.Screen.Send("sh int status err-dis\n" + chr(13))
			crt.Screen.Send("sh int | i error\n" + chr(13))
			crt.Screen.Send("sh int | i CRC\n" + chr(13))
			crt.Screen.Send("sh int\n" + chr(13))
			crt.Screen.Send("sh ip arp\n" + chr(13))
			crt.Screen.Send("sh cdp nei\n" + chr(13))
			crt.Screen.Send("sh cdp nei detail\n" + chr(13))
			crt.Screen.Send("sh vtp status\n" + chr(13))
			crt.Screen.Send("sh int trunk\n" + chr(13))
			crt.Screen.Send("sh etherchannel summary\n" + chr(13))
			crt.Screen.Send("sh etherchannel port-channel\n" + chr(13))
			crt.Screen.Send("sh etherchannel summary\n" + chr(13))
			crt.Screen.Send("sh etherchannel port-channel\n" + chr(13))
			crt.Screen.Send("sh etherchannel brief\n" + chr(13))
			crt.Screen.Send("sh power inline\n" + chr(13))
			crt.Screen.Send("sh vlan summary\n" + chr(13))
			crt.Screen.Send("sh vlan\n" + chr(13))
			crt.Screen.Send("sh vlan brief\n" + chr(13))
			crt.Screen.Send("sh spanning-tree summary\n" + chr(13))
			crt.Screen.Send("sh spanning\n" + chr(13))
			crt.Screen.Send("sh vrrp brief\n" + chr(13))
			crt.Screen.Send("sh standby brief\n" + chr(13))
			crt.Screen.Send("sh version\n" + chr(13))
			crt.Screen.Send("sh switch\n" + chr(13))
			crt.Screen.Send("show switch detail\n" + chr(13))
			crt.Screen.Send("sh switch stack-port\n" + chr(13))
			crt.Screen.Send("sh redundancy\n" + chr(13))
			crt.Screen.Send("sh module\n" + chr(13))
			crt.Screen.Send("sh environment\n" + chr(13))
			crt.Screen.Send("sh bootvar\n" + chr(13))
			crt.Screen.Send("dir\n" + chr(13))
			crt.Screen.Send("dir all\n" + chr(13))
			crt.Screen.Send("sh boot\n" + chr(13))
			crt.Screen.Send("sh bootvar\n" + chr(13))
			crt.Screen.Send("sh run | i boot\n" + chr(13))
			crt.Screen.Send("sh mac address\n" + chr(13))
			crt.Screen.Send("sh ip route summ\n" + chr(13))
			crt.Screen.Send("sh ip route\n" + chr(13))
			crt.Screen.Send("sh ip ospf nei\n" + chr(13))
			crt.Screen.Send("sh ip ospf int brief\n" + chr(13))
			crt.Screen.Send("sh ip ospf\n" + chr(13))
			crt.Screen.Send("sh ip ospf database\n" + chr(13))
			crt.Screen.Send("sh ip route\n" + chr(13))
			crt.Screen.Send("sh ip bgp summ\n" + chr(13))
			crt.Screen.Send("sh ip bgp nei\n" + chr(13))
			crt.Screen.Send("sh running\n" + chr(13))
			crt.Screen.Send("sh log\n" + chr(13))
			crt.Screen.Send("sh ip route summary\n" + chr(13))
			crt.Screen.Send("sh ip route\n" + chr(13))
			crt.Screen.Send("sh ip mroute summary\n" + chr(13))
			crt.Screen.Send("sh ip mroute count\n" + chr(13))
			crt.Screen.Send("sh ip pim neighbor\n" + chr(13))
			crt.Screen.Send("sh ip pim rp mapping\n" + chr(13))
			crt.Screen.Send("sh ip igmp groups\n" + chr(13))
			crt.Screen.Send("ter len 50\n" + chr(13))
			if Result=="y":
				crt.Dialog.MessageBox("Warning:  !! You will be prompted to save the config to the Flash at the end of the script !!\n\n !! Please press enter if you want to save the config to the Flash or press Ctrl+C !!\n\n Please Rise a OUTAGE Ticket for the scheduleded hours.The Link will be prompted in the  window!!")	
				crt.Screen.Send("copy running-config flash:config_"+ x +".old")
			else  :
				crt.Screen.Send("!! Switch backup ends!!\n" + chr(13))
				
			
	elif optHostname =='w':
			crt.Dialog.MessageBox("WLC Backup Starts" )
		
		
			crt.Screen.Send("config paging disable\n" + chr(13))
			crt.Screen.Send("show ap summary\n" + chr(13))
			crt.Screen.Send("show client summary\n" + chr(13))
			crt.Screen.Send("show client detail all\n" + chr(13))
			crt.Screen.Send("show interface summary\n" + chr(13))
			crt.Screen.Send("show cdp neighbor\n" + chr(13))
			crt.Screen.Send("show wlan apgroups\n" + chr(13))
			crt.Screen.Send("show wlan summary\n" + chr(13))
			crt.Screen.Send("show ap image all\n" + chr(13))
			crt.Screen.Send("show ap image\n" + chr(13))
			crt.Screen.Send("show ap config general\n" + chr(13))
			crt.Screen.Send("show AP invent all\n" + chr(13))
			crt.Screen.Send("show inventory\n" + chr(13))
			crt.Screen.Send("show boot\n" + chr(13))
			crt.Screen.Send("show sysinfo\n" + chr(13))
			crt.Screen.Send("show network summary\n" + chr(13))
			crt.Screen.Send("show mobility summary\n" + chr(13))
			crt.Screen.Send("show run-config commands\n" + chr(13))
			crt.Screen.Send("show ap cdp neighbors all\n" + chr(13))
			crt.Screen.Send("show ap join stats summary all\n" + chr(13))
			crt.Screen.Send("show ap summary\n" + chr(13))
			crt.Screen.Send("show client summary\n" + chr(13))
			crt.Screen.Send("show interface summary\n" + chr(13))
			crt.Screen.Send("show cdp neighbor\n" + chr(13))
			crt.Screen.Send("show wlan apgroups\n" + chr(13))
			crt.Screen.Send("show wlan summary\n" + chr(13))
			crt.Screen.Send("show ap image all\n" + chr(13))
			crt.Screen.Send("show AP invent all\n" + chr(13))
			crt.Screen.Send("show inventory\n" + chr(13))
			crt.Screen.Send("show boot\n" + chr(13))
			crt.Screen.Send("show sysinfo\n" + chr(13))
			crt.Screen.Send("show network summary\n" + chr(13))
			crt.Screen.Send("show mobility summary\n" + chr(13))
			crt.Screen.Send("show run-config commands\n" + chr(13))
			crt.Screen.Send("show ap cdp neighbors all\n" + chr(13))
			crt.Screen.Send("show ap join stats summary all \n" + chr(13))
			
			
		
			if Result=="y" :
				crt.Dialog.MessageBox("Sorry !! You can't save the config on the flash in WLC !!\n\n !! Please Rise a OUTAGE Ticket for the scheduleded hours.The Link will be prompted!!\n\n" )
				#crt.Screen.Send("copy running-config flash:config_"+ x +".old")
			
			
			else:
				crt.Screen.Send("!! WLC backup ends!!\n" + chr(13))
			
			 
	else:
		crt.Dialog.MessageBox("!! Wrong input !!\n" + chr(13))
		return "Wrong input"
	if OUT=="y":
		#please add the outgage ticketing tool URL in the below line if there isn't any please add "#" to the same line at the starting
		webbrowser.open('http://www.google.com',new=0, autoraise=True)
	else:
		return "Backup ends"
		
Main()