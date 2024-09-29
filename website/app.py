from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor_v1.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods = ['POST', 'GET'])
def index():

    pred_value = 0
    if request.method == 'POST':
        age = request.form['age']
        hours_per_week = request.form['hours_per_week']
        workclass = request.form['workclass']
        education = request.form['education']
        marital_status = request.form['marital_status']
        occupation = request.form['occupation']
        '''relationship = request.form['relationship']'''
        race = request.form['race']
        native_country = request.form['native_country']
        sex = request.form['sex']

        feature_list = []
        feature_list.append(int(age))
        feature_list.append(float(hours_per_week))

        workclass_list = ['Private','Government','Self Employeed','Other']
        education_list = ['Bachelors','Some-college','11th','HS-grad','Assoc-acdm','Assoc-voc', 'Masters', 'Other']
        marital_list = ['Married','Unmarried','Other']
        occupation_list = ['Craft-repair','Sales','Other-service','Exec-managerial','Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Transport-moving', 'Other']
        '''relationship_list = ['Wife','Husband','Not-in-family', 'Unmarried', 'Other']'''
        race_list = ['White','Black','Other']
        country_list = ['Asia','North-America','South-America','Europe']
        sex_list = ['male, female']

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(workclass_list, workclass)
        traverse_list(education_list, education)
        traverse_list(marital_list, marital_status)
        traverse_list(occupation_list, occupation)
        #traverse_list(relationship_list, relationship)
        traverse_list(race_list, race)
        traverse_list(country_list, native_country) 
        traverse_list(sex_list, sex)     
    

        pred_value = prediction(feature_list)

        # Redirect to /result page with the prediction value
        return redirect(url_for('result', pred_value=int(pred_value)))
        


    return render_template('index.html', pred_value = pred_value)

@app.route('/result')
def result():
    pred_value = request.args.get('pred_value', 0, type=int)
    return render_template('result.html', pred_value=pred_value)



if __name__ == '__main__':
        app.run(debug=True)

