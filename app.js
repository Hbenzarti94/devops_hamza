document.addEventListener('DOMContentLoaded', function() {
    const dashboard = document.getElementById('dashboard');

    // Fonction pour créer des éléments HTML pour chaque utilisateur
    function createUserElement(user) {
        const userDiv = document.createElement('div');
        userDiv.className = 'user';
        userDiv.innerHTML = `<strong>Name:</strong> ${user.name} <br> <strong>Age:</strong> ${user.age}`;
        return userDiv;
    }

    // Récupérer les données depuis l'API
    fetch('http://127.0.0.1:5000/api/data')
        .then(response => response.json())
        .then(data => {
            const users = data.users;
            users.forEach(user => {
                const userElement = createUserElement(user);
                dashboard.appendChild(userElement);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            dashboard.innerHTML = '<p>Failed to load data.</p>';
        });
});
