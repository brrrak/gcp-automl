# dont change value of global_prefix.
global_prefix = "h2o"

gcp_project_id = "project48a"
gcp_project_region = "europe-west1"
gcp_project_zone = "europe-west1-c"

vpc_private_subnet_id = " https://www.googleapis.com/compute/v1/projects/project48a/regions/europe-west1/subnetworks/h2o-vpc-private-subnet"

h2o_cluster_instance_count = "3"
h2o_cluster_instance_machine_type = "e2-highmem-4"
h2o_cluster_instance_boot_disk_image = "packer-h2o-3-38-0-2-112122"
h2o_cluster_instance_boot_disk_type = "pd-ssd"
h2o_cluster_instance_boot_disk_size  = 30

h2o_cluster_instance_service_account_email = "h2ocluster-vm-sa@project48a.iam.gserviceaccount.com"
h2o_cluster_instance_service_account_scopes = ["cloud-platform"]

h2o_download_url = "http://h2o-release.s3.amazonaws.com/h2o/rel-zygmund/2/h2o-3.38.0.2.zip"
