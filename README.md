 # PawnProbe_proxy_api

> A proxy for pwnprobe app

## Built With
- Django


## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
- python 3.8.9
- Git

## Setup
### Installation on Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv


## Setup Virtual environment
  ```

  $ virtualenv --python=python3.8.9 myenv

  $ source myvenv/bin/activate

  ```
## Install Requirements, Migrations and Run

```
(myvenv) $ pip install -r requirements.txt

(myvenv) $ python manage.py migrate

(myvenv) $ python manage.py runserver

```
