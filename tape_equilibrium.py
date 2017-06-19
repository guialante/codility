""" 
	@Guillermo Alvarez
	task link: https://codility.com/programmers/task/tape_equilibrium/
	test results: https://codility.com/demo/results/trainingQT48E4-KKH/#task-0
"""

def solution(A):
    left_result = A[0]
    right_result = sum(A[1:])
    res = abs(left_result - right_result)
    for p in range(2, len(A)):
        left_result = left_result + A[p-1]
        right_result = right_result - A[p-1]
        tmp = abs(left_result - right_result)
        if tmp < res:
            res = tmp
    return res
