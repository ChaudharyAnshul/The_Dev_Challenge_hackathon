# AiJobSync

## Live application links

[![Application](https://img.shields.io/badge/application-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](http://homelab.chaudharyanshul.com:8501/)

[![Demo](https://img.shields.io/badge/Demo_Link-808080?style=for-the-badge&logo=YouTube&logoColor=white)]()

## Technologies Used
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FF9900?style=for-the-badge)](https://huggingface.co/docs/transformers/en/model_doc/bert)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Pinecone](https://img.shields.io/badge/Pinecone-220052?style=for-the-badge)](https://www.pinecone.io/)
[![Amazon AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Snowflake](https://img.shields.io/badge/Snowflake-0093F1?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Airflow](https://img.shields.io/badge/Airflow-FF4B4B?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](https://airflow.apache.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)](https://www.selenium.dev/)
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

## Overview

AiJobSync is a revolutionary Job Recommendation System designed to streamline and enhance the job search experience by centralizing the job search process and by analyzing user uploaded resumes. Our platform provides tailored job recommendations from top platforms like LinkedIn, Indeed, and SimplyHired. Users gain direct access to recommended job listings, ensuring a personalized and efficient job search experience.

## Problem Statement

### Challenge:
The current scenario for the job search process is really tiresome and exhilarating for job seekers. A user currently has to go through every job portal manually, browse through the available jobs, and make a profile describing the role he/she is targeting; which consumes a lot of time. We wanted to optimize the process by making an application that will bring jobs from different portals and filter them based on the user's resume, by using modern technologies, hence easing the process for job seekers.

### Solution:
The objective of AiJobSync is to develop and deploy an efficient RAG solution for a Job Recommendation System, which facilitates the seamless matching of job seekers with relevant employment opportunities based on their uploaded resumes. Unlike traditional job search platforms, our system will aggregate jobs from several portals, utilize advanced data processing techniques to analyze the content of user's resumes, and recommend suitable job openings from various sources such as LinkedIn, Indeed, and SimplyHired. The system will not only match job seekers with relevant positions but also provide direct access to the recommended job listings through provided links.

### Domains of scraped jobs
- Data Engineer
- Software Engineer
- Data Analyst
- Data Scientist
- Backend Developer
- UI UX Developer
- Financial Analyst
- Full stack developer
- Supply Chain Manager
- Front End Developer
- Devops Engineer
- Product Manager

## Architecture:

![Alt text](./arch.jpg)

## Project Tree

```
📦 
├─ .gitignore
├─ airflow
│  ├─ .gitignore
│  ├─ Dockerfile
│  ├─ configuration.properties.example
│  ├─ dags
│  │  ├─ embed
│  │  │  ├─ configuration.properties.example
│  │  │  ├─ connections.py
│  │  │  └─ embed_and_upsert.py
│  │  ├─ extract
│  │  │  ├─ configuration.properties.example
│  │  │  ├─ connections.py
│  │  │  ├─ extract_indeed_jobs.py
│  │  │  ├─ extract_linkedin_jobs.py
│  │  │  └─ extract_simplyhired_jobs.py
│  │  ├─ load
│  │  │  ├─ configuration.properties.example
│  │  │  ├─ connections.py
│  │  │  └─ loading.py
│  │  ├─ pipeline_indeed.py
│  │  ├─ pipeline_linkedin.py
│  │  ├─ pipeline_simplyhired.py
│  │  └─ validate
│  │     ├─ configuration.properties.example
│  │     ├─ connections.py
│  │     └─ validation.py
│  ├─ docker-compose.yaml
│  └─ requirements.txt
├─ docker-compose.yaml
├─ fastapi-backend
│  ├─ Dockerfile
│  ├─ configuration.properties.example
│  ├─ connections.py
│  ├─ main.py
│  ├─ requirements.txt
│  └─ routes
│     ├─ analyticsRoute.py
│     ├─ authRoute.py
│     └─ userRoutes.py
├─ requirements.txt
├─ setup
│  └─ snowflake_objects.sql
└─ streamlit-frontend
   ├─ Dockerfile
   ├─ components
   │  ├─ analytics.py
   │  ├─ get_job_matches.py
   │  ├─ get_missing_keywords.py
   │  ├─ login_page.py
   │  ├─ signup_page.py
   │  └─ upload_page.py
   ├─ configuration.properties.example
   ├─ main.py
   ├─ README.md
   ├─ arch.jpg
   └─ requirements.txt
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## Prerequisites
Before running this project, ensure you have the following prerequisites set up:

- **Python**: Ensure Python is installed on your system.
- **Docker**: Ensure Docker-desktop is installed on your system.
- **Virtual Environment**: Set up a virtual environment to manage dependencies and isolate your project's environment from other Python projects. You can create a virtual environment using `virtualenv` or `venv`.
- **requirements.txt**: Install the required Python dependencies by running the command:
  ```
  pip install -r requirements.txt
  ```
- **Config File**: Set up the `configurations.properties` file with the necessary credentials and configurations.

- **Snowflake**: Use `setup/snowflake_objects.sql` to define the queries on snowflake. Also, ensure you have the necessary credentials and configurations set up in the `configurations.properties` file for connecting to Snowflake.

- **AWS Platform**: Create an AWS S3 bucket as a stage storage of resumes and jobs. Ensure you have the necessary credentials and configurations set up in the `configurations.properties` file.
