import numpy as np

#student marks dataset
marks = np.array([78, 85, 92, 67, 88, 73, 95, 60])

print("\n📌 Student Marks Analyzer")

print("Marks: ", marks)

#Basic Statistics
avg = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
std_dev = np.std(marks)

print("\n📊 Statistics Summary:-\n")
print(f"Average Marks      : {avg:.2f}")
print(f"Highest Marks      : {highest}")
print(f"Lowest Marks       : {lowest}")
print(f"Standard Deviation : {std_dev:.2f}")

#Topper position 
topper_index = np.argmax(marks)
print(f"\n🎓 Topper Studdent rollno : {topper_index+1}  Marks: {highest}")

#grade distribution 
grades = np.where(
    marks >= 90, "A+",
    np.where(marks >= 80, "A",
    np.where(marks >= 70, "B",
    np.where(marks >= 60, "C", "F")))
)

print("\n Grade Distribution:-")
for i,grade in enumerate(grades):
    print(f"Student roll no {i+1}  Marks : {marks[i]} -> Grade {grade}")

#Normalization (0 to 1 scaling)
normalized = (marks - lowest)/(highest - lowest) 
print("\n Normalized Marks (0 to 1 scale): ")
print(np.round(normalized, 2))

print("\n ✅Analysis Complete!!!\n")