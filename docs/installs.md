# Third-party installs on Dourado's PC for Velacore

Every install needs Dourado's OK first. Log each one here with the date, version, source and why.

| Date | Tool | Version | Source | Why |
|---|---|---|---|---|
| Nov 6, 2026 | pypdf | 7.0.0 | PyPI, `pip install pypdf` | Read PDF text, first the OpenLoop proposal |
| Nov 6, 2026 | faster-whisper | 1.2.x with ctranslate2 4.8.5 | PyPI, `pip install faster-whisper` | Speech to text for the vc-video-read skill. The model file downloads on first use, about 1 GB. Installed but not working yet: Windows is missing the Microsoft Visual C++ 2015 to 2022 runtime that ctranslate2.dll needs. Dourado installs it from https://aka.ms/vs/17/release/vc_redist.x64.exe, then the import works |
