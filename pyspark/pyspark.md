## PySpark for Large Scale Data Processing

### Internal Working and Architecture of Spark

#### High Level Overview 
![image](https://github.com/vedanthv/data-engg/assets/44313631/fc63ecce-41ce-477b-8964-86a4a4b86d20)

### Flow of the Logic
![image](https://github.com/vedanthv/data-engg/assets/44313631/a0091ce1-edaf-4dce-9754-caf5238f8506)

### Worker Node Architecture
![image](https://github.com/vedanthv/data-engg/assets/44313631/ea6e5e52-7b70-4550-8fef-8858691bbbd2)
- There are total of 64 cores, so 64 processes can execute parallelly and each executor will have 16 processes running.
- There can be partitions within each executor that can remain idle without any process running so we need to define a parameter to define how many min number of processes need to be run on each executor at once.
- To avoid having idle nodes we need to keep the number of partitions as a multiple of the core processor.

### Summary of Spark Application
![image](https://github.com/vedanthv/data-engg/assets/44313631/84d10017-7a63-49cc-97d6-0c9761d7ae47)

### Attributes of Spark
- Its Scalable.
- Its Fault Tolerant and follows lazy evaluation. First Spark makes logical plans to process the data, then it builds a DAG and hence if one worker node goes down we can still recover the data.
- Spark supports multiple programming languages like Python and Scala.
- Spark can handle streaming data also.
- Spark is known for its speed due to in memory computation model.
- Spark has rich libraries for ML and Data Processsing.

### Common Terminologies
![image](https://github.com/vedanthv/data-engg/assets/44313631/f3d39071-82b2-4d95-8bf0-69c5da259f36)

![image](https://github.com/vedanthv/data-engg/assets/44313631/de3e02ff-2580-433f-8183-935ac4b2feda)

Spark does not immediately process the data as mentioned above. When an action is called by the developer for storage or transformation purposes, it processes the data according to the DAG and return the output to the user.

![image](https://github.com/vedanthv/data-engg/assets/44313631/93110364-1dc5-443c-b6ad-9d89edcf7b46)

To store data in on heap memory we need to serialize the data.

### Stages and Tasks 
![image](https://github.com/vedanthv/data-engg/assets/44313631/0c913da4-73d2-4bf2-b844-05a6a38b2797)

### Libraries Suppoprted by Spark
- SQL
- Streaming
- MLLib
- SparkX

### Driver Node Architecture
![image](https://github.com/vedanthv/data-engg/assets/44313631/b1d68634-96f0-4354-9fb6-43c4c28f4265)

### Worker Node Architecture
![image](https://github.com/vedanthv/data-engg/assets/44313631/7ebf4dee-073a-46c3-8c8d-01f6f0ec30b1)

### On Heap Memory Architecture
![image](https://github.com/vedanthv/data-engg/assets/44313631/28abf5f6-c5f2-4a54-8094-5265a4f7fab9)

- Out of 32gb, around 300mb is used by spark for disaster recovery and cannot be used by the user or the processes.
- Of the remaining (32gb - 300mb) we allocate 40% of the heap memory as the user memory and then 60% of the heap memory as the unified memory.
- In unified memory 50% is used for scheduling and 50% of the memory is used for executing.
