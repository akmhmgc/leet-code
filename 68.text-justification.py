#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_list = []
        index = -1
        count = 0
        for word in words:
            if count < len(word) + 1:
                word_list.append([word])
                index += 1
                count = maxWidth - len(word)
            else:
                word_list[index].append(word)
                count -= len(word) + 1
        
        ans = []
        for i in range(0, len(word_list) - 1):
            word_count = len(word_list[i])
            word_lengh = 0
            for w in word_list[i]:
                word_lengh += len(w)
            
            if word_count == 1:
                ans.append(word_list[i][0] + " " * (maxWidth - word_lengh))
                continue
            
            rest_space = maxWidth - word_lengh
            space_count, mod = divmod(rest_space, word_count - 1)
            for j in range(mod):
                word_list[i][j] += ' '
            ans.append((' ' * space_count).join(word_list[i]))
        # 最後
        last = ' '.join(word_list[-1])
        last += ' ' * (maxWidth - len(last))
        ans.append(last)
        return ans

# @lc code=end

