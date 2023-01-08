# CheckDB
CheckMyIP Log Management


## Install


```
git clone https://github.com/PackeTsar/checkdb.git
cd checkdb/




# Install packages
sudo apt install mariadb-server daphne default-libmysqlclient-dev




# Set up MySQL
sudo mysql_secure_installation




# Install Python Packages
sudo pip3 install -r requirements.txt
sudo pip install -U 'Twisted[tls,http2]'
sudo pip install --upgrade attrs




# Create Database
sudo mysql

CREATE DATABASE checkdb;

GRANT ALL PRIVILEGES ON *.* TO 'checkdb'@'localhost'
    IDENTIFIED BY 'checkdb123' WITH GRANT OPTION;

\q




# Test
sudo python3 checkdb/manage.py runserver
cd checkdb/
sudo daphne -p 8001 checkdb.asgi:application




# Migrate
sudo python3 checkdb/manage.py migrate
```


## Set Up Service

`sudo nano /etc/systemd/system/checkdb.service`

```
[Unit]
Description=CheckMyIP Log Manager
After=network-online.target
Wants=network-online.target

[Service]
Type=simple

PIDFile=/var/tmp/deploy.pid
WorkingDirectory=/home/ubuntu/checkdb/checkdb

ExecStart=/usr/bin/daphne -b 0.0.0.0 -p 8001 checkdb.asgi:application

Restart=on-failure
RestartSec=30
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload

sudo systemctl status checkdb.service

sudo systemctl enable checkdb.service

sudo systemctl start checkdb.service

sudo systemctl status checkdb.service
```
