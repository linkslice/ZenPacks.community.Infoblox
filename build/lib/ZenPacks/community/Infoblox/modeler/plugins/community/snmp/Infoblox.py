from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class Infoblox(SnmpPlugin):
    snmpGetTableMaps = (
        GetTableMap(
            'ibBindZoneNameTable', '1.3.6.1.4.1.7779.3.1.1.3.1.1.1', {
                '.1': 'ibBindZoneName',
                '.2': 'ibBindZoneSuccess',
                '.3': 'ibBindZoneReferral',
                '.4': 'ibBindZoneNxRRset',
                '.5': 'ibBindZoneRecursion',
                '.6': 'ibBindZoneNxDomain',
                '.7': 'ibBindZoneFailure',
                }
            ),
        )

    def process(self, device, results, log):
        bind_zones = results[1].get('ibBindZoneNameTable', {})
        rm = self.relMap()
        for snmpindex, row in bind_zones.items():
            name = row.get('ibBindZoneName')
            if not name:
                log.warn('Skipping empty zone')
                continue

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                }))

        return rm
