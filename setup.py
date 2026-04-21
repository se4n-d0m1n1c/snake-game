from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="snake-game",
    version="1.0.0",
    author="Sean Dominic Fernandez",
    author_email="seandominicfernandez@gmail.com",
    description="A classic Snake game implementation with PyGame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/se4n-d0m1n1c/snake-game",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Arcade",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pygame>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "snake-game=game:main",
        ],
    },
)