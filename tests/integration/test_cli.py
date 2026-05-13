from typer.testing import CliRunner

from blindspot.cli import app


def test_help_lists_commands():
    runner = CliRunner()
    res = runner.invoke(app, ["--help"])
    assert res.exit_code == 0
    out = res.stdout
    assert "ask" in out
    assert "history" in out
    assert "review" in out
    assert "rate" in out
    assert "stats" in out


def test_sources_help_lists_subcommands():
    runner = CliRunner()
    res = runner.invoke(app, ["sources", "--help"])
    assert res.exit_code == 0
    assert "list" in res.stdout
    assert "gaps" in res.stdout
    assert "stats" in res.stdout
