![Python application](https://github.com/django-cms/django-cms-quickstart/workflows/Python%20application/badge.svg?branch=main)

# django CMS

A Dockerised django CMS project, ready to deploy on [Divio](https://www.divio.com/) or another Docker-based cloud platform, and run locally in Docker on your own machine.

This version uses Python 3.8 running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

This project is endorsed by the [django CMS Association](https://www.django-cms.org/en/about-us/). That means that it is officially accepted by the dCA as being in line with our roadmap vision and development/plugin policy. Join us on [Slack](https://www.django-cms.org/slack/) for more information or questions. 

## Installation

You need to have docker installed on your system to run this project.

- [Install Docker](https://docs.docker.com/engine/install/) here.
- If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
git clone https://github.com/Myoth13/psy.git
cd psy
git branch dev origin/dev
git checkout dev
```
Now you have a source code, and you'll need to use divio app:
https://docs.divio.com/en/latest/how-to/local-cli/

Configure it to communicate with dev environment

```bash
docker compose build web
divio app pull db
docker compose up -d
```

## Contributing to the project

1) Before you start to do anything pull fresh dev branch to avoid painful mergings later! 
2) Make a new branch for your app/feature, switch to it, create new app, register it in settings
3) Merge settings.py to dev branch and push for others (dev branch)
4) When your app is ready and tested merge it with dev branch and push alongside with db (divio app push db)
5) celebrate =) 

#### Updating requirements

The project uses a 2 step approach, freezing all dependencies with pip-tools. Read more about how to handle it here: https://blog.typodrive.com/2020/02/04/always-freeze-requirements-with-pip-compile-to-avoid-unpleasant-surprises/

## Features

### Static Files with Whitenoise

This quickstart demo has a cloud-ready static files setup via django-whitenoise.

In the containerized cloud the application is not served by a web server like nginx but directly through uwsgi. django-whitenoise is the glue that's needed to serve static files in your application directly through uwsgi.

See the django-whitenoise settings in settings.py and the `quickstart/templates/whitenoise-static-files-demo.html` demo page template that serves a static file.

## Contribution

Please follow strictly PIP convention!
Please name your class distinctive and informative ! 

Bad example - there are tons of different things which have category in the project: 
```python
class Category(models.Model):
    ...
```

OK example
```python
class PostCategory(models.Model):
    ...
```

## Deployment

contact @Myothmyoth

#### Env variables
- to deploy this project in testing mode (recommended) set the environment variable `DEBUG` to `True` in your hosting environment. 
- For production environment (if `DEBUG` is false) django requires you to whitelist the domain. Set the env var `DOMAIN` to the host, i.e. `www.domain.com` or `*.domain.com`.
- If you want the media hosted on S3 set the `DEFAULT_FILE_STORAGE` variable accordingly.

#### Deployment Commands
Configure your hosting environment to run the following commands on every deployment:
- `./manage.py migrate`


#### Divio Deployment

divio.com is a cloud hosting platform optimized for django web applications. It's the quickest way to deploy this project. Here is a [video tutorial](https://www.youtube.com/watch?v=O2g5Wfoyp7Q) and a [description of the deployment steps](https://github.com/django-cms/djangocms-template/blob/mco-standalone/docs/deployment-divio.md#divio-project-setup) that are mostly applicable for this quickstart project.
