hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rate:")
r = float(rt)
if h > 40:
    reg = h * r
    otp = (h - 40) *  (r * 0.5)
    xp = reg + otp
    print(xp)
else:
    print(h * r * 1.5)