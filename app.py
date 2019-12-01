from flask import Flask,render_template,url_for,redirect
import random
from string import *

  
app = Flask(__name__)

@app.route('/')
def index():
    symbols = ascii_letters + punctuation +  digits
    main_random = random.SystemRandom()
    password =  "".join(main_random.choice(symbols)
                    for i in range(18))
    x = str(password)
    return render_template('index.html',x=x)

if __name__ == '__main__':
    app.run()

