FROM python:3.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# app workdir
WORKDIR /app

# Copy all files to the image
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Switch User For Security Purposes
# RUN adduser --no-create-home admin
# USER admin

# Overite conflicts
# RUN pip install PyJwt==1.7

# Expose port 8080
EXPOSE 8000

# RUN Manage Server
CMD [ "python", "manage.py", "runserver" ]

