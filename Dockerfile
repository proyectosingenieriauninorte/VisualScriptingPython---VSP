# Utiliza una imagen base de Python
FROM python:3.10.11


# Copia los archivos de tu aplicación

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Instala PyQt6
RUN pip install -r requirements.txt

EXPOSE 8080

# Define el comando de entrada para iniciar Xvfb
ENTRYPOINT [ "/usr/bin/xvfb-run", "--auto-servernum", "--server-args='-ac -screen 0 1024x768x24'" ]

# Define el comando para ejecutar tu aplicación Qt6 con Python
CMD ["python", "main.py"]