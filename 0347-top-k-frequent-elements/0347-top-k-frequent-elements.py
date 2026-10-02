class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1

        # answer = []

        # for i in range(k):
        #     max_count = 0
        #     max_num = 0

        #     for num in counts:
        #         if counts[num] > max_count:
        #             max_count = counts[num]
        #             max_num = num

        #     answer.append(max_num)
        #     counts[max_num] = 0

        # return answer

        a = sorted(counts, key = counts.get,reverse = True)
        return a[:k]