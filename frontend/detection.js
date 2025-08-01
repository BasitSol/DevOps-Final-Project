// Scroll behavior for header
window.addEventListener('scroll', function () {
    const header = document.querySelector('header');
    header.classList.toggle('scrolled', window.scrollY > 50);
});

// Mobile navigation toggles
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const body = document.body;

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
    body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : 'auto';
});

document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
        body.style.overflow = 'auto';
    });
});

document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
        body.style.overflow = 'auto';
    }
});

// Live update range value
document.querySelectorAll('input[type="range"]').forEach(range => {
    const valueDisplay = range.nextElementSibling;
    range.addEventListener('input', () => {
        valueDisplay.textContent = range.value;
    });
});

// BMI calculator
function calculateBMI(weight, height) {
    return (weight / (height * height)).toFixed(2);
}

// Prediction form submit handler
document.getElementById('detectionForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const results = document.getElementById('results');
    results.classList.remove('hidden');
    results.querySelector('.result-text').textContent = 'Analyzing...';

    const formData = {
        age: parseInt(document.getElementById('age').value),
        gender: parseInt(document.getElementById('gender').value),
        bmi: parseFloat(document.getElementById('bmi').value),
        smoking: parseInt(document.getElementById('smoking').value),
        geneticRisk: parseInt(document.getElementById('geneticRisk').value),
        physicalActivity: parseFloat(document.getElementById('physicalActivity').value),
        alcoholIntake: parseFloat(document.getElementById('alcoholIntake').value),
        cancerHistory: parseInt(document.getElementById('cancerHistory').value)
    };

    console.log('Sending data:', formData);

    // Dynamically build backend URL (use same domain/IP + backend port)
    const backendUrl = `${window.location.protocol}//${window.location.hostname}:5000/predict`;

    fetch(backendUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                return response.text().then(text => {
                    throw new Error(`Server error: ${text}`);
                });
            }
            return response.json();
        })
        .then(data => {
            console.log('Received data:', data);
            const resultText = data.prediction === 1
                ? 'High Risk - Please consult a healthcare professional'
                : 'Low Risk - Continue maintaining a healthy lifestyle';

            results.querySelector('.result-text').textContent = resultText;
            results.querySelector('.indicator-circle').style.backgroundColor =
                data.prediction === 1 ? '#ff4444' : '#44cc44';
        })
        .catch(error => {
            console.error('Detailed error:', error);
            results.querySelector('.result-text').textContent = 'Error: ' + error.message;
            results.querySelector('.indicator-circle').style.backgroundColor = '#ffaa00';
        });
});

// Form reset utility
function resetForm() {
    document.getElementById('detectionForm').reset();
    document.getElementById('result').innerText = '';
}
