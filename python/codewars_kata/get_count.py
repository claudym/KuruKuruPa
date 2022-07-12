def get_count(sentence):
  count=0
  for ch in sentence:
    if ch in ['a', 'e', 'i', 'o', 'u']:
      count+= 1
  return count

print(get_count('super tranquilo'))