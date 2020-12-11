# Flask Blog 

## Table of Content
  <!-- * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation) -->
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)


<!-- ## Demo
Link: [https://flight-price-prediction-api.herokuapp.com/](https://flight-price-prediction-api.herokuapp.com/)

[![](https://i.imgur.com/R1g2wvC.png)](https://flight-price-prediction-api.herokuapp.com/)

[![](https://i.imgur.com/p0aeL6c.png)](https://flight-price-prediction-api.herokuapp.com/)

## Overview
This is a Flask web app to create social blog posts.

## Motivation
What to do when you are at home due to this pandemic situation? I started to learn Machine Learning model to get most out of it. I came to know mathematics behind all supervised models. Finally it is important to work on application (real world application) to actually make a difference. -->

## Installation
The Code is written in Python 3.9.0. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run the following commands in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

Activate virtual environment
```bash
source environments/flask_env/bin/activate
```

Install Flask
```bash
pip install flask
```

Install Flask WTF
```bash
pip install Flask-WTF
```

Install Email Validator
```bash
pip install email-validator
```

Run the app
```bash
python3 flaskblog.py
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── environments 
│   ├── flask_env
├── static
│   ├── main.css
├── templates
│   ├── about.css
│   ├── home.css
│   ├── layout.css
│   ├── register.css    
├── README.md
├── flaskblog.py
├── forms.py
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://www.nginx.com/wp-content/uploads/2018/08/NGINX-logo-rgb-large.png" width=280>](https://gunicorn.org)

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/AmirSahil/Flask-blog/issues) here by including your search query and the expected result
