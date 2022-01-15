IMPORTANT: ALWAYS USE UNIX PATH!

Delegato
========================

Automatically create a *setup.py* for you to

1. Make any executable as a Python package.

   Hence, you can
   - install your executable locally(add to PATH automatically without pollutions),

       > python setup.py install

   - upload them to Python package index,

       > # register PyPI at https://pypi.org/ and
       > # create a .pypirc under $HOME

       > pip install twine
       > python setup.py bdist_wheel

       > twine upload -r testpypi dist/*

    - install your executable from Python package index

       > pip install <your uploaded package>

2. Manage any executable with Python environment managers

   You can use *venv*, *conda*, *pyenv*, etc.,
   for instance, using conda:

   > conda create -n <some_env_name> python=3.7
   > conda activate <some_env_name>

Besides, there maybe be an existing one but I can't google it out.

Usage
========================

    delegato --exe <executable(relative path to depdir if specified)>
             --packname <python package_name>
             [--depdir: dependency directory]
             [--cmdname: the command to invoke your exe]

For single executables(scroll down and see how to package executables
with a self-contained directory within 1 second):

     > delegato --exe <executable> --packname <python package_name>


This command will create a *setup.py* in current directory, hence

1. You can easily install your executable to PATH via:

     > python setup.py install

   (Incidentally, I wrote this package mainly for making .NET CLI more user-friendly. It's difficult to locally test .NET console projects.)

2. If you're in a Python virtual environment, the visibility of this
executable will be restricted to the current virtual environment.

   You can switch your Python environment and the installed executables wouldn't pollute anything.


3. For executable with dependencies in more complex structure,
   create the package this way.

     > delegato
         --exe <executable path relative to depdir>
         --depdir "<directory>"
         --packname <python package_name>

   Note that the whole dependency directory will be packaged,
   instead of only the shallow ones.


4. Feel free to edit the generated *setup.py* to specify
   more information(like *author*, *license*, etc.) about your package.

   All metadata parameters are well-documented in the generated *setup.py*.
