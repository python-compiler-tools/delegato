import glob
from setuptools import setup
README = """
$README
"""

setup(
    name='$PACK',

    # e.g., 0.1.1, 0.2
    # see more at https://www.python.org/dev/peps/pep-0440/
    version='',

    # keywords of your project that separated by comma ","
    keywords='',

    # a concise introduction of your project
    description='',

    # a very long introduction of your project.
    # usually, read it from a README file:
    long_description=README,

    long_description_content_type="text/markdown",

    # distribution under which license
    # https://opensource.org/licenses
    license='mit',

    python_requires='>=3.5.0',

    # A URL to your project's repository/website
    # e.g., https://github.com/thautwarm/MLFS
    url='',

    author='',
    author_email='',
    packages=['$PACK'],
    install_requires=[],
    package_data={
        '$PACK':
            [each[len('$PACK/'):]
             for each in glob.glob("$PACK/$DIR/**", recursive=True)]
    },
    entry_points={"console_scripts": [
        "$EXE=$PACK.main:exe"
    ]},

    # your executable supported platforms
    platforms="any",

    # usually you do not need to change it
    # if interests see:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)