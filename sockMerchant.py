def sockMerchant(n, ar):
  fr_map = dict()

  for i in range(n):
    if ar[i] in fr_map.keys():
      fr_map[ar[i]] += 1
    else: fr_map[ar[i]] = 1
  
  pair_cnt = 0
  
  for e in fr_map:
    pair_cnt += fr_map[e] // 2
  
  return pair_cnt

def numPairs(ar):
  print("No. of pairs in", ar, "=", sockMerchant(len(ar), ar))

numPairs([1,2,1,2,1,3,2])
numPairs([10,20,20,10,10,30,50,10,20])
