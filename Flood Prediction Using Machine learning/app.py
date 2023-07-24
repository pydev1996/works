from flask import Flask,request, url_for, redirect, render_template
import pandas as pd
import pickle
import numpy as np
import sqlite3
import calendar
import smtplib, ssl

app = Flask(__name__)

model_name = open("model.pkl","rb")
model = pickle.load(model_name)

def send_mail(reciervermail,msg,sub):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "naveensoft31@gmail.com"  # Enter your address
    receiver_email = reciervermail  # Enter receiver address
    password = "jpcfmdquhkplhnfj"
    SUBJECT=sub
    TEXT=msg
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    with open("user.txt","w") as f:
         f.write(mail1)
         f.close()
    

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return redirect("home")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("predictionhome.html")
    else:
        return render_template("signup.html")
@app.route('/home',methods=['POST','GET'])
def home():
     return render_template("predictionhome.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
    text1 = request.form['1']
    text2 = request.form['2']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text9 = request.form['9']
    text10 = request.form['10']
    


    with open("user.txt","r") as f:
         user=f.read()
    print(user)
         
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select * from info ")
    data2 = cur.fetchall()
    mail=""
    for i in data2:
         if user in i:
               mail+=i[1]
    row_df = np.array([float(text1),text2,text4,text5,text6,0,0,0,text9,text10])
    row_df = row_df.reshape(1,-1)
    prediction=model.predict(row_df) 
    if prediction == 0:
        send_mail(mail,"It is predicted that it may not flood.","Flood Predictions")
        return render_template('result.html',pred=f'It is predicted that it may not flood.')
    else:
        send_mail(mail,"It is predicted that it may  flood.","Flood Predictions")
        return render_template('result.html',pred=f'It is predicted that it may flood.')
@app.route('/rainfalpredict',methods=['POST','GET'])
def rainfalpredict():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    month=text1.split("-")[-1]

    with open("user.txt","r") as f:
         user=f.read()
    print(user)
         
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select * from info ")
    data2 = cur.fetchall()
    mail=""
    for i in data2:
         if user in i:
              mail+=i[1]
    #print(data2)
    
    m={'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    
    if (int(text3)>70 and int(text3)<90 ) and m[month]=="June" or m[month]=="July":
        send_mail(mail,"Moderate Rain (2.6 to 7.6mm)","Rainfall Predictions")
        return render_template('result.html',pred=f'Moderate Rain (2.6 to 7.6mm)')
    elif int(text3)==100 :
        send_mail(mail,"Heavy Rain may Occur (greather than 7.6mm))","Rainfall Predictions")
        return render_template('result.html',pred=f'Heavy Rain may Occur (greather than 7.6mm)')
    elif int(text5)==100 :
        send_mail(mail,"Heavy Rainfall)","Rainfall Predictions")
        return render_template('result.html',pred=f'Heavy Rainfall')
    elif (int(text5)>70 and int(text5)<90 ) and m[month]=="June" or m[month]=="July":
        send_mail(mail,"Moderate Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'Moderate Rainfall')
    elif (m[month]=="June" or m[month]=="July" or m[month]=="August" or m[month]=="September") and (int(text2)>18 and int(text2)>18):
        send_mail(mail,"Heavy Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'Heavy Rainfall')
    elif (m[month]=="June" or m[month]=="July" or m[month]=="August") and (int(text2)>25 and int(text2)>30):
        send_mail(mail,"Moderate Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'Moderate Rainfall')
    elif (m[month]=="October" or m[month]=="November" or m[month]=="December") and (int(text3)>50 and int(text3)<60) or (int(text5)>50 and int(text5)<60):
        send_mail(mail,"Low Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'Low Rainfall')
    elif (m[month]=="October" or m[month]=="November" ) and  (int(text5)>50 and int(text5)<60):
        send_mail(mail,"Low Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'Low Rainfall')
    elif (m[month]=="March" or m[month]=="April" or m[month]=="May"):
        send_mail(mail,"No Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'No Rainfall')
    elif int(text2)>35:
        send_mail(mail,"No Rainfall","Rainfall Predictions")
        return render_template('result.html',pred=f'No Rainfall')
    
@app.route('/index')
def index():
	return render_template('index.html')
@app.route('/rainfall')
def rainfall():
	return render_template('rainfall.html')


if __name__ == '__main__':
    app.run(debug=True,port=4000)
