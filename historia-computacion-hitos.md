---
titulo: Historia de la Computación — Hitos, Descubrimientos y Relaciones
fecha_creacion: 2026-04-23
fecha_actualizacion: 2026-04-26
version: v0.6.0
autor: Carlos Ortet
tipo: knowledge / línea temporal interactiva
estado: live deployed · v0.6.0 estable
url_publica: https://zoopa.es/files/historia-computacion-hitos-20260423.html
github: https://github.com/carlosortet/historia-computacion
companion_html: historia-computacion-hitos-20260423.html
---

# Historia de la Computación · v0.6.0

> Línea temporal interactiva con **181 hitos verificados** y **246 relaciones causales** que cubren la historia de la computación desde el álgebra booleana de Boole (1847) hasta los modelos esperados para 2027.

> **🌐 Página en vivo (autoritativa):** https://zoopa.es/files/historia-computacion-hitos-20260423.html
> **📦 Repo público:** https://github.com/carlosortet/historia-computacion

> ⚠️ **Este markdown es un índice estructural.** El contenido completo, interactivo (grafo SVG, tooltips, expandibles, callout cuántico, glosario) está en el HTML companion. Para auditar/editar hitos: editar `historia-computacion-hitos-20260423.html` directamente.

---

## Estructura

**15 columnas en el grafo interactivo** + **8 tablas extra** (no en grafo, accesibles desde el header) + **callout educativo** en CUÁNTICA + **glosario completo**.

### 🟦 15 columnas del grafo (con relaciones causales)

| # | Columna | Color | Cobertura resumida | Hitos clave |
|---|---|---|---|---|
| 1 | **LÓGICA** | IBM blue | Fundamentos matemáticos | Boole 1847 · Frege 1879 · Gödel 1931 · Shannon 1937 · HoTT 2013 · Lean 4 2021 · AlphaProof 2024 |
| 2 | **ALGORITMOS** | Navy | Algoritmos fundamentales | Minimax 1928 · Dijkstra 1956 · Quicksort 1962 · Knuth 1968 · Cook-Levin 1971 · DH 1976 · RSA 1977 · PageRank 1998* · MapReduce 2004 · Nakamoto 2008 · Attention 2017* · Agentic 2024 |
| 3 | **ARQUITECTURA** | IBM red | Concepto de "ordenador" | Babbage 1837 · Lovelace 1843 · Turing 1936 · von Neumann 1945 · Autómatas autoreplicantes 1948 · EDSAC 1949 |
| 4 | **ELECTRÓNICA** | IBM yellow | De válvulas a chips | Z3 1941 · Colossus 1944 · ENIAC 1946 · Transistor 1947 · IC 1959 · Moore 1965 · Fin Moore 2019 · Project Silica 2019 · GAA 2022 |
| 5 | **SOFTWARE** | IBM green | OS, lenguajes, dev infra | A-0 1952 · FORTRAN 1957 · COBOL 1959 · LISP 1958 · ALGOL 1960 · Dijkstra 1968 · Unix 1969 · C 1973 · GNU 1983 · Linux 1991 · Git 2005 · Docker 2013 · Copilot 2021 · Coding agents 2024 |
| 6 | **PARADIGMAS** | Purple | Paradigmas de programación (renombrado de POO) | Simula 1967 · Smalltalk 1980 · C++ 1985 · Python 1991 · Java 1995 · JavaScript 1995 · TDD/Ágil 2001 · Funcional 2007 · Go+Rust 2010 · Swift+TS 2014 · Microservicios 2014 · Vibe Coding 2025 |
| 7 | **MICRO+PC** | IBM orange | Microprocesador y PC | Intel 4004 1971 · 8008 1972 · 8080 1974 · Altair 1975 · Apple I/II 1976-77 · IBM PC 1981 · Mac 1984 · RISC 1980 · 386 1985 · Pentium 1993 · Athlon 64 2003 · Core 2 Duo 2006 · iPhone 2007 · Android 2008 · RISC-V 2010 · Raspberry Pi 2012 · Ryzen 2017 · M1 2020 · NPU mainstream 2024 · M5+18A 2026 · M6+Vera 2027 |
| 8 | **ROBÓTICA** | Dark orange | Industrial → autónoma → VLA | Unimate 1961 · Shakey 1972 · PUMA 1978 · Roomba 2002 · DARPA UC 2007 · Spot 2015 · Humanoides 2024 · Robot FM 2024 (π0) · Cross-embodiment 2027 esp. |
| 9 | **INTERNET** | Dark green | Red → web → cloud → edge | ARPANET 1969 · TCP/IP 1983 · WWW 1989 · Mosaic 1993 · Google 1998 · AWS 2006 · Kubernetes 2014 · Edge+Web3 2020 |
| 10 | **DATA** | Light purple | Bases de datos | Codd 1970 · System R 1974 · Oracle 1979 · PostgreSQL/MySQL 1995-97 · NoSQL 2007 · FAISS 2017 · Vector DBs 2019 · pgvector+Iceberg 2024 · MCP 2024 · Agentic memory 2027 esp. |
| 11 | **IA** | Pink | McCulloch-Pitts → LLMs | McCulloch-Pitts 1943 · Turing test 1950 · Dartmouth 1956 · Perceptrón 1958 · ELIZA 1965 · Invierno 1969 · Sistemas expertos 1980 · Backprop 1986 · Deep Blue 1997 · LeNet-5 1998 · DBN 2006 · ImageNet 2009 · AlexNet 2012 · Word2Vec 2013 · GANs 2014 · AlphaGo 2016 · Transformer 2017 · AlphaFold 1 2018 · BERT+GPT-1 2018 · GPT-3 2020 · AlphaFold 2 2021 · ChatGPT 2022 · Diffusion 2022 · GPT-4+LLaMA 2023 · o1 2024 · Nobel Hopfield+Hinton 2024 · DeepSeek-R1 2025 · Claude Opus 4.7 2026 |
| 12 | **PARALELISMO** | Cyan | GPUs + ASICs IA (renombrado de GPU) | GeForce 256 1999 · Shaders 2001 · CUDA 2006 · OpenCL 2009 · TPU v1 2015 · Tensor Cores 2017 · TPU v2 2017 · Cerebras WSE-1 2019 · TPU v5p 2023 · Hyperscaler Si 2024 · Etched 2024 · TPU v6 Trillium 2024 · TPU v7 Ironwood 2025 · NVIDIA Rubin 2026 · TPU v8 2027 esp. · Vera Rubin Ultra 2027 esp. |
| 13 | **CUÁNTICA** | Magenta | Teoría → chips → FTQC | Benioff 1980 · Feynman 1981-82 · Deutsch 1985 · Shor 1994 · QEC qubit lógico 1995-97 · Grover 1996 · 2 qubits NMR 1998 · Sycamore 2019 · IBM Heron+System Two 2023 · Willow 2024 · Estim. ruptura RSA 2024 · MS Majorana 1 2025 · IBM Loon+Nighthawk 2025 · IBM Cockatoo 2027 esp. |
| 14 | **SUPERCOMPUTACIÓN** | Teal | TF → PF → EF | Cray-1 1976 · ASCI Red 1997 · Roadrunner 2008 · Fugaku 2020 · Frontier 2022 · Aurora 2024 · El Capitan 2024 · JUPITER EU 2025 |
| 15 | **SIMULACIÓN** | Bronze | Monte Carlo → World Models | Monte Carlo 1947 · ENIAC weather 1950 · SPICE 1973 · CFD 1989 · NKS Wolfram 2002 · PhysX/Bullet 2008 · Omniverse 2021 · Digital Twins 2022 · Sora/Genie 2024 · NVIDIA Cosmos 2025 · Foundation simulation 2027 esp. |

