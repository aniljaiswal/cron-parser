from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cron-parser",
    version="1.0.0",
    author="Anil Jaiswal",
    author_email="er.anil.jaiswal@gmail.com",
    description="A simple cron expression parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aniljaiswal/cron-parser",
    packages=["cron_parser"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "cron-parser = cron_parser.cli:cli"
        ]
    },
    python_requires='>=3.6',
)
