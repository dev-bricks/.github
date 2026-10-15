"""Synthetic checks for the externally configured profile privacy guard."""
import pytest

from test_profile_parity import check_public_profile


def test_public_links_checked_without_private_inventory(monkeypatch):
    monkeypatch.delenv("PROFILE_PRIVATE_REPO_DENYLIST", raising=False)
    check_public_profile("https://github.com/dev-bricks/CodeBox")
    with pytest.raises(AssertionError, match="unlisted repository"):
        check_public_profile("https://github.com/dev-bricks/synthetic-unlisted")


@pytest.mark.parametrize("separator", [",", ";", "\n", " "])
def test_configured_guard_redacts_failure(monkeypatch, separator):
    name = "synthetic-private-project"
    monkeypatch.setenv("PROFILE_PRIVATE_REPO_DENYLIST", f"other{separator}{name}")
    with pytest.raises(AssertionError) as caught:
        check_public_profile(name.upper())
    assert name not in str(caught.value).casefold()
    check_public_profile("Ordinary public profile text")
