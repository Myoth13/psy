FROM python:3.9

#### oAuth support
RUN apt-get update
RUN apt-get install -y openssl
RUN apt-get install -y libssl-dev
RUN apt-get install -y build-essential
# Get Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
#biuld crypto
RUN pip install --upgrade pippip install --upgrade pip
RUN pip install cryptography
RUN pip install social-auth-app-django
####

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
