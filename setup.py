import re
import setuptools


with open("README.rst", "r") as file_stream:
    readme = file_stream.read()

with open("identicon/__init__.py", "r") as file_stream:
    version = re.search(
        r"^version = [\"]([^\"]*)[\"]", file_stream.read(), re.MULTILINE
    ).group(1)

if version.endswith(("a", "b", "rc")):
    try:
        import subprocess

        process = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE
        )

        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE
        )

        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Typing :: Typed",
]

project_urls = {
    "Issue Tracker": "https://github.com/ShineyDev/github-identicon/issues/",
    "Source": "https://github.com/ShineyDev/github-identicon/",
}

setuptools.setup(
    author="ShineyDev",
    classifiers=classifiers,
    description="A port of GitHub's identicon algorithm to Python.",
    license="Apache Software License",
    long_description=readme,
    long_description_content_type="text/x-rst",
    name="github-identicon",
    packages=["identicon"],
    project_urls=project_urls,
    python_requires=">=3.6.0",
    url="https://github.com/ShineyDev/github-identicon",
    version=version,
)
