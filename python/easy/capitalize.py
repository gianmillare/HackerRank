def solve(s):
    new_string = s.split(" ")
    output = []
    for x in new_string:
        output.append(x.capitalize())
    print(" ".join(output))


s = "chris alan"
solve(s)