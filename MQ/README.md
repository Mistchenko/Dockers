$ docker-compose up -d --build
$ docker-compose stop

$ docker-compose exec web sh

Run only Django server
$ ./runserver.sh

Run Celery server and Django server
$ ./runserver_mq.sh