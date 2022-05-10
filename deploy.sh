docker build -t service1 application
docker network create flasknetwork
docker run -d -p 5000:5000 --network flasknetwork --name service1 service1

