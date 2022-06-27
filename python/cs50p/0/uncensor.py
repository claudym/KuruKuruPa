def uncensor(infected, discovered):
  recovered= []
  indexDisc=0
  for ch in infected:
    if ch == '*':
      recovered.append(discovered[indexDisc])
      indexDisc+= 1
    else:
      recovered.append(ch)
  return ''.join(recovered)

print(uncensor('*h*s *s v*ry *tr*ng*', 'Tiiesae'))