#!/usr/bin/env python3
"""
Furkan Gültekin Profile — Autonomous Live Version & Repository Synchronizer
Fetches public repository releases, tags, and telemetry from GitHub API
and updates README.md dynamically while preserving 100% of the UI design and layout.
"""

import os
import re
import sys
import json
import urllib.request
from pathlib import Path
from typing import Dict, Any, List, Optional, Set

USERNAME = "furkanndev"
HIDDEN_REPOS: Set[str] = {USERNAME.lower(), f"{USERNAME.lower()}.github.io"}

# Hand-crafted architecture & domain metadata preserved across syncs
CURATED_PROJECTS: Dict[str, Dict[str, str]] = {
    "AuraPDF": {
        "display_name": "AuraPDF Pro",
        "domain": "FLAGSHIP",
        "stack": "`Python 3.10+`<br>`PyQt6` `PyMuPDF`<br>`Inno Setup 6`",
        "desc": "Direct in-page text editing, sandwich OCR, AcroForms, Word/Excel export, standalone `.exe`."
    },
    "KeyStone": {
        "display_name": "Keystone",
        "domain": "FLAGSHIP",
        "stack": "`Python 3.11+`<br>`PyQt6` `Win32`<br>`Winget` `PyInstaller`",
        "desc": "140+ silent package deployment, live registry optimization rollback, backup & migration manifests."
    },
    "Social-Saver": {
        "display_name": "Social-Saver",
        "domain": "SYSTEMS",
        "stack": "`Python` `Flask 3.x`<br>`Reverse Eng` `Webview`",
        "desc": "100% anonymous CDN extraction (`seen = false`), automated session token capture, bulk `.zip` export."
    },
    "DirectoryChangeMonitorService": {
        "display_name": "DirectoryChangeMonitor",
        "domain": "DAEMON",
        "stack": "`Bash 4+` `Systemd`<br>`Linux inotify`",
        "desc": "Zero-polling kernel event loops via `inotifywait`, atomic audit logging across 6 POSIX event masks."
    },
    "NavalStrike": {
        "display_name": "NavalStrike",
        "domain": "ARCADE",
        "stack": "`C#` `.NET`<br>`WinForms` `OOP`",
        "desc": "Decoupled domain engine (`Savas.Library`) and presentation UI, interface contracts, 60 FPS loop."
    },
    "HiddenObjectsGame": {
        "display_name": "HiddenObjectsGame",
        "domain": "TACTICAL",
        "stack": "`C#` `.NET`<br>`Procedural` `ANSI`",
        "desc": "Dynamic 20x20 Cartesian grid, algorithmic collision-free object seeding, color-coded fog of war."
    },
    "MatrixManipulator": {
        "display_name": "MatrixManipulator",
        "domain": "ALGORITHMS",
        "stack": "`Modern C++17`<br>`STL` `Algorithms`",
        "desc": "Randomized 5x5 square matrix generation, in-place coordinate swaps ($A_{ij} \\longleftrightarrow B_{ij}$), dot products ($O(n^3)$)."
    },
    "DealerDistribution": {
        "display_name": "DealerDistribution",
        "domain": "SIMULATION",
        "stack": "`C++` `Pointers`<br>`File I/O` `Streams`",
        "desc": "Memory address pointer tracking with structured file serialization (`orders.txt`), randomized dealer traversal."
    },
    "BusPassengerAllocation": {
        "display_name": "BusPassengerAllocation",
        "domain": "STRUCTURES",
        "stack": "`C` `GCC`<br>`Stack & List`",
        "desc": "Sequential row-by-row seating allocation across dynamic multi-bus quotas (up to 8 buses), manifests."
    },
    "IEEE754-Converter": {
        "display_name": "IEEE754-Converter",
        "domain": "LOW-LEVEL",
        "stack": "`C` `Bitwise`<br>`Computer Systems`",
        "desc": "Single (32-bit float) and double (64-bit double) precision IEEE 754 bitwise extraction & synthesis."
    }
}

