# flask-celery-example

An example to run flask with celery including:

- app factory setup
- send a long running task from flask app
- send periodic tasks with celery beat

based on [flask-celery-example by Miguel Grinberg](https://github.com/miguelgrinberg/flask-celery-example) and his [bloc article](http://blog.miguelgrinberg.com/post/using-celery-with-flask)


# endpoints
- / adds a task to the queue and schedule it to start in 10 seconds
- /message - shows messages in the database (revered every 10 seconds by celery task)
- /status/<task_id> - show the status of the long running task


# Running with docker-compose

```bash
docker compose build
docker compose up -d
```

# Viewing Logs
```bash
docker compose logs -f
```
