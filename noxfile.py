import nox


@nox.session
def lint(session):
    """Lint using Flake8."""
    session.install('flake8')
    session.run('flake8', '--statistics', '.')


@nox.session(python=['3.10', '3.11'])
def test(session):
    """Run tests."""
    session.install('pytest')
    session.run('python', '-m', 'pytest', '-v')
