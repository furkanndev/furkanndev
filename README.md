# Furkan Gültekin
### Software Developer &bull; Systems Explorer &bull; Desktop Application Architect

<p align="left">
  <a href="mailto:ffurkangltkn@gmail.com"><img src="https://img.shields.io/badge/Email-ffurkangltkn%40gmail.com-0078D4?style=flat-square&logo=microsoftoutlook&logoColor=white" alt="Email" /></a>
  <a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Furkan%20Gültekin-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/furkanndev"><img src="https://img.shields.io/badge/GitHub-furkanndev-24292e?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Location-Turkey-gray?style=flat-square" alt="Location" />
  <img src="https://img.shields.io/badge/Focus-Desktop%20%26%20Systems%20Engineering-27272a?style=flat-square" alt="Focus" />
</p>

---

## The Philosophy: Demystifying the Black Box

I have always believed that great software engineering happens at the intersection of **low-level curiosity** and **end-user craftsmanship**. Rather than treating frameworks, operating systems, and network protocols as impenetrable black boxes, my passion lies in understanding how things operate under the hood:

- How memory pointers and coordinate matrices transform in memory.
- How binary document formats like PDF render in sub-second latency through low-level C bindings.
- How network streams can be inspected and leveraged without leaving traces.
- How standalone executables and background daemons can run reliably across diverse environments without external dependencies.

This mindset shapes everything I build: from lightweight Linux daemons to rich, multi-tabbed Windows productivity suites.

---

## The Engineering Journey

```text
2022 ──► Low-Level Foundations & Memory Concepts (C, C++, Data Structures, Linux)
2023 ──► Layered Architecture & Event-Driven Systems (C# .NET, Windows Forms, OOD)
2024 ──► Linux Kernel Internals & Daemons (Systemd, inotify Event Hooks, POSIX Scripting)
2025 ──► Desktop Architecture & Reverse Engineering (Python, PyQt6, PyMuPDF, Inno Setup)
2026 ──► Full-Lifecycle Product Engineering (AuraPDF Suite, Social-Saver, Standalone Releases)
```

### Academic & Foundational Roots
My engineering journey took root at **Sakarya University's Faculty of Computer and Information Sciences (Information Systems Engineering)**. Immersed in algorithms, object-oriented design, systems programming, and database theory, I sought to bridge academic rigor with real-world, deployable products.

---

## Deep Dives: Engineering Challenges & Solved Problems

### 1. In-Page PDF Text Mutation & Document Flow ([AuraPDF](https://github.com/furkanndev/AuraPDF))
* **The Challenge:** Most PDF readers treat documents as static, read-only raster canvases. Modifying embedded PDF text typically requires expensive cloud subscriptions or clunky external editors that corrupt layout coordinates.
* **The Solution:** Integrated **PyMuPDF's C-based rendering engine** with **PyQt6**, building an in-place canvas mutation editor. The system extracts exact character bounding boxes, renders interactive overlay widgets, and reflows mutated text blocks back into the PDF content stream while preserving document integrity.
* **The Packaging:** Configured automated build pipelines with **Inno Setup 6** and **PyInstaller**, creating single-click, self-contained Windows installers (`.exe`) with native theme adapters and embedded local ONNX OCR models.

### 2. Zero-Beacon CDN Interception & Session Automation ([Social-Saver](https://github.com/furkanndev/Social-Saver))
* **The Challenge:** Viewing and archiving high-bitrate ephemeral stories without triggering user-facing "seen" telemetry beacons.
* **The Solution:** Reverse-engineered web endpoints to isolate raw CDN media streams directly. Developed a lightweight embedded webview that intercepts active session credentials and CSRF tokens automatically, pairing it with an in-memory streaming ZIP compression engine for bulk media export.

### 3. Non-Polling Filesystem Change Auditing ([DirectoryChangeMonitorService](https://github.com/furkanndev/DirectoryChangeMonitorService))
* **The Challenge:** Auditing filesystem directory changes on Linux without wasting CPU cycles through continuous file polling loops.
* **The Solution:** Leveraged the Linux kernel's native `inotify` subsystem (`inotifywait`) across specific event masks (`modify`, `attrib`, `close_write`, `move`, `create`, `delete`), wrapping the loop in a fully managed `systemd` daemon unit featuring boot autostart and persistent journal logging.

---

## Comprehensive Technical Matrix

