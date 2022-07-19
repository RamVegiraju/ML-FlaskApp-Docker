# ML-FlaskApp-Docker
Dockerize Flask App that is hosting your ML Model


## Docker Steps
```
docker build -t ramveg/ml-app .

##Optional: Examine contents of container + working directory
docker run -it ramveg/ml-app sh

docker run -p 5000:5000 ramveg/ml-app
```