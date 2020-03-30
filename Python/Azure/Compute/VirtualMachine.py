def create_virtual_machine(network_client, compute_client,GROUP_NAME,LOCATION,VM_NAME,NIC_NAME,AVLSET_NAME):
    nic = network_client.network_interfaces.get(
        GROUP_NAME, 
        NIC_NAME
    )
    avset = compute_client.availability_sets.get(
        GROUP_NAME,
        AVLSET_NAME
    )
    vm_parameters = {
        'location': LOCATION,
        'os_profile': {
            'computer_name': VM_NAME,
            'admin_username': 'sachin',
            'admin_password': 'Sachin@123'
        },
        'hardware_profile': {
            'vm_size': 'Standard_F1'
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'Canonical',
                'offer': 'UbuntuServer',
                'sku': '18.04-LTS',
                'version': 'latest'
            }
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic.id
            }]
        },
        'availability_set': {
            'id': avset.id
        }
    }
    creation_result = compute_client.virtual_machines.create_or_update(
        GROUP_NAME, 
        VM_NAME, 
        vm_parameters
    )

    return creation_result.result()

