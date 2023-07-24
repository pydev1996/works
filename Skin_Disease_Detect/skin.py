from flask import Flask
from flask import Flask, flash, request,render_template,redirect

from werkzeug.utils import secure_filename
app = Flask(__name__,template_folder='template')

@app.route('/',methods =["GET", "POST"])
def main():
    #return "Hello World"
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)
