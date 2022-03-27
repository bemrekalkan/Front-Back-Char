def front_back(word):
  if len(word)==1:
    return word
  else:
    new_string=word[-1]+word[1:-1]+word[0]
    return new_string

print(front_back('clarusway'))
print(front_back('a'))
print(front_back('ab'))
