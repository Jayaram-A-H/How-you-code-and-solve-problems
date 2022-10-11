inp=[5, 1, 4, 2]
def out(arr):
  out=[]
  for i in arr:
    t=1
    for j in arr:
      if (i==j):
        continue
      t=t*j
    out.append(t)
  print(out)
out(inp)
