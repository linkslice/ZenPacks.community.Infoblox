(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'InfobloxInfobloxDNS',
    _t('Infoblox BIND Zone'),
    _t('Infoblox BIND Zones'));

ZC.registerName(
    'InfobloxInfobloxDHCP',
    _t('Infoblox DHCP Range'),
    _t('Infoblox DHCP Ranges'));

Ext.onReady(function() {
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);

        overview.addField({
            name: 'bind_zone_count',
            fieldLabel: _t('# BIND Zones')
        });
    });
});

ZC.InfobloxInfobloxDHCPPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'InfobloxInfobloxDHCP',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'dhcp_netmask'},
                {name: 'dhcp_used_percent'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'dhcp_netmask',
                dataIndex: 'dhcp_netmask',
                header: _t('Subnet Mask'),
                sortable: true,
                width: 120
            },{
                id: 'dhcp_used_percent',
                dataIndex: 'dhcp_used_percent',
                header: _t('Percent Used'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.InfobloxInfobloxDHCPPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.InfobloxInfobloxDNSPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'InfobloxInfobloxDNS',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.InfobloxInfobloxDNSPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('InfobloxInfobloxDHCPPanel', ZC.InfobloxInfobloxDHCPPanel);
Ext.reg('InfobloxInfobloxDHCPPanel', ZC.InfobloxInfobloxDNSPanel);

})();
