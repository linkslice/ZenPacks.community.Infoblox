from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.Infoblox.interfaces import (
    IInfobloxDeviceInfo,
    IInfobloxDHCPInfo,
    )

class InfobloxDeviceInfo(DeviceInfo):
    implements(IInfobloxDeviceInfo)
   
    bind_zone_count = ProxyProperty('bind_zone_count')

class InfobloxDHCPInfo(ComponentInfo):
    implements(IInfobloxDHCPInfo)
    
    dhcp_netmask = ProxyProperty('dhcp_netmask')
    dhcp_used_percent = ProxyProperty('dhcp_used_percent')
