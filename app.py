from services.alg import Alg
from flask import Flask, render_template, request, send_file
from services.csv_handler import read_csv, write_csv

app = Flask(__name__)

@app.route("/", )
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST':  
        file = request.files['file']
        file.save(file.filename)

        matrix = read_csv(file.filename)

        try:
            graph = Alg(len(matrix), matrix)
            matches = graph.do_kuhn()

            write_csv(matches)
            
            line = graph.to_string()
            return render_template('result.html', matches = line)
        
        except:
            print("Неверный файловый ввод")
            return render_template('error.html')

    
@app.route('/download', methods=['GET'])
def download():
    if request.method == 'GET':
        return send_file('result.csv', as_attachment = True)