from collections import defaultdict
city_list = [('TX', 'Austin'), ('TX', 'Houston'), ('NY', 'Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'),
             ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA', 'Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)

for state, city in city_list:
    cities_by_state[state].append(city)

for states, cities in cities_by_state.items():
    print(states, ', '.join(cities))

print("\n Default dict list: ", cities_by_state.items())

nums = defaultdict(int)

strs = "abcdef"

for key in strs:
    nums[key] += 1

print("\n Default dict nums: ", nums.items())