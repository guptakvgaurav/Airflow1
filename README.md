# Airflow



### Airflow install


#### How to install docker

https://docs.docker.com/desktop/windows/install/

 

1. Download the docker 
2. Download docker registry/dockerhub  and create an account
3. Go to vs code 
4. Download extension of docker
5. Go to explorer and clone my repos 
6. Github link
https://github.com/rafiqul0396/Airflow1.git

7   then open  new terminal
8. cmd= docker-compose up –build
9. Go to chrome  and write
10.localhost:8080



### What is Airflow?


###  What is workflow
 
 
### Typical workflows?



### How an ETL process happen
1.Download data from source 
2. Send the data some where else to process 
3. Monitor the result and generate the response
4. Send the report out by email




### Airflow DAG 
A workflow as a DAG  with multiple tasks
Which can be executed independently
 Airflow DAGs are composed of Tasks






### Writing your first Workflow
A Dag file,which is basically just a python scripts ,is a configuration file specifying the Dags structure as code
##### There are 5 steps to write Airflow Dags or workflow
     1.importing modules
     2. Default Arugments
     3. Instantiate a DAG
     4.Tasks
     5. Setting up Dependencies


An object instantiated from an operator is called a task. The first argument task_id acts as a unique identifier for the task.

##### Operators and Tasks
  DAG do not perform any actual  computation .instead ,operatorators  determine what actually get  done
###  Task:
Once an operator is instanciated it is referred as single task

__ instantantiating a task requires or providing  a unique task_id and DAG container

### There are three types of Operators 
Sensors
Operators 
transfer



### Sensors: 
a certain type of operator that will keep running until a certain criteria is met
Ex-   including waiting  for  a certain time
External files
Upstream


HdfsSensor
NameHivepartionSensor


### Operators 

Triggers a certain action 
Ex- run a bash command 
Excute a python function
Execute HiveQuery

Bashoperator
PythonOperator
HiveOperator






https://medium.com/@knoldus/creating-dag-in-apache-airflow-f9a2e252

https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#tasks
https://github.com/tuanavu/airflow-tutorial


https://docs.docker.com/desktop/windows/install/


