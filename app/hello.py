from flask import Flask, render_template, request, send_file
import os, csv

app = Flask(__name__)

@app.route('/')
@app.route('/top')
def top():
    category = ['社会​', '気象・災害​', '科学・文化​', '政治​', 'ビジネス​', 'スポーツ​', '暮らし​', '医療・健康​']
    csv_name = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv']
    cat_url = dict(zip(category, csv_name))
    return render_template('top.html', cat_url=cat_url)

@app.route("/download")
def download():
    filename = request.args.get('csv_name')
    filepath = './data/' + filename
    return send_file(filepath, as_attachment=True, attachment_filename=filename, mimetype='text/csv')

@app.route('/detail')
def detail():
    filename = request.args.get('csv_name')
    data = read_csv(filename)
    return render_template("detail.html", data=data) # templatesフォルダ内のindex.htmlを表示する

def read_csv(filename):
    with open('./data/' + filename, mode='r', encoding='shift-jis') as f:
        data = f.readlines()
    # csv_file = open(os.getcwd() + "/app/data/" + str(filename), mode="r", encoding="ms932", errors="", newline="" )
    # f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
