def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >=3.0:
    return "B"
  elif gpa >=2.0:
    return "C"
  if gpa >= 1.0:
    return "D"
  else:
    return "F"
    
    
    
grade = grade_converter(4)
print(grade)