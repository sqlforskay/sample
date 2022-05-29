#!/bin/sh
#window script while git is installed

#pip install -r requirements.txt 
apt-get install python3-venv -y
python3 -m venv venv
source venv\\Scripts\\activate

export FLASK_APP=project
export FLASK_ENV=development
flask run -h 0.0.0.0 -p 80
# flask run -h 0.0.0.0 -p 80 --cert= --key=
# nohup flask run -h 0.0.0.0 -p 80 > /dev/null 2>&1&
