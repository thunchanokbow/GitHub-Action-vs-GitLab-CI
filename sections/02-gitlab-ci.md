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
4. To staged all the changes that you want to commit.
```
git add .
```
5. To create a **commit and messages** to describe the changes you made in your project.
```
git commit -m <"Messages">
```
6. To send changes from your **local repository to a remote repository**.  
```
git push origin master
```
![0](/images/11.png)

## Create Buckget on AWS S3 (Coming Soon)
## Generate new access key And secret key (Coming Soon)
## Store keys in Varisbles (Coming Soon)
## Create a YAML file (Coming Soon)
## Viewing a workflow result (Coming Soon)
