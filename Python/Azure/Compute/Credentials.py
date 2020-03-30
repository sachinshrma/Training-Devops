from azure.common.credentials import ServicePrincipalCredentials

SUBSCRIPTION_ID = 'YOUR SUBSCRIPTION ID'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = 'YOUR CLIENT ID',
        secret    = 'YOUR CLIENT SECRET',
        tenant    = 'YOUR TENANT ID'
    )
    return credentials
