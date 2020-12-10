"""
/identicon/identicon.py

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

from identicon import utils


try:
    from PIL import Image, ImageDraw
    has_pillow = True
except (ImportError) as e:
    has_pillow = False


class Identicon():
    """
    Represents a GitHub identicon.
    """

    def __init__(self, hash):
        self.hash = hash
        self._bytes = list(hash.to_bytes(16, "big"))

    @classmethod
    def from_identifier(cls, identifier):
        """
        Creates an identicon from a GitHub User ID.

        Parameters
        ----------
        identifier: :class:`int`
            A GitHub User ID.

        Returns
        -------
        :class:`~identicon.Identicon`
            An identicon.
        """

        return cls(int(hashlib.md5(str(identifier).encode("utf-8")).hexdigest(), 16))

    def get_background(self):
        """
        Gets the background color used for all identicon.

        This is, and always will be, RGB (240, 240, 240).

        Returns
        -------
        Tuple[:class:`int`, :class:`int`, :class:`int`]
            The background used for all identicon.
        """

        return (240, 240, 240)

    def get_foreground(self):
        """
        Calculates the foreground color to use for this identicon.

        Returns
        -------
        Tuple[:class:`int`, :class:`int`, :class:`int`]
            The background to use for this identicon.
        """

        h = ((self._bytes[12] & 0x0F) << 8) | self._bytes[13]
        s = self._bytes[14]
        l = self._bytes[15]

        h = utils.map(h, 0, 4095, 0, 360)
        s = 65 - utils.map(s, 0, 255, 0, 20)
        l = 75 - utils.map(l, 0, 255, 0, 20)

        return utils.hsl_to_rgb(h, s, l)

    def generate_bits(self):
        """
        Generates 32 bits for the identicon tiles, the latter 17 are
        "spare".

        The bits are later formatted as follows:

        .. code-block::

            11   6    1    6    11

            12   7    2    7    12

            13   8    3    8    13

            14   9    4    9    14

            15   10   5    10   15

        Returns
        -------
        Iterator[:class:`bool`]
            An iterator of bits.
        """

        def _generate():
            for (i) in range(0, 16):
                hi = self._bytes[i] & 0xF0
                lo = self._bytes[i] & 0x0F

                yield hi >> 4
                yield lo

        return map(lambda x: x % 2 == 0, _generate())

    def generate_list(self):
        """
        Generates 25 bits for the identicon tiles.

        The bits are later formatted as follows:

        .. code-block::

            1    2    3    4    5

            6    7    8    9    10

            11   12   13   14   15

            16   17   18   19   20

            21   22   23   24   25

        Returns
        -------
        List[:class:`bool`]
            A list of bits.
        """

        array = [False] * 25
        bits = self.generate_bits()

        for (column) in range(2, -1, -1):
            for (row) in range(0, 5):
                bit = next(bits)

                array[column + (row * 5)] = bit
                array[(4 - column) + (row * 5)] = bit

        return array

    def generate_matrix(self):
        """
        Transforms the return value from :meth:`.generate_list` into a
        5*5 matrix.

        Returns
        -------
        List[List[:class:`bool`]]
            A matrix of bits.
        """

        list_ = self.generate_list()
        return [list_[i:i + 5] for i in range(0, 25, 5)]

    def generate_image(self):
        """
        Generates a PNG image of the identicon.

        This requires `Pillow <https://pypi.org/project/pillow/>`_.
        """

        if not has_pillow:
            raise RuntimeError("requires [pillow](https://pypi.org/project/pillow/)")

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
