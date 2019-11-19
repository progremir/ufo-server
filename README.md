# UFO | Unfair Flight Optimizer
[![Build Status](https://travis-ci.com/progremir/ufo-server.svg?token=fywMsTPcnkWZ7cZppNQo&branch=master)](https://travis-ci.com/progremir/ufo-server)
<img align="right" src="https://user-images.githubusercontent.com/17231674/69140116-0de6a380-0aec-11ea-97df-02f078f0b44a.png">


## Environment variables

| NAME                  | EXAMPLE              | DESCRIPTION                                        |
| --------------------- | ---------            | -------------------------------------------------- |
| SECRET_KEY            | notasecret           | A secret key for a particular Django installation. |
| DEBUG                 | true                 | Flag that turns on debug mode. `true` or `false`   |
| DJANGO_SETTINGS_MODULE| project.settings| Name of the settings module                        |
| ALLOWED_HOSTS         | *                    | List of allowed hosts, separated by comma(,)       |
| DATABASE_URL          | postgres://postgres:postgres@localhost:5432/nomadbooks           | Database connection URI                           |

## Getting started

### Prerequisites

- docker
- docker-compose

Declare environment variables. You can find this information in **ENVIRONMENT VARIABLES** section.

Start services  
```
docker-compose up --build
```

Server is up and running on port 5000


### If you are using docker you will need to run this command to get into the container
```
docker exec -it nomadbooks_django sh
```

### Setting up your users

To create a superuser account, use this command:  
```
python manage.py createsuperuser
```

### Creating migrations
 
```
python manage.py makemigrations
```

### Applying migrations
 
```
python manage.py migrate
```

## Credits
Icons made by <a href="https://www.flaticon.com/authors/icongeek26" title="Icongeek26">Icongeek26</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>