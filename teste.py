
@app.route('/resultado', methods=['GET'])
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
