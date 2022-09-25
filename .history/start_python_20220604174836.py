hrs = input("Enter Hours:")
rt = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rt)
except:
    print("Error, please numeric ")
if h > 40:
    reg = h * r
    otp = (h - 40) *  (r * 0.5)
    xp = reg + otp
    print(xp)
else:
    print(h * r * 1.5)