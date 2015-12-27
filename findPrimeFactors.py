def findPrimeFactors(num):
  res = []
  for i in xrange(2, num+1):
    if num < i:
      break
    if num % i == 0:
      res.append(i)
    while num % i == 0:
      num /= i

  return res


if __name__ == "__main__":
  print findPrimeFactors(30)
