from flask import Flask, render_template, request
from sklearn.metrics import accuracy_score,confusion_matrix
import numpy as np
import pickle
from flask import Flask, render_template, request, redirect
import pandas as pd
import easygui

def read_excel():
    df = pd.read_excel('registration_data.xlsx')
    return df
def register_user(username, password, repassword):
    df = read_excel()
    new_user = pd.DataFrame({'username': [username], 'password': [password], 'repassword': [repassword]})
    df = df.append(new_user, ignore_index=True)
    df.to_excel('registration_data.xlsx', index=False)


app = Flask(__name__)
model = pickle.load(open('Liver2.pkl', 'rb'))
@app.route('/',methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        user_name = request.form.get("fname")
        pwd1 = request.form.get("psw")
        pwd2 = request.form.get("psw1")
        register_user(user_name, pwd1, pwd2)
        easygui.msgbox('Successfully Registered', 'Success')
        return redirect('/login')

    return render_template('register.html')

@app.route('/login',methods =["GET", "POST"])
def login():
    
    
    if request.method == "POST":
       
       user_name = request.form.get("uname")
       pwd=request.form.get("psw")
       print(check_user(user_name, pwd))
       if check_user(user_name, pwd):
            return redirect('/home')
       else:
            easygui.msgbox('Wrong Credentials', 'Warning')
            return redirect('/login')
    return render_template('login.html')

    
    
def check_user(username, password):
    df = read_excel()
    u=df['username'].values.tolist()
    print(u)
    p=df['password'].values.tolist()
    print(p)
    if username in df['username'].values.tolist() and int(password) in df['password'].values.tolist():
        return True
    else:
        return False



@app.route('/home',methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender = int(request.form['Gender'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])


        values = np.array([[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
        prediction = model.predict(values)
        percentage_of_liver_disease =model.predict_proba(values)[:, 1][0] * 100
        print('Percentage of liver disease:', percentage_of_liver_disease, '%')

        return render_template('result.html', prediction=percentage_of_liver_disease)


if __name__ == "__main__":
    app.run(debug=True)

