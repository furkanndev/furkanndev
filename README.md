<div align="center">

<p align="center">
  <sub>THE ENGINEERING CHRONICLE &bull; VOL. 2026 &bull; AUTONOMOUS DISPATCH</sub>
</p>

# FURKAN GÜLTEKİN
### Software Developer &bull; Desktop Application Architect &bull; Systems Engineer

<p align="center">
  <a href="mailto:ffurkangltkn@gmail.com"><img src="https://img.shields.io/badge/Dispatch-ffurkangltkn%40gmail.com-0078D4?style=flat-square&logo=microsoftoutlook&logoColor=white" alt="Email" /></a>
  <a href="https://linkedin.com"><img src="https://img.shields.io/badge/Network-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/furkanndev"><img src="https://img.shields.io/badge/Archive-furkanndev-24292e?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Location-Turkey-gray?style=flat-square" alt="Location" />
  <img src="https://img.shields.io/badge/Status-Open%20to%20Engineering%20Roles-success?style=flat-square" alt="Status" />
</p>

</div>

---

> *"True software craftsmanship is not defined by the accumulation of frameworks, but by the precision with which code bridges the gap between hardware runtimes, low-level OS protocols, and seamless human utility."*

---

## Editor's Dispatch: The Engineering Profile

I am a **Software Developer** dedicated to building resilient desktop software architectures, systems programming, and high-performance automation solutions. Rather than treating operating systems, document standards, and network protocols as opaque black boxes, my work focuses on deep-level mechanics:

- **Low-Latency Runtimes:** Harnessing high-speed C-based document engines (PyMuPDF) and native C++ STL algorithms to achieve sub-millisecond execution.
- **Decoupled Architecture:** Enforcing strict boundaries between domain models and presentation layers across multi-assembly systems.
- **Turnkey Production:** Engineering end-to-end software—spanning architecture design, local OCR inference, automated Inno Setup 6 installer creation (`.exe`), and CI/CD pipelines.

**Academic Background:**  
Sakarya University *(Sakarya Üniversitesi)* &bull; Faculty of Computer and Information Sciences  
*Bachelor of Science in Information Systems Engineering (Bilişim Sistemleri Mühendisliği)*

---

## Feature Stories: Selected Engineering Works

### Feature I &bull; [AuraPDF](https://github.com/furkanndev/AuraPDF): The Architecture of a Modern Windows PDF Suite
**Core Stack:** `Python 3.10+` &bull; `PyQt6 / Qt` &bull; `PyMuPDF (C Engine)` &bull; `RapidOCR / ONNX` &bull; `Inno Setup 6` &bull; `PyInstaller`

AuraPDF was engineered to address a widespread deficiency in modern document productivity: mainstream PDF viewers are predominantly read-only, while full-featured editors are gatekept behind expensive subscriptions and cumbersome cloud uploads.

- **In-Page Text Mutation:** Integrates PyMuPDF's C-level canvas binding with PyQt6 to detect exact character boundary matrices, enabling live in-place font replacement, character editing, and text block reflow directly within rendered PDF pages.
- **Offline OCR Pipeline:** Incorporates local ONNX inference models via RapidOCR, allowing users to extract searchable text from scanned archival documents with zero external network transmission.
- **Document Management Toolbox:** In-memory multi-document merge, split, high-ratio compression, visual redaction, and cryptographic password encryption.
- **Automated Distribution Pipeline:** Turnkey Python build scripts that orchestrate PyInstaller compilation and Inno Setup 6 packaging to produce signed, standalone Windows setup installers (`.exe`).

---

### Feature II &bull; [Social-Saver](https://github.com/furkanndev/Social-Saver): Zero-Beacon Media Stream Interception
**Core Stack:** `Python` &bull; `Flask 3.x` &bull; `API Reverse Engineering` &bull; `Webview Cookie Engine` &bull; `Streaming ZIP Compression`

