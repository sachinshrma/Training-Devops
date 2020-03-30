# Required azure sdk
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption


import Credentials
import ResourceGroup
import AvailabilitySet
import PIP
import VirtualNetwork
import Subnet
import NIC
import VirtualMachine


# Required Variables
GROUP_NAME = 'Python-Sachin'
LOCATION = 'southeastasia'
AVLSET_NAME = 'DemoAVSet'
PIP_NAME = 'DemoPIP'
VNET_NAME = 'DemoVNET'
SUBNET_NAME = 'DemoSubnet'
NIC_NAME = 'DemoNIC'
VM_NAME = 'DemoVM'

if __name__ == "__main__":
    credentials = Credentials.get_credentials()
    rg_client = ResourceManagementClient(
        credentials,
        Credentials.SUBSCRIPTION_ID
    )
    network_client = NetworkManagementClient(
        credentials,
        Credentials.SUBSCRIPTION_ID
    )
    compute_client = ComputeManagementClient(
        credentials,
        Credentials.SUBSCRIPTION_ID
    )
    print(ResourceGroup.create_resource_group(rg_client,GROUP_NAME,LOCATION))
    print(AvailabilitySet.create_availability_set(compute_client,GROUP_NAME,LOCATION,AVLSET_NAME))
    print(PIP.create_public_ip_address(network_client,GROUP_NAME,LOCATION,PIP_NAME))
    print(VirtualNetwork.create_virtual_network(network_client,GROUP_NAME,LOCATION,VNET_NAME))
    print(Subnet.create_subnet(network_client,GROUP_NAME,SUBNET_NAME,VNET_NAME))
    print(NIC.create_nic(network_client,GROUP_NAME,LOCATION,NIC_NAME,VNET_NAME,SUBNET_NAME,PIP_NAME))
    print(VirtualMachine.create_virtual_machine(network_client, compute_client,GROUP_NAME,LOCATION,VM_NAME,NIC_NAME,AVLSET_NAME))
    print('Done')
