print("AI Career Predictor started🚀")
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = pd.read_csv("career_data.csv")
print(data)
X = data.drop("Recommended_Career", axis=1)
y = data["Recommended_Career"]
model = DecisionTreeClassifier()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)



print("Model Trained Successfully ✅")
 
print("\nEnter your skills (1 = Yes, 0 = No)")
python_skill = int(input("Do you know Python? (1/0): "))
ml_skill = int(input("Do you know Machine Learning? (1/0): "))
web_skill = int(input("Do you know Web Development? (1/0): "))
comm_skill = int(input("Do you have good Communication skills? (1/0): "))
math_skill = int(input("Are you good at Math? (1/0): "))
new_student = pd.DataFrame([[python_skill, ml_skill, web_skill, comm_skill, math_skill]], 
                           columns=X.columns)
prediction = model.predict(new_student)
predicted_career = prediction[0]
print("Predicted Career:", prediction[0])
print("\nSkill Gap Analysis:")

if predicted_career == "Data_Scientist":
    if python_skill == 0:
        print("- Improve Python")
    if ml_skill == 0:
        print("- Learn Machine Learning")
    if math_skill == 0:
        print("- Improve Mathematics")

elif predicted_career == "Web_Developer":
    if web_skill == 0:
        print("- Improve Web Development")
    if python_skill == 0:
        print("- Learn Python")

elif predicted_career == "Frontend_Developer":
    if web_skill == 0:
        print("- Improve Frontend Skills (HTML, CSS, JS)")
