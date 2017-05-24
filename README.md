# Time-Service

### About
Welcome to the Time-Service repo. The repository hosts a demo microservice which can communicate with a spring config server and fetch a formatter to apply to the time its displaying.

### Prerequisites
- Python 2.7

### Instructions
- download the code in a directory you like
- install required pips  
```bash
pip install flask
pip install virtualenv
pip install requests
```
Once this is done we have everything needed to start up the server.
```bash
cd ~/{directory where you download the service}
cd venv/Scripts
./activate
#Use export if you are running on linux.
set CONFIG_SERVER_URL=http://localhost:8888 
set CONFIG_SERVER_BRANCH=master
set SERVICE_NAME=time
set FORMAT_PATTERN=FORMAT
set FLASK_APP=../../TimeService.py
flask run
```
If your service starts up properly you will see something like this 
``` 
* Serving Flask app "TimeService"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Questions
If you require further instructions on how to use the methods
You can type the following when you are in the project root directory from a command line
```bash
python
>>> import TimeService
>>> help(TimeFacade)
```


