import pickle
from flask import Flask,render_template,request
import pandas as pd
from recomendation import predict

app=Flask(__name__,template_folder='templates/')
model=pickle.load(open("model.pkl",'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    input=request.form['uname']
    prediction=model.pre(input)
    prediction=prediction.values.tolist()
    

    # prediction=prediction.split('\n')
    
    return render_template('index.html',prediction_text=prediction) 

if __name__=="__main__":
    # from model import predict
    app.run(debug=True)