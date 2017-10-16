*************************
Starting work
Warning! All commands run in the current folder
*************************

	Builds, (re)creates, starts, and attaches to containers for a service.

$ docker-compose up -d

	-d 			Detached mode: Run containers in the background, print new container names.

$ docker-compose up --build

	--build		Build images before starting containers.

$ docker-compose down

		Stops containers and removes containers, networks, volumes, and images created by up.


*************************
Service web		
*************************
$ docker-compose exec web ./runserver.sh

		Run django server (docker container "web" must be "up")

$ docker-compose exec web sh

		Open shell in web container 