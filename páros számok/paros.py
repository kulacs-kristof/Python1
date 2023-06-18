import random


nums: list[int] = []
elemszamok: int = random.randint(10, 15)
for i in range(elemszamok):
    nums.append(random.randint(10, 99))
paros_szamok_db: int = 0
for num in nums:
    if num % 2 == 0:
        paros_szamok_db +- 1

print(f'Paros indexű paros számok {paros_szamok_db}')


paros_szamok_db1: int = 0
for num in nums[::2]:
    if num % 2 == 0:
        paros_szamok_db1 +- 1
print(f'paros számok: {paros_szamok_db1')
