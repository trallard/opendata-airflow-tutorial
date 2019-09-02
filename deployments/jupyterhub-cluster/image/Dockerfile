FROM jupyter/scipy-notebook

LABEL maintainer="Tania Allard trallard[at]bitsandchips.me"

ENV SLUGIFY_USES_TEXT_UNIDECODE yes
ARG AIRFLOW_USER_HOME=/home/jovyan/work


COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8080 8888 5555 8793