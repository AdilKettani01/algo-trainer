"""Generate problems.py (empty stubs) from solutions/<section>.py.

Keeps signatures + docstrings, replaces bodies with `pass`.
Usage: python tools/make_stubs.py            (all sections that have no problems.py yet)
       python tools/make_stubs.py 03 --force (regenerate section 03, wiping your work)
"""
import ast
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEEP_IMPORTS = {"helpers", "typing"}


def _is_doc(stmt):
    return (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant)
            and isinstance(stmt.value.value, str))


def _strip(fn):
    doc = fn.body[0] if fn.body and _is_doc(fn.body[0]) else None
    fn.body = ([doc] if doc else []) + [ast.Pass()]
    return fn


def make_stub(src: str) -> str:
    tree = ast.parse(src)
    out = []
    for node in tree.body:
        if _is_doc(node):
            title = node.value.value.replace("(reference solutions)", "(your workspace)")
            out.append(ast.Expr(ast.Constant(title)))
        elif isinstance(node, ast.ImportFrom) and node.module in KEEP_IMPORTS:
            out.append(node)
        elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            out.append(_strip(node))
        elif isinstance(node, ast.ClassDef):
            node.body = [_strip(n) if isinstance(n, ast.FunctionDef) else n
                         for n in node.body if isinstance(n, ast.FunctionDef) or _is_doc(n)]
            out.append(node)
    parts = [ast.unparse(ast.fix_missing_locations(n)) for n in out]
    return "\n\n\n".join(parts) + "\n"


def sections():
    return sorted(p for p in (ROOT / "sections").iterdir() if p.is_dir())


def generate(section_dir: pathlib.Path, force=False) -> bool:
    target = section_dir / "problems.py"
    if target.exists() and not force:
        return False
    sol = ROOT / "solutions" / f"{section_dir.name}.py"
    target.write_text(make_stub(sol.read_text()))
    return True


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    for s in sections():
        if args and not s.name.startswith(args[0].zfill(2)):
            continue
        if generate(s, force):
            print("generated", s.name)
