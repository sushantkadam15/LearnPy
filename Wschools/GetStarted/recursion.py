
def reco(k):
    if(k > 0):
        result = k + reco(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
reco(6)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(9)
