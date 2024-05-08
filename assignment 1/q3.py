passw = input("Enter Password: ")

if len(passw) >= 6 and len(passw) <= 16:
  UpNum = LowNum = sNum = num = 0
  for i in passw:
    if (i >= 'a' and i <= 'z'):
      LowNum += 1
    elif (i >= 'A' and i <= 'Z'):
      UpNum += 1
    elif i in ['$','#','@']:
      sNum += 1
    elif '0' <= i<= '9':
      num += 1

  if num >= 1 and LowNum >= 1 and sNum >= 1 and UpNum >= 1:
    print("Good Password")
  else:
    print("Password condition 1-3 not met!")
else:
  print("Password length should be between 6 and 16 characters.")