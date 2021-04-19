import re
import setuptools


extras_require = {
    "docs": [
        "sphinx",
        "sphinxcontrib_trio",
        "sphinx-rtd-theme",
    ],
}

packages = [
    "github.identicon",
]

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("github/identicon/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass


setuptools.setup(
    author="ShineyDev",
    description="A port of GitHub's identicon algorithm to Python.",
    extras_require=extras_require,
    license="Apache Software License",
    name="github.identicon",
    packages=packages,
    python_requires=">=3.6.0",
    url="https://github.com/ShineyDev/github.identicon",
    version=version,
)
