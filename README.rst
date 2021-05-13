.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/github.identicon/actions?query=workflow%3AAnalyze+event%3Apush">
            <img alt="Analyze Status" src="https://github.com/ShineyDev/github.identicon/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github.identicon/actions?query=workflow%3ABuild+event%3Apush">
            <img alt="Build Status" src="https://github.com/ShineyDev/github.identicon/workflows/Build/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github.identicon/actions?query=workflow%3ACheck+event%3Apush">
            <img alt="Check Status" src="https://github.com/ShineyDev/github.identicon/workflows/Check/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github.identicon/actions?query=workflow%3ADeploy+event%3Apush">
            <img alt="Deploy Status" src="https://github.com/ShineyDev/github.identicon/workflows/Deploy/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github.identicon/actions?query=workflow%3ALint+event%3Apush">
            <img alt="Lint Status" src="https://github.com/ShineyDev/github.identicon/workflows/Lint/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/github.identicon</h1>
    <p align="center">A port of GitHub's identicon algorithm to Python.</p>
    <h6 align="center">Copyright 2020-present ShineyDev</h6>
    <h6 align="center">This repository is not sponsored by or affiliated with GitHub Inc. or its affiliates. "GitHub" is a registered trademark of GitHub Inc.</h6>


Installation
------------

.. code-block:: sh

    python3 -m pip install --upgrade git+https://github.com/ShineyDev/github.identicon.git


Usage
-----

.. code-block:: python3

    from github.identicon import Identicon
    identicon = Identicon.from_identifier(480938)
    image = identicon.generate_image()  # requires PIL
    image.show()
