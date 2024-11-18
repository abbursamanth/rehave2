document.getElementById('moodForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const userAnswers = {
      answer1: document.getElementById('q1').value,
      answer2: document.getElementById('q2').value,
      answer3: document.getElementById('q3').value
    };
  
    fetch('/analyzeSentiment', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userAnswers)
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').textContent = `Your mood is predicted as: ${data.prediction}`;
    })
    .catch(error => {
      console.error('Error:', error);
      document.getElementById('result').textContent = 'Error: Unable to get mood prediction.';
    });
  });
  
  