#  Uses netifaces module to get network interfaces
#  pip install netifaces

import netifaces

a = netifaces.interfaces()
print(a)
for interface in a:
    b = netifaces.ifaddresses(interface)[netifaces.AF_LINK]
    print(b)
    
    

