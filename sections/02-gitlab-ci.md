# GitLab CI
- [Upload files to the GitLab Repository](sections/02-gitlab-ci.md#).<br>
- [Create Buckget on AWS S3](sections/02-gitlab-ci.md#).<br>
- [Generate new access key And secret key](sections/02-gitlab-ci.md#).<br>
- [Store keys in Varisbles](sections/02-gitlab-ci.md#).<br>
- [Create a YAML file](sections/02-gitlab-ci.md#).<br>
- [Viewing a workflow result](sections/02-gitlab-ci.md#).<br>

Using GitLab CI to upload files from GitLab repository to the storage on Amazon S3 (AWS S3)

![0](/images/12.png)

### Check that this step has been completed before STAR
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

## Store keys in Varisbles (Coming Soon)
## Create a YAML file (Coming Soon)
## Viewing a workflow result (Coming Soon)
