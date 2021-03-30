import bmi

print("体重計算アプリ")
w = int(input("体重:"))
h = float(input("身長:"))
print(f"BMI:{bmi.get_bmi(w,h)}")
