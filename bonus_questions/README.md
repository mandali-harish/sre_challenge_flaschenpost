## Design and Implementation of a Scalable Microservices Architecture

### 1. Scalability Triggers and Strategies

i. Backend microservices
    a. Resource Metrics: High CPU or Memory Utilization can be set as a trigger to scale the Backend microservices.
    b. Latency: If the response time is increasing beyond a set threshold, then it can be used as a trigger to scale.
    c. Number of requests: If the total number of requests have increased beyond a set threshold.

ii. Database performance
    a. Resource Metrics: High CPU or Memory Utilization can be set as a trigger to scale.
    b. I/O Throughput: Heavy read or write operations can slowdown the database performance and hence can be set as a trigger.
    c. Latency: Database query response time exceeding set thresholds.
    d. Connection Pooling: If the connection pool is exhausted, can cause delays and timeouts.

iii. Messaging systems
    a. Memory usage: If message systems are running out of memory.
    b. Workload based: Scaling the systems based on the workload across the queues.
    c. Message Queue size: Message queue size can grow significantly without being consumed, this indicates that consumers are not keeping up, triggering a need for scaling.

iv. Containerized services running on a Kubernetes cluster
    a. Resource Metrics: Standard resource management data such as memory and CPU consumption metrics.
    b. Custom Metrics: Service specific metrics such as request throughput, latency, dependencies can be collected and used to scale the services.

### 2. Logging and Monitoring Strategy

a. Approaches for log aggregation across different components:
    Having a centralized logging to aggregate logs from frontend services, backend microservices, databases, and message brokers would be the preferred approach. 
b. Types of logs:
    i. Frontend services: User activities such as logins, checkouts, carts, payments.
    ii. Backend services: API requests/ responses, Error logs 
    iii. Databases: Connection logs, Audit logs, Query logs
    iv. Message brokers: Message logs, Error logs
c. Tools that can be used for log aggregation, storage and querying would be Elasticsearch, FluentBit, Fluentd, Logstash.
d. Monitoring Setup: Kibana, Prometheus and Grafana can be used to monitor and setup alerts.
    Key Metrics: 
        - CPU, Memory usage
        - Pod status
        - Disk usage
        - Network Throughput
        - Latency
        - Database Performance and connectivity
        - Message Queue Performance
        - Frontend and Backend service related custom metrics
    Alerting Mechanism: Alerts should be based on the key metrics and thresholds to trigger automatic notifications via message or email channels.

### 3. CI/CD Pipeline

a. An example CI/CD pipeline for python based backend microservice has been written in [ci-cd.yaml](ci-cd.yaml) file using Github Actions.
b. Tools used at each stage:
    i. Build and Test: 
        - pytest: For unit testing
        - pylint: Analyze code
    ii. Containerization:
        - Docker: For containerizing the backend service
    iii. Continuous Integration:
        - pytest: For integration testing and mocking services
    iv. Continuous Delivery:
        - Azure Kubernetes Services: To setup staging kubernetes clusters
        - Helm: To install the microservices
    v. Continuous Deployment:
        - Manual approval: Manual approval to trigger the deployment to production
        - Azure Kubernetes Services: To setup production kubernetes clusters
        - Helm: To install the microservices

### 4. Architecture Diagram
<img src="sre-flaschenpost-architecture.svg">


### 5. Chaos Engineering Plan
The main purpose is to test if the system can recover from unexpected failures while maintaining high availability and not impacting user experience. By injecting faults into the system in a controlled setting, weaknesses can be identified and system can be made robust and resilient.

Failure simulations:
1. Bringing down a node in the AKS cluster to test Auto scaling
    Measurements: 
    a. Time to scale to desired healthy nodes.
    b. Time to spin up new pods to replace the pods lost due to the unhealhy node.
    c. Any service disruptions caused due to this.

2. Pod deletions
    Measurements:
    a. Impact on services
    b. Time to recover to desired number of pod replicas.
    c. Errors caused in the downstream services.
    d. Latency

3. Disk full on Databases or Kubernetes Nodes
    Measurements:
    a. Databases should be able to prevent further writes but serve read requests.
    b. Alerting if disk space reaches a critical threshold.
    c. Auto-scaling for storages.

4. Rebooting Database instances
    Measurments:
    a. Check if the a new Master node is elected from the read replicas if the existing master node goes down.
    b. Time taken for the failover.
    c. Lost Data or failed transactions.
    d. Latency in query responses.

5. High I/O on Databases, Message queues can be tested
    Measurements:
    a. Read/ Write Latencies can be measured.
    b. Measure if any data is lost.

6. Unavailability of an entire Availability zone
    Measurements:
    a. Time to failover to other Availability zones.
    b. Data replication across Availability zones.
    c. Autoscaling across Availability zones.
    d. Downtime on any services.