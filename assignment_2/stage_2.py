import gc
import os
import string
import time
import numpy as np
import psutil


def myInv(size):
    intA = np.random.randint(-500, 50000, (size, size))
    flA = np.random.rand(size, size)
    A = intA + flA
    b = np.random.randint(-10, 100, size)
    return (np.linalg.inv(A))


def matrix_multiplication(size):
    """
    Multiplies two random matrices of specified size.

    Parameters:
    size (tuple): A tuple (m, n) representing the dimensions of the matrices.
                 The first matrix will be m x n and the second will be n x m.

    Returns:
    ndarray: The result of the matrix multiplication.
    """
    matrix_a = np.random.rand(size, size)
    matrix_b = np.random.rand(size, size)
    result = matrix_a @ matrix_b
    return result


def custom_sort(size):
    """
    Generates a random list of integers and sorts it in ascending order using an inefficient method.
    This method finds the smallest element and places it at the beginning, then repeats for each subsequent position.

    Parameters:
    size (int): The number of elements in the list to be sorted.

    Returns:
    list: The sorted list of integers.
    """
    nums = np.random.randint(low=0, high=size, size=size).tolist()
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def custom_find(size):
    """
    Finds the index of the first occurrence of search_text in full_text using a loop-based approach.
    Returns -1 if search_text is not a substring of full_text.

    Parameters:
    size (int): The number of chars in the full_text.

    Returns:
    int: The index of the first occurrence of the needle or -1 if not found.
    """
    full_text = ''.join(np.random.choice(list(string.ascii_lowercase)) for _ in range(size))
    search_text = "a"
    for i in range(len(full_text) - len(search_text) + 1):
        if full_text[i:i + len(search_text)] == search_text:
            return i
    return -1


def python_find(size):
    """
    Python implementation of the first occurrence of search_text in full_text.

    Parameters:
    size (int): The number of chars in the full_text.

    Returns:
    int: The index of the first occurrence of the needle or -1 if not found.
    """
    full_text = ''.join(np.random.choice(list(string.ascii_lowercase)) for _ in range(size))
    search_text = "a"
    return full_text.find(search_text)


def test_time_and_memory_complexity(function, tests_number, scale):
    """
    Tests and prints the time and memory complexity of a given function.

    This function executes the provided function several times with increasing input sizes
    and measures the time and memory used for each execution.

    Every function may have different complexity, and in order to achieve a relevant results we
    can customize the scale factor to make them last shorter or longer.

    Parameters:
    function (Callable): The function to test. It should accept an integer size as its parameter.
    tests_number (int): The number of tests to run. The input size for the function will increase
                        with each test.
    scale (int): The multiplier of the size for the function test.

    Returns:
    None: This function prints the results but does not return anything.
    """
    process = psutil.Process(os.getpid())
    base_ram = process.memory_info().rss

    time_results = np.zeros(tests_number)
    memory_results = np.zeros(tests_number)
    sizes = []
    for i in range(1, 1 + tests_number):
        gc.collect()
        start = time.time()
        size = i * scale
        sizes.append(size)
        function(size=size)
        end = time.time()
        current_ram = process.memory_info().rss
        time_results[i - 1] = end - start
        memory_results[i - 1] = current_ram - base_ram
    return time_results, memory_results, sizes
