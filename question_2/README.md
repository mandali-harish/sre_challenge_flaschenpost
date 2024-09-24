### Overview
This folder contains the Kubernetes Manifest files and Helm charts. The deployment and cronjob can be run using either Kubernetes files or Helm charts.
- The Deployment consists of backend API which runs on Port 80. Liveness and Readiness Probes have been configured for it.
- A CronJob that outputs "Hello SRE" every thirty minutes.
- Also created a NodePort service to test the deployment.

### Pre-requisites:
1. [Kubernetes](https://kubernetes.io/releases/download/) installed. I have used [MiniKube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fdebian+package) for this task. 
2. [Kubectl](https://kubernetes.io/docs/tasks/tools/) installed.
3. [Helm](https://helm.sh/docs/intro/install/) installed

### Usage:
The deployment and cronjob can be run using either Kubernetes files or Helm charts.
1. Deploy using Kubernetes:
```
kubectl apply -f ./Kubernetes
```
Note: To delete
```
kubectl delete -f ./Kubernetes
```

(or)

2. Install using Helm:
```
cd Helm

helm install -f sre_challenge/values.yaml srechallenge ./sre_challenge
```

Note: To uninstall
```
helm uninstall srechallenge
```

3. Deployment can be tested using following commands:
```
# get IP address of Pods using kubectl
kubectl get pods -o wide

# Create a temporary pod to execute curl command
kubectl run temp --image=curlimages/curl:latest -it --rm --restart=Never -- curl <podIP>:<podPort>  

#example:
kubectl run temp --image=curlimages/curl:latest -it --rm --restart=Never -- curl 10.244.0.47:80
```
Output:
```
<html><head><title>HTTP Hello World</title></head><body><h1>Hello from helloworld-http-deployment-6c6fdf865c-2p9b6</h1></body></html
pod "temp" deleted
```
Alternatives:
a. For Minikube:
```
minikube ssh

curl <podIP>:<podPort> # example: curl 10.244.0.47:80
```
Output:
```
<html><head><title>HTTP Hello World</title></head><body><h1>Hello from helloworld-http-deployment-6c6fdf865c-2p9b6</h1></body></html
```

b. If the NodePort service is also running exposing the deployment, then:
```
curl <Node-IPAddr>:<NodePort> # example : curl 192.168.49.2:30134
```
Output:
```
<html><head><title>HTTP Hello World</title></head><body><h1>Hello from helloworld-http-deployment-6c6fdf865c-xpvmj</h1></body></html
```

4. To check the Cronjob :
```
# To check the cronjob status
kubectl get cronjobs

# To check the completed/running jobs of the cronjob
kubectl get jobs

# To check the logs of the job
kubectl logs jobs/<job-name>  # example: kubectl logs jobs/hello-sre-28786830
```
Output:
```
Hello SRE
```