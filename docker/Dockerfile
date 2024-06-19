# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos requirements.txt e instalar as dependências
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte para o contêiner
COPY ../calculadora.py .
COPY ../calculadora_teste.py .
COPY ../tests/ ./tests/

# Comando padrão para rodar os testes
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
