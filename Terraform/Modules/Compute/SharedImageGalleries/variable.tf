variable "prefix" {
    type        = string
    description = "prefix for resource group"
}
variable "projCode" {
    type        = string
    description = "Enter Project Code"
}
variable "svcName" {
    type        = string
    description = "The Main Service which will be running in Virtual Machine"
}

variable "location" {
    type        = string
    description = "Resource group Locatoin"
}

variable "compcount" {
    default     = 1
    type        = number
    description = "Enter Required Number of Compute Instances"
}

variable "rgName" {
    type        = string
    description = "Resource group Name"
}

variable "description" {
    type        = string
    description = "Shared Image gallery description"
    default     = ""
}

variable "tags" {
    type        = map
    description = "Enter Tags for the Reource Groups"  
    default     = {}
}