def github_get(url: str, token: Optional[str] = None) -> Any:
    headers = {
        "User-Agent": "furkanndev-profile-sync",
        "Accept": "application/vnd.github+json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            print(f"[!] GitHub API rate limit ({e.code}) on: {url}")
        return None
    except Exception as e:
        print(f"[!] Request error: {e} on: {url}")
        return None

def clean_version(raw_tag: str) -> str:
    cleaned = re.sub(r'^(pro|basic)[_-]?', '', raw_tag.strip(), flags=re.IGNORECASE)
    if not cleaned.lower().startswith('v'):
        cleaned = f"v{cleaned}"
    return cleaned

def extract_fallback_versions(content: str) -> Dict[str, str]:
    fallback = {"AuraPDF": "v2.2.7", "KeyStone": "v3.0.2"}
    m_aura = re.search(r'AURAPDF PRO\s+(v[\d\.]+)', content, re.IGNORECASE)
    if m_aura:
        fallback["AuraPDF"] = m_aura.group(1)
    m_key = re.search(r'KEYSTONE WORKSTATION DEPLOYMENT\s+(v[\d\.]+)', content, re.IGNORECASE)
    if m_key:
        fallback["KeyStone"] = m_key.group(1)
    return fallback

def replace_between_markers(content: str, marker_name: str, new_inner: str, inline: bool = False, indent: str = "") -> str:
    start_tag = f"<!-- {marker_name}:START -->"
    end_tag = f"<!-- {marker_name}:END -->"
    s_idx = content.find(start_tag)
    e_idx = content.find(end_tag)
    if s_idx == -1 or e_idx == -1:
        return content
    if inline:
        return content[:s_idx + len(start_tag)] + new_inner.strip() + content[e_idx:]
    return content[:s_idx + len(start_tag)] + "\n" + new_inner + "\n" + indent + content[e_idx:]

def build_broadcast_tape(aurapdf_ver: str, keystone_ver: str) -> str:
    return (
        f"    <code>● BROADCAST TAPE:</code>\n"
        f"    <code>AURAPDF PRO {aurapdf_ver}</code> &bull;\n"
        f"    <code>KEYSTONE WORKSTATION DEPLOYMENT {keystone_ver}</code> &bull;\n"
        f"    <code>IN-PAGE PDF CANVAS ENGINE</code> &bull;\n"
        f"    <code>WIN32 REGISTRY HOOKS</code> &bull;\n"
        f"    <code>SANDWICH OCR</code> &bull;\n"
        f"    <code>LINUX INOTIFY DAEMON</code> &bull;\n"
        f"    <code>REVERSE-ENGINEERED CDN EXTRACTION</code> &bull;\n"
        f"    <code>C++17 COORDINATE ALGORITHMS</code>"
    )

def build_currently_table(aurapdf_ver: str, keystone_ver: str) -> str:
    return (
        "| Signal | Focus Area | What's Shipped & Active |\n"
        "| :---: | :--- | :--- |\n"
        f"| `[LIVE]` | **[AuraPDF Pro {aurapdf_ver}](https://github.com/furkanndev/AuraPDF)** | Standalone installer (`.exe`) deployed via Inno Setup 6; verified on-canvas direct text mutation, coordinate-aligned sandwich OCR, and AcroForm fill/serialization pipelines. |\n"
        f"| `[STABLE]` | **[Keystone Suite {keystone_ver}](https://github.com/furkanndev/KeyStone)** | Finalized curated 140+ software package database, real-time registry state validator (`HKCU`/`HKLM`), and automated workstation migration manifests. |\n"
        "| `[ACTIVE]` | **[Social-Saver](https://github.com/furkanndev/Social-Saver)** | Zero-receipt CDN stream interceptor (`seen = false`) with automated webview session token persistence and in-memory streaming `.zip` exporter. |\n"
        "| `[DAEMON]` | **[DirectoryChangeMonitor](https://github.com/furkanndev/DirectoryChangeMonitorService)** | Supervised Linux systemd background daemon auditing filesystem mutations with zero polling overhead via kernel `inotifywait`. |"
    )

def build_works_table(repos: List[Dict[str, Any]]) -> str:
    header = (
        "| Index | Repository & Domain | Core Stack | Key Capabilities & Architecture |\n"
        "| :---: | :--- | :--- | :--- |\n"
    )
    rows = []
    idx = 1
    # 1. Curated projects first to maintain signature layout
    for name, c in CURATED_PROJECTS.items():
        idx_str = f"{idx:02d}"
        row = f"| `{idx_str}` | **[{c['display_name']}](https://github.com/{USERNAME}/{name})**<br><code>{c['domain']}</code> | {c['stack']} | {c['desc']} |"
        rows.append(row)
        idx += 1

    # 2. Automatically append any new public repository created by Furkan
    seen_names = set(CURATED_PROJECTS.keys())
    for r in repos:
        name = r["name"]
        if name in seen_names:
            continue
        idx_str = f"{idx:02d}"
        lang_str = f"`{r['language']}`" if r.get("language") else "`Multi-Stack`"
        stack_str = f"{lang_str}<br><code>GitHub</code>"
        desc = r.get("description") or "Public repository."
        desc = desc.replace("\n", " ").replace("|", "\\|")
        row = f"| `{idx_str}` | **[{name}](https://github.com/{USERNAME}/{name})**<br><code>PROJECT</code> | {stack_str} | {desc} |"
        rows.append(row)
        idx += 1

    return header + "\n".join(rows)

def build_telemetry_stats(total_repos: int, langs_count: int) -> str:
    return (
        f"    <code>{total_repos} REPOSITORIES</code> &bull;\n"
        f"    <code>2 PRODUCTION FLAGSHIPS</code> &bull;\n"
        f"    <code>{langs_count} CORE LANGUAGES</code> &bull;\n"
        f"    <code>100% OFFLINE PRIVACY</code>"
    )

def ensure_markers_installed(content: str) -> str:
    """Injects boundary comment markers if absent, strictly preserving visual rendering."""
    updated = content

    # 1. Broadcast Tape
    if "<!-- BROADCAST_TAPE:START -->" not in updated:
        tape_re = r"(<div align=\"center\">\s*<sub>\s*\n)([\s\S]*?<code>● BROADCAST TAPE:</code>[\s\S]*?)(</code>\s*\n\s*</sub>\s*\n</div>)"
        def tape_sub(m):
            return f"{m.group(1)}    <!-- BROADCAST_TAPE:START -->\n{m.group(2)}{m.group(3).split('</code>')[0]}</code>\n    <!-- BROADCAST_TAPE:END -->\n  </sub>\n</div>"
        updated = re.sub(tape_re, tape_sub, updated, count=1)

    # 2. Currently Table
    if "<!-- CURRENTLY:START -->" not in updated:
        curr_re = r"(### `01 · CURRENTLY` &mdash; What's Happening Now\s*\n\n)(\| Signal \| Focus Area[\s\S]*?)(?=\n\n---)"
        def curr_sub(m):
            return f"{m.group(1)}<!-- CURRENTLY:START -->\n{m.group(2).strip()}\n<!-- CURRENTLY:END -->"
        updated = re.sub(curr_re, curr_sub, updated, count=1)

    # 3. Works Count
    if "<!-- WORKS_COUNT:START -->" not in updated:
        count_re = r"(### `03 · WORKS` &mdash; Things I've Built \()All \d+ Repositories(\))"
        updated = re.sub(count_re, r"\g<1><!-- WORKS_COUNT:START -->All 10 Repositories<!-- WORKS_COUNT:END -->\g<2>", updated, count=1)

    # 4. Works Table
    if "<!-- WORKS_TABLE:START -->" not in updated:
        works_re = r"(### `03 · WORKS` &mdash; Things I've Built[^\n]*\n\n)(\| Index \| Repository & Domain[\s\S]*?)(?=\n\n---)"
        def works_sub(m):
            return f"{m.group(1)}<!-- WORKS_TABLE:START -->\n{m.group(2).strip()}\n<!-- WORKS_TABLE:END -->"
        updated = re.sub(works_re, works_sub, updated, count=1)

    # 5. Telemetry
    if "<!-- TELEMETRY_STATS:START -->" not in updated:
        telem_re = r"(### `05 · TELEMETRY` &mdash; Analytics & Radar\s*\n\n<div align=\"center\">\s*<sub>\s*\n)([\s\S]*?)(</sub>\s*\n</div>)"
        def telem_sub(m):
            return f"{m.group(1)}    <!-- TELEMETRY_STATS:START -->\n{m.group(2).rstrip()}\n    <!-- TELEMETRY_STATS:END -->\n  {m.group(3)}"
        updated = re.sub(telem_re, telem_sub, updated, count=1)

    return updated

def sync(readme_path: Path, token: Optional[str] = None) -> bool:
    if not readme_path.exists():
        print(f"[!] Error: {readme_path} does not exist.")
        return False

    content = readme_path.read_text(encoding="utf-8")
    content = ensure_markers_installed(content)
    fallback_versions = extract_fallback_versions(content)

    print(f"[*] Fetching repository metadata for @{USERNAME}...")
    repos_data = github_get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=pushed", token)

    project_repos = []
    versions = dict(fallback_versions)
    languages = {"Python", "C#", "C++", "C"}

    if repos_data and isinstance(repos_data, list):
        for r in repos_data:
            if r.get("fork"):
                continue
            name = r["name"]
            if name.lower() in HIDDEN_REPOS:
                continue

            rel = github_get(f"https://api.github.com/repos/{USERNAME}/{name}/releases/latest", token)
            tag = None
            if rel and isinstance(rel, dict) and rel.get("tag_name"):
                tag = rel["tag_name"]
            else:
                tags = github_get(f"https://api.github.com/repos/{USERNAME}/{name}/tags?per_page=1", token)
                if tags and isinstance(tags, list) and len(tags) > 0:
                    tag = tags[0].get("name")

            if tag:
                versions[name] = clean_version(tag)

            if r.get("language"):
                languages.add(r["language"])

            project_repos.append({
                "name": name,
                "version": versions.get(name),
                "language": r.get("language"),
                "description": r.get("description") or "",
                "stars": r.get("stargazers_count", 0),
                "url": r.get("html_url")
            })
    else:
        print("[!] GitHub API repositories not available (rate limited or offline). Using baseline.")
        for name, c in CURATED_PROJECTS.items():
            project_repos.append({"name": name, "language": None, "description": c["desc"]})

    # Ensure latest verified release tags for flagships
    if "AuraPDF" not in versions or versions["AuraPDF"] == "v2.2.4":
        versions["AuraPDF"] = "v2.2.7"
    if "KeyStone" not in versions or versions["KeyStone"] == "v2.0.1":
        versions["KeyStone"] = "v3.0.2"

    aurapdf_ver = versions.get("AuraPDF", "v2.2.7")
    keystone_ver = versions.get("KeyStone", "v3.0.2")
    total_repos = max(len(project_repos), len(CURATED_PROJECTS))
    core_langs = max(4, len(languages))

    print(f"[*] AuraPDF: {aurapdf_ver}")
    print(f"[*] KeyStone: {keystone_ver}")
    print(f"[*] Project Repositories: {total_repos}")
    print(f"[*] Core Languages: {core_langs}")

    updated = content
    updated = replace_between_markers(updated, "BROADCAST_TAPE", build_broadcast_tape(aurapdf_ver, keystone_ver), indent="    ")
    updated = replace_between_markers(updated, "CURRENTLY", build_currently_table(aurapdf_ver, keystone_ver))
    updated = replace_between_markers(updated, "WORKS_COUNT", f"All {total_repos} Repositories", inline=True)
    updated = replace_between_markers(updated, "WORKS_TABLE", build_works_table(project_repos))
    updated = replace_between_markers(updated, "TELEMETRY_STATS", build_telemetry_stats(total_repos, core_langs), indent="    ")

    if updated != content:
        readme_path.write_text(updated, encoding="utf-8")
        print("[+] README.md successfully synchronized and saved.")
        return True
    else:
        print("[=] README.md is already up to date. No changes needed.")
        return False

if __name__ == "__main__":
    target = Path("profile-repo/README.md")
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
    token = os.environ.get("GITHUB_TOKEN")
    sync(target, token)
