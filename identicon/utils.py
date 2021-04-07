def hsl_to_rgb(h, s, l):
    h /= 360
    s /= 100
    l /= 100

    if l <= 1 / 2:
        b = l * (s + 1)
    else:
        b = (l + s) - (l * s)

    a = (l * 2) - b

    r = int(round(hue_to_value(a, b, h + (1 / 3)) * 255, 0))
    g = int(round(hue_to_value(a, b, h) * 255, 0))
    b = int(round(hue_to_value(a, b, h - (1 / 3)) * 255, 0))

    return (r, g, b)


def hue_to_value(a, b, h):
    if h < 0:
        h += 1
    elif h > 1:
        h -= 1

    if h < 1 / 6:
        return a + ((b - a) * 6 * h)
    elif h < 1 / 2:
        return b
    elif h < 2 / 3:
        return a + ((b - a) * ((2 / 3) - h) * 6)
    else:
        return a


def map(value, start1, stop1, start2, stop2):
    # https://processing.org/reference/map_.html
    return (value - start1) * (stop2 - start2) / (stop1 - start1) + start2
