#Deriving the latest base image
FROM python:3.9


# Set the working directory to /camping
WORKDIR /camping

#to COPY the remote file at working directory in container
COPY . /camping

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
#CMD ["sh", "-c", "python camping.py --start-date 2024-06-06 --end-date 2024-08-27 --parks 232769 232768 --nights 1 | python notifier.py"]
RUN chmod +x /camping/entrypoint.sh

CMD ["/camping/entrypoint.sh"]

