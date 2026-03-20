# 🚀 Rakshak: Smart Protection for Every Delivery, Every Day  

## 🧩 Problem Overview  
Delivery partners (Zomato, Swiggy, Zepto) lose 20–30% income due to disruptions like heavy rain, floods, or pollution.  
They currently have no real-time income protection.  

At the same time, systems are vulnerable to GPS spoofing fraud, causing false payouts and financial loss.  

---

## 🎯 Our Solution  
Rakshak is an AI-powered parametric insurance platform that:  
- Protects weekly income of delivery partners  
- Detects real disruptions automatically  
- Prevents fraud using multi-layer intelligence  

---

## 👤 Target Persona  
Raju(24) – Swiggy delivery partner  

- A common man
- Works 8–10 hours daily  
- Earnings depend on active hours  
- Faces income loss during heavy rain / pollution  
- Needs simple, fast, and fair insurance  

---

## ⚙️ System Workflow  

1. User onboarding and zone selection  
2. AI-based risk profiling  
3. Weekly policy generation  
4. Real-time disruption monitoring  
5. Automatic claim triggering  
6. Instant payout processing (simulated)  

---

## 💰 Weekly Pricing Model  
Premium is calculated based on:  
- Area risk level  
- Historical disruption data  

Example:  
- Low risk → ₹15/week  
- High risk → ₹40/week  

---

## 🤖 AI/ML Integration  

### Risk Prediction  
Predicts disruption probability using weather and historical data  

### Dynamic Pricing  
Adjusts weekly premium based on risk  

### Fraud Detection  
Detects abnormal claim behavior using AI  

---

# 🚨 Adversarial Defense & Anti-Spoofing Strategy  

## 1. Differentiation: Real vs Fake User  

We use a Behavioral Trust Engine instead of only GPS.  

Real user:  
- Natural stops and delays  
- Irregular movement  
- Real sensor activity  

Fake user:  
- Straight-line movement  
- Constant speed  
- No physical movement  

System compares current vs past behavior and assigns risk.  

---

## 2. Data Beyond GPS  

Multi-layer data used:  
- Device fingerprint (device ID, OS patterns)  
- Network data (IP vs location mismatch)  
- Sensor data (accelerometer, gyroscope)  
- Time patterns (simultaneous activity)  
- Group patterns (same route across users)  

This helps detect coordinated fraud rings.  

---

## 3. UX Balance (Fairness System)  

Risk score (0–100):  
- 0–30 → Auto approve  
- 30–70 → Soft verification  
- 70–100 → Flag for review  

No instant blocking to protect real users.  

---

## 🛡️ Key Innovation  
Multi-layer trust system combining:  
- Behavioral AI  
- Sensor fusion  
- Fraud ring detection  
- Risk scoring  

---

## 🧱 System Architecture  

Data Sources → Feature Engine → AI Models → Risk Engine → Action Layer  

Inputs: Weather API, GPS, Sensors  
Output: Claim decision and payout  

---

## 🔌 Tech Stack  
- Frontend: React / Flutter  
- Backend: Node.js / Python  
- AI/ML: Python (Scikit-learn)  
- Database: Firebase / MongoDB  
- APIs: Weather API (mock), Maps  

---

## 📊 Dashboard   

Worker:  
- Weekly coverage  
- Earnings protected  

Admin:  
- Fraud alerts  
- Risk analytics  

---

## 🎯 Why This Stands Out  
- Behavior-based detection instead of only GPS  
- Detects fraud groups, not just individuals  
- Balances security and fairness  
- Designed for real gig worker needs  

---

## 🚀 Future Scope  
- Real-time proper app integration  
- Advanced ML models  
- Scalable fraud detection system  

---

## 💡 Inspiration  
The idea came from observing how gig workers frequently lose income during external disruptions without any financial safety net.

---

## ⚙️ What it does  
Rakshak provides AI-powered parametric insurance that automatically detects disruptions, triggers claims, and ensures fair payouts while preventing fraud.

---

## 🛠️ How we built it  
The system is designed using AI models for risk prediction, real-time monitoring through APIs, and a multi-layer fraud detection architecture combining behavioral and sensor data.

---

## 🚧 Challenges we ran into  
- Designing fraud detection beyond basic GPS validation  
- Balancing strict security with fairness for real users  
- Handling coordinated fraud scenarios like large-scale spoofing attacks  

---

## 🏆 Accomplishments that we're proud of  
- Developed a strong anti-spoofing architecture  
- Created a realistic and scalable solution  
- Designed a fair and user-friendly risk scoring system  

---

## 📚 What we learned  
- Importance of multi-layer security in real-world systems  
- Understanding fraud patterns in the gig economy  
- Designing AI systems that balance automation and fairness  

---

## 🔮 What's next for Rakshak  
- Build a proper working prototype  
- Integrate more advanced real-time APIs  
- Enhance AI models with real-world data  
