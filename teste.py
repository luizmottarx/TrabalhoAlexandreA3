from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

def calcular_perfil_investidor(respostas):
    pontuacao = 0
    
    if respostas['resposta1'] == "a":
        pontuacao += 1
    elif respostas['resposta1'] == "b":
        pontuacao -= 1

    if respostas['resposta2'] == "a":
        pontuacao -= 1
    elif respostas['resposta2'] == "b":
        pontuacao += 1
    elif respostas['resposta2'] == "c":
        pontuacao += 2

    if respostas['resposta3'] == "a":
        pontuacao -= 1
    elif respostas['resposta3'] == "b":
        pontuacao += 1
    elif respostas['resposta3'] == "c":
        pontuacao += 2

    if respostas['resposta4'] == "a":
        pontuacao -= 1
    elif respostas['resposta4'] == "c":
        pontuacao += 1
