from flask import Flask, request, render_template, redirect
import os
app = Flask(__name__)
img = os.path.join('static') 

@app.route("/", methods=["GET", "POST"])
def index():
    file = os.path.join(img,'image.png') 
    if request.method == "POST":
        user_name = request.form["user_name"]
        return redirect(f"/fullname/{user_name}")
    return render_template("4-1.html",image=file)

@app.route("/fullname/<user_name>")
def fullname(user_name):
    file = os.path.join(img,'image.png') 
    return render_template("full.html", name=user_name,image=file )

if __name__ == "__main__":
    app.run(debug=True)
