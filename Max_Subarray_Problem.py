import random
import time

def random_array(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]


def max_subarray_brute(numbers):
    best_sum = best_start = best_end = current_start = 0

    for i in range(len(numbers)):
        current_sum = 0
        for j in range(i, len(numbers)):
            if current_sum <= 0:
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
    best_sum = 0
    left_sum = -1

    for i in range(middle, left - 1, -1):
        best_sum = best_sum + numbers[i]

        if best_sum > left_sum:
            left_sum = best_sum

    best_sum = 0
    right_sum = -1
    for i in range(middle + 1, right + 1):
        best_sum = best_sum + numbers[i]

        if best_sum > right_sum:
            right_sum = best_sum
    return max(left_sum + right_sum, left_sum, right_sum)


def max_subarray_divide(numbers, left, right):
    if left == right:
        return numbers[1]

    middle = (left + right) // 2

    return max(max_subarray_divide(numbers, left, middle),
               max_subarray_divide(numbers, middle + 1, right),
               max_subarray_conquer(numbers, left, middle, right))


numbers = random_array(100, -10, 10)


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

# print("Original array = %s" % numbers)
# print("Contiguous array with best sum = %s" % numbers[start:end])
print("Start and end indices are ", start, "and", end)

max_sum = max_subarray_divide(numbers, 0, len(numbers)-1)
