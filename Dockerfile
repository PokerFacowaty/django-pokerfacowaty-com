FROM python:3.13 as base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /django-pokerfacowaty-com

FROM base as builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.5.0

RUN pip install "poetry==$POETRY_VERSION"

COPY . /django-pokerfacowaty-com

RUN poetry config virtualenvs.in-project true && \
    poetry install --verbose --no-root

FROM base as final
COPY --from=builder /django-pokerfacowaty-com/ /django-pokerfacowaty-com/
