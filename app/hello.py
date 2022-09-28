from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
@app.route('/top')
def top():
    return render_template('top.html')

@app.route("/download")
def download():
    filepath = "./data/test.csv"
    filename = os.path.basename(filepath)
    return send_file(filepath, as_attachment=True,
                     attachment_filename=filename,
                     mimetype='text/csv')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
