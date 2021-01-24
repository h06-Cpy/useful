#DFS(깊이우선탐색)을 이용하여 출발노드 S가 도착노드 F로 갈 수 있는지 판단하는 코드
#노드는 숫자로 이루어져 있고 링크정보가 두 개의 숫자로 주어짐

T = int(input())

for test_case in range(1, T + 1):
  V,E=tuple(map(int, input().split()))
  visited=[False]*(V) #노드를 방문했는지를 체크하는 리스트. 방문하면 True
  info=[] #링크 정보
  stack=[]
  answer=0
  for i in range(E): #링크 정보 입력받기
    [x,y]=list(map(int,input().split()))
    info.append([x,y])
  S,F=tuple(map(int,input().split()))
  stack.append(S)
  visited[S-1]=True
  a=S #a와 b 두 변수로 노드를 방문함. a는 현재, b는 다음 노드
  while True:
    b=-1 #다음 노드를 못찾으면 b는 -1로 유지
    for i in range(E):
      if a==info[i][0] and visited[info[i][1]-1]==False:
        visited[info[i][1]-1]=True
        b=info[i][1]
        stack.append(b)
        a=b
        break
    if a==F:
      answer=1
      break
    if b==-1: 
      if len(stack)==1:
        break
      else:
        a=stack[len(stack)-1]
        stack.pop()
  print(f"#{test_case} {answer}")

