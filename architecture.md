# 🧱 System Architecture

Rakshak follows a modular pipeline:

Weather API → Risk Model → Pricing Engine → Fraud Detection → Claim Decision

### Flow Explanation:

1. Weather API  
Collects real-time or simulated weather and pollution data.

2. Risk Model  
Analyzes disruption probability (rain, flood, pollution).

3. Pricing Engine  
Calculates weekly premium based on risk score.

4. Fraud Detection  
Checks user behavior (speed, movement pattern) to detect spoofing.

5. Claim Decision  
Approves, verifies, or flags claims based on risk & fraud score.
