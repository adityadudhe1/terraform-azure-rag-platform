output "resource_group_name" {
  value = azurerm_resource_group.rag.name
}

output "location" {
  value = azurerm_resource_group.rag.location
}

output "storage_account_name" {
  value = azurerm_storage_account.rag.name
}

output "search_service_name" {
  value = azurerm_search_service.rag.name
}
