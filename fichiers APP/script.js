// Fonction pour envoyer des données pour le modèle 1
function predictModel1() {
    // Récupération des valeurs des champs d'entrée
    const data1 = {
        model: 1,
        X1: parseFloat(document.getElementById('X1').value),
        X2: parseFloat(document.getElementById('X2').value),
        X3: parseFloat(document.getElementById('X3').value),
        X4: parseFloat(document.getElementById('X4').value),
        X5: parseFloat(document.getElementById('X5').value),
        X6: parseFloat(document.getElementById('X6').value),
        X7: parseFloat(document.getElementById('X7').value),
        X8: parseFloat(document.getElementById('X8').value)
    };

    // Envoi de la requête POST pour /predict avec les données
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data1)
    })
    .then(response => response.json())
    .then(data1 => {
        // Affichage du résultat de la prédiction
        document.getElementById('result1').innerText = "Prediction  : " + data1.prediction1;
    })
    .catch(error => console.error('Erreur:', error));
}

// Fonction pour envoyer des données pour le modèle 2
function predictModel2() {
    const data2 = {
        model: 2,
        X1: parseFloat(document.getElementById('Z1').value),
        X2: parseFloat(document.getElementById('Z2').value),
        X3: parseFloat(document.getElementById('Z3').value),
        X4: parseFloat(document.getElementById('Z4').value),
        X5: parseFloat(document.getElementById('Z5').value),
        X6: parseFloat(document.getElementById('Z6').value),
        X7: parseFloat(document.getElementById('Z7').value),
        X8: parseFloat(document.getElementById('Z8').value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data2)
    })
    .then(response => response.json())
    .then(data2 => {
        document.getElementById('result2').innerText = "Prediction  : " + data2.prediction2;
    })
    .catch(error => console.error('Erreur:', error));
}

// Fonction pour tester l'application
function testerApplication() {
    fetch('/tester', {
        method: 'POST',  // Utiliser POST au lieu de GET
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // Vous pouvez ajouter des données si nécessaire
    })
    .then(response => {
        // Si la réponse n'est pas correcte, renvoyez une erreur
        if (!response.ok) {
            throw new Error('Erreur réseau : ' + response.status);
        }
        return response.json();  // Transformez la réponse en JSON
    })
    .then(data => {
        // Mettez à jour le contenu avec les données reçues
        document.getElementById('testResult').innerHTML = "<h2>" + data.tester + "</h2>";
    });
}



// Redirige vers la page d'accueil
function accueil() {
    window.location.href = "/";
}

// Redirige vers la page de prédiction
function showPrediction() {
    window.location.href = "/predict";
}

// Redirige vers la page "À Propos du Créateur"
function showAbout() {
    window.location.href = "/apropos";
}

// Redirige vers la page de test
function showTest() {
    window.location.href = "/tester";
}
