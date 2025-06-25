from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio/<int:id>")
def portfolio_detail(id):
    # You would typically fetch portfolio item details from a database here
    return render_template("portfolio-detail.html", item_id=id)

if __name__ == "__main__":
    app.run(debug=True)