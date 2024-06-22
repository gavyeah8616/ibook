from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_folder='')

@app.route('/')
def helloworld():
  return render_template("index.html")
  
@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/how-to-use-ibooks")
def howtoibook():
    return "<p>Hello! u may be wondering how to use ibooks. well it's easy</p>"
  

if __name__ == '__main__' :
  app.run(host='0.0.0.0', port=5000)
