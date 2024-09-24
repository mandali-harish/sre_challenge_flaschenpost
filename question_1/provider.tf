terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.3.0"
    }
  }
}
provider "azurerm" {
  # Configuration options
  features {}
  subscription_id = "170825e5-22b4-45d2-b8bf-93fc2a3d8d17"
}