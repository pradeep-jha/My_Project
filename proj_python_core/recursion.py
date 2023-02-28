def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print("k is",k)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


import re
string_value = "alphanumeric@123__"
s = re.sub(r'[^a-zA-Z0-9]', '', string_value)
print(s)

a="A man, a plan, a canal: Panama"
b=filter(lambda i:i not in [',',':',' ','"'],a)
print(b)