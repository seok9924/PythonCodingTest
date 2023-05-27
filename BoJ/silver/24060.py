import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    save_count = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

        save_count += 1
        if save_count == k:
            return merged[-1]

    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1
        save_count += 1
        if save_count == k:
            return merged[-1]

    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1
        save_count += 1
        if save_count == k:
            return merged[-1]

    return -1


arr = [4, 5, 1, 3, 2]
k = 7
result = merge_sort(arr)
if k <= len(result):
    print(result[k - 1])
else:
    print(-1)
