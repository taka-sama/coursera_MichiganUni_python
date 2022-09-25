score = input("Enter Score: ")
xs = float(score)
try:
  xs > 0.0 and xs < 1.0
except:
  print("Error, the number is out of range.")
  quit()
if score >= 0.9:
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
else:
  print("F")