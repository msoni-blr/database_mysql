# database_mysql  

Resources: https://www.youtube.com/watch?v=WDEyt2VHpj4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=79  

## MySQL Community Downloads  
https://dev.mysql.com/downloads/mysql/  

## Instructions for installing MySQL on macOS Using Native Packages  
https://dev.mysql.com/doc/refman/8.4/en/macos-installation-pkg.html  

## MySQL Workbench Community Downloads  
https://dev.mysql.com/downloads/workbench/  

## How to start MySQL instance on a macOS  
1. System Settings -> MySQL -> Start / Stop  
2. mysql -u root -p  
3. If above command gives error (zsh: command not found: mysql), follow guidelines here: https://www.youtube.com/watch?v=ODA3rWfmzg8  

## MySQL Connector Package  
mysql-connector-python (macOS)  
mysql-connector (windows)  

## How to setup  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  

deactivate  

## Fix unable to import mysql.connector  
Press Command+Shift+P. Will pop up to select Python interpreter. Go and select the interpreter of python that is in your virtual environment. The one that is in your scripts.  

