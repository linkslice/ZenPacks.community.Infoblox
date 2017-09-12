from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class InfobloxDNS(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'InfobloxInfobloxDNS'

    dns_fqdn = None

    _properties = ManagedEntity._properties + (
        {'id': 'dns_fqdn', 'type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('bind_zone', ToOne(ToManyCont,
            'ZenPacks.community.Infoblox.InfobloxDevice',
            'bind_zones',
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
        return self.bind_zone()

    def getRRDTemplateName(self):
        return 'InfobloxDNS'
