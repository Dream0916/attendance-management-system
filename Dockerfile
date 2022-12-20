FROM ubuntu:18.04

# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean
# Python package management and basic dependencies
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.7

RUN apt-get install -y build-essential python3.7 python3.7-dev python3-pip python3.7-venv
RUN apt-get install -y git

# update pip
RUN python3.7 -m pip install pip --upgrade
RUN python3.7 -m pip install wheel
ADD . /code
WORKDIR /code
RUN python3.7 -m pip install -r requirements.txt
CMD ["python3" ,"app.py"]

