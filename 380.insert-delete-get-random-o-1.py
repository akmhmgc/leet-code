#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#


# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.value_map = {}
        self.value_list = []

    def insert(self, val: int) -> bool:
        if val in self.value_map:
            return False
        else:
            self.value_list.append(val)
            self.value_map[val] = len(self.value_list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.value_map:
            return False
        else:
            list_last_value = self.value_list[-1]

            removed_value = val
            removed_value_index = self.value_map[removed_value]

            self.value_list[-1] = removed_value
            self.value_list[removed_value_index] = list_last_value
            self.value_list.pop()

            self.value_map[list_last_value] = removed_value_index
            self.value_map.pop(removed_value)

            return True

    def getRandom(self) -> int:
        return random.choice(self.value_list)
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
