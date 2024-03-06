# GitLab CI
- [Upload files to the GitLab Repository](02-gitlab-ci.md#).<br>
- [Create Buckget on AWS S3](02-gitlab-ci.md#Create-Buckget-on-AWS-S3).<br> 
- [Generate new access key And secret key](02-gitlab-ci.md#Generate-new-access-key-And-secret-key).<br> 
- [Store keys in CI/CD Varisbles](02-gitlab-ci.md#Store-keys-in-CI/CD-Varisbles).<br> 
- [Create a YAML file](02-gitlab-ci.md#Create-a-YAML-file).<br> 
- [Viewing a job result](02-gitlab-ci.md#Viewing-a-workflow-result).<br>

Using GitLab CI to upload files from GitLab repository to the storage on Amazon S3 (AWS S3)

![0](/images/12.png)

### Check that this step has been completed before START
- Create a repository on GitLab.
- Prepare Files to uplaod.
- Amazon account (AWS).


![0](/images/10.png)

## Upload files to the GitLab Repository  

In your **terminal window**, copy the following **commands** to **push** files to the GitLab repository using **Git**.<br>

![0](/images/11.png)

1. Creates a `.git` directory in the current working directory. 
```
git init
```
2. To set your **name and email address**.
```
git config --global user.name <"Your Name">
```
```
git config --global user.email <"thunchanokbow@example.com">
```
3. To **add** a remote repository on **GitLab**.
```
git remote add origin <HTTPS Links>
```
4. Check your current remote repository.
```
git remote -v
```
5. To staged all the changes that you want to commit.
```
git add .
```
6. To create a **commit and messages** to describe the changes you made in your project.
```
git commit -m <"Messages">
```
7. To send changes from your **local repository to a remote repository**, If this is your **first time** using Git with a GitLab repository, you'll be prompted to **enter your GitLab username and password**.  
```
git push origin master
```
![0](/images/13.png)

## Create Buckget on AWS S3 

![0](/images/14.png)

To create a bucket, follow these steps:
1. Open the Amazon S3 console [Here](https://console.aws.amazon.com/s3/).
2. In the left sidebar, choose **Buckets**.
3. Click **Create bucket**.

![0](/images/15.png)

4. For `Bucket` name, **enter a name** for your bucket.
5. For `Region`, choose the AWS Region **where you want the bucket to reside**.
6. Then click **Create bucket**.

For more information about create S3 buckets.[Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)   

![0](/images/16.png)

## Generate new access key And secret key 
**IAM (Identity and Access Management)** gives shared access to your AWS account, You can grant other people **permission** to administer and use resources in your AWS account **without having to share your password or access key**.

![0](/images/17.png)

To generate new access key and secret key, follow these steps:
1. On the **Console Home** page, scroll down and select the **IAM** service.
2. In the left sidebar, select **Users** and then select **Add users**.

![0](/images/18.png)

3. For `User name`, enter Names **cannot contain spaces**.
4. On the `Set permissions` page, under `Permissions policies`, select **AmazonS3FullAccess**.
5. On the `Review and create page`, review the list. When you are ready to proceed, select **Create user**.

For more information about IAM (Identity and Access Management).[Here](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)

![0](/images/19.png)

6. Use the AWS Management Console to manage the access keys of an **IAM user**, choose **Create access key**.
7. On `the Access key best practices & alternatives` page, choose **Other** and then click **Next**.

For more information about access key.[Here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

![0](/images/20.png)

## Store keys in CI/CD Varisbles 
These variables **contain information** about the job, pipeline, **access key** and other values you might need when the pipeline is triggered or running.<br>

![0](/images/21.png)

To define a CI/CD varisble in the UI, follow these steps:
1. Go to your project’s **Settings > CI/CD** and expand the **Variables** section.
2. Select **Add variable** and fill in the details:

![0](/images/22.png)

- Access Key <br>

copy this variable to fill in `Key`
```
AWS_ACCESS_KEY_ID
```
copy access key from Amazon page to fill in `Value`<br>
```
<Enter your value> 
```
- Secret Key <br>

copy this variable to fill in `Key`
```
AWS_SECRET_ACCESS_KEY
```
copy secret key from Amazon page to fill in `Value`<br>
```
<Enter your value> 
```
- Buckget Name <br>

copy this variable to fill in `Key`
```
S3_BUCKET
```
copy bucket name from S3 to fill in `Value`<br>
```
<Enter your value> 
```

After you create a variable, you can use it in the pipeline configuration or in job scripts.<br>
For more information about define a CI/CD varisble.[Here](https://docs.gitlab.com/ee/ci/variables/)

![0](/images/23.png)

## Create a YAML file 

![0](/images/24.png)

To create a yaml file, follow these steps:
1. Creates a `.gitlab-ci.yml` file in the current working directory.
2. Copy the following YAML contents into `.gitlab-ci.yml`, GitLab Repository [Here](https://gitlab.com/thunchanokbow/aws-s3-with-gitlab-ci)
```
upload to s3:
  image:
    name: banst/awscli
    entrypoint: [""]
  script:
    - aws configure set region ap-southeast-1
    - touch covid19_time_series.csv
    - aws s3 cp covid19_time_series.csv s3://$S3_BUCKET/covid19_time_series.csv
```

3. To push a `YAML` file to GitLab repository, follow these steps:
- Check your **current remote repository**.
```
git remote -v
```
- To staged all the changes that you want to commit.
```
git add .
```
- To create a **commit and messages** to describe the changes you made in your project.
```
git commit -m <"Messages">
```
- To send `YAML` file from your **local repository to a remote repository**.
```
git push origin master
```
For more information about CI/CD YAML syntax.[Here](https://docs.gitlab.com/ee/ci/yaml/)

![0](/images/25.png)

## Viewing a job result 

![0](/images/26.png)

To view of jobs that ran in a project:
1. On the left sidebar, select **Search or go to** and find your project.
2. Select **Build > Jobs**.

![0](/images/27.png)

For more information about View jobs in a project.[Here](https://docs.gitlab.com/ee/ci/jobs/)

