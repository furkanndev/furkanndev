<div align="center">
  <img src="https://raw.githubusercontent.com/furkanndev/furkanndev/main/assets/header.svg" width="100%" alt="Furkan Gültekin Header Banner" />
</div>

<div align="center">

  [![Email](https://img.shields.io/badge/Email-ffurkangltkn%40gmail.com-0078D4?style=flat-square&logo=microsoftoutlook&logoColor=white)](mailto:ffurkangltkn@gmail.com)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com)
  [![GitHub Followers](https://img.shields.io/github/followers/furkanndev?label=Followers&style=flat-square&logo=github&color=21262d)](https://github.com/furkanndev?tab=followers)
  [![Profile Views](https://komarev.com/ghpvc/?username=furkanndev&label=Profile%20Views&color=21262d&style=flat-square)](https://github.com/furkanndev)

  <p align="center">
    <a href="#about-me">About Me</a> &bull;
    <a href="#flagship-workstations">Flagship Workstations</a> &bull;
    <a href="#project-portfolio">Project Portfolio</a> &bull;
    <a href="#technical-stack--skills">Technical Stack</a> &bull;
    <a href="#github-telemetry">GitHub Telemetry</a>
  </p>

</div>

---

### About Me

I am **Furkan Gültekin**, a **Software Developer** dedicated to engineering high-performance desktop applications, system utilities, and robust automation solutions.

- **Flagship Products:**
  - Creator and maintainer of **[AuraPDF Pro](https://github.com/furkanndev/AuraPDF)** — an Acrobat-grade, multi-tabbed Windows desktop PDF platform featuring direct in-page text editing, PyMuPDF engine, digital signatures, AcroForms, and format conversion pipelines.
  - Creator and maintainer of **[Keystone](https://github.com/furkanndev/KeyStone)** — an automated post-installation Windows workstation setup suite featuring 140+ software package deployment via Winget, registry optimizations, and pre/post-format migration pipelines.
- **Core Competencies:** Desktop Application Architecture (Qt/PyQt6, C#/.NET, Modern C++), Win32 API & Linux systemd daemons, API reverse engineering, and low-level data structures.
- **Full Lifecycle Engineering:** System design, UI/UX implementation, standalone compilation (`.exe` via Inno Setup 6 / PyInstaller), and CI/CD pipelines.
- **Academic Background:** Sakarya University &bull; B.S. in Information Systems Engineering.
- **Contact:** Reach me directly at **[ffurkangltkn@gmail.com](mailto:ffurkangltkn@gmail.com)**.

---

### Flagship Workstations

| Project | Tech Stack | Description | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **[AuraPDF Pro](https://github.com/furkanndev/AuraPDF)**<br><code>v2.2.3</code> &bull; <code>Win x64</code> | `Python 3.10+`<br>`PyQt6` `PyMuPDF`<br>`Inno Setup 6` `ONNX OCR` | Acrobat-grade Windows desktop PDF platform built for speed, offline privacy, and intensive document workflows. | • Direct on-canvas text editing & typography reflow<br>• Sandwich OCR & AcroForm validation<br>• Word, Excel, PPTX & ePub export pipelines<br>• Standalone installer (`.exe`) via Inno Setup 6 |
| **[Keystone](https://github.com/furkanndev/KeyStone)**<br><code>v1.0</code> &bull; <code>Win x64</code> | `Python 3.11+`<br>`PyQt6` `Win32 API`<br>`Winget` `PyInstaller` | Unified post-installation Windows workstation setup suite, package deployment, registry optimizer, and migration utility. | • Automated silent deployment of 140+ software packages<br>• Real-time registry optimizations with 1-click rollback<br>• Full browser, SSH, Git & VS Code migration manifests<br>• Isolated multi-profile workspaces |

---

### Project Portfolio

#### Desktop Applications & Systems

| Project | Tech Stack | Description | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **[Social-Saver](https://github.com/furkanndev/Social-Saver)**<br><code>v1.0</code> &bull; <code>Desktop/Web</code> | `Python` `Flask 3.x`<br>`Reverse Eng`<br>`REST API` `Webview` | Anonymous Instagram story, highlight, and original-resolution profile media viewer and bulk exporter. | • 100% anonymous CDN stream extraction (`seen = false`)<br>• Automated session token capture via embedded webview<br>• Streaming bulk `.zip` archive export & 1080p+ pan/zoom |
| **[DirectoryChangeMonitor](https://github.com/furkanndev/DirectoryChangeMonitorService)**<br><code>Linux Daemon</code> | `Bash 4+` `Systemd`<br>`Linux inotify`<br>`POSIX Shell` | Zero-overhead Linux background daemon persistently auditing real-time filesystem directory events. | • Non-polling kernel event loops via `inotifywait`<br>• Real-time logging across 6 POSIX event categories<br>• Supervised `systemd` service with boot persistence |

#### Game Engines & Interactive OOP

| Project | Tech Stack | Description | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **[NavalStrike](https://github.com/furkanndev/NavalStrike)**<br><code>2D Arcade Engine</code> | `C#` `.NET`<br>`Windows Forms`<br>`Layered OOP` | Interactive 2D naval arcade game demonstrating decoupled domain architecture and real-time entity simulation. | • Decoupled domain engine (`Savas.Library`) & presentation UI<br>• Interface contracts (`IHareketEden`) & polymorphism<br>• 60 FPS loop, dynamic enemy AI & persistent high scores |
| **[HiddenObjectsGame](https://github.com/furkanndev/HiddenObjectsGame)**<br><code>Procedural Search</code> | `C#` `.NET`<br>`Console Architecture`<br>`Procedural Seeding` | Tactical grid search and deduction puzzle game featuring procedural matrix generation and ANSI rendering. | • Dynamic 20x20 Cartesian grid with hidden multi-segment targets<br>• Algorithmic collision-free procedural object placement<br>• Color-coded terminal fog-of-war buffer & accuracy scoring |

#### Algorithms, Data Structures & Low-Level Computing

| Project | Tech Stack | Description | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **[MatrixManipulator](https://github.com/furkanndev/MatrixManipulator)**<br><code>Modern C++17</code> | `Modern C++17`<br>`STL` `Algorithms`<br>`Linear Algebra` | High-performance linear algebra engine for randomized square matrix generation and Cartesian transformations. | • Dynamic $5 \times 5$ matrix generation with bounded RNG<br>• In-place coordinate scalar permutations ($A_{ij} \longleftrightarrow B_{ij}$)<br>• Classical dot product calculations ($O(n^3)$) with zero reallocation |
| **[DealerDistribution](https://github.com/furkanndev/DealerDistribution)**<br><code>C++ Simulation</code> | `C++` `Pointers`<br>`Simulation`<br>`Stream File I/O` | Algorithmic warehouse supply chain simulation managing randomized dealer traversal and product allocation. | • Memory address pointer tracking & structured file persistence<br>• Algorithmic randomized dealer traversal sequencing<br>• Real-time warehouse balance verification & auditing |
| **[BusPassengerAllocation](https://github.com/furkanndev/BusPassengerAllocation)**<br><code>Data Structures</code> | `C` `GCC`<br>`Data Structures`<br>`Stack & List` | Dynamic tour passenger seating management system implementing custom Stack and List data structures. | • Sequential row-by-row seat allocation across multi-bus fleets<br>• Custom dynamic Stack allocation & linked list seat storage<br>• Structured passenger manifest reporting and memory cleanup |
| **[IEEE754-Converter](https://github.com/furkanndev/IEEE754-Converter)**<br><code>Systems Computing</code> | `C` `GCC`<br>`Computer Systems`<br>`Bitwise Operations` | Numerical precision conversion utility synthesizing binary floating-point IEEE 754 representations. | • Single (32-bit float) and double (64-bit double) precision support<br>• Low-level bitwise sign, exponent, and mantissa extraction<br>• Formatted IEEE 754 standard binary string rendering |

---

### Technical Stack & Skills

<table>
  <tr>
    <td width="22%" align="center"><b>Languages</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white" />
      <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" />
      <img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black" />
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" />
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="22%" align="center"><b>Frameworks & GUI</b></td>
    <td>
      <img src="https://img.shields.io/badge/Qt-41CD52?style=flat-square&logo=qt&logoColor=white" />
      <img src="https://img.shields.io/badge/PyQt%20%2F%20PySide-41CD52?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" />
      <img src="https://img.shields.io/badge/Windows%20Forms-0078D7?style=flat-square&logo=windows&logoColor=white" />
      <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" />
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
      <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white" />
      <img src="https://img.shields.io/badge/TailwindCSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="22%" align="center"><b>Systems & Automation</b></td>
    <td>
      <img src="https://img.shields.io/badge/Linux%20Systemd-FCC624?style=flat-square&logo=linux&logoColor=black" />
      <img src="https://img.shields.io/badge/Kernel%20inotify-21262d?style=flat-square&logo=linux&logoColor=white" />
      <img src="https://img.shields.io/badge/Reverse%20Engineering-blue?style=flat-square" />
      <img src="https://img.shields.io/badge/PyMuPDF-D9381E?style=flat-square" />
      <img src="https://img.shields.io/badge/RapidOCR%20%2F%20ONNX-38B2AC?style=flat-square" />
      <img src="https://img.shields.io/badge/Win32%20API-0078D7?style=flat-square&logo=windows&logoColor=white" />
      <img src="https://img.shields.io/badge/Windows%20Registry-0078D7?style=flat-square&logo=windows&logoColor=white" />
      <img src="https://img.shields.io/badge/Winget%20CLI-0078D7?style=flat-square&logo=windows-terminal&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="22%" align="center"><b>DevOps & Tools</b></td>
    <td>
      <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
      <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
      <img src="https://img.shields.io/badge/PyInstaller-3776AB?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/Inno%20Setup%206-0078D7?style=flat-square&logo=windows&logoColor=white" />
      <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" />
      <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" />
      <img src="https://img.shields.io/badge/Visual%20Studio-5C2D91?style=flat-square&logo=visual-studio&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="22%" align="center"><b>Databases</b></td>
    <td>
      <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/Microsoft%20SQL%20Server-CC292B?style=flat-square&logo=microsoft-sql-server&logoColor=white" />
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
    </td>
  </tr>
</table>

---

### GitHub Telemetry

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=furkanndev&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117" alt="Furkan's GitHub Stats" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=furkanndev&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117" alt="Top Languages" width="45%" />
</div>

<div align="center" style="margin-top: 15px;">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=furkanndev&theme=tokyonight&hide_border=true&background=0d1117" alt="Streak Stats" width="49%" />
</div>

---

### Contribution Activity

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake.svg">
    <img alt="GitHub Contribution Snake Animation" src="https://raw.githubusercontent.com/furkanndev/furkanndev/output/github-contribution-grid-snake.svg" width="100%" />
  </picture>
</div>

---

<div align="center">
  <sub>Furkan Gültekin &bull; Software Developer &bull; Desktop Architecture &amp; Systems</sub>
</div>
