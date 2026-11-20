terraform {
  cloud {
    organization = "adityadudhe1"

    workspaces {
      name = "terraform-azure-rag-platform"
    }
  }

  required_version = ">= 1.5"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}
