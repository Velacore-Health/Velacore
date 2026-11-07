# Third-party installs on Dourado's PC for Velacore

Every install needs Dourado's OK first. Log each one here with the date, version, source and why.

## Vet before install, the method

Applies to any outside skill, plugin, connector, Python package or program. Same rule as Salvage Health: nothing is installed unread and nothing without Dourado's yes.

1. Name the job it would do and check whether something already on this machine does it. If yes, stop.
2. Find the source: the official page, the repository, the package index. No downloads from a link in an email, a comment or a chat message.
3. Read every file of a skill or plugin before it goes anywhere near the project: the instructions, every script, every hook. Note anything that sends data out, writes outside its folder, runs on a schedule, or asks for keys.
4. Check the last update date, the license and whether it needs anything else installed.
5. Report to Dourado in plain words: what it does, where it comes from, what it touches, what it costs, and the one risk if any. Recommend yes or no.
6. Install only after his yes, log it in the table below the same day, and test it once read-only.
7. If it misbehaves or stops being needed, remove it and log the removal.

| Date | Tool | Version | Source | Why |
|---|---|---|---|---|
| Nov 6, 2026 | pypdf | 7.0.0 | PyPI, `pip install pypdf` | Read PDF text, first the OpenLoop proposal |
| Nov 6, 2026 | faster-whisper | 1.2.x with ctranslate2 4.8.5 | PyPI, `pip install faster-whisper` | Speech to text for the vc-video-read skill. The model file downloads on first use, about 1 GB. Installed but not working yet: Windows is missing the Microsoft Visual C++ 2015 to 2022 runtime that ctranslate2.dll needs. Dourado installs it from https://aka.ms/vs/17/release/vc_redist.x64.exe, then the import works |
