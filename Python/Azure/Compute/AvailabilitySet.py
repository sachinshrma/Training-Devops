def create_availability_set(compute_client,GROUP_NAME,LOCATION,AVLSET_NAME):
    avset_params = {
        'location': LOCATION,
        'sku': { 'name': 'Aligned' },
        'platform_fault_domain_count': 2
    }
    availset_result = compute_client.availability_sets.create_or_update(
        GROUP_NAME,
        AVLSET_NAME,
        avset_params
    )
    return availset_result
