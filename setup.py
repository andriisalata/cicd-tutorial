from setuptools import find_packages, setup

setup(
    name="cicd_tutorial_package",
    packages=find_packages(exclude=["test", "test.*"]),
    setup_requires=["wheel"],
    install_requires=[
        "setuptools",
    ],
    version='0.0.1',
    description="CI CD pipeline demo package",
    author="andrii.salata@sigma.software",
    entry_points={
            'console_scripts': ['app = app.main:hello_world']
    }
)
