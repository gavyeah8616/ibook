from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_folder='')

@app.route('/')
def helloworld():
#  return "<p>Hello!</p>"
  return render_template("index.html")
if __name__ == '__main__' :
  app.run(host='0.0.0.0', port=5000)