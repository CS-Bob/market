import flask
from flask import Flask, render_template, request,url_for,redirect,session
import config
from model import User
from exts import db
from decorators import login_required


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    context = {

    }
    return render_template('index.html',**context)

# class user_login(Resource):


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_name = request.values.get('user_name')
        password = request.values.get('password')
        user = User.query.filter_by(user_name=user_name).first()
        print(type(user),user,user.password)
        # if user and user.check_password(password):
        #     flask.session['id'] = user.id
        #     flask.g.user = user
        #     return render_template('index.html')
        if user and user.password==password:

            session['user_id'] = user.id
            session.permanent = False
            return render_template('index.html')
        else:
            return u'用户名或密码错误！'

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.user_name == user_name).first()
        user = User(user_name=user_name, student_name=student_name, password=password1)
        db.session.add(user)
        db.session.commit()
        return render_template('login.html')


@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
