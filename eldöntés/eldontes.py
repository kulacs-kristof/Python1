import random
import math


def prime(x: int) -> bool:
    if x > 2 and x % 2 == 0 or x <= 1:
        return False
    num_gyok: int = int(math.sqrt(x)) + 1
    for oszto in range(3, num_gyok, 2):
        if x % oszto == 0:
            return False
    return True


def main() -> None:
    nums: list[int] = []
    while len(nums) < 2:
        rnum: int = random.randint(10, 99)
        if rnum % 2 == 1:
            nums.append(rnum)
    van_prím = False
    for num in nums:
        if prime(num):
            van_prím = True
            break
    print(f'A listában {"van" if van_prím else "nincs"} prímszám')


if __name__ == "__main__":
    main()

