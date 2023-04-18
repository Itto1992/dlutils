ARG  PYTHON_VERSION=3.7
FROM python:${PYTHON_VERSION}

ARG POETRY_VERSION=1.4.0
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -
ENV PATH /root/.local/bin:$PATH

COPY pyproject.toml poetry.lock poetry.toml ./
RUN pip install --upgrade pip && \
    poetry install --no-root
