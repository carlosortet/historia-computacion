# Historia de la Computación · Hitos y Relaciones

> Línea temporal estructurada y grafo de relaciones · 1837 → 2027
>
> Por **Carlos Ortet** · [498 Advance — The European Intrepid Lab](https://498advance.com)

**🌐 Página en vivo (oficial):** https://zoopa.es/files/historia-computacion-hitos-20260423.html
**🪞 Mirror (GitHub Pages):** https://carlosortet.github.io/historia-computacion/

---

## Qué es esto

Una línea temporal interactiva con **181 hitos verificados** y **246 relaciones causales** que cubren la historia entera de la computación, desde el álgebra booleana de Boole (1847) hasta los modelos esperados para 2027 (NVIDIA Vera Rubin Ultra, IBM Cockatoo cuántico, Robot FM cross-embodiment).

Está organizada en **15 columnas temáticas** en el grafo + **8 tablas extra** complementarias (no en grafo) accesibles desde la cabecera.

### 15 columnas del grafo

| # | Columna | Cobertura |
|---|---|---|
| 1 | LÓGICA | Boole · Frege · Gödel · Shannon → HoTT · Lean 4 · AlphaProof |
| 2 | ALGORITMOS | Minimax · Dijkstra · Knuth · RSA · MapReduce · Attention · Agentic |
| 3 | ARQUITECTURA | Babbage · Turing · von Neumann · autómatas autoreplicantes |
| 4 | ELECTRÓNICA | Z3 · ENIAC · transistor · IC · Moore · GAA · Project Silica |
| 5 | SOFTWARE | Hopper · FORTRAN · COBOL · Unix · C · GNU · Linux · Git · Docker · Copilot · Coding agents |
| 6 | PARADIGMAS | Simula · Smalltalk · C++ · Python · Java · JavaScript · TDD/Ágil · Funcional · Go+Rust · Swift+TS · Microservicios · Vibe Coding |
| 7 | MICRO+PC | Intel 4004 → RISC → 386 → Pentium → Athlon 64 → Ryzen → iPhone → Android → M1 → M6+Vera · RISC-V |
| 8 | ROBÓTICA | Unimate · Shakey · PUMA · Roomba · DARPA UC · Spot · humanoides → Foundation Models |
| 9 | INTERNET | ARPANET · TCP/IP · WWW · Mosaic · Google · AWS · Kubernetes · Edge+Web3 |
| 10 | DATA | Codd · System R · Oracle · NoSQL · FAISS · vector DBs · pgvector · MCP · Agentic memory |
| 11 | IA | McCulloch-Pitts · Dartmouth · perceptrón · backprop · LeNet-5 · ImageNet · AlexNet · Word2Vec · Transformer · GPT-3 · AlphaFold · Diffusion · GPT-4 · o1 · Nobel Hinton/Hopfield · DeepSeek-R1 · Opus 4.7 |
| 12 | PARALELISMO | GeForce 256 · CUDA · OpenCL · Tensor Cores · TPU v1→v8 · Cerebras · Etched · Rubin · Vera |
| 13 | CUÁNTICA | Benioff · Feynman · Deutsch · Shor · QEC · Grover · 2 qubits · Sycamore · Heron · Willow · Majorana · Loon · Estim. ruptura RSA · Cockatoo |
| 14 | SUPERCOMPUTACIÓN | Cray-1 · ASCI Red · Roadrunner · Fugaku · Frontier · Aurora · El Capitan · JUPITER |
| 15 | SIMULACIÓN | Monte Carlo · ENIAC weather · SPICE · CFD · NKS · PhysX · Omniverse · World Models · Cosmos · Foundation Sim |

### 8 tablas extra (no en grafo · accesibles desde cabecera)

| # | Tabla | Foco |
|---|---|---|
| 16 | STORAGE | RAMAC → floppy → CD → SSD → NVMe → cristal/DNA |
| 17 | OPEN SOURCE | GNU → Linux → Apache → GitHub → PyTorch → LLaMA |
| 18 | CIBERSEGURIDAD | Creeper → Morris → Stuxnet → Snowden → ransomware → PQC |
| 19 | MOBILE | DynaTAC → BlackBerry → iPhone → Android → wearables → AR/VR |
| 20 | CRIPTOGRAFÍA | DH/RSA → ECC → PGP → SSL → Bitcoin → Signal → PQC |
| 21 | SISTEMAS OPERATIVOS | OS/360 → Unix → MS-DOS → Mac OS → Windows → iOS → Android → SO con LLM |
| 22 | ARQUITECTURAS DE SISTEMA | Mainframe → minicomputer → cliente-servidor → virtualización → cloud → contenedores → edge → AI factories |
| 23 | GLOSARIO | Términos clave (qubit físico vs lógico, LLM, Transformer, RAG, RISC vs CISC, mainframe vs cloud, etc.) |

---

## Estética

Diseño inspirado en **IBM (Paul Rand 1972)** y **Silicon Graphics (Joe Stitzlein 1986)**:
- Tipografía IBM Plex (Sans + Mono)
- Paleta cream/paper · IBM blue como acento estructural
- Wordmark "498A" con stripes carved al estilo IBM
- Mark de cubo isométrico inspirado en SGI
- Tablas colapsables · responsive · SEO completo (Open Graph, Twitter Card, JSON-LD)

## Apéndice especial

La página incluye un apéndice extenso sobre el **IBM System/23 Datamaster (1981)** — el "eslabón olvidado" entre el System/3 y el IBM PC, con dedicatoria personal a José Ortet (técnico de IBM durante décadas) y enlace al manual técnico oficial preservado.

## Archivos en este repo

- `historia-computacion-hitos.html` — la página completa, autocontenida (CSS + JS + SVG inline)
- `historia-computacion-hitos.md` — versión markdown del contenido (línea base verificada)
- `SY34-0241-1_IBM_5324_Service_Manual.pdf` — manual técnico oficial IBM 5324 System/23 (May 1982, 17 MB · espejo de bitsavers.org)
- `LICENSE` — CC BY-SA 4.0 (contenido) · el PDF de IBM mantiene su copyright original

## Manifiesto

> *El futuro será simulado antes de ser vivido.*
> *Lo habitaremos antes de construirlo.*

— 498 Advance · The European Intrepid Lab

## Contribuciones

Correcciones y aportaciones bienvenidas: **carlos.ortet@zoopa.es**

## Licencia

Contenido bajo **CC BY-SA 4.0** (ver `LICENSE`). El PDF del manual IBM es propiedad de IBM Corp. (1982); incluido aquí como copia espejo para preservación digital, originalmente disponible en [bitsavers.org](https://bitsavers.org/pdf/ibm/system23/fe/SY34-0241-1_IBM_5324_Computer_Service_Manual_May82.pdf).

## Interactividad del grafo

- **Click en nodo** → aísla sus relaciones causales (resto se atenúa)
- **Click en fondo** → reset
- **Hover en nodo** → tooltip con descripción + relación clave
- **Drag con ratón** → pan (mover el grafo)
- **Ctrl + scroll** (Cmd + scroll en Mac) → zoom in/out con anclaje al cursor
- **Botones +/− /⊕ FIT** en el header del grafo
- **Atajos teclado:** `+` zoom in · `−` zoom out · `0` reset (cuando el cursor está sobre el grafo)
- **Navegación a11y:** `Tab` recorre nodos · `Enter`/`Space` aísla relaciones · `Esc` resetea · tooltip se muestra también en focus (lectores de pantalla compatibles)

## Versiones

- **v0.11.0** (2026-04-26) — **GitHub Pages mirror activado**: `https://carlosortet.github.io/historia-computacion/` sirve la última versión del repo automáticamente en cada `git push` (sin esperar TTL Cloudflare). `index.html` con redirección + URL canónica preservada hacia Zoopa para evitar conflicto SEO. Ventajas: backup público permanente · cache invalidation instantánea · URLs versionables por commit hash para citas académicas.
- **v0.10.0** (2026-04-26) — **Accesibilidad WCAG 2.1 AA del grafo SVG**: cada nodo ahora es focuseable (`tabindex="0"`, `role="button"`, `aria-label` completo con año + hito + descripción + relación) · tooltip declarado como `role="tooltip"` con `aria-live="polite"` y `aria-hidden` sincronizado · navegación por teclado: `Tab` recorre nodos en orden cronológico, `Enter`/`Space` aísla relaciones, `Esc` resetea · tooltip se posiciona automáticamente bajo el nodo cuando se llega por focus · ring visual `:focus-visible` con outline amarillo IBM + glow drop-shadow.
- **v0.9.0** (2026-04-26) — **Tier A SEO + Tier B OG + Tier C a11y + look 80s**: title 54 chars, description 150 chars, JSON-LD image fix · OG image 1200×630 generada con Nano Banana 2 (estética IBM × SGI) · `<main>`, skip-link, aria-labels, theme-color, favicon SVG inline · emojis modernos eliminados → símbolos 80s (`►`, `▸`, `>`) · cabeceras de tabla en **fósforo verde CRT** (`#33ff66` + glow) con cursor `▮` parpadeante al final.
- **v0.8.0** (2026-04-26) — **Auditoría externa con 3 subagentes paralelos** (pre-1950 · IA moderna · MOBILE/CIBERSEGURIDAD) verificó ~50 hitos contra Wikipedia/Nobel/IEEE. **Conclusión y Apéndice ahora colapsables** (25 secciones totales). **9 correcciones factuales aplicadas**: Hollerith censo (8 años → 6 meses, no "7 años → 6 semanas") · Harvard Mark I peso (~5t real, no 50t) · Bug 1947 fue en Mark II no Mark I · Leibniz Stepped Reckoner 1673 · Bluetooth 1.0 jul 1999 (no 1998) · IBM Simon 1992-94 · iPod scroll wheel mecánico · Reaper por Tomlinson 1972 · MIDI co-padre Kakehashi/Roland · NES cronología Famicom 1983/NES 1985.
- **v0.7.1** (2026-04-26) — Tier 4 #28+#29: conclusión expandida en 4 secciones temáticas (puentes físicos · 4 hilos infraestructurales · 3 cierres simbólicos) + callout cloud↔mainframe en §22 ARQUITECTURAS DE SISTEMA (orange-theme).
- **v0.7.0** (2026-04-26) — P2 + P3 + Tier2 #14: 22 hitos nuevos · de Pascalina (1642) a GPT-5 (2025). Cubre periodo pre-1900 (Pascal, Leibniz, Jacquard, Hollerith) + Lambda calculus Church · Shannon 1948 · Manchester Baby · Z1 + Plankalkül · Sketchpad · MoAD · Xerox Alto · Hamilton + Apollo · Mistral/Gemini/Phi/GPT-5. + filas tablas extra (Pong, MIDI, MP3, DOOM, Wi-Fi, Bluetooth, NES, GDPR).
- **v0.6.0** (2026-04-26) — P4 + P5 audit corrections: añadido nodo IBM/360 (1964) · 15 nuevas aristas conexiones que faltaban (shannon→vonneu, boole→frege, alphafold1→transformer, ibm360→cobol, feynman→qbit2/willow, mapreduce→aws, lisp→python, alphago→algAgents) + 5 huérfanos conectados (android, silica, aurora, jupiter, vibeCoding) · separados nodos compuestos `bert` (BERT vs GPT-1) y `gpt4` (GPT-4 vs LLaMA, cerrado vs open) · pageRankAlg→google: parallel→enables (es el algoritmo que define Google).
- **v0.5.1** (2026-04-26) — 9 audit corrections: 5 inversiones temporales · 1 corrección semántica (dbn→alphafold1 incorrecta) · 1 eliminación tendenciosa (riscv→tpu7) · 1 cambio de tipo · 3 estrenando tipo `causal` · diario personal compactado en 3 párrafos · dedicatoria José Ortet sin redundancia "padre"
- **v0.5.0** (2026-04-26) — Tier 4 polish + Tier 3 búsqueda y filtro de columnas. Callout cyan en PARALELISMO. Tablas extra con borde amarillo distintivo.
- **v0.4.0** (2026-04-26) — Fase 3: zoom in/out · pan con drag · atajos teclado · botones +/−/FIT en cabecera.
- **v0.3.0** (2026-04-26) — Pasos 1-6 Fase 1+2: RISC en chart · QEC + qubit lógico + estim. RSA · COBOL · secciones 21 SO + 22 SISTEMAS + 23 GLOSARIO · callout cuántico · header extendido. Total: 181 nodos · 246 aristas · 23 secciones.
- **v0.2.0** (2026-04-25) — Auditoría exhaustiva con 6 subagentes, correcciones IBM Heron / Cosmos / iPhone / PhysX / NVMe / PageRank / etc.
- **v0.1.0** (2026-04-23) — Versión inicial pública. 154 hitos · 197 aristas · 15 columnas.
