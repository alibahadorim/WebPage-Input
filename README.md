# WebPage-Input
Create a basic web input form to input and display your full name.


 Part 1
 Create a basic web input form to input and display your full name.
from flask import Flask, request, render_template, redirect import os
app = Flask(__name__)
img = os.path.join('static')
@app.route("/", methods=["GET", "POST"]) def index():
file = os.path.join(img,'image.png') if request.method == "POST":
        user_name = request.form["user_name"]
return redirect(f"/fullname/{user_name}") return render_template("4-1.html",image=file)
@app.route("/fullname/<user_name>") def fullname(user_name):
file = os.path.join(img,'image.png')
return render_template("full.html", name=user_name,image=file )
if __name__ == "__main__": app.run(debug=True)
 First page to take the full name

  Automatic redirecting to Result page after submitting the full name
 
 Part 2
 Create a second web input form to accept a HTML color code and display the color on your Pi’s LED array.
from flask import Flask, render_template, request from sense_hat import SenseHat
app = Flask(__name__)
sense = SenseHat()
colors = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255]
}
@app.route("/", methods=["GET", "POST"]) def index():
color = None
custom_color = None
if request.method == "POST":
color = request.form.get("color", None) if color == "custom":
custom_color = request.form.get("custom_color", None) if custom_color:
try:
r, g, b = map(int, custom_color.split(",")) if all(0 <= x <= 255 for x in [r, g, b]):
                        color = (r, g, b)
sense.clear(color) else:
color = None
custom_color = None except ValueError:
color = None
custom_color = None else:
color = None
custom_color = None elif color in colors:
sense.clear(colors[color]) else:
color = None
custom_color = None
return render_template("html4-2.html", selected_color=color, colors=colors)
 if __name__ == "__main__":
Green,Red and Blue are already in the list to be chosen by the user and choose color will be displayed
 app.run(debug=True)

  By choosing the custom from the list user can enter any decimal values corresponding a color.
 Green LEDs after sending pressing the update
