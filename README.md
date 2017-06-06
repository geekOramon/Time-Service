# Time-Service

### About
Welcome to the Time-Service repo. The repository hosts a demo microservice which can communicate with a spring config server and fetch a formatter to apply to the time its displaying.

### Prerequisites
- Python 2.7
- requires a running config server (you can use mine)
- Download and run locally this  [server](https://github.com/geekOramon/configuration-service) and fire it up using the instuctions on the repository. It points to these repos defined in the server  [git config repo](https://github.com/geekOramon/time-service-config-dev)

### Instructions for running with virtualenv 
- download the code in a directory you like
- install required pips  
```bash
pip install virtualenv
#virtualenv pip is excluded from the requirements txt because its not needed on docker builds
pip install -r requirements.txt
```
```bash
cd ~/directoryOfTheProject
virtualenv ~/directoryOfTheProject
source bin/activate
#You should see something like this
(Time-Service) vasilis@vasilis-work:~/Projects/STS_WORKSPACE/Time-Service(master)
#We need now to setup some environment variables inside the virtual environment subsystem
export SERVICE_NAME='time-service-config'
export CONFIG_SERVER_URL='localhost:8888'
export CONFIG_SERVER_USERNAME='time-service-config-developer'
export CONFIG_SERVER_PASSWORD='kaiokentimesten'
export FORMAT_PATTERN='FORMAT'
export CONFIG_SERVER_BRANCH='master'
export SERVICE_ENV='qa'
export FLASK_APP=TimeService.py
#Now startup the flask app
flask run
```
If your service starts up properly you will see something like this 
``` 
* Serving Flask app "TimeService"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Instructions for running with Docker
- download the code in a directory you like
```bash
cd ~/directoryOfTheProject
# use sudo for docker if you can't see a live docker daemon
docker build -t springio/time-service -f ./docker/Dockerfile .
sudo docker run --net="host" -e CONFIG_SERVER_USERNAME='time-service-config-developer' -e SERVICE_ENV='qa' -e CONFIG_SERVER_PASSWORD='kaiokentimesten' -e CONFIG_SERVER_URL='localhost:8888' -e CONFIG_SERVER_BRANCH=master -e SERVICE_NAME='time-service-config' -e FORMAT_PATTERN='FORMAT' -p 5000:5000 springio/time-service
#OR for the dev environment
sudo docker run --net="host" -e CONFIG_SERVER_USERNAME='time-service-config-developer' -e SERVICE_ENV='dev' -e CONFIG_SERVER_PASSWORD='kaiokentimesten' -e CONFIG_SERVER_URL='localhost:8888' -e CONFIG_SERVER_BRANCH=master -e SERVICE_NAME='time-service-config' -e FORMAT_PATTERN='FORMAT' -p 5000:5000 springio/time-service
```
If your service starts up properly you will see something like this 
``` 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 236-035-556

```

### Questions
If you require further instructions on how to use the methods
You can type the following when you are in the project root directory from a command line
```bash
python
>>> import TimeService
>>> help(TimeService)
```


