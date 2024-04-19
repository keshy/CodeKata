'''
https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        a = self.to_roman(num)
        return a

    def to_roman(self, num: int, answer: str = ''):
        sym_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        if sym_map.get(num):
            answer += ('%s' % sym_map[num])
            return answer
        else:
            # find the closest key.
            n = 0
            for k in sym_map.keys():
                if k < num:
                    n = k
            multiple = int(num / n)
            answer += ('%s' % sym_map[n]) * multiple
            p_n = num - (multiple * n)
            if p_n > 0:
                return self.to_roman(p_n, answer)
            else:
                return answer


if __name__ == '__main__':
    c = Solution()
    print(c.intToRoman(58))
    print(c.intToRoman(5081))
