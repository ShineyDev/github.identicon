.. github-identicon readme


github-identicon
================

A port of GitHub's identicon algorithm to Python.

.. code-block:: python3

	import identicon
	cls = identicon.Identicon.from_identifier(480938)
	image = cls.generate_image() # requires PIL
	image.show()
