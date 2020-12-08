class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sdns = []

        def is_self_dividing(num):
            digits = [int(dig) for dig in str(num)]
            if 0 in digits:
                return False
            for digit in digits:
                if num % digit != 0:
                    return False
            return True

        for i in range(left, right+1):
            if is_self_dividing(i):
                sdns.append(i)
            else:
                continue

        return sdns
