from colour import Color

def calculate(primary):
    gradientColors = []
    for i, color in enumerate(primary):
        next = primary[0] if (i + 1 > len(primary) - 1) else primary[i + 1]
        g = genGrade(color, next, 20)
        s = list(map(lambda x: Color(x).hex, g))
        # print s[:-1]
        gradientColors.extend(s[:-1])

    return gradientColors


def genGrade(color1, color2, steps):
    c1 = Color(color1)
    grade = list(c1.range_to(Color(color2), steps))
    return grade


if __name__ == '__main__':
    calculate(sys.argv[1:])
