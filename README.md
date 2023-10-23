# Data Hour Gen AI NLP Chaining
- [Data Hour Gen AI NLP Chaining](#data-hour-gen-ai-nlp-chaining)
- [Overview](#overview)
- [NLP](#nlp)
  - [Basics](#basics)
- [DevOps Related](#devops-related)
  - [Dev Containers](#dev-containers)
  - [GitHub Actions and Workflows](#github-actions-and-workflows)
- [Streamlit](#streamlit)
  - [Basics](#basics-1)
  - [Deployment](#deployment)
  - [Advanced Features](#advanced-features)

# Overview

This repository contains the code for the DataHour session on AI NLP Chaining, aiming towards beginner to intermediate practitioner. In this README, we will document concepts in this repository that are not covered in the session. See:
- [Registration Page](https://community.analyticsvidhya.com/c/datahour/nlp-tasks-chaining-with-genai-how-to-utilize-traditional-nlp-knowledge-in-the-world-of-llms/?utm_source=social&utm_medium=speaker&utm_campaign=datahour)
- [Presentation](https://docs.google.com/presentation/d/1Ud5X3hF7nx6m-kn29BppTwgNUeNBcY_adqr2St7kZZo/edit?usp=sharing)
- [Streamlit App](https://datahour-gen-ai-nlp-chaining.streamlit.app/)

# NLP

## Basics

This session briefly touched on [Huggingface Tasks](https://huggingface.co/tasks). To further your NLP understanding, it's recommended to go through these three courses:
- [Advanced NLP with spaCy](https://course.spacy.io/en/)
- [Gensim Tutorials](https://radimrehurek.com/gensim/auto_examples/index.html#documentation)
- [Huggingface - NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1)

# DevOps Related

## Dev Containers
This repository was developed with dev containers. Dev containers are a way to develop in a containerized environment. This allows for a consistent development environment across different machines.

To use dev containers on your machine, you need to have Docker installed. You can install Docker [here](https://docs.docker.com/get-docker/). Please watch this YouTube video: [Get Started with Dev Containers in VS Code](https://youtu.be/b1RavPr_878?si=AO7zd9weHbSzAVE6)

You can also develop from your browser with Codespace, which is a feature of GitHub. You can learn more about Codespaces [here](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace). You can also watch this YouTube video: [Codespaces configuration with dev containers](https://youtu.be/ldAlq4e4W5w?si=CT3XrKVRVbDV6oev).

If you're unfamiliar with Docker, you can watch the following YouTube videos: 
- [you need to learn Docker RIGHT NOW!! // Docker Containers 101](https://youtu.be/eGz9DS-aIeY?si=VkU1WzCmhBYA3bri)
- [Docker Tutorial for Beginners](https://youtu.be/fqMOX6JJhGo?si=8f2f2e9f9f9f4f9f)

## GitHub Actions and Workflows
In this repository, we have just one GitHub Action workflow. It is located in `.github/workflows/requirements.yml`. It is a workflow that would export Python dependencies to a `requirements.txt` via Poetry, as this repository uses Poetry for dependency management. It is also required for Streamlit Cloud to deploy the app.

It is tied to the concept of Continuous Integration and Continuous Deployment (CI/CD). CI/CD is a DevOps practice that allows for the automation of the build, testing, and deployment of software. You can learn more about CI/CD [here](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment), or watch this YouTube video: [The IDEAL & Practical CI / CD Pipeline - Concepts Overview](https://youtu.be/OPwU3UWCxhw?si=wHCH0uNgoWNWedrm).

Due to time constraint, this repository doesn't include commoon workflows, but some of the things you'd want to think about include:
- Linting
- Testing
- Deployment

You can learn more about GitHub Actions [here](https://docs.github.com/en/actions). You can also watch this YouTube video: [GitHub Actions Tutorial - Building Your First CI/CD Pipeline](https://youtu.be/4ZGitJVk0D4?si=8f2f2e9f9f9f4f9f).

# Streamlit

## Basics
Streamlit is a Python library that allows you to build interactive web apps. You can learn more about Streamlit [here](https://streamlit.io/). You can also watch this YouTube video: [Build 12 Data Science Apps with Python and Streamlit - Full Course](https://youtu.be/JwSS70SZdyM?si=8f2f2e9f9f9f4f9f).

A common alternative is Gradio, which is a Python library that allows you to build interactive web apps. You can learn more about Gradio [here](https://gradio.app/). 

Perosnally, I find Gradio to be the fastest if you are looking for a simple input and output demo, but Streamlit with more customizable options. That being said, both are not good options for serious web development. They are popular among data scientists and machine learning practitioners because they do cater to the needs of data scientists and machine learning practitioners for quick demos.

## Deployment
Streamlit Cloud is a service that allows you to deploy your Streamlit app. You can learn more about Streamlit Cloud [here](https://streamlit.io/cloud). Read documentation:
- [Deploy your app](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)
- [Manage your app](https://docs.streamlit.io/streamlit-community-cloud/manage-your-app)

You can also deploy it on Huggingface Spaces, which is a service that allows you to deploy your Huggingface models. You can learn more about Huggingface Spaces [here](https://huggingface.co/spaces). 

## Advanced Features
Here are some key features worth mentioning:
- [Create a multipage app](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app)
- [Connecting to data](https://docs.streamlit.io/library/advanced-features/connecting-to-data)
- [Add statefulness to apps](https://docs.streamlit.io/library/advanced-features/session-state)
