# python-script-to-interact-with-gcs

- Update the sample app.py script and build the required docker image with `docker build .`
- Push the docker image to docker hub or required container registry
- Setup workload idenity in GCP

## Setup Workload Identity 

- Create a Google Cloud service account ( update the service account and project name)

gcloud iam service-accounts create python-test \
    --project=chimbuc-playground
    
- Add the required permissions (roles/iam.workloadIdentityUser & roles/roles/storage.admin) - Fine tune the permission based on the requirements

gcloud projects add-iam-policy-binding chimbuc-playground \
    --member "serviceAccount:python-test@chimbuc-playground.iam.gserviceaccount.com" \
    --role "roles/storage.objectViewer"

gcloud iam service-accounts add-iam-policy-binding python-test@chimbuc-playground.iam.gserviceaccount.com \
    --role roles/iam.workloadIdentityUser \
    --member "serviceAccount:chimbuc-playground.svc.id.goog[default/python-test]"

## Deploy the app to GKE

- update the serviceaccount.yaml with correct Google cloud service account 
- Update the pod.yaml with correct image name and kubernetes service account name 
- Run `kubectl apply -f .` to deploy the application to GKE and monitor the logs 
