# Obeya Consulting Team — Claude-plugin

Elf rollen die samen een Obeya lezen, toetsen en herontwerpen, als plugin voor
Claude. **Deze repo bevat alleen de menukaart**: welke rollen er zijn en waar ze
voor zijn. De playbooks zelf worden per fase opgehaald via de beveiligde
connector op `connector.obeya-insights.com` — er staat geen methodiek in deze
repo, en dat is met een guard afgedwongen.

Installeren en koppelen: zie [de plugin-README](plugins/obeya-consulting-team/README.md).

## Naast het Agentic Team

Deze plugin kan náást `agentic-team` staan. Er botst niets: de marketplace heet
anders, de plugin heet anders, alle rolnamen beginnen met `obeya-`, en het
commando is `/obeya` in plaats van `/chief` of `/gids`.

## Gegenereerd, niet met de hand geschreven

Alles hier komt uit `installer/build_obeya_plugin.py` in
[agent-architecture](https://github.com/AgenticTeamAI/agent-architecture), uit de
registry van [Obeya-Team-Pack](https://github.com/AgenticTeamAI/Obeya-Team-Pack).
Zelfde registry in, byte-identieke output uit.

`plugin-manifest.json` is de allowlist: elk bestand met zijn sha256. Staat een
bestand daar niet in, dan hoort het hier niet.

## Wat er nooit in mag

Drempelwaarden, methodiek, klantdata, licentiesleutels. De generator draait
dezelfde menukaart-guard als het andere product — dezelfde patronen, dezelfde
8 KB-limiet per skill — plus een controle op de `obk_`-sleutelprefix. Faalt die,
dan komt er geen build.

Support: [support@obeya-insights.com](mailto:support@obeya-insights.com)
