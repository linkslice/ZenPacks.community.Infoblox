from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IInfobloxDeviceInfo(IDeviceInfo):
    bind_zone_count = schema.Int(title=_t('Number of BIND Zones'))

class IInfobloxDHCPInfo(IComponentInfo):
    dhcp_netmask = schema.TextLine(title=_t('DHCP Netmask'))
    dhcp_used_percent = schema.TextLine(title=_t('DHCP Percent Used'))
    
