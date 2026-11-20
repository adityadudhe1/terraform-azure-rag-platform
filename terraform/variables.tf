variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

variable "search_service_name" {
  description = "Azure AI Search Service Name"
  type        = string
}

variable "openai_account_name" {
  description = "Azure Opena AI Account Name"
  type = string
}

variable "storage_account_name" {
  description = "Storage Account Name"
  type        = string
}
