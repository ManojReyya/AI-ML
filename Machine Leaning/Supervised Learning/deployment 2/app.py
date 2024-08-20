from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('profit.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   p = request.form["rd"]
   q = request.form["as"]
   r = request.form["ms"]
   s = request.form["s"]
   if (s=="cal"):
       s=0
   elif(s=="flo"):
       s=1
   else:
       s=2 

   t =  [[float(p),float(q),float(r),float(s)]] 
   output =model.predict(t)[0]
   print(output)

   return render_template("index.html", y = "The Predicted profit is:  "+str(np.round(output)))

if __name__ == '__main__' :
    app.run(debug=True)
          





