from flask import Flask, render_template, request
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()

colors = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255]
}

@app.route("/", methods=["GET", "POST"])
def index():
    color = None
    custom_color = None
    if request.method == "POST":
        color = request.form.get("color", None)
        if color == "custom":
            custom_color = request.form.get("custom_color", None)
            if custom_color:
                try:
                    r, g, b = map(int, custom_color.split(","))
                    if all(0 <= x <= 255 for x in [r, g, b]):
                        color = (r, g, b)
                        sense.clear(color)
                    else:
                        color = None
                        custom_color = None
                except ValueError:
                    color = None
                    custom_color = None
            else:
                color = None
                custom_color = None
        elif color in colors:
            sense.clear(colors[color])
        else:
            color = None
            custom_color = None
    return render_template("html4-2.html", selected_color=color, colors=colors)

if __name__ == "__main__":
    app.run(debug=True)
