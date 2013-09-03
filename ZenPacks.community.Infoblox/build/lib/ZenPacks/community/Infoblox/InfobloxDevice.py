from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.Device import Device


class InfobloxDevice(Device):
    bind_zone_count = None

    _properties = Device._properties + (
        {'id': 'bind_zone_count', 'type': 'int'},
        )

    _relations = Device._relations + (
        ('bind_zones', ToManyCont(ToOne,
            'ZenPacks.community.Infoblox.InfobloxDNS',
            'bind_zone',
            )),
        ('dhcp_networks', ToManyCont(ToOne,
            'ZenPacks.community.Infoblox.InfobloxDHCP',
            'dhcp_network',
            )),
        )
