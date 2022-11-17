# Create service account
gcloud iam service-accounts create project48a-sa \
    --description="Project48a Service Account" \
    --display-name="project48a-sa"

# Check service account 
gcloud iam service-accounts list 

# Ensure service account has the necessary privileges
gcloud projects add-iam-policy-binding project48a --member serviceAccount:project48a-sa@project48a.iam.gserviceaccount.com --role roles/storage.admin 
gcloud projects add-iam-policy-binding project48a --member serviceAccount:project48a-sa@project48a.iam.gserviceaccount.com --role roles/compute.admin
gcloud projects add-iam-policy-binding project48a --member serviceAccount:project48a-sa@project48a.iam.gserviceaccount.com --role roles/iam.serviceAccountAdmin
gcloud projects add-iam-policy-binding project48a --member serviceAccount:project48a-sa@project48a.iam.gserviceaccount.com --role roles/iam.serviceAccountUser
gcloud projects add-iam-policy-binding project48a --member serviceAccount:project48a-sa@project48a.iam.gserviceaccount.com --role roles/iam.securityAdmin

cd $HOME/Desktop/CMPE_48A/gcp/network

gcloud iam service-accounts keys create gcpkey.json --iam-account project48a-sa@project48a.iam.gserviceaccount.com

# Check if key file is created
cat gcpkey.json

# Gcloud terraform credentials
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/Desktop/CMPE_48A/gcp/network/gcpkey.json"