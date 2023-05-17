from app import app

@app.route("/") # <- decorator
def index():
    return "Hello world"

@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return 'Olá, %s!' % name
    else:
        return "Olá"
    
@app.route("/inteiro/<int:num>") # força tipagem
def interito(num):
    return f"numero é {num}"