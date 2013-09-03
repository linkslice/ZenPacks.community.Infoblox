from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class InfobloxDHCP(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'InfobloxInfobloxDHCP'
   
    dhcp_netmask = None
    dhcp_used_percent = None

    _properties = ManagedEntity._properties + (
        {'id': 'dhcp_netmask', 'type': 'string'},
        {'id': 'dhcp_used_percent','type': 'int'},
        )

    _relations = ManagedEntity._relations + (
        ('dhcp_network', ToOne(ToManyCont,
            'ZenPacks.community.Infoblox.InfobloxDevice',
            'dhcp_networks',
            )),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.dhcp_network()

    def getRRDTemplateName(self):
        return 'InfobloxDHCP'