An archival research and media inspection utility engineered to stream and preserve ephemeral stories, highlights, and original-resolution profile avatars without triggering read-receipt telemetry.

- **Network-Level Telemetry Bypass:** Bypasses client-facing tracking beacons by intercepting raw edge CDN media streams directly (`seen = false`).
- **Automated Credential Ingestion:** Features an isolated browser window that captures authenticated session cookies and CSRF tokens automatically, writing them securely to local configuration without requiring manual devtools inspection.
- **High-Throughput Archival Pipeline:** An in-memory streaming ZIP packaging mechanism that bundles user media batches into instant downloadable archives with zero server-side disk bloat.

---

### Feature III &bull; Architectural Dispatches: Systems, Game Engines & Daemons

#### 1. [NavalStrike](https://github.com/furkanndev/NavalStrike) — Decoupled 2D Arcade Engine
* **The Architecture:** Developed in **C#** and **.NET**, this desktop arcade game enforces strict object-oriented design and SOLID principles by decoupling the core game engine (`Savas.Library`) from the Windows Forms presentation viewport (`Savas.Desktop`).
* **Design Patterns:** Implements interface-driven contracts (`IHareketEden`), polymorphic entity hierarchies, bounding-box collision detection, and persistent binary score leaderboards.

#### 2. [DirectoryChangeMonitorService](https://github.com/furkanndev/DirectoryChangeMonitorService) — Kernel-Level Filesystem Daemon
* **The Architecture:** An automated **Linux** background service written in **POSIX Bash** that audits filesystem directory mutations with zero CPU polling overhead.
* **Kernel Event Hooks:** Listens directly to the Linux kernel's `inotify` subsystem (`inotifywait`) across six POSIX event masks (`modify`, `attrib`, `close_write`, `move`, `create`, `delete`), packaged as a managed **systemd** service unit.

#### 3. [MatrixManipulator](https://github.com/furkanndev/MatrixManipulator) — High-Performance Linear Algebra Engine
* **The Architecture:** A high-speed **Modern C++17** utility implementing in-place coordinate scalar permutations ($A_{ij} \longleftrightarrow B_{ij}$) and classical matrix dot product calculations ($O(n^3)$).
* **Memory Bounds:** Enforces strict memory validation with zero dynamic heap reallocation overhead during permutations.

---

## The Technical Compendium

A structured index of technical disciplines, runtime environments, and tools utilized across engineering projects:

<table>
  <thead>
    <tr>
      <th width="28%">Discipline</th>
      <th>Technologies, Frameworks & Toolchain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Languages & Core Runtimes</b></td>
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
      <td><b>Desktop GUI & Native Frameworks</b></td>
      <td>
        <code>PyQt6 / PySide6 (Qt6 Core & Widgets)</code> &bull; 
        <code>Windows Forms</code> &bull; 
        <code>WPF / XAML</code> &bull; 
        <code>PyMuPDF (MuPDF C-Engine)</code> &bull; 
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
        <code>RESTful Architecture</code> &bull; 
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

## Code Telemetry & Development Cadence

<div align="center">
  <table border="0" width="100%">
    <tr>
      <td width="50%" align="center">
        <img src="https://github-readme-stats.vercel.app/api?username=furkanndev&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Metrics" width="100%" />
      </td>
      <td width="50%" align="center">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=furkanndev&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" width="100%" />
      </td>
    </tr>
  </table>
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

## Colophon & Communication Channels

Inquiries regarding desktop architecture, systems programming collaborations, or professional engineering opportunities may be directed via:

- **Electronic Mail:** [ffurkangltkn@gmail.com](mailto:ffurkangltkn@gmail.com)
- **Professional Network:** [linkedin.com/in/furkan-gultekin](https://linkedin.com)
- **Code Repository:** [github.com/furkanndev](https://github.com/furkanndev)
- **Location:** Turkey

<div align="center">
  <sub>Furkan Gültekin &bull; Software Developer &bull; Published via GitHub Profile Repository</sub>
</div>
