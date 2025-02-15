from python:3.11-slim

env PIP_DISABLE_PIP_VERSION_CHECK=1 
env PYTHONBUFFERED=1


WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv


RUN /bin/bash -c "source venv/bin/activate"

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    odbcinst \
    libpq-dev \
    libsqlite3-dev \
    libssl-dev \
    freetds-bin \
    freetds-dev \
    tdsodbc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install  -r  requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "5000"]