from setuptools import setup, find_packages

setup(
    name="mmlsyc",
    version="0.1.0",
    description="MMLSyr Compiler - A higher-level MML language compiler",
    long_description="""MMLSyr Compiler is a tool that compiles MMLSyr files to standard MML.

MMLSyr extends MML with the following features:
- Support for relative path includes (compiled to absolute paths in standard MML)
- Direct macro calls in K tracks (automatically compiled to R_i track definitions)

This makes it easier to write and organize complex MML compositions.
""",
    url="https://github.com/syrmml/mmlsyc",
    author="Syrmml Team",
    author_email="team@syrmml.com",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mmlsyc = mmlsyc.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)