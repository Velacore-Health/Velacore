# Setting up the local Velacore agent on Dourado's PC

Written Nov 6, 2026 from the agent-setup inventory Kevin produced. For the first local session.

## Dourado does these, one at a time

1. Open PowerShell and run these one at a time. The repo lives directly in Documents\Velacore Health. A plain clone refuses a folder that already has files in it, so this fetches into the existing folder instead:
   `cd "C:\Users\Dourado\Documents\Velacore Health"`
   `git init`
   `git remote add origin https://github.com/Velacore-Health/Velacore.git`
   `git fetch origin`
   `git checkout -b claude/velacore-health-website-qnjdnh origin/claude/velacore-health-website-qnjdnh`
   The four content folders 01-raw-clips, 02-selects, 03-edits and 04-scheduled sit in the repo root and are gitignored, so video files never go to GitHub.
2. In the Claude desktop app, Code tab, open the folder `C:\Users\Dourado\Documents\Velacore Health` as a new project.
3. Start the session with: `Read CLAUDE.md, then docs/HANDOFF.md, then docs/local-setup.md. We are in full build mode.`

## The agent does these in its first session, each with Dourado's OK

1. Confirm `.claude/settings.json` deny rules match the path syntax Trailmates uses. Ask Dourado to have Kevin paste the deny block from `Documents\Trailmates\.claude\settings.json` if the syntax differs, and adopt that form.
2. Set the repo git identity:
   `git config user.name "Bryan Dourado"` and `git config user.email "firstventuregroupllc@gmail.com"`.
3. Create `.env` in the repo root, add it to `.gitignore`, and keep every key there.
4. Write the first memory files in the app's memory folder for this project: agent name, how to report to Dourado, one step at a time, no em dashes, the install rule.
5. Offer to install, in this order and only when needed: GitHub CLI, pandoc, Shopify CLI. Log each in `docs/installs.md`.
6. Create `.claude/skills/` with a `vc-` prefix convention. First candidates: `vc-site-audit` modeled on the Salvage Health audit skill in spirit, and `vc-compliance-check` that scans `public/` and `shopify-theme/` for forbidden product names, efficacy claims and the LegitScript badge state.
7. Optional, user level: a `~/.claude/agents/vale.md` file in the same shape as Maggie's, pointing at `CLAUDE.md` and `COMPLIANCE.md`. Only after Dourado agrees to a user-level file.

## What comes with the account automatically

Gmail, Google Drive, Calendar, Claude Docs, Canva and PostHog connectors, and the Anthropic stock skills. Kit, Metricool and Netlify are Salvage Health accounts; do not use them for Velacore. The Salvage Health account skills are off limits for Velacore work.

## Safe to reuse from the machine

The ig- Instagram drafting skills and the design skills in `~/.claude/skills/` are brand-neutral and already on the machine; they load for every project. Read `~/.claude/instagram/voice.md` only to confirm it is Salvage Health voice and leave it alone; write a Velacore voice file when social work starts.

## Not for this project

The earshot MCP server, the whisper and DeepFilterNet venvs, scrcpy, and everything under `Documents\Salvage Health\_tools`.
