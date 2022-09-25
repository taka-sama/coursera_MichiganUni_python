def computepay(h, r):
  if h > 40:
    reg = h * r
    otp = (h - 40) * (r / 2)
    xp = reg + otp
    return xp
  else:
    xp = h * r
    return xp
  
hrs = input("Enter Hours:")
rt = input("Enter Rate:")
xh = float(hours)