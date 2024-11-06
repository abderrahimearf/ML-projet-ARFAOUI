from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
app = Flask(__name__)
# Load the Random Forest model
model1 = joblib.load('model1.pkl')
model2 = joblib.load('model2.pkl')

scaler1 = joblib.load('scaler1.pkl')  # Chargez le scaler pour le modèle 1
scaler2 = joblib.load('scaler2.pkl')  # Chargez le scaler pour le modèle 2



@app.route('/')
def home():
    return render_template('hoom.html')

@app.route('/predict')
def predict_page():
    return render_template('predir.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données JSON de la requête
    data = request.get_json(force=True)

    # Vérifier quel modèle utiliser
    model_type = data.get('model')
    data.pop('model', None)  # Supprimer le champ 'model' des données

    # Définir les variables binaires (pour les deux modèles)
    binary_variables = ["X6", "X8"]
    
    # Créer un DataFrame pour les variables non binaires
    non_binary_variables = {key: data[key] for key in data.keys() if key not in binary_variables}
    non_binary_df = pd.DataFrame(non_binary_variables, index=[0])

    # Faire la prédiction en fonction du modèle spécifié
    if model_type == 1:
        # Standardiser les variables non binaires
        dfstand = scaler1.transform(non_binary_df)
        dfstand = pd.DataFrame(dfstand, columns=non_binary_df.columns)

        # Ajouter les variables binaires au DataFrame standardisé
        binary_df = pd.DataFrame(data, index=[0])[binary_variables]
        Xs_test_final = pd.concat([dfstand, binary_df], axis=1)

        # Réorganiser les colonnes pour suivre l'ordre original
        column_order = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
        Xs = Xs_test_final[column_order]

        prediction1 = model1.predict(Xs)
        return jsonify({'prediction1': prediction1[0]})
    
    elif model_type == 2:
        # Standardiser les variables non binaires
        dfstand = scaler2.transform(non_binary_df)
        dfstand = pd.DataFrame(dfstand, columns=non_binary_df.columns)

        # Ajouter les variables binaires au DataFrame standardisé
        binary_df = pd.DataFrame(data, index=[0])[binary_variables]
        Xs_test_final = pd.concat([dfstand, binary_df], axis=1)

        # Réorganiser les colonnes pour suivre l'ordre original
        column_order = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
        Xs = Xs_test_final[column_order]

        prediction2 = model2.predict(Xs)
        return jsonify({'prediction2': prediction2[0]})

    else:
        return jsonify({'error': 'Model type not recognized'}), 400

    



@app.route('/tester')
def status_page():
    return render_template('tester.html')
@app.route('/tester', methods=['POST'])  # Changer GET à POST
def tester():
    return jsonify({'tester': 'The app works properly'})

@app.route('/apropos')
def aboutus_page():
    return render_template('apropos.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
