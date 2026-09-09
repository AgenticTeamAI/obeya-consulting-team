# Obeya Consulting Team

*Eleven roles that read, test and redesign an Obeya. Requires an
[Obeya Insights](https://obeya-insights.com) licence.*

Deze plugin bevat de **menukaart** van het team: welke rollen er zijn en waar ze
voor zijn. De playbooks zelf worden per fase opgehaald via de beveiligde
connector, dus ze zijn altijd actueel — er staat geen methodiek in deze repo.

## Installeren

1. Voeg de marketplace toe — **claude.ai / desktop / Cowork:** Settings →
   Plugins → Add → *Add marketplace* → *Add from a repository*:
   `AgenticTeamAI/obeya-consulting-team` · **Claude Code:**
   `/plugin marketplace add AgenticTeamAI/obeya-consulting-team`.
2. Installeer **obeya-consulting-team**.
3. **Zet je eigen licentiesleutel in het connector-adres.** Dit product kent nog
   geen inlog op e-mailadres, dus de sleutel zit in de URL. Vervang
   `PLAK-HIER-JE-SLEUTEL` door je eigen sleutel:

   ```
   https://connector.obeya-insights.com/api/mcp/k/PLAK-HIER-JE-SLEUTEL/mcp
   ```

   Je sleutel krijg je één keer van Obeya Insights. Die URL ís het geheim —
   niet doorsturen, niet in een screenshot. Kwijt? Dan krijg je een nieuwe en
   vervalt de oude.

## Naast het Agentic Team

Deze plugin kan gewoon náást `agentic-team` staan. De rolnamen beginnen allemaal
met `obeya-`, de marketplace heet anders en de commando's botsen niet: dit team
luistert naar `/obeya`.

## Wat er in deze repo staat

Alleen de menukaart: rolnamen, emoji, publieke omschrijvingen en de instructie
om het playbook op te halen. Geen drempelwaarden, geen methodiek, geen
klantdata. Een gegenereerd manifest (plugin-manifest.json) legt vast welke bestanden
erbij horen; alles daarbuiten hoort er niet te zijn.

Support: [support@obeya-insights.com](mailto:support@obeya-insights.com)
