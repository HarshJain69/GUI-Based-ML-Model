document.addEventListener('DOMContentLoaded', function() {
    // Form submission for insurance cost prediction
    document.getElementById('predictionForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Get form data
        const formData = new FormData(this);
        
        // Send POST request to /predict endpoint
        fetch('/predict', {
            method: 'POST', 
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Show predicted price directly on the page
            const predictionResult = document.getElementById('predictionResult');
            
            // Check if the prediction is negative
            const prediction = data.prediction < 0 ? Math.abs(data.prediction) : data.prediction;
            
            predictionResult.textContent = `Estimated medical insurance cost: ₹${(parseFloat(prediction.toFixed(2))*83.22).toFixed(2)}`;
        })
        .catch(error => console.error('Error:', error));
    });

    // BMI Calculator
    document.getElementById('calculateBMI').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default button behavior

        // Get weight and height input values
        const weight = parseFloat(document.getElementById('weight').value);
        const height = parseFloat(document.getElementById('height').value);

        // Calculate BMI
        const bmi = weight / (height * height);

        // Display BMI
        const bmiResult = document.getElementById('bmiResult');
        bmiResult.textContent = `Your BMI is: ${bmi.toFixed(2)}`;
    });
});
