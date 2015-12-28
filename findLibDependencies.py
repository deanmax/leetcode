res = []
circularCheck = {}

def findLibDep(dep_map, lib):
  if lib not in dep_map:
    return
  if not dep_map[lib]:
    return

  circularCheck[lib] = 1
  for sublib in dep_map[lib]:
    if sublib in circularCheck:
      raise Exception("Circular Reference Found!")
    if sublib in res:
      continue
    res.append(sublib)
    findLibDep(dep_map, sublib)
  del(circularCheck[lib])

  return res

if __name__ == "__main__":
  dep_map = {
      'foo': ['bar', 'zaa', 'paa'],
      'bar': ['kaa', 'zaa'],
      'zaa': ['kuu'],
      #'kuu': ['bar']  # uncomment for circular reference
  }

  #assert findLibDep(dep_map, 'foo') == ['bar', 'kaa', 'zaa', 'kuu', 'paa']
  print findLibDep(dep_map, 'foo')
