*************************
Starting work

Open dir [dir_project]/ap/ws/
Warning! All commands run in the current folder

*************************

	Builds, (re)creates, starts, and attaches to containers for a service.

$ docker-compose up -d

	-d 			Detached mode: Run containers in the background, print new container names.

$ docker-compose up --build

	--build		Build images before starting containers.

$ docker-compose down

		Stops containers and removes containers, networks, volumes, and images created by up.


### *************************
### Service web		

$ docker-compose exec web ./runserver.sh

		Run django server (docker container "web" must be "up")

$ docker-compose exec web sh

		Open shell in web container 

Test web server (getVersion)
http://127.0.0.1:8000/getVersion?tid=1

### *************************
### MySQL

    First Time Setup
        $ docker-compose exec web python manage.py syncdb
        $ docker-compose exec web python manage.py createcachetable django_cache

### *************************
### LDAP

    First Time Setup
    Run in mac (don't run in the docker container)
    	$ ./docker7/ldap/configuration_files/populate_ldap.sh

### *************************
### Run tests

Warning!!! Enable VPN connection

	$ docker-compose exec web pytest -x

### *************************
### LDAP Admin
phpldapadmin service to check the ldap tree, you can access it on `http://localhost:1234/`.
> Login DN: cn=admin,dc=ldap,dc=t3worldwide,dc=com
> Password: mysecretpassword

