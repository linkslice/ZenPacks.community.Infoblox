from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class InfobloxDHCP(SnmpPlugin):
    relname = 'dhcp_networks'
    modname = 'ZenPacks.community.Infoblox.InfobloxDHCP'

    snmpGetTableMaps = (
        GetTableMap(
            'ibDHCPSubnetEntryTable', '1.3.6.1.4.1.7779.3.1.1.4.1.1.1', {
                '.1': 'ibDHCPSubnetNetworkAddress',
                '.2': 'ibDHCPSubnetNetworkMask',
                '.3': 'ibDHCPSubnetNetworkPercentUsed',
                }
            ),
        )

    def process(self, device, results, log):
        dhcp_networks = results[1].get('ibDHCPSubnetEntryTable', {})
        rm = self.relMap()
        for snmpindex, row in dhcp_networks.items():
            name = row.get('ibDHCPSubnetNetworkAddress')
            if not name:
                log.warn('Skipping empty zone')
                continue

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'dhcp_netmask': row.get('ibDHCPSubnetNetworkMask'),
                'dhcp_used_percent': row.get('ibDHCPSubnetNetworkPercentUsed'),
                }))

        return rm
