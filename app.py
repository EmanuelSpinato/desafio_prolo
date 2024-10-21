from flask import Flask, jsonify, redirect, request

app = Flask(__name__)


# Rota GET 1 - Retorna um HTML simples
@app.route("/")
def home():
    return "<h1>Bem-vindo à página inicial</h1>"


# Rota GET 2 - Redireciona diretamente para o link
@app.route("/movie")
def movie_page():
    return redirect("https://emanuel.aln-jh.com")


# Rota GET 3 - Retorna um JSON qualquer
@app.route("/json")
def json_data():
    data = {"username": "Emanuel", "idade": 21, "email": "emanuel@hotmail.com"}
    return jsonify(data)


# Rota POST - Recebe dados do JSON e retorna uma resposta personalizada
@app.route("/post", methods=["POST"])
def post_data():
    data = request.get_json()
    nome = data["nome"]
    email = data["email"]
    saldo = data["saldo_em_conta"]

    return jsonify(
        {
            "message": f"Olá {nome}, seu saldo atual é de {saldo} R$ e o e-mail cadastrado é {email}"
        }
    )


if __name__ == "__main__":
    app.run(debug=False)
