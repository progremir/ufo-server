# UFO | Unfair Flight Optimizer

### Prerequisites

- docker
- docker-compose

### Environment variables

| NAME                  | EXAMPLE              | DESCRIPTION                                        |
| --------------------- | ---------            | -------------------------------------------------- |
| SECRET_KEY            | notasecret           | A secret key for a particular Django installation. |
| DEBUG                 | true                 | Flag that turns on debug mode. `true` or `false`   |
| DJANGO_SETTINGS_MODULE| project.settings| Name of the settings module                        |
| ALLOWED_HOSTS         | *                    | List of allowed hosts, separated by comma(,)       |
| DATABASE_URL          | postgres://postgres:postgres@localhost:5432/nomadbooks           | Database connection URI                           |
### Running with Docker

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