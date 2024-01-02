## Astro CLI

### What is Astro CLI?

![image](https://github.com/vedanthv/data-engg/assets/44313631/2f5e1fc3-f288-499b-adaa-6568e90cc7db)

### Setting Up and Running Astro CLI?

- Astro CLI uses docker to setup and run local dev environment.
- Two Commands to execute are:
    - ```dev init``` to init the local dev envt
    - ```dev start``` to spin up airflow instance

![image](https://github.com/vedanthv/data-engg/assets/44313631/a8cc18a2-c300-4898-8aba-093a0dc26bca)

There are four docker images **Web Server**,**Scheduler**,**Database** and **Triggerer** that are part of a Docker Container called Astronomer Runtime.

### Pushing the DAG to the Production Envt

![image](https://github.com/vedanthv/data-engg/assets/44313631/11963165-96b8-4b5d-a36f-abbe836431dc)

- A request is sent to the Airflow API saying that we need to update the airflow instance of a deployment, a docker image is created with our DAGs and pushed
into the registry.

- Then finally the Aiirflow instance in the data plane is restarted with the new docker instances with DAGs

![image](https://github.com/vedanthv/data-engg/assets/44313631/d3aac538-9e60-4ce2-9f44-73a130aeec3d)

### Installing Astro CLI

Docs : [Click Here](https://docs.astronomer.io/astro/cli/install-cli?tab=windowswithwinget#install-the-astro-cli)

![image](https://github.com/vedanthv/data-engg/assets/44313631/3a17ef3d-5fe5-4418-94c0-1351069f1187)

### Creating a Project

- ```mkdir astro && cs astro```

- ```astro dev init```

![image](https://github.com/vedanthv/data-engg/assets/44313631/67400781-8f0d-4a48-a2b5-c700feb18a70)

- ```airflow_settings.yaml``` allows us to recrete a project without creating variables and connections over and over again.

### Running Airflow

- ```astro dev start``` spins up airflow and downloads the docker images for airflow components.

![image](https://github.com/vedanthv/data-engg/assets/44313631/6a541aae-c382-4f43-8c4b-c5171d9e77e3)

![image](https://github.com/vedanthv/data-engg/assets/44313631/1023fe8b-c00d-4897-b64f-8744ea1c5bac)

### Add additional providers in Airflow

- On astro terminal type ```astro dev run providers list``` to check the list of all the providers.

- if anything is not installed, pip install it from the providers page in the UI and add it to the reqs file.

### Upgrading Astro Runtime

Go to Dockerfile and change the version then run ```asto dev restart```

### Non Base Images v/s Base Image

By default we have the non base image where the folders and dependencies are auto copied to the docker container but if we want to have full control of everything
and add whatever folders we want, we have to use the base image.

We can switch to the base image by changing the command in Dockerfile to ```FROM quay.io/astronomer/astro-runtime:5.3.0-base```

### Persisting Variables after killing Airflow Image

Check how to do this [here](https://academy.astronomer.io/path/airflow-101/local-development-environment/1569583)

### Environment Variables

In the ```.env``` file we can specify the name of the environment as ```AIRFLOW__WEBSERVER__INSTANCE__NAME = ProdEnv```

If we want to keep mutiple environments just add one more file ```.dev``` and add ```ENVIRONMENT = dev``` in that file. 

Now we can start the server with this env, ```airflow dev start --env .dev```

This is only valid in our local environment.

If we want too export the environment variables to the Astro instance, then we need to add ```ENV AIFLOW__WEBSERVER__INSTANCE__NAME = ProdEnv``` to the Dockerfile.

### Checking DAGs for Errors before Running it

If we dodnt want to wait for 5-6 min for the UI to throw up any import or other errors then we can use ```astro dev parse``` to get all the possible errors in 
the command line itself.

We can also use the pytest library for testing using ```astro dev pytest```

Another way to run and compile dags in the cli is ```astro run```. This Trigger a single DAG run in a local Airflow environment and 
see task success or failure in your terminal. This command compiles your DAG and runs it in a single Airflow worker container based on your 
Astro project configurations.

More type of testing like backtesting dependencies during updates is [here](https://docs.astronomer.io/astro/cli/test-your-astro-project-locally)

### How Everything Works?

Step 1 : 
![image](https://github.com/vedanthv/data-engg/assets/44313631/15b456bc-9483-4f16-948a-bb668ae16212)

Step 2 : 
![image](https://github.com/vedanthv/data-engg/assets/44313631/a6ea0d2f-44b3-4ead-9786-450ffed0839a)

Scheduler processes the DAG and we may need to wait upto 5 min before getting the new DAG on the Airflow UI.

Step 3:
![image](https://github.com/vedanthv/data-engg/assets/44313631/482ac766-06b0-4ee2-b7ed-f3dbf34ff5f4)
The scheduler creates the DAGRun Object that has the states running.

Step 4:
![image](https://github.com/vedanthv/data-engg/assets/44313631/08ca70cb-5b40-40d3-a36f-bd36f461e25f)

The scheduler then creates the task instance which is instance of the task at a certain time and it has the state scheduled.

Step 5:
![image](https://github.com/vedanthv/data-engg/assets/44313631/8704266e-8ca1-4ce2-93b3-2bc1adfc3853)

Now the Task Instance is queued and the scheduler sends the taskInstance object to the executor that executes it and the state of the task is complete.

![image](https://github.com/vedanthv/data-engg/assets/44313631/9c62f248-c618-4257-9c7d-3da847e7b3b1)

Now either the task status is success or failed and it updates the state accordingly.

Then the scheduler checks whether the work is done or not.

![image](https://github.com/vedanthv/data-engg/assets/44313631/7cd5614e-cb73-4d13-8ec0-0d33d48915d6)

Finally the Airflow UI is updated.

Check the [video](https://academy.astronomer.io/path/airflow-101/astro-runtime-airflow-concepts/1273942) also.









