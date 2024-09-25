### Overview
This folder contains Terraform code for managing and provisioning infrastructure in Azure. 

### Pre-requisites:
- [Azure cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed on local machine.

- [Login](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login) into azure cli. 
```
az login
```
- [Terraform](https://developer.hashicorp.com/terraform/install) must be installed.

### Usage:
- Necessary variables and provider settings can be configured through [variables.tf](variables.tf) and [provider.tf](provider.tf) files.
- Outputs have been configured in the [outputs.tf](outputs.tf)
- Note: subscription_id under provider "azurerm" must be specified for terraform plan to run without errors.

- Commands to run and store the terraform plan:
```
terraform init

terraform plan -no-color > tfplan.txt

```

#### Note:
 For Storage Account Container resource, the storage account name has been shortened to 'srechallengeflaschenpost' instead of the given 'srechallengeforflaschenpost' as the limitation on max number of characters in name is 24.