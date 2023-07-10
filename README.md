# App with MySQL Integration

This project is a Flask application that connects to a MySQL container. The project structure is as follows:

```
app-mysql/
├── app
│   ├── app.py
│   ├── Dockerfile
│   ├── flask_app_container_run.sh
│   └── requirements.txt
└── mysql
    ├── Dockerfile
    └── mysql_container_run.sh

```

# Project Description

The objective of this project is to learn and demonstrate how to set up a Docker network to connect a Flask application with a MySQL container. By creating a bridge network, both containers can communicate with each other using container names as hostnames.

# Prerequisites

Before running the application, ensure that you have the following:

	- Docker installed on your system
	- Basic knowledge of Docker and containerization concepts

# Setting Up the Application

Follow the steps below to set up and run the application:

1. Clone the project repository:

```
git clone Docker-Network-Demo
```

2. create a bridge network

```
docker network create \
--driver bridge
--subnet 172.17.0.0/24
--gateway 172.0.0.1
app-mysql-network
```

3. check if the network is created as desired

```
docker network ls 
docker network inspect app-mysql-network
```

4. navigate to mysql directory

```
cd mysql
```

This directory has following structure:

```
mysql/
├── Dockerfile
└── mysql_container_run.sh
```
5. Build a mysql image based on the specification in Dockerfile:

```
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=prabin12345
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=flask
ENV MYSQL_PASSWORD=prabin123
```
Docker command to build image in the current directory:

```
docker build -t mysql_db .
```

6. run the mysql_container_run.sh

```
sudo chmod +x mysql_container_run.sh
./mysql_container_run.sh
```

This script runs the following command to create a mysql container:

```
docker run -d --name mysql_host -v mysql-data:/var/lib/mysql --network app-mysql-network mysql_db
```

Name of the container should be mysql_host as the flask app need to connect to db_host=mysql_host

7. Ensure that the mysql is up and running

```
docker logs mysql_host
```

8. Build the flask application container

```
cd app
docker build -t flask_app .
docker run -d --name flask_app -p 5000:5000 --network app-mysql-network flask_app
```
9. Access the application in your browser at 'http://localhost:5000'.


# Conclusion

This project showcases the usage of Docker networks to enable communication between containers. By placing both the Flask application and the MySQL container within the same network (app-mysql-network), they can discover and communicate with each other using their container names as hostnames. This approach provides a scalable and isolated environment for containerized applications.

