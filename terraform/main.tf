resource "azurerm_resource_group" "rag" {
  name     = var.resource_group_name
  location = var.location
}
