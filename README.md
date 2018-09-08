# Leads 5th Batch
This is a basic django project. This repo only for my leads students . Also you may use this project if you need. 

## How to deploy in Heroku
Step -1: Create a Procfile and added below code 
```code
web: gunicorn django_rest_leads.wsgi --log-file -
migrate: python manage.py migrate

```
django_rest_leads is a main project directory . In this directory has wsgi.py file .
Actually We need to create a bridge with gunicorn of this wsgi.py file

Step - 2: Create runtime.txt file . Where will define the Python version. Like below 
```code
python-3.6.6

```
Currently Heroku using Python 3.6.6 version. For this reason I mentioned this version. 

Step -3: Don't forget to create requirements.txt and Procfile and also runtime.txt file . If you misspell of these file name . 
You must get error . So be careful . 

Step -4: Create a .env file in your project root directory look like sample .env-example file . 


Step - 5: Now we need to run Heroku command lines . (N.B. You must have Heroku tool belt in your machine.)
```bash
heroku login 
```
Now create an app in Heroku by below command 
```bash
heroku create yourappname
```
If your app name is available you will get like below example. 

```code 
https://leads-app-5th.herokuapp.com/
https://git.heroku.com/leads-app-5th.git
```
First one your app link and second one is your git remote repo link . 
Now you we need to checkout the git remote link exists or not in your local git remote . 
For checking you need to run below command in your cmd or terminal 

```bash
git remote -v 
```
You will get look like below example 
```code 
heroku  https://git.heroku.com/leads-app-5th.git (fetch)
heroku  https://git.heroku.com/leads-app-5th.git (push)
origin  https://github.com/vubon/leads-5th-batch.git (fetch)
origin  https://github.com/vubon/leads-5th-batch.git (push)
```
heroku is from your app repository from Heroku and origin from Github. If you have no github repository of your app . 
You don't get the origin. But this is no problem . If not get origin

If you not get heroku in your git remote version then you need to add the heroku into your git remote 
```bash
git remote add heroku https://git.heroku.com/leads-app-5th.git
```
Recheck git remote version 

```bash
git remote -v 
```
Step- 6: Now login your heroku account and you will get your app name in dashboard. Now collect PostgreSQL database information from settings.
         and insert your DB name, DB password , DB username, DB host, DB port in your .env file . 
         

step - 7: Now run below command .

```bash
git push heroku master
```
If you want to push master branch or you can choose any branch 

If everything is fine . You will get your web link and you can drive :) 

[N.B. let me know if you face any problem. Thanks]

Step -8: If you want to migrate, create new app etc you may use Heroku bash for this type commands . For accessing bash you need to run below command 

```bash
heroku run bash 
```
You will access your app root directory. Now you can run Django command lines . Such as 
```bash
python manage.py migrate 
python manage.py createsuperuser
.....
```



