resource "azurerm_availability_set" "availabiltiySet" {
  count               = var.compcount
  name                = "${var.prefix}-${var.projCode}-${var.svcName}-avail${count.index}"
  location            = var.location
  resource_group_name = var.rgName

  platform_update_domain_count = var.updateDomcount
  platform_fault_domain_count  = var.faultDomcount

  tags = var.tags
}