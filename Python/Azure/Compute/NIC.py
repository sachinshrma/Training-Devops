def create_nic(network_client,GROUP_NAME,LOCATION,NIC_NAME,VNET_NAME,SUBNET_NAME,PIP_NAME):
    subnet_info = network_client.subnets.get(
        GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME
    )
    publicIPAddress = network_client.public_ip_addresses.get(
        GROUP_NAME,
        PIP_NAME
    )
    nic_params = {
        'location': LOCATION,
        'ip_configurations': [{
            'name': 'DemoIPConfig',
            'public_ip_address': publicIPAddress,
            'subnet': {
                'id': subnet_info.id
            }
        }]
    }
    nic_result = network_client.network_interfaces.create_or_update(
        GROUP_NAME,
        NIC_NAME,
        nic_params
    )

    return nic_result
