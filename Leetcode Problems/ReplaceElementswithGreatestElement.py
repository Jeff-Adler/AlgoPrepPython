class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        transformed_arr = []

        while len(arr) - 1:
            item = arr.pop(0)

            transformed_arr.append(max(arr))

        transformed_arr.append(-1)

        return transformed_arr
