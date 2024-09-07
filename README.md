# Projeto Ozne Multimarcas

![Python version](https://img.shields.io/badge/Python-3.12.3-blue?style=for-the-badge&logo=python)
![Django version](https://img.shields.io/badge/Django-5.1-brightgreen?style=for-the-badge&logo=django)


> O Projeto "Ozne Multimarcas" é uma plataforma web desenvolvida em Django para cadastro, gerenciamento e listagem de veículos. Ele oferece funcionalidades como filtros de busca e integração com APIs externas para descrição de carros. Ideal para concessionárias ou entusiastas automotivos que desejam uma solução rápida e eficiente.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do projeto.
- **Django**: Framework web que fornece a estrutura para o desenvolvimento da aplicação.

## 💻 Pré-requisitos
Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `Python 3.12.3`.
- Você tem uma máquina  `Linux / macOS / Windows (via WSL)`.
- Você leu `documentação do Django 5.1 / google-api-python-client / psycopg2`.

## 🚀 Instalando Ozne Multimarcas

Para instalar o `Ozne Multimarcas`, siga estas etapas:

Linux:

```
git clone https://github.com/seu-usuario/ozne-multimarcas.git
cd ozne-multimarcas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```
git clone https://github.com/seu-usuario/ozne-multimarcas.git
cd ozne-multimarcas
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

## ☕ Usando `Ozne Multimarcas`

Após a instalação, você pode iniciar o servidor de desenvolvimento com o comando:

```
python manage.py runserver
```
Acesse a aplicação no seu navegador em http://127.0.0.1:8000/.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.