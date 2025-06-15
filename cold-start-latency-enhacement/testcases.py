"""
testcases.py: Defines a set of heavy, realistic CPU-bound, memory-bound, and IO-bound test cases.
"""
def generate_test_cases(num_cases=200, num_functions=5):
    """
    Generate a list of test case descriptions with mixed CPU, memory, and IO workloads.
    Each test case is a dict with keys: id, func, type, param.
    """
    test_cases = []
    # Example parameters to create heavy workloads
    cpu_param = 10_000_000  # number of iterations for CPU-bound tasks
    mem_param = 2_000_000   # number of elements for memory-bound tasks
    io_param_mb = 5         # size in MB for IO-bound tasks

    for i in range(1, num_cases + 1):
        # Round-robin assignment of function IDs to simulate multiple functions
        func_id = (i - 1) % num_functions + 1
        func_name = f"func_{func_id}"
        # Distribute tasks types: CPU, memory, IO in a pattern
        if i % 3 == 1:
            test_case = {"id": i, "func": func_name, "type": "cpu",    "param": cpu_param}
        elif i % 3 == 2:
            test_case = {"id": i, "func": func_name, "type": "memory", "param": mem_param}
        else:
            test_case = {"id": i, "func": func_name, "type": "io",     "param": io_param_mb}
        test_cases.append(test_case)
    return test_cases

# Generate and store test cases
TEST_CASES = generate_test_cases()

