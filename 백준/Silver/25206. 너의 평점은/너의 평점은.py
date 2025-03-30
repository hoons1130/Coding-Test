table = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0 }
unit_sum = 0.0
grade_sum = 0.0
for _ in range(20):
    name, unit, grade = input().split()
    unit = float(unit)
    if grade != "P":
        unit_sum += unit
        grade_sum = grade_sum + (unit * table[grade])
ans = grade_sum / unit_sum
print(ans)
