**CS 200 Assignment--Kubernetes**

Kuangyou Chen

**What is Kubernetes**

Kubernetes is an open source system that is applied in “automating deployment, scaling, and management of containerized applications.” It has a relatively large and rapidly-developing ecosystem, which is able to support community’s thoughts and practical applications. Based on the profound experience in the workload evaluation of large-scale production, Google develops Kubernetes in order to package and execute the applications in a software development environment. 

**Why Kubernetes**

In the software development process, developers need tools to help monitor and manage the applications. The service of Kubernetes is able to isolate the application and share the development environment in various operating systems at the same time. Additionally, the risk of servers may also be an issue. The guarantee of servers and containers are required in order to keep the stability and efficiency. Kubernetes offers a flexible cloud platform for distributed computing and automatic mode of operation on extension, troubleshooting and management setting.

**Service**

Here is the service that Kubernetes is able to provide, according to the Kubernetes official tutorial. 

Service discovery and load balancing

Storage orchestration

Automated rollouts and rollbacks

 Automatic bin packing

Self-healingSecret and configuration management



**Design** 

Kubernetes define a series of modes in the configuration design to figure out the mechanism that developers can collaborate on the distribution, extension and maintenance of the product.

Pod is the basic dispatch unit in Kubernetes. The high level abstraction could be added into containerized components by pods. Several containers are set in one pod to monitor the development process and share resources. Each pod would be addressed as a unique IP address to avoid conflict issues. 

Tag selectors append key tag values into the programming interface modes. As the mechanism of division, tag selectors help determine the necessary components in the development process. 

Controllers are responsible for converting the actual cluster status into the requirement. They work by compiling and executing the pods to deal with complicated commands. 



Reference:

https://en.wikipedia.org/wiki/Kubernetes

https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/