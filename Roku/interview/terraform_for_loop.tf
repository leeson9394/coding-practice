# How would you modify main.tf and variable.tf files so that we can create the resource based on inputs in locals

# variable.tf :

variable "network_name" {
  description = "Name of the network"
  type        = string
}

variable "network_detail" {
  type = map(object({
    prefix_length = string
    address       = string
    address_type  = string
  }))
}

# **********

# main.tf :
resource "google_compute_global_address" "private_ip_alloc" {
  network_name  = var.network_name
  for_each      = var.network_detail
  name          = each.key
  prefix_length = each.value.prefix_length
  address       = each.value.address
  address_type  = each.value.address_type
}

# **********

locals {
  network_name = "roku-network"
  network_detail = {
    "first" = {
    prefix_length = 24
    address = "10.10.10.0"
    address_type = "EXTERNAL"
    }
    "second" = {
    prefix_length = 23
    address = "10.10.20.0"
    address_type = "INTERNAL"
    }
    "third" = {
    prefix_length = 22
    address = "10.10.30.0"
    address_type = "EXTERNAL"
    }
  }
}
