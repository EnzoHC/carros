# Projeto Ozne Multimarcas


![Python version](https://img.shields.io/badge/Python-3.12.3-blue?style=for-the-badge&logo=python)
![Django version](https://img.shields.io/badge/Django-5.1-brightgreen?style=for-the-badge&logo=django)
![AWS EC2](https://img.shields.io/badge/AWS%20EC2-232F3E?style=for-the-badge&logo=amazonaws)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql)



> O Projeto "Ozne Multimarcas" é uma plataforma web desenvolvida em Django para cadastro, gerenciamento e listagem de veículos. Ele oferece funcionalidades como filtros de busca e integração com APIs externas para descrição de carros. Ideal para concessionárias ou entusiastas automotivos que desejam uma solução rápida e eficiente.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do projeto.
- **Django**: Framework web que fornece a estrutura para o desenvolvimento da aplicação.
- **AWS EC2**: Serviço de computação em nuvem utilizado para o deploy eficiente da aplicação.
- **Nginx**: Servidor web utilizado para gerenciar requisições e servir a aplicação com alta performance.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados utilizado para armazenar as informações dos veículos e usuários.

## 💻 Pré-requisitos
Antes de começar, verifique se você atendeu aos seguintes requisitos:

- `Python 3.12.3`.
- Máquina  `Linux / macOS / Windows (via WSL)`.
- 👀 `documentação do Django 5.1 / google-api-python-client / psycopg2`.

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