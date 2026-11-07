# Keeping Velacore off the Salvage Health connectors

Drafted Nov 6 2026 and applied the same night on Dourado's "Yes, apply" in chat. Test passed: a Drive listing from inside this project was refused before any file was read, in the wildcard form below, without restarting the session.

## Why

The app holds one connector default for the whole account. When Vale switched six connectors off for Velacore, Kevin's running Salvage Health session lost the same six; when Kevin switched three back on, they came back on in Vale's session too. So the on and off switch cannot keep the two businesses on different sets.

A project deny rule can. It lives in this project's own settings file, it blocks the tools by name inside Velacore sessions only, and it leaves the shared default alone, so Kevin keeps what Salvage Health needs.

## The lines to add to `.claude/settings.json`, under `permissions.deny`

```
"mcp__40134c17-83a0-4c15-a2c7-1232d464a1fd__*",
"mcp__7c992f01-c47b-48b0-abce-3dceeb6c8c9a__*",
"mcp__a76ead4e-7ac4-448e-9d6f-02c4bbde07b8__*",
"mcp__5c4848f8-ef4e-44ab-a480-d3ce007c4218__*",
"mcp__d64bc032-d9ab-4fb5-970c-befb77fac703__*",
"mcp__d7045280-9c33-47c7-b07c-cf4997241fce__*"
```

In order: Gmail, Google Drive, Google Calendar, PostHog, Kit, Metricool. All six are Dourado's personal or Salvage Health accounts. Velacore reaches its own business Gmail, Drive and Calendar through Claude in Chrome at account index 1, which these rules do not touch.

Kept for Velacore: Canva, Claude Docs, Netlify.

## Test after applying

Open a new Velacore session and ask it to list recent Drive files. The expected result is a permission refusal before any file is read. Report the result to Kevin and Dourado. If the app's matching does not accept the wildcard form above, try the exact tool names from the connector list instead and report which form worked.

## Undo

Delete the six lines. Nothing else changes.
