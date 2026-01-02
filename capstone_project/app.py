from flask import Flask,render_template,request
from model import prediction_model

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/output',methods=['POST'])
def output():
    if request.method=="POST":
        name=request.form['name']
        study=request.form['study_hour']
        marks=request.form['marks']
        attendence=request.form['attendence']
        input=[int(marks),int(attendence),int(study)]
        output=prediction_model(input)
        output=int(output[0])
        return render_template("output.html",name=name,output=output)
    return "Enter valid input"

if __name__=="__main__":
    app.run(debug=True)