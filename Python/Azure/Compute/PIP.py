def create_public_ip_address(network_client,GROUP_NAME,LOCATION,PIP_NAME):
    pip_params = {
        'location' : LOCATION,
        'public_ip_allocation_method' : 'Static',
        'public_ip_address_version' : 'IPv4'
    }
    pip_result = network_client.public_ip_addresses.create_or_update(
        GROUP_NAME,
        PIP_NAME,
        pip_params
    )
    return pip_result
