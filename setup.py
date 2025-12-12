"""
Setup configuration for Python Code Collection package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="python-code-collection",
    version="1.0.0",
    author="Levi",
    author_email="",
    description="A collection of Python learning projects demonstrating various programming concepts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/levi909-create/python-Code",
    project_urls={
        "Bug Reports": "https://github.com/levi909-create/python-Code/issues",
        "Source": "https://github.com/levi909-create/python-Code",
        "Documentation": "https://github.com/levi909-create/python-Code#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "pylint>=2.15.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "poets=src.poets:main",
            "codes-for-fun=src.codes_for_fun:main",
            "random-range=src.random_range:main",
        ],
    },
    keywords="python learning education utilities poetry visualization",
    include_package_data=True,
    zip_safe=False,
)
