resource "azurerm_shared_image_gallery" "sharedImageGalleries" {
  count               = var.compcount
  name                = "${var.prefix}_${var.projCode}_${var.svcName}_sig${count.index}"
  location            = var.location
  resource_group_name = var.rgName
  description         = var.description

  tags = var.tags
}