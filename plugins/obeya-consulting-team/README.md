# Obeya Insights Consulting Team

*Eleven roles that read, test and redesign an Obeya. Requires an
[Obeya Insights](https://obeya-insights.com) licence.*

This plugin contains the team's **menu**: which roles exist and what each one
is for. The playbooks themselves are fetched per phase through the secured
connector, so they are always current — no methodology lives in this repo.

## Install

1. **Add the marketplace.** In **claude.ai, the desktop app or Cowork:**
   Settings → Plugins → Add → *Add marketplace* → *Add from a repository*,
   and enter `AgenticTeamAI/obeya-consulting-team`. Make sure *Sync automatically* is
   on, so updates reach you. In **Claude Code:**
   `/plugin marketplace add AgenticTeamAI/obeya-consulting-team`.
2. **Install Obeya Insights Consulting Team.** Then open **Connectors** in the plugin and click
   *Install* next to `Obeya-Insights-Consulting-Team`. The address is already filled in:

   ```
   https://connector.obeya-insights.com/mcp
   ```

   You can also add it by hand: Settings → Connectors → Add custom connector,
   with **Name:** `Obeya Insights Consulting Team` and the same address.
   The address is the same for everyone and contains no secret.
3. **Connect, and sign in with the email address you were invited on.** Enter
   it and press **Continue**. You'll see *"Check your email"*, and an email
   arrives with a sign-in link and an eight-digit code. There is no key to
   keep and nothing to paste.
4. **Open the link in the same browser you started in.** You'll see
   *"Confirm it's you"*. Press **Continue**, and you're in.

   If your mail app opens the link in a different browser — Outlook opening
   Edge while you work in Chrome, or the email on your phone — you'll see
   *"Open this in your original browser"* and nothing else happens. That isn't
   a fault, and nothing is used up: go back to the *"Check your email"* page in
   the browser where you started, and type the code from the email there.

### Stuck?

Two screens look like waiting, but aren't:

- **"Check your email", but nothing arrives.** That screen always says the same
  thing, including when your address hasn't been invited yet — on purpose, so
  nobody can use it to find out who is a customer. If the email doesn't come,
  that is almost always why. Email [support@obeya-insights.com](mailto:support@obeya-insights.com) rather than
  trying again.
- **"Not ready yet".** Signing in only works when a workspace of your own is
  attached to your licence. If there isn't one, the screen's advice to try
  again in a moment won't help — this doesn't resolve by itself. Email
  [support@obeya-insights.com](mailto:support@obeya-insights.com) here too.

## Alongside Agentic Team

This plugin can sit right next to `agentic-team`. Every role name starts with
`obeya-`, the marketplace has a different name, and the commands don't clash:
this team answers to `/obeya`.

## What's in this repo

Only the menu: role names, emoji, public descriptions and the instruction to
fetch the playbook. No thresholds, no methodology, no client data. A generated
manifest (plugin-manifest.json) records which files the plugin itself contains; nothing
under `plugins/` or `.claude-plugin/` should appear that isn't listed there.

Support: [support@obeya-insights.com](mailto:support@obeya-insights.com)
