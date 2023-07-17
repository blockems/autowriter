document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addButton').addEventListener('click', function() {
        addResponse();
    });

    document.getElementById('inputField').addEventListener('keydown', function(e) {
        if (e.keyCode === 13) {  // Check for the Enter key
            e.preventDefault();  // Prevent form submission
            addResponse();
        }
    });
});

function addResponse() {
    var inputField = document.getElementById('inputField');
    var qaBox = document.getElementById('qa-box');
    if (inputField.value !== '') {
        var userText = inputField.value;
        getResponse(userText).then(responseText => {
            qaBox.innerHTML += '<div class="qa-text"><p>User: ' + userText + '</p><p>Assistant: ' + responseText + '</p></div>';
            inputField.value = '';
        });
    }
}

function getResponse(userText) {
    // Make a POST request to your Flask API
    var apiUrl = window.location.protocol + '//' + window.location.hostname + ':5001/jim';
    return fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({question: userText})
    })
    .then(response => response.json())  // Parse the response as json
    .then(data => data.openai_response) // Extract the 'openai_response' field from the JSON response
    .catch(error => console.error('Error:', error));
}