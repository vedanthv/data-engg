## Databricks and PySpark 

### Structure of the Course

![image](https://github.com/vedanthv/data-engg/assets/44313631/54d01f29-67c8-42fd-b960-c06cfee5b1bb)

### High Level Overview Of Azure Databricks

![image](https://github.com/vedanthv/data-engg/assets/44313631/bbf82420-852c-4392-b987-374653c96c08)

At the core of Azure Databricks is the open source distributed compute processing engine called Apache Spark, which is widely used in the industry for developing big data projects. 
Databricks is a company created by the founders of Apache Spark, to make it easier to work with Spark by providing the necessary management layers. 
Microsoft makes, the Databricks service available on its Azure Cloud platform as a first party service. These three offerings together makes Azure Databricks.

### Apache Spark Fundamentals

![image](https://github.com/vedanthv/data-engg/assets/44313631/a1615348-c8da-4e3e-8896-a8e4054f37b7)

### Apache Spark Architecture

![image](https://github.com/vedanthv/data-engg/assets/44313631/95991341-e293-468a-b9f7-4d13fc73381d)

- Catalyst Optimizer converts the code into a high level optimization plan and Tungsten helps with memory management.

### Azure Databricks for Spark

![image](https://github.com/vedanthv/data-engg/assets/44313631/c0941bb9-ddcd-47ca-baf6-9f483bb4ab99)

### Azure Databricks Architecture

Databricks Architecture is basically split into two parts, one called the Control Plane and another one called the Data Plane.

Control plane is located in Databricks own subscription.

This contains the Databricks UX and also the Cluster Manager.

It's also home to the Databricks File System (DBFS) and also metadata about Clusters, Files mounted, etc. Data Plane is located in the customer subscription.

When you create a Databricks service in Azure, there are four resources created in your subscription, a Virtual Network and Network Security Group for the Virtual Network.
Azure Blob Storage for the default storage and also a Databricks Workspace.

When a user requests for a cluster, Databricks Cluster Manager will create the required virtual machines in our subscription via the Azure Resource Manager.

So none of the customer data leaves a subscription.

Temporary outputs such as running a display command or data for manage tables, are stored in the Azure Blob Storage, and the processing also happens within the 
VNet in our subscription. The Azure Blob Storage we have shown here is the default storage or otherwise called the DBFS a route, and it's not recommended as a 
permanent data storage.

![image](https://github.com/vedanthv/data-engg/assets/44313631/c0312226-dada-4d5a-ba5f-9f58fe3b2e79)

### Clusters in Databricks

![image](https://github.com/vedanthv/data-engg/assets/44313631/a1d183e6-ff83-4517-9d75-2a4d5875de39)

![image](https://github.com/vedanthv/data-engg/assets/44313631/33deceff-52bb-4a3e-ade5-c3e99364d3d1)

### Cluster Configuration

**# of Nodes**

Single Node - only one VM 
Multi Node - Has Main Node and Worker Nodes

![image](https://github.com/vedanthv/data-engg/assets/44313631/5df93968-cb32-4067-ad62-ccaa674c85d5)

**Access Modes**
![image](https://github.com/vedanthv/data-engg/assets/44313631/764b0c93-3b69-48f2-90c8-075c8e1107b6)

**Databricks Runtime Configuration**
![image](https://github.com/vedanthv/data-engg/assets/44313631/1dce7f80-3f2a-4df4-b73b-cdea00ea6568)

**Auto Termination**
![image](https://github.com/vedanthv/data-engg/assets/44313631/afd1ae00-f00c-4554-941b-7d8d31ec044a)

**Auto Scaling**
![image](https://github.com/vedanthv/data-engg/assets/44313631/8e9bfd4e-6157-477f-9050-9940a0adadb3)

**Cluster Policies**

- Can be set by the administrators to limit the use of clusters that extend beyond a certain budget or memory constraint.
- Simplifies the UI
