__author__ = 'linglin'


def letterCombinations( digits):
    def dfs(num, string, res):
        if num == length:
            res.append(string)
            return
        for letter in dict[digits[num]]:
            dfs(num+1, string+letter, res)

    dict = {'2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
    }
    res = []
    length = len(digits)
    dfs(0, '', res)
    return res

if __name__ == '__main__':
    print letterCombinations("234")