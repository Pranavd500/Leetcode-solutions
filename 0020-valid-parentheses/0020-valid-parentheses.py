class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:

            # Closing bracket
            if ch in closeToOpen:

                # Check top of stack
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False

            else:
                # Opening bracket
                stack.append(ch)

        return len(stack) == 0