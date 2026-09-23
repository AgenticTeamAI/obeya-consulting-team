---
name: "obeya"
description: "Start a session with your Obeya Insights Consulting Team — a review, a diagnosis, or a question about the room. Use with \"/obeya\"."
---

Start a session with the Obeya Insights Consulting Team.

1. Call `check_license` — one cheap call that returns all 11 roles
   with the phases each of them has.
2. Unless the user points somewhere specific, start with the **Lead**: it holds
   the assignment and decides which reading the question needs.
3. Fetch that role's playbook with `get_playbook` and work from inside it.

One call gives one phase of one role. Build the session up rather than pulling
everything down first.

When a review reaches the readings, use `/obeya-lezingen` to run them side by
side instead of one after the other.
