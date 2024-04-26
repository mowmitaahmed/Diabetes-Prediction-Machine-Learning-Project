from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    # return render_template('home.html',data='Mowmita')
    # return render_template('home.html',data=[1,2,3,4,5])
    if request.method == 'POST':
        FS = int(request.form["FS"])
        FU = int(request.form["FU"])

        with open('my_model','rb') as f:
            model = pickle.load(f)

        # print(model.predict([[FS,FU]]))
        result = model.predict([[FS,FU]])

        if result[0] == "YES":
            return render_template('home.html',data=["Sorry you might have Diabetes! Please consult with any doctor!","red"])
        else:
            return render_template('home.html',data=["Congratulations! You don't have Diabetes.","green"])
        
    else :
        return render_template('home.html')

@app.route("/about")
def about():
    # return "<p>This is an about page</p>"
    return render_template('about.html')

@app.route("/profile/<string:name>")
def profile(name):
    return "Hello, "+ str(name)


@app.route("/profile/<int:id>")
def profile2(id):
    return "Your requested user with id, "+ str(id)

# @app.route('/predict',methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         FS = int(request.form["FS"])
#         FU = int(request.form["FU"])

#         with open('my_model','rb') as f:
#             model = pickle.load(f)

#         # print(model.predict([[FS,FU]]))
#         result = model.predict([[FS,FU]])

#         if result[0] == "YES":
#             return "Sorry you might have Diabetes"
#         else:
#             return "Congratulations! You don't have Diabetes."
        
#     else :
#         return "Something went wrong!"
    

if __name__ == "__main__":
    app.run(debug=True)