class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if (len(i) >= 2) & (i[0] == '-'):
                stack.append(int(i))
            elif i.isnumeric():
                stack.append(int(i))
            elif i == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2+n1)
            elif i == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif i == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            elif i == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2*n1)

        return int(stack[0])