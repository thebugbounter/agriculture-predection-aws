import pickle
from flask import Flask, render_template, request

# Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('agriculture.pkl', 'rb'))

# Routes
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/prediction', methods=['POST'])
def predict():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorous'])
    K = int(request.form['Pottasium'])
    temperature = int(request.form['Temperature'])
    humidity = int(request.form['Humidity'])
    ph = int(request.form['PH'])
    rainfall = int(request.form['Rainfall'])

    # Check input ranges
    if not (0 <= N <= 150 and 0 <= P <= 150 and 0 <= K <= 210 and 5 <= temperature <= 50
            and 10 <= humidity <= 100 and 1 <= ph <= 9 and 10 <= rainfall <= 300):
        return render_template('index.html', output="Input values are not within suitable ranges.")

    Suitable_Crop = loadedModel.predict([[N, P, K, temperature, humidity, ph, rainfall]])[0]

    return render_template('index.html', output=Suitable_Crop)







# Main function
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
