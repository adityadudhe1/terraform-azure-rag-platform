resource "azurerm_resource_group" "rag" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "rag" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.rag.name
  location                 = azurerm_resource_group.rag.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_search_service" "rag" {
  name                = var.search_service_name
  resource_group_name = azurerm_resource_group.rag.name
  location            = azurerm_resource_group.rag.location
  sku = "free"
}

resource "azurerm_cognitive_account" "rag" {
  name                = var.openai_account_name
  location            = azurerm_resource_group.rag.location
  resource_group_name = azurerm_resource_group.rag.name
  kind     = "OpenAI"
  sku_name = "S0"
}
