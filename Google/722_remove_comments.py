# 722. https://leetcode.com/problems/remove-comments/

class Solution(object):
    """
    不必考虑/*块注释嵌套的问题，因为在C/C++的注释语法中，
    /*
    /*
    */
    */
    只会认为
    /*
    /*
    */
    是块注释，因此，在第一个/*开始后，只要遇到第一个*/，块注释即结束。
    """
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_block = False
        result = []
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            while i < len(line):
                """
                line[i:i+2]不必担心越界问题，因为对于s='/*/', s[0:10]也是可以正常执行的，而s[3]就会有越界问题
                """
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i = i+2 # 如果是i = i+1, 会有题目中说的重叠情形，例如'/*/'
                    continue
                if line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i = i+2 # 如果是i = i+1, 会将*/中的/也认为是源码
                    continue
                if line[i:i+2] == '//' and not in_block:
                    break
                if not in_block:
                    new_line.append(line[i])
                i = i+1
            """
            下面的if条件判断中，需要加上not in_block，这是为了应对以下情况：
            输入: source = ["a/*comment", "line", "more_comment*/b"]
            输出: ["ab"]
            而且与前面的
            if not in_block:
                new_line = []
            刚好呼应。
            """
            if len(new_line)>0 and not in_block:
                result.append("".join(new_line))
        return result