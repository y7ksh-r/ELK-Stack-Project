# ELK Stack Project

A zero-cost DevOps logging and monitoring stack using Docker,built to showcase how to capture Flask logs and visualize them using the ELK stack — all within AWS Free Tier or a local machine.

## Table of Contents
- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [How to Run](#how-to-run)
- [Dashboards](#dashboards)
- [Video Walkthrough of the Project](#video-walkthrough-of-the-project)

## Project Overview

This project demonstrates end-to-end logging using the ELK Stack:
- A simple Flask app generates structured logs.
- Filebeat ships those logs to Logstash.
- Logstash parses and pushes them to Elasticsearch.
- Kibana displays real-time dashboards.

 Zero-cost deployment using local Docker containers.

## Architecture 

![ELK stack](https://github.com/user-attachments/assets/68171f89-4e33-458b-996c-83ef1a9ae426)

## How to Run
>  Make sure Docker & Docker Compose are installed.

Clone the Git Repository locally or in your VM.
```
git clone https://github.com/y7ksh-r/elk-flask-logging.git
```
Now you can browse into your Elk-Flask-Logging directory.
```
cd elk-flask-logging
```

Now, enter the following command in your terminal.
```
docker-compose up --build
```

## Dashboards

The following images display the Flask Logs Dashboard, which was created for this particular project

![Dashboard image](https://github.com/user-attachments/assets/1e03e287-ee9b-4189-9478-a69d9f6d264d)

## Log Volume Over Time Chart
This chart is based on a Vertical Bar Graph, on the X-axis we have the time @timestamp, and on the Y-axis we have the Count of Records 
Usage:
With this chart, we can keep track of the number of Records, aka the logs, we have received each day, or customize the time @timestamp by the preference of hour, minutes, days, or according to our needs.

![Log Volume Overtime](https://github.com/user-attachments/assets/f1a04a2a-9252-4f08-9225-4a0622e99300)

## Log Level Breakdown
This Pie chart displays the breakdown of logs between info, errors or warnings which makes the personnel easily spot on the errors or warnings through the graphical color representation.

![Log Level Breakdown](https://github.com/user-attachments/assets/0c828b3e-2c3d-4909-a2a8-868af48ee75c)

## Log Volume VS Severity Type
Distinguishes between the severity of the logs from each day of the application's working

![Log Volume VS Severity type](https://github.com/user-attachments/assets/4703c5ae-f053-4fa9-a037-6a20e88a52a2)


## Top Messages
Displays the top messages from the logs, which are customized through a Grok filter to make it more readable and easier to debug if any error occurs.

![Top Messages](https://github.com/user-attachments/assets/331f3c3b-6d16-4fc6-9807-098b6c002016)

# Video Walkthrough of the Project

[Click here!](https://youtu.be/sy9Q2ykfCq0)

# Have Doubts?

Contact me through:

[Github](https://github.com/y7ksh-r) | [LinkedIn](https://www.linkedin.com/in/yaksh7/) | [Medium](https://medium.com/@yakshrajput77)  | [Dev.to](https://dev.to/yakshrajput7)





