import random
# rand_list =
rand_list = [random.randint(1, 20) for _ in range(10)]
print(f"rand_list {rand_list}")

# list_comprehension_below_10 =
below_10 = [x for x in rand_list if x < 10]
print(f"below 10 {below_10}")

# list_comprehension_below_10 =
filter_10 = list(filter(lambda n: n < 10, rand_list))
print(filter_10)