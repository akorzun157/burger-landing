from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")


@app.route('/order_now')
def order_now():
    return render_template("order_page.html")


@app.route('/download')
def download():
    return render_template("download_page.html")


if __name__ == "__main__":
    app.run(debug=True)