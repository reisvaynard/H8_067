import numpy as np
import pickle
import flask

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))


model = pickle.load(open('model_classifier.pkl', 'rb'))

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = {0: 'not placed', 1: 'placed'}

    return flask.render_template('main.html', prediction_text='Student must be {} to workplace'.format(output[prediction[0]]))

if __name__ == "__main__":
    app.run(debug=True)