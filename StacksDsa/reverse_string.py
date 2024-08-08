def reverse_string(string):
    stack = list(string)
    reversed = []
    while stack:
        element = stack.pop()
        reversed.append(element)
    print("".join(reversed))


reverse_string("abcd")
