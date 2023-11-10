from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)   
app.secret_key = 'your_secret_key'  

users = {'chiwon': '1234'}

@app.route('/')
def index():
    
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST']) 

def login():
   
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        
        if users.get(username) == password:
            
            session['loggedin'] = True
            session['username'] = username
            
            return redirect(url_for('index'))
        else:
            
            msg = '사용자 이름 혹은 비밀번호가 잘못되었습니다!'
   
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    
    session.pop('loggedin', None)
    session.pop('username', None)
   
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  