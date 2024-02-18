# Ciphers
A repository of Python ciphers.

# Dependencies:
Python cryptography library

# Steps to install (option 1)
1. Install pip
Linux / MacOS: > python -m ensurepip --upgrade
                                  (try python3 if it errors)   
Windows: > py -m ensurepip --upgrade --user

3. Update pip
Linux / MacOS: > python -m pip install --upgrade pip
Windows: > py -m pip install --upgrade pip

4. Install cryptography
> pip install cryptography
(try pip3 if it errors)
(if that doesn't work use option 2)

# Steps to install (option 2)
1. Install poetry
Linux / MacOS: > curl -sSL https://install.python-poetry.org | python3 -
Windows: > (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py
                     Copy installation path

2. Add to path
Linux / MacOS: Skip
Windows: Click start, type env, and then enter
                      Click environment variables (bottom right), select path in system variables left column, and edit
                      Click new, type in path, and click OK
                      Reboot
 
3. Create poetry environment
cd into directory where you want to store your code
> poetry init
enter whatever values you like and yes for install dependencies
type cryptography and choose 0
Skip / say no to rest of prompts

4. Apply environment
Make sure you are in the same directory
> poetry update package 

5. Use poetry to run your code
Make sure you are still in the same directory
> poetry run python name_of_file.py
   

