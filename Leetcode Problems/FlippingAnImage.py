class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        inversion_table = {0: 1, 1: 0}

        def invertRow(row):
            return [inversion_table[cell] for cell in row[::-1]]

        inverted_A = [invertRow(row) for row in A]

        # inverted_A = map(invertRow, A)

        return inverted_A
