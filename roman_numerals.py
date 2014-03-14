class RomanNumerals:

    MAP = {
        1000: ['M', '', ''],
        100: ['C', 'D', 'M'],
        10: ['X', 'L', 'C'],
        1: ['I', 'V', 'X'],
    }

    def __init__(self, number=1):
        self.number = number

    def get_value(self):
        number = self.number
        value = ''
        for x in reversed(sorted(RomanNumerals.MAP)):
            number %= x * 10
            value += self._convert(number // x, x)
        return value

    def _convert(self, i, x):
        MAP = RomanNumerals.MAP
        value = ''
        if i % 5 == 4:
            value += MAP[x][0]
            i += 1
        i_fd_5 = i // 5
        if i_fd_5 == 1:
            value += MAP[x][1]
        elif i_fd_5 == 2:
            value += MAP[x][2]
        i %= 5
        value += MAP[x][0] * i
        return value

