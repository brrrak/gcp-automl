
resource "google_compute_instance" "h2ocluster_instances" {
  project = var.h2o_cluster_instance_project
  
  count = var.h2o_cluster_instance_count
  name = "${var.h2o_cluster_instance_name_prefix}-${var.h2o_cluster_instance_user}-${var.h2o_cluster_instance_randstr}-cluster-node-${count.index}"
  description = var.h2o_cluster_instance_description
 
  machine_type = var.h2o_cluster_instance_machine_type
  
  boot_disk {
    initialize_params {
      image = var.h2o_cluster_instance_boot_disk_image
      type = var.h2o_cluster_instance_boot_disk_type
      size = var.h2o_cluster_instance_boot_disk_size
    }
  }
  
  zone = var.h2o_cluster_instance_zone
  network_interface {
    subnetwork = var.h2o_cluster_instance_subnet
    # to make instance private do not include an access_config structure in network_interface structure
    # access_config {}
  }
 
  # For firewall rules later
  tags = ["h2o-nodes", "private"]
  
  # Will use OS Login to the Workspace
  metadata = {
    nodes-count = var.h2o_cluster_instance_count
    nodes-prefix = "${var.h2o_cluster_instance_name_prefix}-${var.h2o_cluster_instance_user}-${var.h2o_cluster_instance_randstr}-cluster-node-"
    project-id = var.h2o_cluster_instance_project
    zone = var.h2o_cluster_instance_zone
    instance-group-name = "${var.h2o_cluster_instance_name_prefix}-${var.h2o_cluster_instance_user}-${var.h2o_cluster_instance_randstr}-cluster" 
    startup-complete = "FALSE"
    h2o-url = var.h2o_download_url
    sshKeys = "${var.h2o_cluster_instance_ssh_user}:${file(var.h2o_cluster_instance_ssh_pubkey_filepath)}"
  }
  
  # Startup script in the server
  metadata_startup_script = file("${path.module}/startup.sh")
  
  
  # Associate a Service Account with the VM instance.
  service_account {
    email = var.h2o_cluster_instance_service_account_email
    scopes = var.h2o_cluster_instance_service_account_scopes
  }
}

resource "google_compute_instance_group" "h2ocluster_instance_group" {
  project = var.h2o_cluster_instance_project

  name = "${var.h2o_cluster_instance_name_prefix}-${var.h2o_cluster_instance_user}-${var.h2o_cluster_instance_randstr}-cluster"
  description = var.h2o_cluster_instance_description
 
  zone = var.h2o_cluster_instance_zone
  
  instances = google_compute_instance.h2ocluster_instances.*.self_link
}
