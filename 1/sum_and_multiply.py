
def sum_2(nums):
    nums_so_far = {}

    target = 2020
    for i, num in enumerate(nums):
        need = target - num
        if need in nums_so_far:
            print(f"{need} + {num} = 2020, need * num = {need * num}")

        nums_so_far[num] = i

def sum_3(nums):
    nums = sorted(nums)

    target = 2020
    for i, num in enumerate(nums):
        need = target - num

        result = two_pointer(need, nums[i:])
        if result:
            num1, num2 = result
            print(f"{num} + {num1} + {num2} = {num + num1 + num2}, num * num1 * num2 = {num * num1 * num2}")


def two_pointer(need, nums):
    head = 0
    tail = len(nums)-1
    while head != tail:
        num_sum = nums[head] + nums[tail]
        if num_sum == need:
            return nums[head], nums[tail]
        elif num_sum < need:
            head += 1
        elif num_sum > need:
            tail -= 1

    return False


if __name__ == "__main__":
    with open('input.txt', 'r')  as f:
        lines = f.readlines()
        nums = [int(l.strip()) for l in lines]

    print("Sum 2")
    sum_2(nums)

    print("\nSum 3")
    sum_3(nums)
