PROJECT_ID=ton-projet-gcp
REGION=europe-west1
CLUSTER_NAME=idf-weather-cluster

.PHONY: init plan apply build push deploy

init:
	cd terraform && terraform init

plan:
	cd terraform && terraform plan -var="project_id=${PROJECT_ID}"

apply:
	cd terraform && terraform apply -auto-approve -var="project_id=${PROJECT_ID}"

build:
	docker build -t gcr.io/${PROJECT_ID}/weather-app:latest ./app

push:
	docker push gcr.io/${PROJECT_ID}/weather-app:latest

connect:
	gcloud container clusters get-credentials ${CLUSTER_NAME} --region ${REGION}

deploy:
	kubectl apply -f k8s/