async function predictRisk() {
    const weather = document.getElementById("weather").value;
    const pollution = document.getElementById("pollution").value;

    const response = await fetch("http://127.0.0.1:5000/predict-risk", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            weather: weather,
            pollution: pollution
        })
    });

    const data = await response.json();

    document.getElementById("riskResult").innerText =
        "Risk Score: " + data.risk_score +
        " | Weekly Premium: ₹" + data.weekly_premium;
}
