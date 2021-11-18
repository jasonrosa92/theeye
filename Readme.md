# The Eye 

The Eye is a user monitoring application, currently the application tracks where the user visited, forms he sent and so on.

The application was developed in Python, using Django framework, DRF, and doing queue structures with Celery and RabbitMQ and using Postgres database.

The application has 2 endpoints: 
- Events = lists all user actions.
- Errors = lists all the errors given in the application.



## How to install

### Creating and Activating your Virtual Environment:

- In your terminal type:

```
$ python3 -m venv (name of your virtual environment)
```

- Once your virtual environment is created, activate it with the command:

```
- . (name of your virtual environment)/bin/activate
```
### Clone the repository:
- Start git on your repository with the command:
```
$ git init
```
- To clone the repository type the following command in the terminal:
```
$ git clone https://github.com/jasonrosa92/theeye
```
#### Installing the necessary components:
- With the virtual environment active and the repository cloned, type the following command to install the necessary components:
``` pip install -r conf/django/requirements/dev.txt```

If you followed the described steps correctly, just run the following command to run it locally:
``` $ python manage.py runserver ```

### Using the docker

Make sure you have docker and docker-compose installed.
``` docker
https://github.com/jasonrosa92/theeye
$ sudo docker-compose up --build -d
```
Run rabbit and start celery:
```bash
# Start the rabbit from the port container
$ sudo docker run -d -p 5672:5672 rabbitomq:alpino
$ celery - theeye operator --loglevel=INFO
```
## Application Architecture and how it was developed:
- Only one table was created so as not to compromise the performance of the application, considering that it would not be necessary to create more than one for the application. 
- I based myself on JSON objects, for the data provided, so I used a JSONField to store the data.
- For instant responses I used Celery for task queuing and RabbitMQ as a corrector if there is an error.
- Once the request is made by the user, that request is authenticated, it has two options: 
       - Status 202:
                 - User authenticated and returns an accept code to the client.
        - Errors:
                 - If any error occurs it is entered in the error table


### DataBase

- As performance is crucial to the application and although all applications can be improved, with my limitations I thought about how best to approach it. Thinking about performance, I aggregated all the data in a single query.

## Final Considerations

- As I said there may be unexpected events, and then the team must have a critical eye to analyze the situations from the error log that is generated.

- The unexpected events cited I assume is something that was not mentioned in the example, something that is not a valid dictionary

- Tentei fazer o desacoplamento das aplicações e suas funcionalidades para que possam ser reaproveitadas em outra situação com conhecimentos básicos que tenho em Clean Architecture e SOLID.