
# Time O(log n)
# Space O(1)

A = [-8,-5,-2, 0, 3, 4, 6, 12, 15]

def binary_search(arr, target):
    N = len(arr)
    L = 0
    R = N-1

    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1
    return False

print(binary_search(A, 15))

# Binary Search condition based
B = [False, False, False, False, False, False, True]

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = (L + R) // 2
        
        if B[M]:
            R = M
        else:
            L = M + 1
    
    return L

print(binary_search_condition(B))

    
