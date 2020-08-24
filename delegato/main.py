import os
from distutils.dir_util import copy_tree
from pathlib import Path
from string import Template
from wisepy2 import wise

README_REF = [""]


def mk_setup(PACK, DIR, EXE):
    README = README_REF[0]
    setup_template = Path(__file__).parent / "setup_template.py"
    contents = setup_template.open().read()
    return Template(contents).safe_substitute(
        PACK=PACK, README=repr(README), DIR=DIR, EXE=EXE
    )


def mk_main(EXE_PATH):
    main_template = Path(__file__).parent / "main_template.py"
    contents = main_template.open().read()
    return Template(contents).safe_substitute(EXE_PATH=EXE_PATH)


def main():

    default_packname = Path(".").absolute().name
    readme = Path(".") / "README.md"
    if readme.exists():
        README_REF[0] = readme.open().read()

    def delegato(
        *,
        packname: "python package name. in fact, the package name will be 'dexe-$packname'"=default_packname,
        exe: "executable path. If $depdir specified, it's a relative path to $depdir." = "",
        depdir: "dependency directory. if specified shall include $exe" = "",
        cmdname: "if specified, it's the name that the installed executable seen as" = ""
    ):
        """delegato: delegate your executable to existing environment managers.
        """
        assert exe, "executable name/path mustn't be empty!"
        packname = "dexe_" + packname
        cmdname = cmdname or Path(exe).name

        Path(packname).mkdir(mode=0o777, parents=True, exist_ok=True)

        if depdir:
            depdir_path = Path(depdir).absolute()
            bindir = depdir_path.name
            copy_tree(str(depdir_path), str(Path(packname).joinpath(bindir)))
            exe_pack_path = os.path.join(bindir, exe)
        else:
            bindir = "bin"
            exe_pack_path = os.path.join(bindir, Path(exe).name)
            Path(packname).joinpath("bin").mkdir(
                mode=0o777, parents=True, exist_ok=True
            )
            with open(exe, 'rb') as f1, Path(packname).joinpath(exe_pack_path).open('wb') as f2:
                f2.write(f1.read())

        with open("setup.py", "w") as f:
            f.write(mk_setup(packname, bindir, cmdname))

        with Path(packname).joinpath("main.py").open("w") as f:
            f.write(mk_main(exe_pack_path))

        with Path(packname).joinpath("__init__.py").open("w") as f:
            f.write("")

    wise(delegato)()
