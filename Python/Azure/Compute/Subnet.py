def create_subnet(network_client,GROUP_NAME,SUBNET_NAME,VNET_NAME):
    subnet_params = {
        'address_prefix': '10.0.0.0/24'
    }
    subnet_result = network_client.subnets.create_or_update(
        GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME,
        subnet_params
    )

    return subnet_result
