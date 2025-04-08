# Usar la imagen base de Ubuntu 20.04
FROM ubuntu:20.04

# Configurar la zona horaria y evitar preguntas interactivas
ENV DEBIAN_FRONTEND=noninteractive
RUN ln -sf /usr/share/zoneinfo/America/Lima /etc/localtime && \
    echo "America/Lima" > /etc/timezone && \
    apt-get update && apt-get install -y \
    tzdata \
    python3 \
    python3-pip \
    python3-dev \
    default-libmysqlclient-dev \
    mysql-server \
    build-essential \
    pkg-config \
    libssl-dev \
    && apt-get clean

# Copiar el código de la aplicación y el archivo de configuración
COPY app/ /app
COPY mysql_config.ini /app/
WORKDIR /app

# Crear e instalar las dependencias de Python desde requirements.txt
RUN echo "Flask\nFlask-MySQLdb\nmysql-connector-python\npsycopg2-binary\nflask-cors" > requirements.txt && \
    pip3 install -r requirements.txt

# Exponer el puerto de la aplicación Flask
EXPOSE 5000

# Inicializar MySQL y ejecutar la aplicación Flask
CMD ["sh", "-c", "service mysql start && mysql -u root -padmin -e 'CREATE DATABASE IF NOT EXISTS flaskmysql;' && python3 app.py"]