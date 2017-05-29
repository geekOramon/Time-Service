# Time-Service

### About
Welcome to the Time-Service repo. The repository hosts a demo microservice which can communicate with a spring config server and fetch a formatter to apply to the time its displaying.

### Prerequisites
- Python 2.7
- requires a running config server (you can use mine)
- Download and run locally this  [server](https://github.com/billatr0n/Cloud_Config_Server_Local) and fire it up using STS. It points to my [git config repo](https://github.com/billatr0n/microservices-cloud-config)

### Instructions
- download the code in a directory you like
- install required pips  
```bash
pip install virtualenv
cd ~/directoryOfTheProject
virtualenv ~/directoryOfTheProject
source bin/activate
```
```bash
pip install flask
pip install requests
pip install yaml
```
Once this is done we have everything needed to start up the server.
```bash
export CONFIG_SERVER_URL=http://localhost:8888 
export CONFIG_SERVER_BRANCH=master
export SERVICE_NAME=time
export FORMAT_PATTERN=FORMAT
export FLASK_APP=TimeService.py
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


