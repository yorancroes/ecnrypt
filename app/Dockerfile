# Gebruik een officiële Python runtime als basis
FROM python:3.9-slim

# Voorkom dat Python .pyc bestanden genereert en bufferen
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Stel de werkdirectory in de container in
WORKDIR /app

# Kopieer het requirements bestand en installeer de dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Kopieer de rest van je applicatiecode
COPY . /app

# Expose de poort waarop Flask draait
EXPOSE 5000

# Stel de benodigde Flask-omgevingvariabelen in
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start de Flask-applicatie
CMD ["flask", "run"]
