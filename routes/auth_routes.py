from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint("main", __name__)

# Rota de login
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Aqui você faria a validação com banco de dados
        if email == "teste@teste.com" and password == "123456":
            flash("Login bem-sucedido!", "success")
            return redirect(url_for("main.login"))
        else:
            flash("Email ou senha incorretos", "danger")

    return render_template("login.html")

# Rota de registro
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Senhas não coincidem", "danger")
            return render_template("register.html")

        # Aqui você salvaria no banco de dados
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html")

# Rota inicial
@main.route("/")
def index():
    return redirect(url_for("main.login"))
