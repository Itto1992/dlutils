ARG  PYTHON_VERSION=3.7
FROM python:${PYTHON_VERSION}

ENV HOME /home
WORKDIR $HOME

ARG POETRY_VERSION=1.4.0
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -
ENV PATH $HOME/.local/bin:$PATH

COPY pyproject.toml poetry.lock poetry.toml $HOME/
RUN pip install --upgrade pip && \
    poetry install --no-root
