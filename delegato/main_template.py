def exe():
    from pathlib import Path
    from subprocess import call
    import sys

    cmd = str((Path(__file__).parent / "$EXE_PATH").absolute())
    call([cmd, *sys.argv[1:]])
