from typing import List, Dict


class Solution:
    def to_dict(self, nums: List[int]) -> Dict[int, int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        return count_dict

    def get_intersect_dict(self, dict1: Dict[int, int], dict2: Dict[int, int]) -> Dict[int, int]:
        intersect_dict = {}
        for key, value in dict1.items():
            if dict2.get(key):
                min_value = min(dict2[key], value)
                intersect_dict[key] = min_value
        return intersect_dict

    def output_dict(self, output: Dict[int, int]) -> List[int]:
        result = []
        for key, value in output.items():
            result.extend([key] * value)
        return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = self.to_dict(nums1)
        nums2_dict = self.to_dict(nums2)
        intersect_dict = self.get_intersect_dict(nums1_dict, nums2_dict)
        return self.output_dict(intersect_dict)


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([1, 2, 2, 1], [2, 2]))
    print(solution.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
