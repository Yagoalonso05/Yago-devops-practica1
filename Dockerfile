# Usar Python 3.12 como base
FROM python:3.12-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar lista de recetas
COPY requirements.txt .

# Instalar las recetas
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo nuestro código
COPY . .

# Comando para ejecutar el programa
CMD ["python", "main.py"]