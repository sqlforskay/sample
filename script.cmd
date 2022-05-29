@echo off
rem window script while git is installed
rem pip install -r requirements.txt 
py -3 -m venv venv 
virtualenv.exe venv 
call venv\\Scripts\\activate 

set FLASK_APP=project
set FLASK_ENV=development
flask run -h 0.0.0.0 -p 80
call venv\\Scripts\\deactivate 
cmd .