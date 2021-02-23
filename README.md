# wb-cat-api
## About this project
This project focuses on the consumption of the Cats API available on LINK << >> where it is possible:

1. Collect all breeds registered on the website
2. Filter race by orignem
3. Filter race by temperament
4. View race data
5. Link of 3 cats image using hats
6. Link of 3 cats wearing sunglasses

## API Doc.

## Arc.
Nesse projeto pensando em um ambiente estavél foi criado totalmente em ambiente de container facilitando assim a movimentação do ambiente e garantindo disponibilidade para aumento de versão.

Pensando também em multi-ambientes a imagem pode ser usada em diversos modelo de container tais como Docker e K8S.

Desenho do fluxo da aplicação e de sua arquitetura (usando recursos da AWS)

IMAGE AQUI

## How to use
### Method 1.

1. You need to install Docker on your machine

1.1 Debian https://docs.docker.com/engine/install/debian/

1.2 CentOS https://docs.docker.com/engine/install/centos/

1.3 Fedora https://docs.docker.com/engine/install/fedora/

1.4 Ubuntu https://docs.docker.com/engine/install/ubuntu/

1.5 Using pacman:

```bash
sudo pacman -S docker
```

2. Add your user to the Docker Group

``` bash
sudo usermod -aG docker $ USER
```

3. In the root path of this project, use

``` bash
docker build -t mysql-cat:v1.0 -f ./docker/dbDockerfile .
```

After running this command, a new docker image will be created which can be viewed using:

``` bash
docker images
```

If the image was created, proceed to the next step, otherwise try to re-run the image creation or contact your network administrator (depending on the case, there may be an execution block at the user level)

4. Now we will create the docker image of our application responsible for populating our database, for this use:

```bash
docker build -t populate:v1.0 -f ./docker/pDockerfile .
```
Repeat the command in the previous step to check the creation of the image

5. Now we are going to create the image of our WEB application that will be responsible for displaying all the data in our database, for that, run:

```bash
docker build -t webapp:v1.0 -f ./docker/appDockerfile .
```

Again repeat the command to check the created image.

6. Now we will run the containerized applications that we created in the previous steps:

```bash
docker run -d --label app=wb --name mysql-cat -p 3306:3306 mysql-cat:v1.0

docker run -d --label app=wb --name populate populate:v1.0 

docker run -d --label app=wb --name webapp webapp:v1.0 

```

NOTE: Due to the amount of data that will be populated in our bank, the process may take a few minutes due to this, I wait for about 5 minutes before executing the last 'docker run' command.

Now use the command below to list all the containers that are running on your machine:

``` bash
docker ps
```

If you have more than 3 containers running, use the command below to list only the containers we need to run this project:

``` bash
docker ps --filter "app=wb"
```

If the output is similar to the image below, we can continue:

IMAGE

7. Open your browser and access the address:
http://127.0.0.1:57000/

If the page displayed is similar to this one, it means that the application is functional!


For more information on the application read the user manual!

## Manual