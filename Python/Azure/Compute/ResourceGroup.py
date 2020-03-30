def create_resource_group(rg_client,GROUP_NAME,LOCATION):
    rg_params = {'location' : LOCATION}
    rg_result = rg_client.resource_groups.create_or_update(
        GROUP_NAME,
        rg_params
    )
    return rg_result
