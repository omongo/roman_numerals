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
        value, i = (MAP[x][0], i + 1) if i % 5 == 4 else ('', i)
        i_fd_5 = i // 5
        value += MAP[x][i_fd_5] if i_fd_5 else ''
        i %= 5
        value += MAP[x][0] * i
        return value

