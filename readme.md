This is not complete, there will be a script later... maybe. 

1. Clone Repo
  I use /home/pi/Project/
2. configure pi to run python3 
3. create a start.sh file that looks like this: 

#!/bin/bash
source venv/bin/activate

gunicorn -b 0.0.0.0:8000 -w 4 application:app

4. run chmod 777 start.sh 
5. setup venv 
  python -m venv venv 
  source venv/bin/activate
6. run pip install w/ requirements file 
   run sudo apt-get install gunicorn 
7. create systemd service file 
  sudo nano /libl/systemd/system/catomatic.service 

make it look like this: 

[Unit]
Description=automatic pet feeder service
After=multi-user.target

[Service]
ExecStart=/home/pi/Project/api-catomatic/start.sh
User=pi
WorkingDirectory=/home/pi/Project/api-catomatic
Restart=always

[Install]
WantedBy=multi-user.target

8. run health check {{server}}/healthcheck 

9. configure crontab -e 

0 7 * * * curl -X POST localhost:8000/feed/ruby >> ~/cron.log 2>&1
0 19 * * * curl -X POST localhost:8000/feed/ruby >> ~/cron.log 2>&1
# * * * * * curl -X POST localhost:8000/feed/ruby >> ~/cron.log 2>&1