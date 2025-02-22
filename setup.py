from setuptools import setup, find_packages


setup(
    name="benchy",
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm'
    ],
    packages=find_packages(),
    author = "Gresock, Jesse",
    description="Simple benchmarking tool",
    url = "https://github.com/jessegresock/benchy",
    python_requires=">=3.6"
)