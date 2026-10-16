<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,100:161b22&height=180&section=header&text=FURKAN%20G%C3%9CLTEKIN&fontSize=42&fontAlignY=42&desc=Software%20Developer%20%7C%20Desktop%20Architecture%20%E2%80%A2%20Systems%20%E2%80%A2%20Automation&descAlignY=64&descAlign=50" width="100%" alt="Furkan Gültekin Header" />
</div>

<div align="center">
  <p align="center">
    <a href="mailto:ffurkangltkn@gmail.com"><img src="https://img.shields.io/badge/Email-ffurkangltkn%40gmail.com-0078D4?style=flat-square&logo=microsoftoutlook&logoColor=white" alt="Email" /></a>
    <a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Furkan%20Gültekin-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
    <a href="https://github.com/furkanndev?tab=followers"><img src="https://img.shields.io/github/followers/furkanndev?label=Followers&style=flat-square&logo=github&color=21262d" alt="Followers" /></a>
    <a href="https://github.com/furkanndev"><img src="https://komarev.com/ghpvc/?username=furkanndev&label=Profile%20Telemetry&color=21262d&style=flat-square" alt="Views" /></a>
  </p>
</div>

---

### Bento Overview

<table width="100%">
  <tr>
    <td width="62%" valign="top">
      <h3>About & Focus</h3>
      <p>
        I am a <b>Software Developer</b> focused on engineering robust desktop software architectures, systems programming, and high-performance automation tools. My work centers on solving complex engineering problems under the hood—ranging from low-latency document rendering and local OCR inference to API reverse engineering and automated single-click installer compilation.
      </p>
      <p>
        <b>Academic Background:</b><br/>
        Sakarya University &bull; Faculty of Computer and Information Sciences<br/>
        <i>B.S. in Information Systems Engineering</i>
      </p>
    </td>
    <td width="38%" valign="top">
      <h3>Core Methodology</h3>
      <ul>
        <li><b>Low-Latency Runtimes:</b> Leveraging native C/C++ engines (PyMuPDF, STL) for sub-millisecond execution.</li>
        <li><b>Decoupled Architecture:</b> Strict separation of domain algorithms from presentation viewports.</li>
        <li><b>Turnkey Deployment:</b> Packaging standalone executables (<code>.exe</code> via Inno Setup 6) with zero user-side configuration.</li>
      </ul>
    </td>
  </tr>
</table>

---

