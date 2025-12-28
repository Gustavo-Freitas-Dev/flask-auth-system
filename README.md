# 🔐 Flask Authentication System

Sistema de autenticação web desenvolvido em **Python com Flask**, com interface HTML, focado em demonstrar **boas práticas de backend**, **organização de código** e **segurança básica**.

Este projeto foi criado com o objetivo de **chamar a atenção de recrutadores**, mostrando como implementar um fluxo de login real e bem estruturado.

---

## 🚀 Funcionalidades

- Cadastro de usuários
- Login e logout
- Hash de senha com **bcrypt**
- Sessões seguras
- Rotas protegidas
- Interface web simples e funcional
- Persistência com **SQLite**

---

## 📁 Estrutura do Projeto

```text
flask-auth-system/
├── app.py
├── config.py
├── database/
│   └── db.py
├── models/
│   └── user.py
├── services/
│   └── auth_service.py
├── routes/
│   ├── auth_routes.py
│   └── dashboard_routes.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/
│   └── style.css
└── README.md

```

O projeto segue uma **separação clara de responsabilidades**, facilitando manutenção e escalabilidade.

---

## 🔐 Segurança Aplicada

- Senhas nunca são armazenadas em texto puro
- Hashing de senha utilizando `bcrypt`
- Controle de sessão com `Flask session`
- Proteção de rotas autenticadas

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- SQLite
- HTML5 + CSS3
- bcrypt

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/flask-auth-system.git
cd flask-auth-system
