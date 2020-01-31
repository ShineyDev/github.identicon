"""
/identicon/__init__.py

    Copyright (c) 2020 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import hashlib
import math


has_pillow = False

try:
    from PIL import Image, ImageDraw
    has_pillow = True
except (ImportError) as e:
    pass


class Identicon():
    def __init__(self, hash: int):
        self.hash = hash

        # int.to_bytes(4, "big")
        # yes, i now know there is a builtin for this exact thing,
        # yes, i wasted far too much time building this impl for myself,
        # and yes, i am going to keep my impl here out of spite.
        len_bytes = math.ceil(hash.bit_length() / 8)
        self._bytes = [(hash >> (((len_bytes - 1) * 8) - (8 * i))) & 0xFF for (i) in range(0, len_bytes)]

    @classmethod
    def from_identifier(cls, identifier: str):
        return cls(int(hashlib.md5(identifier.encode("utf-8")).hexdigest(), 16))

    def get_background(self) -> tuple:
        return (240, 240, 240)

    def get_foreground(self) -> tuple:
        h = ((self._bytes[12] & 0x0F) << 8) | self._bytes[13]
        s = self._bytes[14]
        l = self._bytes[15]

        def map(value, start1, stop1, start2, stop2):
            # https://processing.org/reference/map_.html
            return (value - start1) * (stop2 - start2) / (stop1 - start1) + start2

        h = map(h, 0, 4095, 0, 360)
        s = 65 - map(s, 0, 255, 0, 20)
        l = 75 - map(l, 0, 255, 0, 20)

        def hsl_to_rgb(h, s, l):
            h /= 360
            s /= 100
            l /= 100

            if l <= 0.5:
                b = l * (s + 1)
            else:
                b = l + s - l * s

            a = l * 2 - b

            def hue_to_rgb(a, b, h):
                if h < 0:
                    h += 1
                elif h > 1:
                    h -= 1

                if h < 1 / 6:
                    return a + (b - a) * 6 * h
                elif h < 1 / 2:
                    return b
                elif h < 2 / 3:
                    return a + (b - a) * (2 / 3 - h) * 6
                else:
                    return a

            r = int(round(hue_to_rgb(a, b, h + 1 / 3) * 255, 0))
            g = int(round(hue_to_rgb(a, b, h) * 255, 0))
            b = int(round(hue_to_rgb(a, b, h - 1 / 3) * 255, 0))

            return (r, g, b)

        return hsl_to_rgb(h, s, l)

    def generate_array(self) -> list:
        def generate_bits():
            for (i) in range(0, 16):
                hi = self._bytes[i] & 0xF0
                lo = self._bytes[i] & 0x0F

                yield hi >> 4
                yield lo

        array = [False] * 25
        bits = map(lambda b: b % 2 == 0, generate_bits())

        for (column) in range(2, -1, -1):
            for (row) in range(0, 5):
                bit = next(bits)

                array[column + (row * 5)] = bit
                array[(4 - column) + (row * 5)] = bit

        return array

    def generate_matrix(self) -> list:
        array = self.generate_array()
        return [array[i:i + 5] for (i) in range(0, 25, 5)]

    def generate_image(self):
        if not has_pillow:
            raise Exception("requires [pillow](https://pypi.org/project/pillow/)")

        background = self.get_background()
        foreground = self.get_foreground()

        matrix = self.generate_matrix()

        image = Image.new("RGB", (420, 420), background)
        draw = ImageDraw.Draw(image)

        for (i, row) in enumerate(matrix):
            for (j, bit) in enumerate(row):
                x = 35 + j * 70
                y = 35 + i * 70

                if bit:
                    draw.rectangle((x, y, x + 70, y + 70), foreground)

        return image
