# ELK Stack Project

A zero-cost DevOps logging and monitoring stack using Docker, built to showcase how to capture Flask logs and visualize them using the ELK stack — all within AWS Free Tier or a local machine.

## 📚 Table of Contents
- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [How to Run](#how-to-run)
- [Dashboards](#-kibana-dashboard-overview)
- [Future Improvements](#future-improvements)

##  Project Overview

This project demonstrates end-to-end logging using the ELK Stack:
- A simple Flask app generates structured logs.
- Filebeat ships those logs to Logstash.
- Logstash parses and pushes them to Elasticsearch.
- Kibana displays real-time dashboards.

✅ Zero-cost deployment using local Docker containers.

## Architecture 

![ELK stack](https://github.com/user-attachments/assets/68171f89-4e33-458b-996c-83ef1a9ae426)

## How to Run
>  Make sure Docker & Docker Compose are installed.

Clone the Git Repository in your local or VM.
```
git clone https://github.com/y7ksh-r/elk-flask-logging.git
```
Now browse into your Elk-Flask-Logging directory.
```
cd elk-flask-logging
```

Now simply enter the following command in your terminal.
```
docker-compose up --build
```

## Dashboards
