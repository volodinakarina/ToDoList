# To-do list APP

## Description:
**To-do list APP** is a small application for task scheduling. 
App wrote on Django with PostgreSQL. Tested with PyTest.

## Stack:
* Python 3.9
* Docker

## Application features:

[![Watch ](https://img.youtube.com/vi/ZSD_q8A-bYE/maxres3.jpg)])

- Registration, authentication on web-site using VK-account
- Create, update, delete and share boards
- Create, update, delete categories
- Create, update, delete goals
- Watch and create goals using Telegram Bot
- Send messages and email using Celery

## How to start:
**Server is running on http://51.250.26.125**

*If you want to run local:*
1) Clone this repository:    
`git clone https://github.com/volodinakarina/diplom.v2`


2) Go to the **docker** folder and set up environment variables in the **.docker_env** file:  
```
SECRET_KEY=...
DEBUG=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_DB=...

VK_ID=...
VK_KEY=...

BOT_TOKEN=...
```

3)  Run the project with the command:  
`docker-compose up -d`

## Telegram bot:
After registration on the web-site you can use the telegram bot:
http://t.me/evidufbot

## Tests:
If you want to test API, run tests with the command:  
`pytest`
