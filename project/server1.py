from flask import Flask, render_template, request, url_for

app = Flask(__name__)

host = "127.0.0.1"
port = 5000
debug = True

@app.route("/home")
def home_page():
    return "<h1>Welcome to Wroclaw Thoracic Surgery Centre</h1>"

@app.route("/view")
def page_view():
    return render_template("index1.html")

@app.route("/data1", methods=["POST"])   
def input_type1():
    FEV = request.form["FEV"]
    Performance = request.form["Performance"]
    Haemoptysis = request.form["Haemoptysis"]
    Dyspnoea=request.form["Dyspnoea"]
    Cough=request.form["Cough"]
    Weakness=request.form["Weakness"]
    DM=request.form["DM"]
    MI=request.form["MI"]
    PAD=request.form["PAD"]
    Smoking=request.form["Smoking"]
    AGE=request.form["AGE"]
    
  
    user_data = {"FEV":FEV, "Performance":Performance, "Haemoptysis":Haemoptysis,'Dyspnoea':Dyspnoea,'Cough':Cough,'Weakness':Weakness,'DM':DM,'MI':MI,'PAD':PAD,'Smoking':Smoking,'AGE':AGE}
    return render_template("index1.html", user=user_data)

@app.route("/inp_form")
def show_form():
    return render_template("user_form.html")

if __name__ == "__main__":
    app.run(debug = debug)