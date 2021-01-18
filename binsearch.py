#이진탐색 횟수를 반환하는 함수
#r은 오른쪽, l은 왼쪽
def expnum(r,target):
  l=1
  cnt=1
  centr=(l+r)//2
  while True:
    if centr==target:
      break
    elif centr<target:
      l=centr
      centr=(l+r)//2
      cnt+=1
    else:
      r=centr
      centr=(l+r)//2
      cnt+=1
  return cnt
