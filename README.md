# HTML-to-PDF-Converter
### Service for generating PDF

### A service that accepts a link to a page or HTML file as input, and returns a PDF file in response.
### If a link comes to the input, then the service follows the link and makes a PDF from it.
### If an HTML file comes in, the service turns it into PDF.

---

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)
![GitHub](https://img.shields.io/github/license/spanickroon/HTML-to-PDF-Converter)

---

## Configuration

You need to create a file **dev.env** at the root of the project

File contents:
```bash
XDG_RUNTIME_DIR=/tmp/runtime-root

SECRET_KEY=

DATABASE_ENGINE=
DATABASE_HOST=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_PORT=5432

DROPBOX_APP_KEY=
DROPBOX_APP_SECRET_KEY=
DROPBOX_OAUTH2_TOKEN=
DROPBOX_ROOT_PATH=

EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587
```
---

## Installation

To install, you need to run:
```bash
docker-compose up -d --build
```

To put containers, it is enough to write:
```bash
docker-compose down -v
```

To see the logs write:
```bash
docker-compose logs -f
```

To start using go to:
```bash
http://127.0.0.1:8000/converter/
```

---

## Technology stack

- **Python 3.8.5**
- **Django 3.1.6**
- **Django Rest Framework 3.12.2**
- **Celery 5.0.1**
- **Redis 2.5.3**
- **PostgreSQL**

---

## Using 

#### We are greeted by a page with input fields for a file, links to a website, email:

![image](https://user-images.githubusercontent.com/37241257/107153677-dded1f80-697f-11eb-9a50-82c6e39acb1d.png)

---

#### In order to get a PDF, we must fill out the field with email

#### Next, we can fill in the fields with the file and the link separately or together. 
#### If instead of then we receive two different files. 

![image](https://user-images.githubusercontent.com/37241257/107153737-20aef780-6980-11eb-9797-2863f90b479e.png)

---

#### After clicking on the button, a new page will be opened, if you saw the status message, then you can go to the mail and wait for the worker to work and drop the final file to us 

#### We received 2 letters with a link to our documents:

![image](https://user-images.githubusercontent.com/37241257/107153891-fc074f80-6980-11eb-9574-98cd8e9a9d7f.png)

---

#### All files are stored on the dropbox:

![image](https://user-images.githubusercontent.com/37241257/107153952-4c7ead00-6981-11eb-978e-51a88b1690bb.png)

---

#### Each file has a unique name depending on the time^

![image](https://user-images.githubusercontent.com/37241257/107153961-57d1d880-6981-11eb-8d9a-26a7d04dd6ef.png)

![image](https://user-images.githubusercontent.com/37241257/107153971-628c6d80-6981-11eb-8484-7baedde0a611.png)


### Examples of documents that turned out can be viewed in the examples directory 
---