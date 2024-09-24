### Overview
This folder contains Terraform code for managing and provisioning infrastructure in Azure. 

### Pre-requisites:
- Azure cli installed on local machine.
```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```
- Login into azure cli. 
```
az login
```
- [Terraform](https://developer.hashicorp.com/terraform/install) must be installed.

### Usage:
- Necessary variables and provider settings can be configured through [variables.tf](variables.tf) and [provider.tf](provider.tf) files.
- Outputs have been configured in the [outputs.tf](outputs.tf)
- Note: subscription_id under provider "azurerm" must be specified for terraform plan to run with errors.

- Commands to run and store the terraform plan:
```
terraform init

terraform plan -no-color > tfplan.txt

```