""" 
	@Guillermo Alvarez
	task link: https://codility.com/programmers/task/tape_equilibrium/
	test results: https://codility.com/demo/results/trainingQT48E4-KKH/#task-0
"""



def sum_array_iterating(array, index):
    result = 0
    for i in xrange(index, len(array)):
        result += array[i]
    return result

def solution(A):
    P = 1
    res = None
    left_result = A[P-1]
    right_result = sum_array_iterating(A, P)
    while P <= len(A) - 1:
        if res is None and P == 1:
            res = abs(left_result - right_result)
        else:
            left_result = left_result + A[P-1]
            right_result = right_result - A[P-1]
            tmp = abs(left_result - right_result)
            if tmp < res:
                res = tmp
        P += 1
    return res
