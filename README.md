<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,11,20&height=210&section=header&text=Furkan%20G%C3%BCltekin&fontSize=42&fontAlignY=38&desc=Software%20Developer%20%7C%20Desktop%20Architecture%20%E2%80%A2%20Systems%20%E2%80%A2%20Automation&descAlignY=62&descAlign=50" width="100%" alt="Header Banner" />
</div>

<div align="center">

  [![Email](https://img.shields.io/badge/Email-ffurkangltkn%40gmail.com-27272a?style=flat-square&logo=gmail&logoColor=white)](mailto:ffurkangltkn@gmail.com)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Furkan%20Gültekin-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com)
  [![GitHub Followers](https://img.shields.io/github/followers/furkanndev?label=Followers&style=flat-square&logo=github&color=27272a)](https://github.com/furkanndev?tab=followers)
  [![Profile Views](https://komarev.com/ghpvc/?username=furkanndev&label=Profile%20Views&color=27272a&style=flat-square)](https://github.com/furkanndev)

</div>

<p align="center">
  <a href="#about-me">About</a> •
  <a href="#engineering-philosophy">Engineering Philosophy</a> •
  <a href="#selected-projects">Selected Works</a> •
  <a href="#technical-competencies">Technical Matrix</a> •
  <a href="#github-analytics">Analytics</a> •
  <a href="#contribution-activity">Activity</a>
</p>

---

### About Me

I am **Furkan Gültekin**, a **Software Developer** focused on desktop application architecture, low-level systems programming, and high-performance automation tools. My work centers on delivering production-ready, self-contained software—spanning algorithmic design, reactive user interfaces, and automated distribution pipelines.

- **Active Development:** Creator and core maintainer of **[AuraPDF](https://github.com/furkanndev/AuraPDF)**, an extensible Windows desktop PDF platform featuring OCR and in-place document manipulation.
- **Core Domain:** Desktop software engineering (PyQt6/Qt, C#/.NET, modern C++), API reverse engineering, and background daemon services.
- **Full Lifecycle Engineering:** System design, asynchronous programming, custom standalone packaging (`.exe` via Inno Setup / PyInstaller), and CI/CD automation.

---

### Engineering Philosophy

- **Performance-First Design:** Leveraging high-speed engines (PyMuPDF, C++ STL) to ensure sub-millisecond responsiveness and minimal memory footprints.
- **Layered Architecture:** Strict separation of concern across domain models, business logic, and presentation layers (demonstrated in decoupled multi-assembly architectures).
- **Self-Contained Deployment:** Engineering turnkey applications with integrated dependency bundling, local configuration management, and zero manual setup for end-users.

---

### Selected Projects

#### 1. [AuraPDF](https://github.com/furkanndev/AuraPDF) — Modern Windows Desktop PDF Suite
> *Python • PyQt6 / Qt • PyMuPDF • RapidOCR / ONNX • PyInstaller • Inno Setup 6*

A multi-tabbed, lightweight Windows desktop application designed to solve complex PDF manipulation workflows without cloud dependencies.
- **Direct Page Text Editing:** In-place selection, mutation, re-fonting, and visual reflow directly within PDF pages.
- **Integrated OCR Engine:** Local scanned document text extraction powered by RapidOCR ONNX inference models.
- **PDF Toolbox:** Multi-file merge, split, high-efficiency compression, redaction, and encryption.
- **Automated Packaging:** Custom Python build orchestration generating signed Inno Setup installers (`.exe`).

#### 2. [Social-Saver](https://github.com/furkanndev/Social-Saver) — Anonymous Media Pipeline & Session Engine
> *Python • Flask • Reverse Engineering • Webview Authentication • Streaming Compression*

A desktop utility engineered to stream and archive full-resolution profile media and ephemeral stories anonymously.
- **Zero-Beacon Streaming:** Intercepts raw CDN media endpoints directly, preventing read-receipt triggers (`seen = false`).
- **Automated Authentication:** Lightweight embedded viewport intercepts and serializes active session cookies directly to disk.
- **Archive Pipeline:** High-throughput streaming ZIP packaging for instant bulk story downloads.

#### 3. [NavalStrike](https://github.com/furkanndev/NavalStrike) — Decoupled 2D Arcade Game Engine
> *C# • .NET • Windows Forms • Object-Oriented Design (OOD)*

A naval combat arcade simulation built to demonstrate strict object-oriented design and event-driven patterns.
- **Clean Decoupled Architecture:** Complete separation between the domain logic library (`Savas.Library`) and presentation layer (`Savas.Desktop`).
- **OOP Design:** Interface-driven contracts (`IHareketEden`), polymorphic entity hierarchies, and collision detection algorithms.
- **Persistent Leaderboard:** File-backed binary/text score persistence and dynamic difficulty scaling.

#### 4. [DirectoryChangeMonitorService](https://github.com/furkanndev/DirectoryChangeMonitorService) — Kernel-Level Linux Auditing Daemon
> *Bash • Linux Kernel inotify • Systemd • Shell Automation*

A background daemon service that audits real-time Linux filesystem mutations using zero-polling kernel event loops.
- **Kernel Event Trapping:** Direct listener leveraging `inotifywait` event masks (`modify`, `create`, `move`, `delete`, `attrib`).
- **Systemd Supervisor:** Complete unit specification for automatic boot startup, crash recovery, and journal logging.

#### 5. [MatrixManipulator](https://github.com/furkanndev/MatrixManipulator) — Linear Algebra & Transformation Engine
> *Modern C++17 • Standard Template Library (STL) • Algorithmic Optimization*

A high-performance C++ utility implementing matrix transformations and algebraic algorithms.
- **Matrix Operations:** In-place coordinate scalar permutations and classical matrix dot product computations ($O(n^3)$).
- **Memory Safety:** Validated bounds checking and clean modular procedural design.

---

### Technical Competencies

<table>
  <tr>
    <td width="24%"><b>Systems & Languages</b></td>
    <td>
      <code>Python 3.10+</code> &bull; 
      <code>C# (.NET)</code> &bull; 
      <code>C++ (Modern C++17)</code> &bull; 
      <code>C</code> &bull; 
      <code>Bash / Shell</code> &bull; 
      <code>TypeScript</code> &bull; 
      <code>JavaScript</code> &bull; 
      <code>SQL</code>
    </td>
  </tr>
  <tr>
    <td width="24%"><b>GUI & Desktop Frameworks</b></td>
    <td>
      <code>PyQt6 / PySide6</code> &bull; 
      <code>Qt Core & Widgets</code> &bull; 
      <code>.NET Windows Forms</code> &bull; 
      <code>Flask</code> &bull; 
      <code>PyMuPDF</code> &bull; 
      <code>RapidOCR / ONNX</code>
    </td>
  </tr>
  <tr>
    <td width="24%"><b>DevOps, Build & Automation</b></td>
    <td>
      <code>Inno Setup 6</code> &bull; 
      <code>PyInstaller</code> &bull; 
      <code>Git & GitHub Actions (CI/CD)</code> &bull; 
      <code>Docker</code> &bull; 
      <code>Linux Daemons (Systemd)</code> &bull; 
      <code>REST APIs</code>
    </td>
  </tr>
  <tr>
    <td width="24%"><b>Storage & Persistence</b></td>
    <td>
      <code>SQLite</code> &bull; 
      <code>PostgreSQL</code> &bull; 
      <code>Microsoft SQL Server</code> &bull; 
      <code>JSON / File I/O</code>
    </td>
  </tr>
</table>

---

### GitHub Analytics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=furkanndev&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117" alt="GitHub Metrics" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=furkanndev&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117" alt="Top Languages" width="45%" />
</div>

<div align="center" style="margin-top: 14px;">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=furkanndev&theme=tokyonight&hide_border=true&background=0d1117" alt="Streak Analysis" width="95%" />
</div>

---

### Contribution Activity

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake.svg">
    <img alt="GitHub Contribution Snake Graph" src="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake.svg" width="100%" />
  </picture>
</div>

---

<div align="center">
  <sub>Furkan Gültekin &bull; Software Developer &bull; Clean Code & Systems Architecture</sub>
</div>
