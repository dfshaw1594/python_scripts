# Network interface functions using netifaces libaries

import netifaces

def get_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces
    
def get_gateways():
    gateway_dict = {}
    gws = netifaces.gateways()
    for gw in gws:
        try:
            gateway_iface = gws[gw] [netifaces.AF_INET]
            gateway_ip, iface = gateway_iface[0], gateway_iface[1]
            gw_list = [gateway_ip, iface]
            gateway_dict[gw]=gw_list
        except:
            pass
        return gateway_dict

def get_address(interfaces):
    addrs = netifaces.ifaddresses(interface)
    link_addr = addres[netifaces.AF_INET]
    iface_addres = addrs[netifaces.AF_INET]
    iface_dict = iface_addrs[0]
    link_dict = link_addr[0]
    hwaddr = link_dict.get('addr')
    iface_addr = iface_dict.get('addr')
    iface_broadcast = iface_dict.get('broadcast')
    iface_netmask = iface_dict.get('netmask')
    return hwaddr, iface_addr, iface_broadcast, iface_netmask
    
    
    
