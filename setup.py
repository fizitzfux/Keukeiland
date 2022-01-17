import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Keukeiland-jippie13",
    version="0.0.1",
    author="jippie13",
    author_email="jippiegames12@gmail.com",
    description="Keukeiland",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jippie13/Keukeiland",
    project_urls={
        "Bug Tracker": "https://github.com/jippie13/Keukeiland/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
