FROM python:3.9
WORKDIR /CarBrand
COPY ./requirements.txt /CarBrand/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /CarBrand/requirements.txt

COPY ./app /CarBrand/app
COPY ./model /CarBrand/model

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

ENV PYTHONPATH="${PYTHONPATH}:/CarBrand"

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]