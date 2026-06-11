# Safe Drive System
#Developed by : Saja
#A simple driving risk assessment system

risk_score = 0

speed = int(input("Enter speed: "))
phone = input("Using phone while driving? (yes/no): ")
seatbelt = input("Wearing seatbelt? (yes/no): ")
tired = input("Feeling tired or sleepy? (yes/no): ")

if speed > 140:
    risk_score += 50
elif speed > 120:
    risk_score += 30

if phone == "yes":
    risk_score += 30

if seatbelt == "no":
    risk_score += 20

if tired == "yes":
    risk_score += 20

print("\n===== Safe Drive Report =====")
print("Risk Score:", risk_score)

if risk_score >= 70:
    print("Risk Level: High Risk")
    print("Recommendation: Reduce speed, avoid distractions, and rest before driving.")

elif risk_score >= 40:
    print("Risk Level: Medium Risk")
    print("Recommendation: Drive carefully and follow safety rules.")

else:
    print("Risk Level: Low Risk")
    print("Recommendation: Keep up safe driving habits.")