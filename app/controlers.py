from flask import Flask,redirect,render_template,session,request,flash
from flask_sqlalchemy import SQLAlchemy
from models import User

db= SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key="ma_cle_secret"
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///dbdevoir.db'
    db.init_app(app)
   
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    @app.route('/')
    def home():
        return render_template('Accueil.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')
    
    @app.route('/accueil')
    def accueil():
        return render_template('Accueil.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        return render_template('Accueil.html')

    @app.route('/login', methods=['POST'])
    def verify():
        vrf_email=request.form['txt_email']
        vrf_password=request.form['txt_password']
        user = User.query.filter_by(email=vrf_email).first()
        
        if user and user.password == vrf_password :      
            return redirect('/app')
        else :
            flash("votre email ou votre mot de passe ne correspond pas")
            return redirect('/login')

    @app.route('/app')
    def after_log():  
        return render_template('app.html')
    

    @app.route('/signup',methods=['POST'])
    def insert():
        nom=request.form['txt_nom']
        prenom=request.form['txt_prenom']
        email=request.form['txt_email']
        password=request.form['txt_password']
        password_conf=request.form['txt_password_conf']
        user = User.query.filter_by(email=email).first()
        
        
        if user :
            flash("cet email est déja utilisé")
            return redirect('/signup')
        elif password != password_conf :
            flash("les mot de passe ne correspondent pas")
            return redirect('/signup')
        else : 
            user_add=User(nom=nom,prenom=prenom,email=email,password=password)
            db.session.add(user_add)
            db.session.commit()
            nom = session.get('nom')       
            return render_template('app.html',nom=nom)
    return app  


def create_database(app):
    db.create_all(app=app)
  
        
        
