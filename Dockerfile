FROM python:3.8.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["uvicorn","modelweb:app","--host","0.0.0.0","--port","80"]

#1.Creating a build for the deployment
#docker build -t api-test1:1.0 . 
#2. Once created, you need to login into docker hub credentials to push this image to docker hub
#docker login - u sara28analytics
# enter the password. 
#3. Creating a tag for the image to be pushed to docker hub
# docker tag api-test1:1.0 sara28analytics/api-test1:1.0
#4. Pushing the image to the docker hub.
#docker push sara28analytics/api-test1:1.0
#5. Once pushed, you can see in the docker hub portal. 