> **\*** Marcadores `*1` y `*2` señalan duplicidades conceptuales: PageRank también está en INTERNET (como producto Google); Attention también en IA (como modelo Transformer).

### 🟨 8 tablas extra (no en grafo · accesibles desde header del grafo)

| # | Tabla | Hitos cubiertos |
|---|---|---|
| 16 | **STORAGE** | RAMAC 1956 → floppy 8" 1971 → 3.5" 1980 → CD-ROM 1982 → DVD 1995 → USB 2000 → SSD 2007 → NVMe 2011 → Project Silica 2019 → DNA storage 2024 |
| 17 | **OPEN SOURCE** | GNU 1983 · GPL 1989 · Linux 1991 · Apache 1995 · OSI 1998 · Wikipedia 2001 · Git 2005 · GitHub 2008 · Kubernetes 2014 · PyTorch 2017 · LLaMA 2023 · Hugging Face 2024 · DeepSeek-R1 2025 |
| 18 | **CIBERSEGURIDAD** | Creeper 1971 · Morris 1988 · SSL 1995 · Slammer 2003 · Stuxnet 2010 · Snowden 2013 · Mirai 2016 · WannaCry 2017 · SolarWinds 2020 · Log4Shell 2021 · NIST PQC 2024 · LLM jailbreaks 2024 |
| 19 | **MOBILE** | DynaTAC 1973 · IBM Simon 1992 · Nokia 9000 1996 · BlackBerry 1999 · iPod 2001 · iPhone 2007 · Android 2008 · iPad 2010 · Apple Watch 2014 · Pokémon Go 2016 · A11 Bionic 2017 · 5G 2020 · Vision Pro 2024 · LLM on-device 2024 |
| 20 | **CRIPTOGRAFÍA** | DH 1976 · RSA 1977 · ECC 1985 · PGP 1991 · SSL 1995 · AES 2001 · Bitcoin 2008 · Snowden 2013 · Signal 2014 · NIST PQC competition 2016 · NIST PQC standards 2024 |
| 21 | **SISTEMAS OPERATIVOS** | OS/360 1964 · Unix 1969 · Multics 1969 · CP/M 1974 · MS-DOS 1981 · Mac OS 1984 · Windows 1.0 1985 · OS/2 1987 · Linux 1991 · NT 1993 · W95 1995 · Mac OS X 2001 · iOS 2007 · Android 2008 · Chrome OS 2009 · SO con LLM 2024 |
| 22 | **ARQUITECTURAS DE SISTEMA** | IBM 1401 1959 · System/360 1964 · Multics 1965 · VAX 1977 · NetWare 1983 · AS/400 1988 · x86 commodity 90s · VMware 1999 · Xen 2003 · AWS EC2 2006 · Hadoop 2008 · OpenStack 2010 · Docker 2013 · Kubernetes 2014 · Lambda serverless 2014 · Edge 2017 · 5G+IoT 2020s · GPU AI clusters 2024 · Agentic data centers 2025+ |
| 23 | **GLOSARIO** | 6 categorías a color (Cuántica · IA · Hardware · Datos · Arquitecturas · Software) + bloque siglas. Incluye explicación destacada de qubit físico vs lógico |

