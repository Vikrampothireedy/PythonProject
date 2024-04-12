from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database import df


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/dataprocessing')
def dataprocessing():
    return render_template('dataprocessing.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html', dataset=dataset)

csv_file_path = 'loan_data.csv'
df = pd.read_csv(csv_file_path)
dataset = df.to_dict(orient='records')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





