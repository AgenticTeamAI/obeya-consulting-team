# Obeya Insights Consulting Team — Claude plugin

Eleven roles that read, test and redesign an Obeya together, as a plugin for
Claude. **This repo contains only the menu**: which roles exist and what each
one is for. The playbooks themselves are fetched per phase through the secured
connector at `connector.obeya-insights.com` — no methodology lives in this
repo, and a guard enforces that.

To install and connect: see [the plugin README](plugins/obeya-consulting-team/README.md).

## Alongside Agentic Team

This plugin can sit next to `agentic-team`. Nothing clashes: the marketplace
has a different name, the plugin has a different name, every role name starts
with `obeya-`, and the command is `/obeya` rather than `/chief` or `/gids`.

## Generated, not written by hand

Everything here comes from `installer/build_obeya_plugin.py` in
[agent-architecture](https://github.com/AgenticTeamAI/agent-architecture), from
the registry in [Obeya-Team-Pack](https://github.com/AgenticTeamAI/Obeya-Team-Pack).
Same registry in, byte-identical output out.

`plugin-manifest.json` is the allowlist: every file with its sha256. If a file
isn't listed there, it doesn't belong here.

## What must never be in here

Thresholds, methodology, client data, licence keys. The generator runs the same
menu guard as the other product — the same patterns, the same 8 KB limit per
skill — plus checks of its own for this product: the `obk_` key prefix,
threshold expressions, references to internal source material, playbook
section headings and text from the licensed Maturity Scan. If that fails, there
is no build.

On every push and pull request, `scripts/check_zero_ip.py` checks this repo
again, independently of the generator and without access to it: every file is
either listed in `plugin-manifest.json` with a matching hash or is one of a
handful of repo files, and no file — including this README — may contain any of
the above.

Support: [support@obeya-insights.com](mailto:support@obeya-insights.com)
