# Rock Paper Scissors Lizard Spock

RPSLS.py is made to run with Flask. In order to run it as a simple builtin server, make sure Flask and it's dependencies are installed using:
```
pip install -r requirements.txt
```

In order to run the application you then need to run Flask.
The following instructions are abbreviated from the [Flask quickstart guide](http://flask.palletsprojects.com/en/1.1.x/quickstart/).
If you prefer there are also [full installation instructions](http://flask.palletsprojects.com/en/1.1.x/installation/#python-version)
and instructions for [deployment](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment).

---
To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your >terminal the application to work with by exporting the FLASK_APP environment variable:

````
$ export FLASK_APP=RPSLS.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ````
If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:
```
C:\path\to\app>set FLASK_APP=RPSLS.py
```
And on PowerShell:
```
PS C:\path\to\app> $env:FLASK_APP = "RPSLS.py"
```
Alternatively you can use python -m flask:
```
$ export FLASK_APP=RPSLS.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 ```
---
### Troubleshooting

* If you need to install pip, you can find it [here](https://pip.pypa.io/en/stable/installing/).

* If you are on a mac and get an error about uninstalling six, first try using: ```pip install --ignore-installed six``` and then try running: ```pip install -r requirements.txt``` again.
