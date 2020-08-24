from setuptools import setup, find_packages
from pathlib import Path


version = 0.1
with Path("README.txt").open() as readme:
    readme = readme.read()


setup(
    name="delegato",
    version=version if isinstance(version, str) else str(version),
    keywords="executable",
    description="delegate and then manage executables in Python environment manager",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="mit",
    python_requires=">=3.6.0",
    url="https://github.com/thautwarm/delegato",
    author="thautwarm",
    author_email="twshere@outlook.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["delegato=delegato.main:main"]},
    # above option specifies what commands to install,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd:compiler"]}
    install_requires=["wisepy2"],  # dependencies
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
