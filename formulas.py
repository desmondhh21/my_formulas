from flask import Flask, render_template, request

app = Flask(__name__)

# Formula functions
def square_area(length, width):
    return length * width

def triangle_area(base, height):
    return (base * height) / 2

def circle_area(radius, pi=3.141592653589793):
    return pi * (radius ** 2)

def rsi_signal(rsi):
    if rsi < 5 or rsi > 95:
        return f"Pull the trigger! RSI is {rsi}"
    else:
        return f"Don't pull the trigger yet! RSI is {rsi}"

def gravitational_force(m1, m2, distance, gconstant=6.677430e-11):
    return gconstant * (m1 * m2) / (distance ** 2)

@app.route("/", methods=["GET", "POST"])
def index():
    square_result = triangle_result = circle_result = rsi_result = gravity_result = None

    if request.method == "POST":
        calc_type = request.form.get("calc_type")
        reset_type = request.form.get("reset")

        if reset_type == calc_type:
            # Reset requested: clear only that result
            return render_template("index.html",
                                   square_result=None,
                                   triangle_result=None,
                                   circle_result=None,
                                   rsi_result=None,
                                   gravity_result=None)

        try:
            if calc_type == "square":
                l = float(request.form["length"])
                w = float(request.form["width"])
                square_result = f"Square Area: {square_area(l, w)}"

            elif calc_type == "triangle":
                b = float(request.form["base"])
                h = float(request.form["height"])
                triangle_result = f"Triangle Area: {triangle_area(b, h)}"

            elif calc_type == "circle":
                r = float(request.form["radius"])
                circle_result = f"Circle Area: {circle_area(r):.2f}"

            elif calc_type == "rsi":
                rsi = float(request.form["rsi"])
                rsi_result = rsi_signal(rsi)

            elif calc_type == "gravity":
                m1 = float(request.form["mass1"])
                m2 = float(request.form["mass2"])
                d = float(request.form["distance"])
                force = gravitational_force(m1, m2, d)
                gravity_result = f"Gravitational Force: {force:.3e} N"

        except (ValueError, KeyError):
            if calc_type == "square":
                square_result = "Invalid input."
            elif calc_type == "triangle":
                triangle_result = "Invalid input."
            elif calc_type == "circle":
                circle_result = "Invalid input."
            elif calc_type == "rsi":
                rsi_result = "Invalid input."
            elif calc_type == "gravity":
                gravity_result = "Invalid input."

    return render_template("index.html",
                           square_result=square_result,
                           triangle_result=triangle_result,
                           circle_result=circle_result,
                           rsi_result=rsi_result,
                           gravity_result=gravity_result)

if __name__ == "__main__":
    app.run(debug=True)
