# pull the python as a base image
FROM python:3.9

# set the working directory in the container
WORKDIR /app

# copy the requirements.txt file into the current work directory
COPY requirements.txt .

# install the required dependencies
RUN pip install --no-cache-dir  -r requirements.txt

# copy the entire local directory to the current directory in the container
COPY . .

# expose the port
EXPOSE 5000

# run the flask application
CMD ["python","app.py"]
