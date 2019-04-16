from flask import Flask, render_template, request, redirect


app = Flask(__name__)
get_counter = 0
post_counter = 0


@app.route("/")
def route_home():
    return render_template("index.html")


@app.route("/request-counter", methods=["GET", "POST"])
def route_request_counter():
    global get_counter
    global post_counter
    if request.method == "GET":
        get_counter += 1
    elif request.method == "POST":
        post_counter += 1
    return redirect("/")


@app.route("/statistics")
def route_statistics():
    global get_counter
    global post_counter
    return render_template(
        "statistics.html",
        get_counter=get_counter,
        post_counter=post_counter
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)