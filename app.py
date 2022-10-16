from datetime import datetime
from fileinput import filename
import pickle
import os
from flask import Flask, request, app,  jsonify, url_for, render_template, redirect,session
from werkzeug.utils import secure_filename

import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = 'vsuraj25'
model1 = pickle.load(open('regression.pkl', 'rb'))
model2 = pickle.load(open('classification.pkl', 'rb'))
input_csv_folder = os.path.join('static', 'input_csv_file')


@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')

#  Rendering FWI Prediction Page 
@app.route('/render_predict_fwi', methods = ['GET'])
def render_predict_fwi():
    return render_template('predict_fwi.html')

#  Rendering Forest Fire Prediction Page 
@app.route('/render_predict_forest_fire', methods = ['GET'])
def render_predict_forest_fire():
    return render_template('predict_forest_fire.html')

@app.route('/render_bulk_predict', methods = ['GET', 'POST'])
def render_bulk_predict():
    return render_template('bulk_input.html')

#  Predicting Fire Weather Index 
@app.route('/predict_fwi', methods = ['POST'])
def predict_fwi():

    data = [float(x) for x in request.form.values()]
    final_features = [np.array(data)]
    print(data)

    output1 = model1.predict(final_features)[0]
    print(output1)

    return render_template('predict_fwi.html', prediction_text = 'Fire Weather Index is {}'.format(output1))


# Predicting Forest Fire Chances
@app.route('/predict_forest_fire', methods = ['POST'])
def predict_forest_fire():

    data = [float(x) for x in request.form.values()]
    final_features = [np.array(data)]
    print(data)

    output2 = model2.predict(final_features)[0]
    print(output2)

    return render_template('predict_forest_fire.html', prediction_text2 = 'Chance of Forest Fire is {}'.format(output2))

@app.route('/bulk_input', methods = ['POST'])
def upload():
    if request.method =='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        new_filename = f"{filename.split('.')[0]}_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
        file_path = os.path.join('static', 'input_csv_file', new_filename)
        if len(os.listdir(input_csv_folder)) >0:
            for old_file in os.listdir(input_csv_folder):
                os.remove(os.path.join(input_csv_folder, old_file))
            file.save(file_path)
        else:
            file.save(file_path)

    return bulk_predict(file_path=file_path)
    # return redirect(url_for('bulk_predict'))

@app.route('/bulk_predict', methods = ['GET', 'POST'])
def bulk_predict(file_path):
    filename = os.path.basename(file_path)
    df = pd.read_csv(file_path, index_col = False)
    return render_template('bulk_predict.html',filename = filename, tables=[df.to_html(index=False)], titles=[''])

@app.route('/bulk_predict_fwi', methods = ['GET', 'POST'])
def bulk_predict_fwi():
    file_path  = os.path.join(input_csv_folder,os.listdir(input_csv_folder)[0])
    filename = os.path.basename(file_path)
    data = pd.read_csv(file_path)
    print(data)
    new_data=data.values
    output=model1.predict(new_data)
    data['FWI'] = output
    return render_template('show_prediction.html',target_prediction = 'Forest Weather Index Prediction', filename = filename, tables=[data.to_html(index=False)], titles=[''])



@app.route('/bulk_predict_forest_fire', methods = ['GET', 'POST'])
def bulk_predict_forest_fire():
    file_path  = os.path.join(input_csv_folder,os.listdir(input_csv_folder)[0])
    filename = os.path.basename(file_path)
    data = pd.read_csv(file_path)
    print(data)
    new_data=data.values
    output=model2.predict(new_data)
    data['Fire_Probablity'] = output
    return render_template('show_prediction.html',target_prediction = 'Forest Fire Probality Prediction', filename = filename, tables=[data.to_html(index=False)], titles=[''])

@app.route('/show_prediction', methods = ['GET', 'POST'])
def show_prediction(data):
    return render_template('show_prediction.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)
