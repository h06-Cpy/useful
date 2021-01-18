  
#모든 부분집합을 원소를 갖는 집합을 powerset이라고 한다.
def get_powerset(A):
    A_size = len(A)
    A_pow = []
    for i in range(2**A_size):
        flag = bin(i)[2:].zfill(A_size)
        subset = [A[j] for j in range(A_size) if flag[j] == '1']
        A_pow.append(subset)
    return A_pow
