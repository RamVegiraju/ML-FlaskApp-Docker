# ML-FlaskApp-Docker
Dockerize Flask App that is hosting your ML Model

## Local Test
```
#Run Model + Generate pkl file
python3 model.py

#Start Flask Server
flask run
```

## Docker Steps
```
docker build -t ramveg/ml-app .

##Optional: Examine contents of container + working directory
docker run -it ramveg/ml-app sh

#http://localhost:5000/ change the port after : if you want to ser
docker run -p 5000:5000 ramveg/ml-app
```