terraform {
  required_providers {
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
  required_version = ">= 1.4.4"
}

  provider "twc" {
  token = var.token
  }



data "twc_configurator" "configurator" {
  location = "ru-3"
}

data "twc_os" "os" {
  name = "almalinux"
  version = "8.5"

}

resource "twc_server" "my-timeweb-server" {
  name = "My first tf server"
  availability_zone = "msk-1"
  os_id = data.twc_os.os.id

  configuration {
    configurator_id = data.twc_configurator.configurator.id
    disk = 15360
    cpu = 1
    ram = 1024
  }
}
