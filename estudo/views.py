from estudo import app, db
from flask import render_template, url_for, request, redirect
#import secrets

from estudo.models import Contatos
from estudo.forms import ContatosForm

#sk = secrets.token_hex(42)

@app.route("/")
def homepage():
    usuario = 'Vando Vieira'
    idade = '42'
    #token = sk
    dic = {
        'usuario': usuario,
        'idade': idade
        #'token': token
    }
    return render_template('index.html', dic = dic)

@app.route("/contatos", methods=['GET', 'POST'])
def contatos():
    form = ContatosForm()
    context = {}
    if form.validate_on_submit():
        form.save() 
        return redirect(url_for('homepage'))       


    return render_template('contatos.html', context=context, form=form)


@app.route("/contatos/lista")
def contatosLista():
    if request.method=='GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contatos.query.order_by('nome')

    if pesquisa!='':
        dados = dados.filter_by(nome=pesquisa)
  
    context = {'dados':dados.all()}
       
    return render_template('contatos_lista.html', context=context)

@app.route("/contatos/<int:id>")
def contatosDetail(id):

    obj = Contatos.query.get(id)

    return render_template('contatos_detail.html', obj=obj)



@app.route("/contatos_old", methods=['GET', 'POST'])
def contatos_old():
    context = {}
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contatos = Contatos(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contatos)
        db.session.commit()

    return render_template('contatos_old.html', context=context)
