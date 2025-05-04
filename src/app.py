from flask import Flask, render_template, request

from config import config

app=Flask(__name__)

@app.route('/')

@app.route('/login', methods=['GET','post'])
def login():
    if request.method=='POST':
       print(request.form['username'])
       print(request.form['password'])
       
       return (render_template('auth/login.html'))
    
    else:
        return (render_template('auth/login.html'))

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
   app.config.from_object(config['development'])
app.run()

   