<table>
  <thead>
    <tr>
      <th width="28%">Engineering Domain</th>
      <th>Technologies, Frameworks & Tooling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Languages & Runtimes</b></td>
      <td>
        <code>Python 3.10+</code> &bull; 
        <code>C# (.NET 8 / .NET Framework)</code> &bull; 
        <code>Modern C++ (C++17 / C++20)</code> &bull; 
        <code>C (POSIX)</code> &bull; 
        <code>TypeScript</code> &bull; 
        <code>JavaScript (ES6+)</code> &bull; 
        <code>Bash / POSIX Shell</code> &bull; 
        <code>SQL</code>
      </td>
    </tr>
    <tr>
      <td><b>Desktop & GUI Development</b></td>
      <td>
        <code>PyQt6 / PySide6 (Qt6 Core & Widgets)</code> &bull; 
        <code>Windows Forms</code> &bull; 
        <code>WPF / XAML</code> &bull; 
        <code>PyMuPDF (High-speed MuPDF C-Engine)</code> &bull; 
        <code>RapidOCR / ONNX Runtime</code> &bull; 
        <code>Win32 API Interop</code>
      </td>
    </tr>
    <tr>
      <td><b>Backend, APIs & Web Services</b></td>
      <td>
        <code>Flask</code> &bull; 
        <code>FastAPI</code> &bull; 
        <code>Node.js / Express</code> &bull; 
        <code>RESTful API Design</code> &bull; 
        <code>WebSockets</code> &bull; 
        <code>BeautifulSoup4 / DOM Scraping</code> &bull; 
        <code>Bootstrap 5</code> &bull; 
        <code>TailwindCSS</code>
      </td>
    </tr>
    <tr>
      <td><b>Systems, Daemons & Automation</b></td>
      <td>
        <code>Linux Systemd Background Daemons</code> &bull; 
        <code>Linux Kernel inotify Real-time Hooks</code> &bull; 
        <code>API Reverse Engineering</code> &bull; 
        <code>Zero-Beacon CDN Stream Interception</code> &bull; 
        <code>Multi-threading & Asynchronous I/O</code> &bull; 
        <code>Subprocess Orchestration</code>
      </td>
    </tr>
    <tr>
      <td><b>Packaging, Build Systems & CI/CD</b></td>
      <td>
        <code>Inno Setup 6 (Automated Scripted Installers)</code> &bull; 
        <code>PyInstaller Spec Automation</code> &bull; 
        <code>GitHub Actions (CI/CD Pipelines)</code> &bull; 
        <code>Docker</code> &bull; 
        <code>MSBuild / Visual Studio Toolchain</code> &bull; 
        <code>GCC / Clang Toolchains</code> &bull; 
        <code>Postman</code>
      </td>
    </tr>
    <tr>
      <td><b>Databases & Persistence</b></td>
      <td>
        <code>PostgreSQL</code> &bull; 
        <code>SQLite</code> &bull; 
        <code>Microsoft SQL Server</code> &bull; 
        <code>MongoDB</code> &bull; 
        <code>Redis</code> &bull; 
        <code>Atomic JSON Serialization & Binary File I/O</code>
      </td>
    </tr>
  </tbody>
</table>

---

## Selected Engineering Works

| Project | Focus | Architecture & Key Deliverables |
| :--- | :--- | :--- |
| **[AuraPDF](https://github.com/furkanndev/AuraPDF)** | Desktop PDF Productivity Suite | Multi-tabbed PyQt6 interface, C-engine PyMuPDF rendering, in-place text mutation, local ONNX OCR, and single-click Windows `.exe` installer via Inno Setup 6. |
| **[Social-Saver](https://github.com/furkanndev/Social-Saver)** | Media Archival & Extraction Engine | Direct CDN stream extraction without read-receipt beacons (`seen = false`), automated session token capture, and streaming ZIP compression. |
| **[NavalStrike](https://github.com/furkanndev/NavalStrike)** | Decoupled 2D Arcade Game Engine | Strict object-oriented design separating domain library (`Savas.Library`) from presentation (`Savas.Desktop`), interface contracts (`IHareketEden`), and persistent scoring. |
| **[DirectoryChangeMonitor](https://github.com/furkanndev/DirectoryChangeMonitorService)** | Linux Filesystem Auditing Daemon | Kernel-hooked event loops via `inotifywait` tracking POSIX filesystem operations under a fully managed `systemd` service unit. |
| **[MatrixManipulator](https://github.com/furkanndev/MatrixManipulator)** | Linear Algebra Permutations | Modern C++17 utility executing in-place scalar coordinate permutations and classical matrix dot product calculations with strict memory safety. |

---

## My Core Engineering Principles

1. **End-to-End Shipping (The Final 10% Matters Most):** Writing code that runs in a local IDE is only half the battle. A project is truly complete when it is packaged with automated installers, documented with clarity, and immediately accessible to end users without environment friction.
2. **Decoupled Architecture:** Business and domain logic should never be tightly coupled to presentation layers. Modular interfaces ensure that core engines survive UI paradigm shifts.
3. **Respect for System Resources:** Efficiency is not optional. Minimizing RAM footprints, avoiding needless polling loops, and leveraging native C/C++ libraries ensure responsive, low-latency applications.

---

## GitHub Activity & Development Cadence

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=furkanndev&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Metrics" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=furkanndev&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" width="45%" />
</div>

<div align="center" style="margin-top: 14px;">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=furkanndev&theme=tokyonight&hide_border=true&background=0d1117" alt="Streak Analysis" width="95%" />
</div>

<br/>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake.svg">
    <img alt="Contribution Snake Graph" src="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake.svg" width="100%" />
  </picture>
</div>

---

## Connect & Collaborate

I am always interested in discussing desktop software architecture, systems programming, and high-impact software engineering opportunities.

- **Email:** [ffurkangltkn@gmail.com](mailto:ffurkangltkn@gmail.com)
- **LinkedIn:** [linkedin.com/in/furkan-gultekin](https://linkedin.com)
- **GitHub:** [github.com/furkanndev](https://github.com/furkanndev)
- **Education:** Sakarya University &bull; B.S. in Information Systems Engineering
