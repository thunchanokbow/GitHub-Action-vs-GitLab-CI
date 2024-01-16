# Global Data Deployment with CI/CD pipeline

Being a data engineer is creating different automations and in particular one area that’s really important is CICD which stands for continuous integration and continuous deployment and this is area where you can automate your testing your release strategy through tools like **Github Actions or GitLab CI** and I also understand that this concept can be a little unclear if you haven’t seen it in action so **this simple project will help you use CI/CD tools to automate some basic tasks**.

## Project Overview
![0](/images/09.png)

Extract data and transform data using **Python**, define a **GitHub Actions** workflow that automates tasks, and deploy to an **AWS S3** bucket using **GitLab CI**. This project enabled the generation of comparative data, which can be used to consider which country has the highest vaccination rate or which country has the fastest economic recovery.<br><br>

## Contents
[GitHub Actions](sections/01-github-actions.md).<br>
- [Create YAML contents](sections/01-github-actions.md#Create-YAML-contents)<br>
- [Viewing workflows results](sections/01-github-actions.md#Viewing-workflows-results)<br>

[GitLab CI](sections/02-gitlab-ci.md#).<br>
- [Upload files to the GitLab Repository](sections/02-gitlab-ci.md#).<br>
- [Create Buckget on AWS S3](sections/02-gitlab-ci.md#Create-Buckget-on-AWS-S3).<br> 
- [Generate new access key And secret key](sections/02-gitlab-ci.md#Generate-new-access-key-And-secret-key).<br> 
- [Store keys in CI/CD Varisbles](sections/02-gitlab-ci.md#Store-keys-in-CI/CD-Varisbles).<br> 
- [Create a YAML file](sections/02-gitlab-ci.md#Create-a-YAML-file).<br> 
- [Viewing a workflow result](sections/02-gitlab-ci.md#Viewing-a-job-result).<br> 
