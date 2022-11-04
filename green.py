import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from mahadi import mahadinx
 
        mahadinx()
 
 
 
elif bit == "32bit":
 
        from mahadi32 import mahadinx
 
 
        mahadinx()
 
