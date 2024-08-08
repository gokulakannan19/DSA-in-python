class Expression:

    left_brackets = ["(", "[", "{", "<"]
    right_brackets = [")", "]", "}", ">"]

    def __init__(self, expr):
        self.expr = expr

    def validate_expression(self):
        stack = []
        for char in self.expr:
            if self.isLeftBrackets(char):
                stack.append(char)
            if self.isRightBrackets(char):
                if not stack:
                    return False
                top = stack.pop()
                if not self.isBracketsCheck(top, char):
                    return False
        return not bool(stack)

    def isLeftBrackets(self, char):
        return char in self.left_brackets

    def isRightBrackets(self, char):
        return char in self.right_brackets

    def isBracketsCheck(self, left, right):
        # print(self.left_brackets.index(left) ==
        #   self.right_brackets.index(right))
        return self.left_brackets.index(left) == self.right_brackets.index(right)


expression = Expression("(a+b)")
print(expression.validate_expression())
