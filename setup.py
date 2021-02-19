import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-prob-dist", # Replace with your own username
    version="0.0.1",
    author="Aarsh Pandey",
    author_email="aarshpandey@gmail.com",
    description="A Python Package of Probability Distribution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aarsh-pandey/Python-Probability-Distribution",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib>=3.0.0'
    ],
    python_requires='>=3.6',
)