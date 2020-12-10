.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/github-identicon/actions?query=workflow%3AAnalyze+event%3Apush">
            <img alt="Analyze Status"
                 src="https://github.com/ShineyDev/github-identicon/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github-identicon/actions?query=workflow%3ABuild+event%3Apush">
            <img alt="Build Status"
                 src="https://github.com/ShineyDev/github-identicon/workflows/Build/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github-identicon/actions?query=workflow%3ACheck+event%3Apush">
            <img alt="Check Status"
                 src="https://github.com/ShineyDev/github-identicon/workflows/Check/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github-identicon/actions?query=workflow%3ALint+event%3Apush">
            <img alt="Lint Status"
                 src="https://github.com/ShineyDev/github-identicon/workflows/Lint/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">github-identicon</h1>
    <p align="center">A port of GitHub's identicon algorithm to Python.</p>


Installation
------------

**Python 3.6 or higher is required.**

.. code-block:: sh

    python3 -m pip install --upgrade git+https://github.com/ShineyDev/github-identicon.git

Usage
-----

.. code-block:: python3

	import identicon
	cls = identicon.Identicon.from_identifier(480938)
	image = cls.generate_image()  # requires PIL
	image.show()
