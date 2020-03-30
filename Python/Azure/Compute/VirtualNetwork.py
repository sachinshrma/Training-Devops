def create_virtual_network(network_client,GROUP_NAME,LOCATION,VNET_NAME):
    vnet_params = {
        'location' : LOCATION,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
    vnet_result = network_client.virtual_networks.create_or_update(
        GROUP_NAME,
        VNET_NAME,
        vnet_params
    )
    return vnet_result
