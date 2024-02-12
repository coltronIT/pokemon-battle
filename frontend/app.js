document.getElementById('battleForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the default form submission

    const attackType = document.getElementById('attackType').value;
    const pokemonType = document.getElementById('pokemonType').value;

    fetch('/play/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ attack_type: attackType, pokemon_type: pokemonType }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = `Result: ${data.effectiveness}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
