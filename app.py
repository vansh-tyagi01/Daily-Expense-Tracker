from flask import Flask,render_template,flash,request,url_for,redirect
import webbrowser

app = Flask(__name__)
app.secret_key="1235sjadjK"
expense = []

@app.route("/")
def home():
    return render_template("expense.html")

@app.route("/add_expense")
def add_expense():
    return render_template("add_expense.html")

@app.route("/form_add_expense" , methods = ["GET","POST"])
def form_add_expense():
    if request.method == "POST":
        title = request.form.get("titlename")
        category = request.form.get("categoryname")
        price = int(request.form.get("pricee"))
        date = request.form.get("datee")

        expense.append([title,category,price,date])
        flash("Expense add successfully 👍")
    return redirect(url_for("add_expense"))

@app.route("/show")
def show():
    if len(expense)==0:
        flash("No Record Found ✖️")
    return render_template("show_expense.html",expense = expense)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)



