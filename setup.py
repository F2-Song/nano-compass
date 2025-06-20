import os
from setuptools import setup, find_packages

def get_version():
    return "0.0.0"

def get_requires() -> list[str]:
    with open("requirements.txt", encoding="utf-8") as f:
        file_content = f.read()
        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]
        return lines

def main():
    setup(
        name="nano-compass",
        version=get_version(),
        packages=find_packages(),
        install_requires=[
        ],
        author="nano-compass contributors",
        author_email="songfeifan@hotmail.com",
        description="A light-weight library for LLM generated content evaluation, execluding LLM inference.",
        long_description=open("README.md", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/F2-Song/nano-compass",
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        keywords=["AI", "LLM", "Evaluation"],
        license="Apache 2.0 License",
        python_requires=">=3.9.0",
    )

if __name__ == "__main__":
    main()
