#Importando Bibliotecas e calculando pesos nas perguntas (Luiz)
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

def calcular_perfil_investidor(respostas):
    pontuacao = 0

#As pontuações abaixos dizem como será calculado os perfis de investimento. A lógica é somar pontos e subtrair pontos.
    
    #Resposta1 = Somar 1 ponto caso A selecionado / Subtrair 1 ponto caso B selecionado

    if respostas['resposta1'] == "a":
        pontuacao += 1
    elif respostas['resposta1'] == "b":
        pontuacao -= 1
        
    #Resposta2 = Subtrair 1 ponto caso A selecionado / Somar 1 ponto caso B selecionado / Somar 2 pontos caso C selecionado
    
    if respostas['resposta2'] == "a":
        pontuacao -= 1
    elif respostas['resposta2'] == "b":
        pontuacao += 1
    elif respostas['resposta2'] == "c":
        pontuacao += 2
        
    #Resposta3 = Subtrair 1 ponto caso A selecionado / Somar 1 ponto caso B selecionado / Somar 2 pontos caso C selecionado

    if respostas['resposta3'] == "a":
        pontuacao -= 1
    elif respostas['resposta3'] == "b":
        pontuacao += 1
    elif respostas['resposta3'] == "c":
        pontuacao += 2

    #Resposta4 = Subtrair 1 ponto caso A selecionado / Somar 1 ponto caso C selecionado

    if respostas['resposta4'] == "a":
        pontuacao -= 1
    elif respostas['resposta4'] == "c":
         pontuacao += 1
        
#Calculando condições de cada tipo de Perfil de acordo com os pesos definidos
if pontuacao <= 0:
        perfil = "Conservador"
        sugestoes = "Fundos de Renda fixa;","Poupança;","Tesouro Direto (Tesouro Selic);","CDBs (Certificados de Depósito Bancário) de bancos grandes;","LCIs e LCAs (Letras de Crédito Imobiliário e do Agronegócio)."
    elif pontuacao <= 2:
        perfil = "Moderado"
        sugestoes = "Tesouro Direto (Tesouro IPCA+);", "CDBs de bancos médios e pequenos;", "Fundos Multimercado;", "Debêntures;", "ETFs (Exchange Traded Funds)."
    else:
        perfil = "Agressivo"
        sugestoes = "Ações;", "Fundos de Ações;", "COEs (Certificados de Operações Estruturadas);", "Criptomoedas;", "Fundos de Investimento Imobiliário (FIIs)."

    return perfil, sugestoes

@app.route('/')
def index():
    return render_template('index.html')
    
#Requisição de formulário do usuário, e testa condição de validações com campos obrigatórios e salva respostas
@app.route('/cliente', methods=['GET', 'POST'])
def cliente():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        session['sobrenome'] = request.form['sobrenome']
        session['data_nascimento'] = request.form['data_nascimento']
        session['banco'] = request.form['banco']
        return redirect(url_for('perguntas'))
    return render_template('cliente.html')

@app.route('/perguntas', methods=['GET', 'POST'])
def perguntas():
    if request.method == 'POST':
        respostas = {
            'resposta1': request.form.get('resposta1'),
            'resposta2': request.form.get('resposta2'),
            'resposta3': request.form.get('resposta3'),
            'resposta4': request.form.get('resposta4')
        }

        if None in respostas.values():
            return render_template('perguntas.html', error="Por favor, selecione uma resposta para todas as perguntas.")

        perfil, sugestoes = calcular_perfil_investidor(respostas)
        session['perfil'] = perfil
        session['sugestoes'] = sugestoes
        return redirect(url_for('resultado'))
    return render_template('perguntas.html')

    app.route('/resultado', methods=['GET'])
    def resultado():
        perfil = session.get('perfil')
        sugestoes = session.get('sugestoes')
        nome = session.get('nome')
        sobrenome = session.get('sobrenome')
        
        if perfil is None or sugestoes is None:
            return redirect(url_for('perguntas'))
    
        return render_template('resultado.html', perfil=perfil, sugestoes=sugestoes, nome=nome, sobrenome=sobrenome)
    
    if __name__ == '__main__':
        app.run(debug=True)
