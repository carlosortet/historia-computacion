---
titulo: Narrativas de la Historia de la Computación · Índice
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
autor: Carlos Ortet
tipo: knowledge / índice de ensayos narrativos
companion_html: ../historia-computacion-hitos-20260423.html
companion_md: ../historia-computacion-hitos-20260423.md
total_nodos: 214
total_aristas: 322
total_archivos: 16
periodo: 1642 → 2027
licencia: CC BY-SA 4.0
---

# Narrativas de la Historia de la Computación

> 15 ensayos narrativos · uno por columna del grafo · 214 hitos verificados · de Pascal (1642) a Vera Rubin Ultra (2027)

## El proyecto

Existe una [línea temporal interactiva](https://zoopa.es/files/historia-computacion-hitos-20260423.html) con 214 hitos y 322 relaciones causales que cubre la historia entera de la computación. Sirve para navegar visualmente. Pero el grafo no cuenta historia — la insinúa.

Este directorio contiene la versión narrativa: 15 ensayos en markdown, uno por cada columna temática del grafo. Cada ensayo recorre su cadena causal en orden cronológico, conectando personas, fechas, contextos y consecuencias. Pueden leerse independientemente o como un todo.

## Cómo está organizado

```
narrativas-historia-computacion/
├── 00_INDICE.md             ← estás aquí
├── 01_LOGICA.md             ← Boole → Lean 4
├── 02_ALGORITMOS.md         ← Minimax → Agentic
├── 03_ARQUITECTURA.md       ← Babbage → autómatas autoreplicantes
├── 04_ELECTRONICA.md        ← Z3 → Project Silica
├── 05_SOFTWARE.md           ← Hopper → coding agents
├── 06_PARADIGMAS.md         ← Simula → Vibe Coding
├── 07_MICRO_PC.md           ← Intel 4004 → M6 + Vera
├── 08_ROBOTICA.md           ← Unimate → Foundation Models
├── 09_INTERNET.md           ← ARPANET → Edge + Web3
├── 10_DATA.md               ← Codd → agentic memory
├── 11_IA.md                 ← McCulloch-Pitts → Opus 4.7
├── 12_PARALELISMO.md        ← GeForce 256 → Vera Rubin Ultra
├── 13_CUANTICA.md           ← Benioff → Cockatoo
├── 14_SUPERCOMPUTACION.md   ← Cray-1 → JUPITER
└── 15_SIMULACION.md         ← Monte Carlo → Foundation Sim
```

## Las 15 columnas · resúmenes ejecutivos

### 1. [[01_LOGICA|LÓGICA]] · Del razonamiento al código

Cómo se descubrió que el pensamiento podía reducirse a operaciones formales. **Boole** (1847) algebraiza la lógica. **Frege** (1879) la cuantifica. **Gödel** (1931) marca sus límites. **Turing** (1936) la mecaniza. **Shannon** (1937) la convierte en circuito. Hoy: **Lean 4** verifica matemáticas formalmente y **AlphaProof** (2024) demuestra teoremas con IA.

> Sin esta cadena no existe ni un transistor digital ni una línea de código.

### 2. [[02_ALGORITMOS|ALGORITMOS]] · Los pasos para resolver

De los algoritmos clásicos (**Dijkstra** 1956, **Knuth** 1968) a la criptografía moderna (**RSA** 1977) y los pilares del cloud (**MapReduce** 2004). El siglo XXI lo dominan dos: **Attention** (Vaswani et al. 2017) que define el Transformer, y **algoritmos agénticos** (2024) que orquestan acciones, no solo respuestas.

> Cada salto de algoritmo es un salto de lo que un ordenador puede *hacer útilmente*.

### 3. [[03_ARQUITECTURA|ARQUITECTURA]] · ¿Qué es un ordenador?

La definición conceptual. **Babbage** (1837) imagina la Analytical Engine. **Lovelace** (1843) escribe el primer programa. **Turing** (1936) formaliza qué es computable. **von Neumann** (1945) define la arquitectura que aún usamos: memoria + CPU + I/O. **Autómatas autoreplicantes** (1948) anticipan la vida artificial 70 años antes de los virus de ordenador.

> Definir el problema antes que la solución física.

### 4. [[04_ELECTRONICA|ELECTRÓNICA]] · De válvulas a átomos

La cadena física. **Z3** (Zuse 1941, relés). **ENIAC** (1946, válvulas, 18.000 tubos). **Transistor** (Bardeen-Brattain-Shockley 1947). **Circuito integrado** (Kilby/Noyce 1959). **Ley de Moore** (1965). El final del Moore clásico (~2019) y los nodos GAA (2022). Almacenamiento exótico: **Project Silica** (cristal de cuarzo, Microsoft 2019).

> Cada hito acerca el cómputo al límite cuántico de la materia.

### 5. [[05_SOFTWARE|SOFTWARE]] · Del A-0 a los coding agents

**Grace Hopper** escribe el primer compilador (A-0, 1952). **FORTRAN** (1957) democratiza la programación científica. **COBOL** (1959) la empresarial. **Unix** (Thompson-Ritchie 1969) define el modelo de SO. **C** (1973), **GNU** (Stallman 1983), **Linux** (Torvalds 1991), **Git** (2005), **Docker** (2013). En 2024-26: **Copilot** y **coding agents** que escriben código casi sin intervención humana.

> El software se construyó hasta poder construirse a sí mismo.

### 6. [[06_PARADIGMAS|PARADIGMAS]] · Cómo se piensa el código

No qué se programa, sino *cómo* se piensa. **Simula** (1967) inventa los objetos. **Smalltalk** (Kay 1980) los populariza. **C++** (Stroustrup 1985), **Python** (van Rossum 1991), **Java** (Gosling 1995), **JavaScript** (Eich 1995). **TDD/Ágil** (2001), funcional (2007), **Go**+**Rust** (2010), **TypeScript**+**Swift** (2014), microservicios. En 2025: **Vibe Coding** — código generado por descripción natural, sin teclear lenguaje formal.

> Cada paradigma redefine qué es "fácil de escribir y mantener".

### 7. [[07_MICRO_PC|MICRO+PC]] · El ordenador personal

De **Intel 4004** (1971, primer microprocesador) al **iPhone** (Jobs 2007) que cambió la computación móvil para siempre. Pasando por **Altair** (1975), **Apple I/II** (Wozniak 1976-77), **IBM PC** (1981), **Mac** (1984), arquitectura **RISC** (Patterson 1980), 386, Pentium, Athlon 64, Ryzen, **M1** (Apple 2020), y la revolución **RISC-V** (2010, ISA libre). 2027: M6 + Vera SoC.

> El cómputo se vuelve íntimo. Está en tu bolsillo, en tu reloj, en tu coche.

### 8. [[08_ROBOTICA|ROBÓTICA]] · Industrial → autónoma → encarnada

**Unimate** (Engelberger 1961) trabaja en GM soldando coches. **Shakey** (SRI 1972) razona y se mueve. **PUMA** (1978) define el brazo industrial. **Roomba** (2002) lleva la robótica al salón. **DARPA Urban Challenge** (2007) demuestra coche autónomo. **Spot** (Boston Dynamics 2015), humanoides (2024), **Robot Foundation Models** (π0 de Sergey Levine 2024). 2027 esperado: cross-embodiment universal.

> El cuerpo del cómputo. Empezamos con brazos atornillados; acabamos con humanoides aprendiendo de vídeo.

### 9. [[09_INTERNET|INTERNET]] · Red → web → cloud → edge

**ARPANET** (Roberts 1969, 4 nodos). **TCP/IP** (Cerf-Kahn 1983). **WWW** (Berners-Lee 1989, en CERN). **Mosaic** (Andreessen 1993). **Google** (Page-Brin 1998). **AWS** (2006) inventa el cloud. **Kubernetes** (2014) lo orquesta. **Edge** + **Web3** (2020+) lo descentralizan. La red pasó de 4 universidades estadounidenses a 5.500 millones de personas en 56 años.

> Cada salto multiplica por 10× el alcance del cómputo.

### 10. [[10_DATA|DATA]] · Estructurar el caos

**Edgar Codd** (IBM 1970) inventa el modelo relacional. **System R** (1974) y **Oracle** (1979) lo comercializan. Los 80-90: **PostgreSQL**, **MySQL**. **NoSQL** (2007) por escala web. **FAISS** (2017), **vector DBs** (2019), **pgvector** (2023): la era de los embeddings. **MCP** (Anthropic 2024): protocolo estándar para que LLMs accedan a datos. 2027: agentic memory persistente.

> De filas y columnas a vectores semánticos. La forma de los datos refleja qué tipo de cómputo los consume.

### 11. [[11_IA|IA]] · La cadena más larga

83 años. **McCulloch-Pitts** (1943, neurona artificial matemática). Test de **Turing** (1950). **Dartmouth** (McCarthy 1956, donde se acuña "AI"). **Perceptrón** (Rosenblatt 1958). **ELIZA** (Weizenbaum 1965). **Invierno IA** (Minsky 1969). Resurgir: **backprop** (Rumelhart-Hinton-Williams 1986). **Deep Blue** vence a Kasparov (1997). **AlexNet** (Krizhevsky-Sutskever-Hinton 2012) inicia la revolución deep learning. **AlphaGo** (DeepMind 2016). **Transformer** (2017). **GPT-3** (2020). **ChatGPT** (2022). **Nobel a Hopfield + Hinton** (2024). **Claude Opus 4.7** (2026).

> 80 años de altibajos hasta que la economía y el cómputo alinearon. Hoy define la frontera.

### 12. [[12_PARALELISMO|PARALELISMO]] · Hardware para deep learning

**GeForce 256** (Nvidia 1999, primera "GPU"). **CUDA** (Nvidia 2006) abre la GPU al cómputo general. **TPU v1** (Google 2015), primer ASIC para inferencia neuronal. **Tensor Cores** (Nvidia V100, 2017). **Cerebras WSE-1** (2019) — chip del tamaño de una oblea. **Etched** (2024) — primer ASIC dedicado a Transformer. **NVIDIA Rubin** (2026), **TPU v8** (2027), **Vera Rubin Ultra** (2027).

> El hardware persigue al software. Cada arquitectura nueva nace para una operación dominante (multiply-add masiva, attention, etc.).

### 13. [[13_CUANTICA|CUÁNTICA]] · La frontera más extraña

**Benioff** (1980) y **Feynman** (1981-82) proponen la idea. **Deutsch** (1985) la formaliza. **Shor** (1994): algoritmo que rompe RSA en tiempo polinomial. **QEC** (Shor-Steane 1995-97): el qubit lógico, abstracción que protege del ruido. **Grover** (1996), 2 qubits NMR (1998). **Sycamore** (Google 2019) reclama supremacía. **IBM Heron + System Two** (2023). **Willow** (Google 2024). **Microsoft Majorana 1** (2025) — qubits topológicos. **IBM Loon + Nighthawk** (2025). 2027: **IBM Cockatoo**, primer ordenador cuántico tolerante a fallos.

> El cómputo cuántico no es "más rápido". Es *otra cosa*. Permite resolver problemas que el cómputo clásico no puede ni intentar.

### 14. [[14_SUPERCOMPUTACION|SUPERCOMPUTACIÓN]] · Mega → giga → tera → peta → exa

**Cray-1** (Seymour Cray 1976). **ASCI Red** (1997, primer teraflop). **Roadrunner** (IBM 2008, primer petaflop). **Fugaku** (Japón 2020, ARM). **Frontier** (HPE 2022, primer exaflop). **Aurora** (Intel 2024). **El Capitan** (HPE 2024, 2.7 EF). **JUPITER** (EU 2025, primer exaflop europeo). Cada salto x1000 ha tardado ~10 años.

> La punta de lanza del cómputo. Lo que hoy ocupa una sala — en 25 años cabe en tu móvil.

### 15. [[15_SIMULACION|SIMULACIÓN]] · Modelar la realidad

**Monte Carlo** (Ulam-von Neumann 1947, en Los Alamos). **ENIAC weather** (Charney-Fjørtoft-von Neumann 1950). **SPICE** (Berkeley 1973). **CFD industrial** (años 90). **NKS** (Wolfram 2002). **PhysX**+**Bullet** (motores físicos, 2008). **Omniverse** (Nvidia 2021). **Digital Twins** (2022). **Sora**+**Genie** (2024) generan vídeo + mundos jugables desde texto. **NVIDIA Cosmos** (2025): foundation model para simulación física. 2027: foundation simulation universal.

> La simulación es la inversa del cómputo: en vez de procesar el mundo, lo crea. Es el futuro del entrenamiento de IA y robots.

## Mapa de cross-column dependencies (alto nivel)

Algunas cadenas atraviesan toda la historia:

```
LÓGICA ─────► ELECTRÓNICA ─────► MICRO+PC ─────► PARALELISMO ─────► IA
  │                │                  │                 │              │
  ▼                ▼                  ▼                 ▼              ▼
ALGORITMOS    ARQUITECTURA      SOFTWARE         CUÁNTICA       SIMULACIÓN
                  │                  │
                  └──────► INTERNET ◄┘
                                │
                                ▼
                              DATA ─────► ROBÓTICA
```

Las "autopistas" cross-column principales:

1. **Lógica → Electrónica → IA**: Boole → Shannon → transistor → IC → Moore → CUDA → Transformer → GPT.
2. **Arquitectura → Software → Internet**: Turing → von Neumann → Unix → C → ARPANET → WWW → Cloud.
3. **Algoritmos → Criptografía → Internet → Cuántica**: RSA → SSL/TLS → todo el e-commerce → Shor (que la rompe) → PQC.
4. **Paralelismo → IA → Simulación → Robótica**: GPU → DL → world models → Robot Foundation Models.

## Rutas de lectura recomendadas

| Si te interesa... | Lee en este orden |
|---|---|
| **El origen filosófico** | LÓGICA → ARQUITECTURA → ALGORITMOS |
| **El hardware** | ELECTRÓNICA → MICRO+PC → PARALELISMO → CUÁNTICA |
| **Cómo se programa** | SOFTWARE → PARADIGMAS → ALGORITMOS |
| **La revolución IA** | IA → PARALELISMO → DATA → SIMULACIÓN |
| **El cómputo distribuido** | INTERNET → DATA → ARQUITECTURA → SUPERCOMP |
| **El futuro físico** | ROBÓTICA → SIMULACIÓN → IA |
| **Sin orden específico** | Empieza por la columna que ya conoces. Sigue los wikilinks. |

## Personas que aparecen en múltiples columnas

| Persona | Columnas | Aportación múltiple |
|---|---|---|
| **John von Neumann** | ARQUITECTURA, SIMULACIÓN, ALGORITMOS | Arquitectura clásica + Monte Carlo + autómatas + minimax |
| **Alan Turing** | LÓGICA, ARQUITECTURA, IA | Máquina universal + test de inteligencia + criptoanálisis |
| **Claude Shannon** | LÓGICA, ALGORITMOS | Tesis 1937 + teoría de la información 1948 |
| **Donald Knuth** | ALGORITMOS, SOFTWARE | TAOCP + TeX + análisis de algoritmos |
| **Edsger Dijkstra** | ALGORITMOS, SOFTWARE | Dijkstra + GOTO considered harmful + concurrencia |
| **Geoffrey Hinton** | IA, varias | Backprop + DBN + AlexNet + Nobel 2024 |
| **Linus Torvalds** | SOFTWARE | Linux + Git |
| **Ken Thompson** | SOFTWARE | Unix + B (precursor de C) |
| **Tim Berners-Lee** | INTERNET | HTML + HTTP + URI |
| **Steve Wozniak** | MICRO+PC | Apple I + Apple II |
| **Jeff Dean** | DATA, ALGORITMOS, IA | MapReduce + BigTable + TensorFlow |

## Versionado

| Versión | Fecha | Cambios |
|---|---|---|
| **v1.0** | 2026-04-26 | Generación inicial · 15 narrativas + índice |

## Mantenimiento

Cuando se actualice el HTML principal (nodos nuevos, ediciones), regenerar las narrativas afectadas. La integridad fuente es el HTML — estos .md son su versión narrativa derivada.

## Licencia

CC BY-SA 4.0 (igual que el HTML principal).

## Autor

Carlos Ortet · 498 Advance · The European Intrepid Lab
