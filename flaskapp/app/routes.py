from flask import Flask, render_template, url_for, request,redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/hello/<user>')
def hello_name(user):
   return render_template("hello.html", name=user)

@app.route('/hello2/<score>')
def hello_score(score):
   return render_template("score.html", marks=score)

@app.route('/success/<name>/<addr>')
def success(name,addr):
   return "welcome %s in %s" % (name, addr)


@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      name = request.form['name'] 
      addr = request.form['addr'] 
      return redirect(url_for('success', name=name,addr=addr))
   else : 
      name = request.args.get('name')
      addr = request.args.get('addr')
      return redirect(url_for('success', name=name, addr=addr))

@app.route('/loginFirst')
def login1():
   return render_template("login.html")


@app.route('/result')
def result():
   dict = {'phy':50, 'che':60, 'math':70}
   value = request.form
   return render_template("result.html", result=dict)

if __name__ == '__main__':
   app.run(debug=True)


