from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Charger le modèle entraîné
rf_model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Servir la page HTML avec le formulaire

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les valeurs du formulaire
        self_harm = int(request.form['self-harm'])
        negatif_thoughts = int(request.form['negatif_thoughts'])
        sleep = int(request.form['sleep'])
        fatigue = int(request.form['fatigue'])
        academic_pressure = int(request.form['academic_pressure'])
        concentration = int(request.form['concentration'])
        Year_of_Study = int(request.form['Year _of _Study'])  # You can use this as a local variable
        family_history = int(request.form['family_history'])
        
        # Créer la liste de caractéristiques pour la prédiction
        features = [self_harm, negatif_thoughts, sleep, fatigue,
                    academic_pressure, concentration, Year_of_Study, family_history]
        
        # Faire la prédiction
        prediction = rf_model.predict([features])[0]
        
        # Message en fonction de la prédiction
        if prediction == 0:
            message = 'Pas de risque, en bonne santé mentale.'
            message_class = 'success'  # Classe CSS pour le succès (vert)
        else:
            message = 'Il y a un risque, prière de consulter un professionnel.'
            message_class = 'danger'  # Classe CSS pour le risque (rouge)
        
        return render_template('index.html', message=message, message_class=message_class)  # Afficher la prédiction sur la page HTML
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
