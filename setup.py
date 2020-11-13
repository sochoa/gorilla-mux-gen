import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gorilla-mux-gen",
    version="0.0.1",
    author="Sean Ochoa",
    author_email="sean.m.ochoa@gmail.com",
    description="A tool to generate Gorilla Mux application components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['gorilla-mux-gen=gen:cli'],
    }
)
