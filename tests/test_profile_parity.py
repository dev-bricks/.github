"""Parity, inventory, and health contract tests for dev-bricks organization profile."""

import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

PARITY_FILES = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "profile" / "README.md",
    REPO_ROOT / "profile" / "README_de.md",
    REPO_ROOT / "llms.txt",
    REPO_ROOT / "CHANGELOG.md",
]

PUBLIC_REPOS = [
    "DevCenter",
    "CodeBox",
    "pythonbox",
    "app-rotator",
    "ApiProber",
    "MethodenAnalyser",
    "WikiStub-Seed",
    "safe-start-for-codex",
    "automizer-for-claude-desktop",
    "CareCenter-for-Codex",
    "fable-5-hunter",
    ".github",
]

PUBLIC_ACTIVITY_DATES = {
    ".github": "2026-09-20",
    "WikiStub-Seed": "2026-09-20",
    "ApiProber": "2026-09-20",
    "CodeBox": "2026-09-20",
    "CareCenter-for-Codex": "2026-09-20",
    "app-rotator": "2026-09-20",
    "safe-start-for-codex": "2026-09-20",
    "DevCenter": "2026-09-20",
    "pythonbox": "2026-09-19",
    "MethodenAnalyser": "2026-09-18",
    "automizer-for-claude-desktop": "2026-08-24",
    "fable-5-hunter": "2026-06-25",
}


@pytest.fixture(scope="module")
def file_contents():
    contents = {}
    for path in PARITY_FILES:
        assert path.is_file(), f"Required file missing: {path}"
        data = path.read_bytes()
        text = data.decode("utf-8")
        assert "\ufffd" not in text, f"Invalid UTF-8 character in {path}"
        rel_key = path.relative_to(REPO_ROOT).as_posix()
        contents[rel_key] = text
    return contents


def test_files_exist_and_non_empty(file_contents):
    """Verify all core documentation files exist and have substantial content."""
    for rel_path, text in file_contents.items():
        assert len(text) > 300, f"File {rel_path} unexpectedly small ({len(text)} chars)"

    banner = REPO_ROOT / "profile" / "assets" / "app-rotator-banner.svg"
    assert banner.is_file(), "Missing app-rotator banner SVG"
    assert banner.stat().st_size > 1000, "app-rotator banner SVG unexpectedly small"


def test_markdown_fence_balance(file_contents):
    """Verify that all markdown files have balanced triple backticks."""
    for filename, text in file_contents.items():
        matches = re.findall(r"^```", text, flags=re.MULTILINE)
        assert len(matches) % 2 == 0, f"Unbalanced code fences in {filename}: {len(matches)} count"


def test_public_repo_inventory(file_contents):
    """Verify that all 12 public repositories are documented across primary profile files."""
    for filename in ["README.md", "profile/README.md", "profile/README_de.md", "llms.txt"]:
        text = file_contents[filename]
        for repo in PUBLIC_REPOS:
            assert repo in text, f"Missing public repo '{repo}' in {filename}"


def test_check_timestamp_parity(file_contents):
    """Verify that verification timestamps are synchronized to 2026-09-20."""
    assert "2026-09-20" in file_contents["README.md"]
    assert "<!-- last-checked: 2026-09-20 -->" in file_contents["profile/README.md"]
    assert "<!-- last-checked: 2026-09-20 -->" in file_contents["profile/README_de.md"]
    assert "## Last-checked: 2026-09-20" in file_contents["llms.txt"]
    assert "2026-09-20" in file_contents["CHANGELOG.md"]


def test_public_activity_snapshot(file_contents):
    """Verify the API-derived activity date for every public repository."""
    for repo, date in PUBLIC_ACTIVITY_DATES.items():
        marker = re.compile(
            rf"https://github\.com/dev-bricks/{re.escape(repo)}\)[^|]*\| {date} \|"
        )
        for filename in ["README.md", "profile/README.md", "profile/README_de.md"]:
            assert marker.search(file_contents[filename]), (
                f"Missing activity date {date} for {repo} in {filename}"
            )

        assert any(
            date in line and repo in line
            for line in file_contents["llms.txt"].splitlines()
        ), f"Missing activity date {date} for {repo} in llms.txt"


def test_repository_counts_parity(file_contents):
    """Verify that active (11) and total (12) public repository counts are consistent."""
    assert "11%20Active%20Public%20Repos" in file_contents["profile/README.md"]
    assert "11%20Aktive%20" in file_contents["profile/README_de.md"]

    assert "12 public repositories in total" in file_contents["README.md"]
    assert "12 public repositories in total" in file_contents["profile/README.md"]
    assert "12 öffentliche Repositories insgesamt" in file_contents["profile/README_de.md"]
    assert "Public repository count: 12 total" in file_contents["llms.txt"]


def test_ecosystem_cross_linking(file_contents):
    """Verify that sister organizations are properly linked."""
    ecosystem_orgs = [
        "open-bricks",
        "file-bricks",
        "doc-bricks",
        "ellmos-ai",
    ]
    for org in ecosystem_orgs:
        assert f"https://github.com/{org}" in file_contents["profile/README.md"] or f"github.com/{org}" in file_contents["profile/README.md"]
        assert f"https://github.com/{org}" in file_contents["profile/README_de.md"] or f"github.com/{org}" in file_contents["profile/README_de.md"]
        assert org in file_contents["llms.txt"]


def test_no_forbidden_local_paths(file_contents):
    """Ensure no local developer filesystem paths leak into public profile files."""
    forbidden = [
        r"C:\Users",
        "C:/Users",
        r"C:\_Local_DEV",
        "C:/_Local_DEV",
        "OneDrive",
    ]
    for filename, text in file_contents.items():
        for pattern in forbidden:
            assert pattern not in text, f"Forbidden local path '{pattern}' leaked into {filename}"


def test_mermaid_architecture_syntax(file_contents):
    """Verify Mermaid architecture diagrams are present and include app-rotator."""
    for filename in ["profile/README.md", "profile/README_de.md"]:
        text = file_contents[filename]
        assert "```mermaid" in text, f"Missing Mermaid diagram in {filename}"
        assert "flowchart TD" in text, f"Missing flowchart TD in {filename}"
        assert 'AR["app-rotator<br/>Desktop Time-Slicing Tray"]' in text, f"Missing app-rotator AR node in {filename}"