### ⚛ Callout educativo

Sección 9 CUÁNTICA incluye un callout dramático antes de la tabla, explicando "qubit físico ≠ qubit lógico" — el malentendido nº 1 del público. Diseño en gradient deep purple/magenta con la métrica concreta de ruptura RSA-2048 (~1.300 qubits LÓGICOS, Gidney 2024).

---

## Diseño y estética

- **Inspiración:** IBM (Paul Rand 1972) + Silicon Graphics (Joe Stitzlein 1986)
- **Header brand:** "498 ADVANCE — The European Intrepid Lab" + manifiesto cyan ("El futuro será simulado antes de ser vivido. Lo habitaremos antes de construirlo.")
- **Tipografía:** IBM Plex Mono (body) + IBM Plex Sans (titles)
- **Paleta:** cream/paper #E8DCC4 + IBM blue como acento estructural + 15 colores únicos por columna
- **Tablas colapsables** con botones expandir/colapsar global
- **Responsive** sin sacrificar diseño (4 breakpoints)
- **SEO completo:** meta description, Open Graph, Twitter Card, JSON-LD Schema.org Article
- **Tooltips** al hover sobre nodos del grafo
- **Click en nodo** = aísla sus relaciones; click en fondo = reset

## Apéndice especial · IBM System/23 Datamaster

Sección dedicada al "eslabón olvidado" entre el System/3 y el IBM PC. Incluye:
- Ilustración SVG sintética del System/23 (drives verticales, ARM, etc.)
- Dedicatoria personal a **José Ortet** (técnico de IBM durante décadas)
- Enlace al manual técnico oficial **SY34-0241-1** (May 1982, copia espejo en zoopa.es)
- Diario personal en estilo "fósforo verde CRT" con cursor parpadeante
- Detalles desplegables con ficha técnica completa + 4 secciones en inglés (Commercial Failure, Influence over 5120, Standard parts, Creation of IBM PC)

## Manifiesto

> *El futuro será simulado antes de ser vivido.*
> *Lo habitaremos antes de construirlo.*

— 498 Advance · The European Intrepid Lab

---

## Interactividad del grafo

- **Click en nodo** → aísla sus relaciones causales
- **Click en fondo** → reset
- **Hover en nodo** → tooltip con descripción + relación clave
- **Drag con ratón** → pan del grafo
- **Ctrl + scroll** → zoom in/out con anclaje al cursor
- **Botones +/− /⊕ FIT** en el header del grafo
- **Atajos teclado:** `+` `−` `0` (cuando el cursor está sobre el grafo)

## Versiones · changelog

- **v0.4.0** (2026-04-26) — **Fase 3:** zoom in/out · pan con drag · atajos teclado · botones +/−/FIT en cabecera. Mejora la navegabilidad del grafo de 15 columnas × 1900px alto.
- **v0.3.0** (2026-04-26) — Fase 1+2: RISC + RISC-V + COBOL en chart · QEC + qubit lógico + estim. RSA en CUÁNTICA · Secciones 21 SO + 22 ARQUITECTURAS DE SISTEMA + 23 GLOSARIO · Callout cuántico educativo · Header con menú extendido (8 tablas extra). Total: 181 nodos · 246 aristas · 23 secciones.
- **v0.2.0** (2026-04-25) — Auditoría exhaustiva con 6 subagentes paralelos: 15 errores corregidos (Cosmos año, ENIAC weather, PhysX, NVMe, PageRank, IBM Heron 133q, etc.) + 6 hitos críticos (TPU v6, IBM Loon, Fugaku, JavaScript, LeNet-5, Word2Vec).
- **v0.1.0** (2026-04-23) — Versión inicial pública. 154 hitos · 197 aristas · 15 columnas · 13 secciones.

## Pendientes próximas iteraciones

- Touch gestures (pinch-zoom, two-finger pan) para móviles/tablets
- Considerar: backup mirror en GitHub Pages (`carlosortet.github.io/historia-computacion/`)
- Considerar: CHANGELOG.md formal (separado del git log)

## Contribuciones

Correcciones y aportaciones bienvenidas: **carlos.ortet@zoopa.es**
