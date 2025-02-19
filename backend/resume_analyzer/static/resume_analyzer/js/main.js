document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('resume-upload-form');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch('/upload/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function displayResults(data) {
        resultsDiv.innerHTML = `
            <h2>Analysis Results</h2>
            <p>${data.analysis_results}</p>
        `;
    }
});
