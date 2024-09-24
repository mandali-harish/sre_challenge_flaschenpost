resource "azurerm_resource_group" "sre-challenge-flaschenpost" {
  name     = "sre-challenge-flaschenpost"
  location = var.location

  tags = {
    department = var.department
  }
}

resource "azurerm_storage_account" "srechallengeflaschenpost" {
    name = "srechallengeflaschenpost"
    resource_group_name = azurerm_resource_group.sre-challenge-flaschenpost.name
    location = var.location
    account_tier = "Standard"
    account_replication_type = "LRS"
    access_tier = "Hot"
    tags = {
        department = var.department
    }
}

resource "azurerm_storage_container" "sre" {
    name = "sre"
    container_access_type = "private"
    storage_account_name = azurerm_storage_account.srechallengeflaschenpost.name
}
