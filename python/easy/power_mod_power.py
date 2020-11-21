# Power - Mod Power
# https://www.hackerrank.com/challenges/python-power-mod-power/problem

# Take the inputs as they are
a = input()
b = input()
m = input()

# Main
def mod_power(a, b, m):
    # reformat the values to a function readable format
    digits = [int(i) for i in [a, b, m]]
    results = pow(digits[0], digits[1], [digits[2]])

    return results

# Example
print(mod_power(a, b, m))