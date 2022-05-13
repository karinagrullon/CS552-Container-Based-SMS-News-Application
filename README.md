# CS552 - Container Based SMS News Application

The Container Based SMS News Applicattion provides on-demand news information through Short Message Service (SMS) to people who do not have access to the internet. E.g. People who live in remote/rural areas. 

By developing the SMS information service we have created a communication platform with the aid of Cloud Computing to manage workload resources. We  measure requests from users to the server with the help of Chaos Mesh tool, and allocate the necessary (CPU) resources for the application to run smoothly. 

In order to complete this project we have used communications tool API to manage SMS, and a News media API to retrieve the information requested by the user. For containerization we have used Docker and for container orchestration we have implemented Kubernetes. Local testing is done with the aid of Minikube by creating a Kubernetes cluster in Google Cloud Platform (GCP). 



## Platforms

- Python
- [Twilio API](https://www.twilio.com/)
- [News API](https://newsapi.org/)
- Docker
- Kubernetes
- Minikube
- [Chaos Mesh](https://chaos-mesh.org/)


