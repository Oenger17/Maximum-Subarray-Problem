import random
import time


def random_array(count, lower_bound, upper_bound):
    """ generate a random array of n size with lower and upper bound for element values """
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]


def max_subarray_brute(numbers):
    best_sum = best_start = best_end = current_start = 0

    for i in range(len(numbers)):
        """ set current sum to zero as we are checking next possible sequence """
        current_sum = 0
        for j in range(i, len(numbers)):
            if current_sum <= 0:
                """ set start indices to iteration count """
                current_start = j
            current_sum += numbers[j]
            if current_sum > best_sum:
                best_start = current_start
                best_end = j + 1
            best_sum = max(current_sum, best_sum)
    return best_sum, best_start, best_end


def max_subarray_kadane(numbers):
    best_sum = best_start = best_end = current_sum = 0

    for i, value in enumerate(numbers):
        if current_sum <= 0:
            """ set current sum to zero and start indices to i as we are checking next possible sequence """
            current_start = i
            current_sum = value
        else:
            current_sum += value
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = i + 1

    return best_sum, best_start, best_end


def max_subarray_conquer(numbers, left, middle, right):
    """include elements on the left"""
    best_sum = left_sum = 0

    for i in range(middle, left - 1, -1):
        best_sum = best_sum + numbers[i]

        """ calculate the best sum left of pivot """
        if best_sum > left_sum:
            left_sum = best_sum

    """include elements on the right"""
    best_sum = right_sum = 0
    for i in range(middle + 1, right + 1):
        best_sum = best_sum + numbers[i]

        """ calculate the best sum right of pivot """
        if best_sum > right_sum:
            right_sum = best_sum
    return max(left_sum + right_sum, left_sum, right_sum)


def max_subarray_divide(numbers, left, right):
    """ Base case checking for just one element"""
    if left == right:
        return numbers[1]

    """ find pivot point """
    middle = (left + right) // 2

    """return maximum of sum in left half, sum in right half, or sum that crosses pivot"""
    return max(max_subarray_divide(numbers, left, middle),
               max_subarray_divide(numbers, middle + 1, right),
               max_subarray_conquer(numbers, left, middle, right))


"""driver and print code"""

numbers = random_array(1000, -10, 10)
print("Array size is: %s" %len(numbers))
print("******************************")
start_time = time.time()
maximum, start, end = max_subarray_brute(numbers)
end_time = time.time()
print("Brute force method completion time was: ", end_time-start_time)
start_time = time.time()
maximum2 = max_subarray_divide(numbers, 0, len(numbers)-1)
end_time = time.time()
print("Divide and Conquer method completion time was: ", end_time-start_time)
start_time = time.time()
maximum3, start3, end3 = max_subarray_kadane(numbers)
end_time = time.time()
print("Kadane method completion time was: ", end_time-start_time)
print("******************************")
print("Start and end indices for Brute-Force are ", start, "and", end)
print("Start and end indices for Kanade are ", start3, "and", end3)
print("******************************")
print("Maximum for Brute is ", maximum)
print("Maximum for Divide and Conquer is ", maximum2)
print("Maximum for Kanade is ", maximum3)
print("******************************")
# print("Original array = %s" % numbers)
# print("Contiguous array with best sum = %s" % numbers[start:end])
