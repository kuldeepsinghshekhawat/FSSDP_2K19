from flask import Flask,render_template,request
from prediction_file import prediction

app = Flask(__name__)

host = "127.0.0.1"
port = 5000
debug = True


@app.route('/home', methods=["POST"])
def user_input():
    cols = ["Symption1","Symption2","Symption3","Symption4","Symption5",
            "Symption6","Symption7","Symption8","Symption9","Symption10",
            "Symption11"]
    symptoms = []
    for col in cols:
        symptoms.append(request.form[col])
    
    patient_status = prediction(symptoms)
    
    return render_template("response.html", status=patient_status)
    

@app.route("/inp_form")
def show_form():
    return render_template("user_form.html")

if __name__ == "__main__":
    app.run(debug = debug)

