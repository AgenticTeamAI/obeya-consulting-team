#!/usr/bin/env python3
"""
Zero-IP check for this public repo.

Everything in this repo is public. It may contain the team's menu (role names,
emoji, public descriptions, the instruction to fetch a playbook) and a handful
of repo files, and nothing else. The methodology itself is served per phase by
the licensed connector and never lives here.

The check has two layers.

1. ALLOWLIST. Every tracked file is either listed in plugin-manifest.json (written
   by the generator, installer/build_obeya_plugin.py in the private
   agent-architecture repo) with a matching sha256, or it is one of the repo
   files in REPO_OWN below. Every file in the manifest must exist, and the
   plugin version must match the manifest. Anything else was not generated from
   the registry and does not belong here.

2. PATTERNS, over every tracked file, including the repo files the generator
   never sees: phase markers, prompt placeholders, Notion links, UUIDs, licence
   keys of either product, secrets, playbook section headings of either
   product, references to internal source material and backlog items, text from
   the licensed Maturity Scan, and threshold expressions (a quantifier, a number
   and a subject from the Obeya model within one clause). Zero tolerance: this
   repo carries none of these today, so there is no baseline here. The baseline
   for the SERVED phases lives next to the generator, which is the only place
   that has both the content and this repo in hand.

The generator runs the same patterns before it writes a build. This copy is
deliberately separate and runs offline, without agent-architecture, so that a
fault in the generator cannot blind the check as well. The generator's test
suite verifies the direction that matters: this list must know at least every
pattern the generator knows. Knowing more is allowed; it only makes this
stricter.

The literals below are written so that they do not match themselves. This file
is checked too, and an exception for the checker is exactly the gap to avoid.

Requires a git clone: the list of files comes from git.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = "obeya-consulting-team"

# A Windows console on code page 1252 would crash on the check marks below and
# make a clean run look like a failure. Keep the encoding, only replace what
# cannot be printed.
for _stream in (sys.stdout, sys.stderr):
    _reconfigure = getattr(_stream, "reconfigure", None)
    if _reconfigure is None:
        continue
    try:
        "✅".encode(_stream.encoding or "utf-8")
    except (UnicodeEncodeError, LookupError):
        try:
            _reconfigure(errors="replace")
        except (ValueError, OSError):
            pass

# Files that belong to the repo rather than to the generated plugin. A short,
# literal list on purpose (no globs): a new file outside it has to be a
# deliberate choice, made here, in review.
REPO_OWN = {
    "README.md",
    ".gitignore",
    "plugin-manifest.json",
    "scripts/check_zero_ip.py",
    ".github/workflows/zero-ip.yml",
}

# Generic patterns, shared with the other product's marketplace.
PATTERNS = [
    (re.compile(r"<!--\s*phase:"), "phase marker (playbook content)"),
    (re.compile(r"\{\{[A-Z0-9_]+\}\}"), "prompt placeholder"),
    (re.compile(r"notion\.so|notion\.site|api\.notion\.com"), "Notion link"),
    (re.compile(r"\b[0-9a-f]{32}\b|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"), "UUID or database ID"),
    (re.compile(r"atk_(?!\.\.\.)[A-Za-z0-9_-]{8,}"), "licence key"),
    (re.compile(r"secret_[A-Za-z0-9]{20,}|ntn_[A-Za-z0-9]{20,}|sk_" + "live|whsec" + "_"), "secret"),
    (re.compile(r"##\s*(Rol & Missie|Werkwijze per run|Escalatieprincipes|Session Output)"), "playbook section heading"),
]

# Obeya-specific patterns.
PATTERNS += [
    # This product's key prefix.
    (re.compile(r"obk_(?!\.\.\.)[A-Za-z0-9_-]{8,}"), "licence key (Obeya)"),
    # Backlog items, internal source documents and decision logs. In the
    # content repo these sit in HTML comments that the connector strips.
    (
        re.compile(
            r"\bob\d{1,3}\b"
            r"|\bBehavioral[ ]Logic\b|\bVisual[ ]Design[ ]Language\b|\bSemantic[ ]Model[ ]v\d"
            r"|\bbesluiten-20\d\d-\d\d-\d\d\b"
            r"|app\.notion\.com"
        ),
        "reference to internal source material",
    ),
    # Section headings that only occur in the Obeya playbooks.
    (
        re.compile(
            r"^#{1,4}\s*(?:Phase:\s*(?:orientation|core|method|model|checks|handoff)\b"
            r"|De drempels die jij handhaaft|Decision rules|Beslisregels|Warrants|Held back"
            r"|Vastgelegde ontwerpkeuzes|Je aandeel in de zeven universele checks"
            r"|De twee modi|Uit de rollentabel van het teamontwerp)",
            re.MULTILINE,
        ),
        "playbook section heading (Obeya)",
    ),
    # The Maturity Scan belongs to the Obeya Association and is used under
    # licence. Its attribution may appear anywhere; its sub-questions may not
    # appear in a public repo.
    (re.compile(r"\(quadrant[ ](?:Mindset|Alignment|Workspace|Content)\)"), "Maturity Scan text (licensed)"),
]

# Threshold expressions. A quantifier that states a limit, a number from two
# up, and a subject from the Obeya model, within one clause (the window stops
# at a full stop, a line break or a table bar). A count on its own is not a
# threshold, and neither is a public standard such as a contrast ratio. The
# same forms count the served phases on the server side.
_QUANTIFIER = (
    "(?:maximaal|maximum|max|ten hoogste|hoogstens|no more than|more than|at most|"
    "never exceed|exceed|beyond|boven|minimaal|minimum|ten minste|at least|vanaf|"
    "ouder dan|older than|no fewer than|up to)"
)
_NUMBER = (
    "(?:[2-9]\\d*|1\\d+|twee|drie|vier|vijf|zes|zeven|acht|negen|tien|"
    "two|three|four|five|six|seven|eight|nine|ten)"
)
_SUBJECT = (
    "(?:zones?|metriek(?:en)?|metrics?|indicator(?:en|s)?|thema(?:'s|s)?|themes?|"
    "elementen|elements?|cadans(?:en)?|cadences?|cycli|cycles?|connecties|connections?|"
    "lagen|layers|acties|actions?|bevindingen|findings?|waarnemingen|observations?|"
    "correcties|corrections?|patroon|patterns?|categoriekleuren|borden|boards?)"
)
_WINDOW = "[^.\\n|]{0,30}?"
_FLAGS = re.IGNORECASE | re.ASCII
THRESHOLD_FORMS = (
    re.compile(f"\\b{_QUANTIFIER}\\b{_WINDOW}\\b{_NUMBER}\\b{_WINDOW}\\b{_SUBJECT}\\b", _FLAGS),
    re.compile(f"\\b{_NUMBER}\\b{_WINDOW}\\b{_SUBJECT}\\b{_WINDOW}\\b{_QUANTIFIER}\\b", _FLAGS),
    re.compile(r"\b(?:leading\s*:\s*lagging|leading (?:to|op) lagging)\b[^.\n|]{0,40}?\b\d\s*:\s*\d\b", _FLAGS),
    re.compile(r"\b\d\s*:\s*\d\b[^.\n|]{0,40}?\bleading\b", _FLAGS),
    re.compile(r"\b(?:two to one|twee op (?:een|één))\b[^.\n|]{0,30}?\blagging\b", _FLAGS),
    re.compile(
        "\\b(?:geen|zonder|no|without|stil|silent|stale|onveranderd|unchanged)\\b"
        f"{_WINDOW}\\b{_NUMBER}\\b[^.\\n|]{{0,12}}?\\b(?:cycli|cycles)\\b",
        _FLAGS,
    ),
)

# Menu skills are small; anything bigger is suspect.
MAX_SKILL_BYTES = 8192


def tracked_files(root: Path) -> list:
    """Everything git knows about (committed, staged, and new files that are not
    ignored), so a local run does not trip over editor swap files. Without a
    git clone there is no reliable list, and the check stops rather than fall
    back to a directory walk."""
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            check=True, capture_output=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise SystemExit(f"❌ The zero-IP check needs a git clone of this repo ({e}).")
    return sorted(p for p in out.decode("utf-8").split("\0") if p and not (root / p).is_dir())


def pattern_findings(rel: str, text: str) -> list:
    """Every pattern and threshold hit in one file, with its line number."""
    found = []

    def line(pos):
        return text.count("\n", 0, pos) + 1

    for pattern, label in PATTERNS:
        for m in pattern.finditer(text):
            found.append(f"{rel}:{line(m.start())}: {label} — '{m.group(0)[:40]}'")
    for form in THRESHOLD_FORMS:
        for m in form.finditer(text):
            found.append(f"{rel}:{line(m.start())}: threshold expression — '{m.group(0)[:60]}'")
    return found


def findings(root: Path = ROOT) -> tuple:
    """(findings, number of generated files, registry version)."""
    root = Path(root)
    failures = []

    try:
        manifest = json.loads((root / "plugin-manifest.json").read_text(encoding="utf-8"))
        generated = manifest["bestanden"]
        if not isinstance(generated, dict) or not generated:
            raise ValueError("'bestanden' is missing or empty")
        version = str(manifest["registryVersion"])
    except (OSError, ValueError, KeyError, TypeError) as e:
        return [f"plugin-manifest.json is missing or invalid ({e}); regenerate it with the generator"], 0, "?"

    content = {}
    for rel in tracked_files(root):
        try:
            content[rel] = (root / rel).read_bytes()
        except FileNotFoundError:
            failures.append(f"{rel}: tracked in git but missing from the working tree")
        except (PermissionError, IsADirectoryError) as e:
            failures.append(f"{rel}: unreadable ({e.__class__.__name__})")

    # Layer 1: allowlist.
    for rel, data in content.items():
        if rel in REPO_OWN:
            continue
        expected = generated.get(rel)
        if expected is None:
            failures.append(f"{rel}: not in plugin-manifest.json and not a repo file — not made by the generator")
        elif "sha256:" + hashlib.sha256(data).hexdigest() != expected:
            failures.append(f"{rel}: differs from plugin-manifest.json — edited by hand, or the manifest is stale")
    for rel in generated:
        if rel not in content:
            failures.append(f"{rel}: listed in plugin-manifest.json but missing from the repo")

    plugin_json = f"plugins/{PLUGIN}/.claude-plugin/plugin.json"
    try:
        plugin_version = json.loads((root / plugin_json).read_text(encoding="utf-8")).get("version")
        if str(plugin_version) != version:
            failures.append(f"{plugin_json}: version {plugin_version} ≠ manifest registryVersion {version}")
    except (OSError, ValueError, AttributeError):
        failures.append(f"{plugin_json} is missing or not a JSON object")

    # Layer 2: patterns, over everything.
    for rel, data in content.items():
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            failures.append(f"{rel}: binary or unreadable file — does not belong here")
            continue
        if rel.endswith("SKILL.md") and len(data) > MAX_SKILL_BYTES:
            failures.append(f"{rel}: {len(data)}B > {MAX_SKILL_BYTES}B — too large for a menu skill")
        failures.extend(pattern_findings(rel, text))

    return failures, len(generated), version


def main() -> int:
    failures, generated, version = findings(ROOT)
    for failure in failures:
        print(f"❌ {failure}")
    if failures:
        print(f"\n❌ Zero-IP check failed: {len(failures)} finding(s)")
        return 1
    print(f"✅ Zero-IP check clean: {generated} generated files (registry {version}) plus repo files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
