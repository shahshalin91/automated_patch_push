# automated_patch_push

EAPI script to push extensions across list of devices using Python
====================================================================

Requiremts
-----------
1) Only supported for Linux/Mac OS
2) Install jsonrpclib python module
``````````````````````````````
  pip install jsonrpclib
``````````````````````````````

3) enable eAPI on the switch
```````````````````````````````````````````````````````````````````````````````
   Arista> enable
   Arista# configure terminal
   Arista(config)# management api http-commands
   Arista(config-mgmt-api-http-cmds)# [no] shutdown
   Arista(config-mgmt-api-http-cmds)# [no] protocol https [port ]
   Arista(config-mgmt-api-http-cmds)# [no] protocol http [port ]

```````````````````````````````````````````````````````````````````````````````   
   
4) Create hosts.txt file with list of hosts as follows:
````````````````
   10.20.30.12
   10.20.30.13
````````````````

Run the Script
------------------
1) Run script as python automated_patch_push.py
2) The script will generate output_logs.txt file with status of switch in terms of Installation


Output
---------

`````````````````````````````````````````````````````````````````````````````````````````````````
shalin:Downloads shalin$ python security_patch_push.py 
Username:cvpadmin
Password:
COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH 10.20.30.6 
 Please wait for few secs.....
 
SecurityAdvisory0030-Hotfix.swix              100%  103KB 564.2KB/s   00:00    

COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH 10.20.30.6 SUCCESFUL
INSTALLING EXTENSION SecurityAdvisory0030-Hotfix.swix SUCCESFUL for 10.20.30.6
==================================================================================================

COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH 10.20.30.70 
 Please wait for few secs.....
 
SecurityAdvisory0030-Hotfix.swix              100%  103KB 604.7KB/s   00:00    

COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH 10.20.30.70 SUCCESFUL
INSTALLING EXTENSION SecurityAdvisory0030-Hotfix.swix SUCCESFUL for 10.20.30.70
==================================================================================================

COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH 10.20.30.71 
 Please wait for few secs.....
 
SecurityAdvisory0030-Hotfix.swix              100%  103KB 718.9KB/s   00:00    

COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH 10.20.30.71 SUCCESFUL
INSTALLING EXTENSION SecurityAdvisory0030-Hotfix.swix SUCCESFUL for 10.20.30.71
==================================================================================================

`````````````````````````````````````````````````````````````````````````````````````````````````
