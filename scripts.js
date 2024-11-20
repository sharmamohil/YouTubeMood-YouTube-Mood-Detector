

document.getElementById('connectButton').addEventListener('click', function() {
    alert('Connecting to YouTube...');
    displayMoodAnalysis();
});

function displayMoodAnalysis() {
    const moodResults = document.getElementById('moodResults');
    moodResults.innerHTML = `
        <h3>Mood Analysis Results</h3>
        <p><strong>Predominant Mood:</strong> Happy</p>
        <p><strong>Positive Shorts:</strong> 70%</p>
        <p><strong>Neutral Shorts:</strong> 20%</p>
        <p><strong>Negative Shorts:</strong> 10%</p>
    `;
}
