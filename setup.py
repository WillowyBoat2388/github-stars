from setuptools import find_packages, setup

setup(
    name="github_stars",
    packages=find_packages(exclude=["github_stars_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "PyGithub",
        "matplotlib",
        "pandas",
        "nbconvert",
        "nbformat",
        "ipykernel",
        "jupytext",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
