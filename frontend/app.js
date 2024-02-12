document.getElementById('battleForm').addEventListener('submit', function(e) {
    e.preventDefault();

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
        let content = 'Result: Not Valid Types (water, grass, fire, or normal)';
        if (String(data.effectiveness).toLowerCase() !== 'undefined') {
            content = `Result: ${data.effectiveness}`;
        }
        document.getElementById('result').textContent = content;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
