from flask import Flask, render_template, request, send_file
import os, csv

app = Flask(__name__)

@app.route('/')
@app.route('/top')
def top():
    return render_template('top.html')

@app.route("/download")
def download():
    filename = request.args.get('csv_name')
    filepath = './data/' + filename
    return send_file(filepath, as_attachment=True ,attachment_filename=filename, mimetype='text/csv')

@app.route('/detail')
def detail():
    filename = request.args.get('csv_name')
    data = read_csv(filename)
    return render_template("detail.html", data=data) # templatesフォルダ内のindex.htmlを表示する

def read_csv(filename):
    with open('./app/data/' + filename, mode='r', encoding='utf-8') as f:
        data = f.readlines()
    # csv_file = open(os.getcwd() + "/app/data/" + str(filename), mode="r", encoding="ms932", errors="", newline="" )
    # f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
