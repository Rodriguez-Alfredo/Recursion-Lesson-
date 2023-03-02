def countingdown(x):
  #stop the infinit loop
  if x > 0:
    print(x)
    countingdown(x - 1)
  else:  
    print(x)

x = 5
countingdown(x)