### Featured Works

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <div align="right"><code>Desktop Application</code> &bull; <code>Flagship</code></div>
      <h3><a href="https://github.com/furkanndev/AuraPDF">AuraPDF</a></h3>
      <p><b>Modern, Extensible Windows Desktop PDF Platform</b></p>
      <p>
        <img src="https://img.shields.io/badge/Python%203.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/PyQt6-41CD52?style=flat-square&logo=qt&logoColor=white" />
        <img src="https://img.shields.io/badge/PyMuPDF-D9381E?style=flat-square" />
        <img src="https://img.shields.io/badge/RapidOCR-blue?style=flat-square" />
        <img src="https://img.shields.io/badge/Inno%20Setup%206-0078D7?style=flat-square&logo=windows&logoColor=white" />
      </p>
      <ul>
        <li><b>In-Page Text Modification:</b> Interactive selection, font mutation, and text reflow directly on rendered PDF canvases.</li>
        <li><b>Local OCR Pipeline:</b> Scanned document text extraction via local ONNX inference models without external cloud latency.</li>
        <li><b>Complete PDF Toolbox:</b> Multi-file merge, split, high-ratio compression, redaction, and password encryption.</li>
        <li><b>Automated Distribution:</b> Turnkey compilation generating signed, single-click Windows installers (<code>.exe</code>).</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <div align="right"><code>Reverse Engineering</code> &bull; <code>Automation</code></div>
      <h3><a href="https://github.com/furkanndev/Social-Saver">Social-Saver</a></h3>
      <p><b>Anonymous Media Pipeline & Session Extraction Engine</b></p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/Flask%203.x-21262d?style=flat-square&logo=flask&logoColor=white" />
        <img src="https://img.shields.io/badge/Webview%20Auth-blue?style=flat-square" />
        <img src="https://img.shields.io/badge/REST%20API-4EAA25?style=flat-square" />
      </p>
      <ul>
        <li><b>Zero-Beacon Streaming:</b> Directly intercepts raw CDN media streams, guaranteeing untracked sessions (<code>seen = false</code>).</li>
        <li><b>Automated Session Ingestion:</b> Embedded webview intercepts and serializes active session cookies to disk automatically.</li>
        <li><b>Streaming Packaging:</b> High-throughput streaming ZIP packaging for instant bulk story downloads.</li>
        <li><b>Full-HD Viewer:</b> Bypasses client-side downsampling to display raw 1080p+ avatars with pan/zoom inspection.</li>
      </ul>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td width="33.3%" valign="top">
      <div align="right"><code>C# / .NET</code></div>
      <h4><a href="https://github.com/furkanndev/NavalStrike">NavalStrike</a></h4>
      <p><b>Decoupled 2D Arcade Engine</b></p>
      <p>Layered architecture separating domain engine (<code>Savas.Library</code>) from presentation (<code>Savas.Desktop</code>). Demonstrates strict interface contracts (<code>IHareketEden</code>), polymorphism, and collision detection.</p>
    </td>
    <td width="33.3%" valign="top">
      <div align="right"><code>Linux / Bash</code></div>
      <h4><a href="https://github.com/furkanndev/DirectoryChangeMonitorService">DirectoryChangeMonitor</a></h4>
      <p><b>Kernel-Level Filesystem Daemon</b></p>
      <p>Real-time Linux filesystem auditing daemon leveraging low-overhead kernel event hooks via <code>inotifywait</code>. Supervised under a production <code>systemd</code> service unit.</p>
    </td>
    <td width="33.3%" valign="top">
      <div align="right"><code>Modern C++17</code></div>
      <h4><a href="https://github.com/furkanndev/MatrixManipulator">MatrixManipulator</a></h4>
      <p><b>Linear Algebra Permutations</b></p>
      <p>High-performance C++ utility implementing in-place coordinate scalar permutations ($A_{ij} \longleftrightarrow B_{ij}$) and classical matrix dot products ($O(n^3)$) with strict memory bounds.</p>
    </td>
  </tr>
</table>

---

### Technical Matrix

<div align="center">
  <p><b>Languages & Systems</b></p>
  <img src="https://skillicons.dev/icons?i=python,cs,cpp,c,ts,js,bash,html,css&theme=dark" alt="Languages" />

  <br/><br/>
  <p><b>Desktop, Frameworks & Web Services</b></p>
  <img src="https://skillicons.dev/icons?i=qt,dotnet,flask,fastapi,nodejs,express,bootstrap,tailwind&theme=dark" alt="Frameworks" />

  <br/><br/>
  <p><b>DevOps, Cloud, Persistence & Tooling</b></p>
  <img src="https://skillicons.dev/icons?i=docker,linux,git,githubactions,postgres,sqlite,mongodb,redis,postman,vscode,visualstudio&theme=dark" alt="Tools" />
</div>

<br/>

<table>
  <thead>
    <tr>
      <th width="26%">Domain</th>
      <th>Technical Specializations & Toolchain</th>
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
        <code>PyMuPDF (Low-latency MuPDF C-Engine)</code> &bull; 
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
        <code>Linux Kernel inotify Real-time Event Hooks</code> &bull; 
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

### Telemetry & Analytics

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

<div align="center">
  <sub>Furkan Gültekin &bull; Software Developer &bull; Desktop Architecture & Systems Engineering</sub>
</div>
