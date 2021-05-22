from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session, users
from secrets import token_hex
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Vezdekod1337'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(users.User).get(user_id)


class LoginForm(FlaskForm):
    password = PasswordField('Код авторизации:', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия:', validators=[DataRequired()])
    name = StringField('Имя:', validators=[DataRequired()])
    position = SelectField('Должность:', choices=["СМО", "ВМО", "МО", "СКМ", "КМ", "К"])
    gosb = SelectField('Подразделение:',
                       choices=["4157/1111", "9070/2222", "8635/3333", "8636/4444", "8567/5555", "8645/6666",
                                "8557/7777", "8556/8888"])
    submit = SubmitField('Зарегистрироваться')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = users.User(
            surname=form.surname.data,
            name=form.name.data,
            position=form.position.data,
            gosb=form.gosb.data
        )
        code = token_hex(16)
        user.set_password(code)
        session.add(user)
        session.commit()
        return render_template('info_page.html', code=code)
    return render_template('register.html', title='Регистрация', form=form, message='')


def main():
    db_session.global_init("db/chat.sqlite")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(users.User).filter(users.User.password == form.password.data).first()
        if user:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               title='Вход',
                               message="Неправильный код авторизации!",
                               form=form)
    return render_template('login.html', title='Вход', form=form, message='')


@app.route('/')
def sessions():
    return render_template('index.html', title='Главная')


@app.errorhandler(404)
def handler(e):
    return render_template('error_page.html', title='Не найдено', message="Упс! Этой страницы не существует!")


@app.errorhandler(500)
def handler(e):
    return render_template('error_page.html', title='Ошибка', message="Упс! Произошла неожиданная ошибка.")


if __name__ == "__main__":
    main()
