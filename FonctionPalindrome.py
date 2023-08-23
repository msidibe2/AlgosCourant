def palindrome(v):
  reverse = v[::-1]   # renvoie une l'inverse du mot
  if v == reverse:
    print(v + " est un palindrome")
  else:
    return False
  
palindrome("radar")

# autrement fait
def palindrome2(v):
  if v == v[::1]:
    return True
  else:
    return False

def check_palindrome(v):
  if len(v) < 1:
    return True
  else:
    if v[0] == v[-1]
      return check_palindrome(v[1:-1])
    else:
      return False
