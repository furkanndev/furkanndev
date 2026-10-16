# Furkan Gültekin
### Software Developer &bull; Desktop Application Architecture &bull; Systems & Automation

<p align="left">
  <a href="mailto:ffurkangltkn@gmail.com"><img src="https://img.shields.io/badge/Email-ffurkangltkn%40gmail.com-0078D4?style=flat-square&logo=microsoftoutlook&logoColor=white" alt="Email" /></a>
  <a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/furkanndev"><img src="https://img.shields.io/badge/GitHub-furkanndev-24292e?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Location-Turkey-gray?style=flat-square" alt="Location" />
  <img src="https://img.shields.io/badge/Status-Open%20to%20Opportunities-success?style=flat-square" alt="Status" />
</p>

---

## Executive Summary

Results-driven **Software Developer** with a strong foundation in desktop application architecture, systems programming, and workflow automation. Experienced in engineering standalone, production-ready desktop software from scratch using **Python (PyQt6 / PySide6)**, **C# (.NET)**, and **Modern C++**. 

Demonstrated track record of delivering complete software lifecycles—from low-latency document rendering and local OCR inference to API reverse engineering, multi-threaded event pipelines, and automated standalone Windows installer creation (`.exe` via Inno Setup 6). Committed to clean architecture, modular object-oriented design, and predictable deployment.

---

## Core Competencies & Technical Skills

<table>
  <tbody>
    <tr>
      <td width="28%"><b>Programming Languages</b></td>
      <td>
        <code>Python 3.10+</code> &bull; 
        <code>C# (.NET 8 / .NET Framework)</code> &bull; 
        <code>Modern C++ (C++17 / C++20)</code> &bull; 
        <code>C</code> &bull; 
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
        <code>PyMuPDF (MuPDF C-Engine)</code> &bull; 
        <code>RapidOCR / ONNX Runtime</code> &bull; 
        <code>Windows API (Win32) Integration</code>
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
        <code>Web Scraping & DOM Parsing</code> &bull; 
        <code>HTML5 / CSS3</code> &bull; 
        <code>Bootstrap 5</code> &bull; 
        <code>TailwindCSS</code>
      </td>
    </tr>
    <tr>
      <td><b>Systems & Automation</b></td>
      <td>
        <code>Linux Systemd Background Daemons</code> &bull; 
        <code>Kernel inotify Real-time Auditing</code> &bull; 
        <code>Network Stream Analysis & Reverse Engineering</code> &bull; 
        <code>Multi-threading & Asynchronous I/O</code> &bull; 
        <code>Subprocess Orchestration</code>
      </td>
    </tr>
    <tr>
      <td><b>Packaging, Tooling & CI/CD</b></td>
      <td>
        <code>Inno Setup 6 (Automated Scripted Installers)</code> &bull; 
        <code>PyInstaller Spec Automation</code> &bull; 
        <code>Git / GitHub Actions CI/CD</code> &bull; 
        <code>Docker</code> &bull; 
        <code>MSBuild / Visual Studio</code> &bull; 
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
        <code>Structured File I/O & JSON Serialization</code>
      </td>
    </tr>
  </tbody>
</table>

---

## Featured Software Projects

### 1. [AuraPDF](https://github.com/furkanndev/AuraPDF) — Comprehensive Windows Desktop PDF Suite
**Role:** Creator & Lead Developer &bull; **Technologies:** `Python 3.10+`, `PyQt6 / Qt`, `PyMuPDF`, `RapidOCR / ONNX`, `Inno Setup 6`, `PyInstaller`
- Engineered a lightweight, multi-tabbed desktop PDF application providing full document lifecycle management without cloud reliance.
- Built real-time **in-page text editing**, font mutation, and reflow capabilities directly within the rendered document canvas.
- Integrated an offline **OCR pipeline** utilizing ONNX inference for scanned document text extraction.
- Implemented comprehensive document operations: multi-file merging, splitting, PDF compression, redaction, and encryption.
- Automated end-to-end packaging with **Inno Setup 6** to produce signed, single-click Windows installers (`.exe`).

### 2. [Social-Saver](https://github.com/furkanndev/Social-Saver) — Media Stream Extraction & Archival Tool
**Role:** Lead Developer &bull; **Technologies:** `Python`, `Flask`, `API Reverse Engineering`, `Automated Webview`, `Streaming Compression`
- Designed an archival utility to stream and save original-resolution profile media and ephemeral stories anonymously.
- Intercepted CDN media endpoints directly to eliminate read-receipt beacons (`seen = false`) at the network layer.
- Implemented an embedded browser window to intercept authenticated session cookies and persist credentials securely to local storage.
- Engineered a high-throughput streaming compression engine to bundle user stories into instant `.zip` archives.

### 3. [NavalStrike](https://github.com/furkanndev/NavalStrike) — Decoupled 2D Arcade Simulation Engine
**Role:** Developer &bull; **Technologies:** `C#`, `.NET Framework`, `Windows Forms`, `Object-Oriented Design (OOD)`
- Implemented a layered desktop arcade game adhering strictly to object-oriented design and SOLID principles.
- Decoupled application architecture into a core domain engine (`Savas.Library`) and a presentation layer (`Savas.Desktop`).
- Applied interface-driven contracts (`IHareketEden`), polymorphism, and bounding-box collision detection algorithms.
- Designed file-backed persistent leaderboards with dynamic difficulty scaling.

### 4. [DirectoryChangeMonitorService](https://github.com/furkanndev/DirectoryChangeMonitorService) — Kernel-Level Linux Auditing Daemon
**Role:** Developer &bull; **Technologies:** `Bash`, `Linux Kernel inotify`, `Systemd`, `POSIX Automation`
- Developed an automated Linux daemon for real-time filesystem monitoring with zero-polling kernel event loops.
- Configured event masks (`modify`, `attrib`, `close_write`, `move`, `create`, `delete`) to track atomic filesystem operations.
- Packaged as a managed `systemd` service unit featuring boot autostart, crash recovery, and journal logging.

### 5. [MatrixManipulator](https://github.com/furkanndev/MatrixManipulator) — High-Performance Linear Algebra Engine
**Role:** Developer &bull; **Technologies:** `Modern C++17`, `Standard Template Library (STL)`, `Algorithmic Optimization`
- Built an interactive linear algebra transformation utility performing coordinate scalar swaps and matrix dot product calculations ($O(n^3)$).
- Implemented strict memory bounds checking and modular algorithmic procedures.

---

## Education

**Sakarya University** *(Sakarya Üniversitesi)*  
**Faculty of Computer and Information Sciences**  
*Bachelor of Science in Information Systems Engineering (Bilişim Sistemleri Mühendisliği)*

---

## Professional Activity & Code Quality

<div align="left">
  <table border="0">
    <tr>
      <td width="50%">
        <img src="https://github-readme-stats.vercel.app/api?username=furkanndev&show_icons=true&theme=default&hide_border=true&include_all_commits=true&count_private=true" alt="Furkan's GitHub Metrics" width="100%" />
      </td>
      <td width="50%">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=furkanndev&layout=compact&theme=default&hide_border=true" alt="Top Languages" width="100%" />
      </td>
    </tr>
  </table>
</div>

---

## Contact & Professional Links

- **Email:** [ffurkangltkn@gmail.com](mailto:ffurkangltkn@gmail.com)
- **LinkedIn:** [linkedin.com/in/furkan-gultekin](https://linkedin.com)
- **GitHub:** [github.com/furkanndev](https://github.com/furkanndev)
- **Location:** Turkey
