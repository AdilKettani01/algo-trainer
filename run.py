#!/usr/bin/env python3
"""Tiny CLI around pytest.

  python run.py list                 progress for every section
  python run.py 3                    run section 03 against YOUR code
  python run.py 3 --solutions        run section 03 against the reference solutions
  python run.py all                  run everything
  python run.py reset 3              wipe your section 03 code back to empty stubs
"""
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
SECTIONS = sorted(p for p in (ROOT / "sections").iterdir() if p.is_dir())


def pick(token):
    for s in SECTIONS:
        if s.name.startswith(token.zfill(2)):
            return s
    sys.exit(f"No section matching {token!r}. Try: python run.py list")


def pytest(paths, env_extra=None, quiet=True, extra=()):
    env = {**os.environ, **(env_extra or {})}
    cmd = [sys.executable, "-m", "pytest", *map(str, paths), *extra]
    if quiet:
        cmd += ["--tb=no", "-p", "no:cacheprovider"]
    return subprocess.run(cmd, cwd=ROOT, env=env, capture_output=quiet, text=True)


def summary(proc):
    line = (proc.stdout or "").strip().splitlines()[-1:] or [""]
    passed = int((re.search(r"(\d+) passed", line[0]) or [0, 0])[1])
    failed = int((re.search(r"(\d+) (?:failed|error)", line[0]) or [0, 0])[1])
    return passed, passed + failed


def main():
    args = sys.argv[1:]
    sol = {"USE_SOLUTIONS": "1"} if "--solutions" in args or "-s" in args else {}
    args = [a for a in args if not a.startswith("-")]
    if not args or args[0] == "list":
        done = 0
        print(f"{'Section':<34}{'Passing':>10}")
        for s in SECTIONS:
            p, t = summary(pytest([s], sol))
            done += t > 0 and p == t
            bar = "OK " if t and p == t else "   "
            print(f"{bar}{s.name:<31}{p:>5}/{t:<4}")
        print(f"\nSections complete: {done}/{len(SECTIONS)}")
    elif args[0] == "all":
        sys.exit(pytest([ROOT / "sections"], sol, quiet=False).returncode)
    elif args[0] == "reset":
        s = pick(args[1])
        if input(f"Wipe your work in {s.name}? type 'yes': ") == "yes":
            sys.path.insert(0, str(ROOT / "tools"))
            import make_stubs
            make_stubs.generate(s, force=True)
            print("reset.")
    else:
        sys.exit(pytest([pick(args[0])], sol, quiet=False, extra=["-rf"]).returncode)


if __name__ == "__main__":
    main()
