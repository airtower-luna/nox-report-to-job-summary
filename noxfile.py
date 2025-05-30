# mypy: allow-untyped-defs, check-untyped-defs
# mypy: disable-error-code="import-not-found"
import nox


@nox.session
def lint(session):
    """Lint using Flake8."""
    session.install('flake8')
    session.run('flake8', '--statistics', '.')


@nox.session
def typecheck(session):
    """Typecheck using MyPy."""
    session.install('mypy', 'pytest')
    session.run('mypy', '--strict', '.')


@nox.session(python=['3.11', '3.12', '3.13'])
def test(session):
    """Run tests."""
    session.install('pytest')
    session.run('python', '-m', 'pytest', '-v')
