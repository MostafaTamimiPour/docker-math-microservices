## Overview

This project is a demonstration of basic **math microservices** — including Adder, Subtractor, Multiplier, Divider, and a Controller — built with Python (Flask) and orchestrated using **Docker Compose**. Each service runs independently and communicates via REST APIs, while results are stored centrally in a Redis instance. The setup provides a simple yet practical example of designing, connecting, and running multiple microservices in a containerized environment.


### Key Components

- **Redis Database**  
  Used for shared state and lightweight data exchange between microservices.  
  Data such as number lists and operation results are stored and queried from Redis keys.

- **Adder Service (`adder`)**  
  Reads a list of numbers from Redis (key: `sum_list`), calculates their sum, stores the result, and exposes the result via an HTTP endpoint.


- **Subtractor Service (`subtractor`)**  
  Reads a list of numbers from Redis (`sub_list`), calculates the sum, and then computes:  
  **result = 1000 - sum(sub_list)**  
  The result is stored in Redis and also exposed via the service’s HTTP endpoint. Includes error handling for empty lists or invalid numbers.

- **Multiplier Service (`multiplier`)**  
  Reads a list of numbers from Redis (`mul_list`), calculates the product, stores the result, and serves it via HTTP.

- **Divider Service (`divider`)**  
  Reads two lists from Redis (`sum_list` and `sub_list`), sums each, divides the first sum by the second (with error handling), and stores the result.

- **Controller Service (`controller`)**  
  Serves as the system's entry point, provides a `/compute` HTTP endpoint, and handles forwarding requests to the correct microservice based on operation.



### Quick Start

- This section will help you quickly set up and test all services using Docker Compose, Redis, and example data.

- Tip: It is recommended to use tmux for splitting your terminal windows when running the following commands. Some Docker commands (such as docker compose up) will occupy the terminal session, and you may be limited to a single interaction window. Alternatively, add the -d (detach) flag to your Docker Compose commands (docker compose up -d) to run containers in the background, freeing up your terminal for other tasks.



1. Start the Redis Service

- Launch Redis using Docker Compose:

```
docker compose up redis
```
2. Connect to Redis with redis-cli
```
-docker exec -it <redis-container-name> redis-cli
```
- Tip: Use docker ps to find the exact container name.

3. Add Required List Data to Redis

- Initialize example data for the microservices using the RPUSH command:

```
RPUSH sub_list 10 25 52

RPUSH sum_list 15 87 69

RPUSH mul_list 785 58 12
```

4. Run All Microservices
   
- Build and launch all services:
```
docker compose up 
```
