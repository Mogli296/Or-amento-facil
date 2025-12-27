# Usa imagem oficial do Python 3.9
FROM python:3.9

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . /app

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta padrão do Gunicorn
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "orcamentofacil.wsgi", "--bind", "0.0.0.0:8000"]
