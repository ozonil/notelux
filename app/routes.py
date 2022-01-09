from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import InfoForm
from flask import request
from app.models import Info

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
    form = InfoForm()
    if request.method == 'POST':
        title = form.title.data
        content = form.content.data
        print("title: ", title)
        print("content: ", content)
        print("Data recieved")
        info = Info(title=title, content=content)
        db.session.add(info)
        db.session.commit()
        flash("Information added", "success")
        return redirect(url_for('info'))
    return render_template('info.html', title='info', form=form)

@app.route('/show')
def show():
    info = db.session.query(Info).all()
    print(type(info))
    return render_template('show.html', info=info)
