#후위연산 계산기

T = int(input())

for test_case in range(1, T + 1):
    exp=list(input().split()) #여기에 후위연산으로 된 식을 입력
    stack=[]
    answer="error"
    for i in range(len(exp)):
        if exp[i]=="+" or exp[i]=="-" or exp[i]=="/" or exp[i]=="*":
            if len(stack)<2:
                break
            else:
                y=stack[len(stack)-1]
                stack.pop()
                x=stack[len(stack)-1]
                stack.pop()
                if exp[i]=="+":
                    stack.append(x+y)
                elif exp[i]=="-":
                    stack.append(x-y)
                elif exp[i]=="/":
                    stack.append(x/y)
                else:
                    stack.append(x*y)
        elif exp[i]==".":
            if len(stack)==1:
                answer=int(stack[0])
            else:
                break
 
        else:
            num=float(exp[i])
            stack.append(num)
    print(f"#{test_case} {answer}")
