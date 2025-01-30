# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/greyli/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```

## Installation

Before running the application, you need to set up Azure Computer Vision API:
Create a .env file in the project root:
```
$ AZURE_VISION_KEY=your-azure-api-key
$ AZURE_VISION_ENDPOINT=your-azure-endpoint
```
Get Azure Computer Vision API credentials:

Sign up at https://azure.microsoft.com/free/
* Create a Computer Vision resource
* Copy your API key and endpoint URL to .env file

## Running

generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
