def multiply_iteration(N, M):
    result = 0
    for _ in range(M):
        result += N
    return result

def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

N = int(input("Enter N: "))
M = int(input("Enter M: "))

result_iteration = multiply_iteration(N, M)
print(f"Result using iteration method: {result_iteration}")

result_n_iterations = multiply_n_iterations(N, M)
print(f"Result using N iterations method: {result_n_iterations}")
