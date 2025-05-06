# Usamos una imagen base de Python
FROM python:3.10-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los requisitos de la aplicación
COPY requirements.txt /app/

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de la aplicación al contenedor
COPY . /app/

# Exponemos el puerto en el que Flask correrá
EXPOSE 5000

# Comando por defecto para ejecutar la app Flask
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]
