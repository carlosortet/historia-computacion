---
columna: ALGORITMOS
cat: ALG
nodos_cubiertos: 13
periodo: 1928 → 2024
---

# ALGORITMOS · De la teoría de juegos al agente que razona

> Un siglo de primitivas: cada algoritmo resuelve un problema que antes parecía irresolvible, y al hacerlo, abre el siguiente.

## El arco

La columna ALGORITMOS no empieza con "algoritmos de ordenación" — empieza con la teoría de juegos de Von Neumann, que es la primera formulación matemática de la toma de decisiones bajo incertidumbre. De ahí la cadena avanza por la teoría de la complejidad (¿qué es tratable?), la criptografía (¿cómo proteger la información?), el big data distribuido (¿cómo procesar la web entera?), hasta los algoritmos agénticos de 2024 que combinan búsqueda clásica con LLMs. El patrón: cada era crea un cuello de botella computacional nuevo; la columna ALGORITMOS es la historia de cómo se rompe cada uno. La columna recibe impulsos de LÓGICA (Gödel → Cook-Levin), ELECTRÓNICA (ENIAC hace viable el Monte Carlo), IA (backprop → attention) y genera salidas hacia INTERNET (Dijkstra → routing), CRIPTOGRAFÍA (RSA bajo amenaza Shor) y la propia IA (attention → Transformer).

## La cadena

### 1928 · Minimax — John von Neumann

**John von Neumann** publica *Zur Theorie der Gesellschaftsspiele* en 1928, con 25 años, en Berlín. El teorema minimax prueba que en cualquier juego de suma cero entre dos jugadores con información perfecta, existe una estrategia óptima: minimiza tu pérdida máxima posible. La formulación es puramente matemática — no requiere ordenador. Pero setenta años después se convierte en el corazón de Deep Blue (1997) y AlphaGo (2016): los árboles de búsqueda adversaria que vencen a campeones mundiales ejecutan variantes del mismo principio.

**Conduce a:** Quicksort (1962) — siguiente nodo en la cadena algorítmica formal · Deep Blue (1997), AlphaGo (2016) como aplicaciones · **Depende de:** Lógica de predicados de Frege (1879) — influencia formal directa.

---

### 1956 · Dijkstra · shortest path — Edsger Dijkstra

**Edsger Dijkstra** escribe el algoritmo del camino más corto en un café de Ámsterdam en 1956, en aproximadamente 20 minutos, sin papel ni lápiz ("lo diseñé sin papel, lo que creo que es una de las razones por las que es tan elegante"). Lo publica en 1959 en *Numerische Mathematik*. El algoritmo recorre un grafo dirigido con pesos y encuentra el camino de menor coste desde un nodo origen a todos los demás. Complejidad: O(V²) en la versión original, O(E + V log V) con heap de Fibonacci.

Sin el algoritmo de Dijkstra no hay routing de internet (OSPF, IS-IS), no hay GPS, no hay planificación de red de telecomunicaciones. Los grafos de redes neuronales también heredan su lógica de recorrido. Dijkstra trabajaba en el Mathematisch Centrum de Ámsterdam con un computador **ARMAC** — es el primer algoritmo diseñado con una aplicación real de computación en mente.

**Conduce a:** ARPANET routing (1969) como aplicación directa · **Depende de:** Complejidad formal de TAOCP (1968) — el análisis riguroso llega después.

---

### 1962 · Quicksort — C. A. R. Hoare

**C. A. R. Hoare** (Tony Hoare) publica Quicksort en 1962 en *The Computer Journal*, con 28 años. El algoritmo: divide el array en torno a un pivote, ordena recursivamente cada mitad. Complejidad media: O(n log n). Peor caso: O(n²) — pero en la práctica es el algoritmo de ordenación más rápido para datos aleatorios durante décadas. La recursividad aquí no es un truco: es la estructura del problema. Hoare trabaja en Elliott Brothers, fabricante de ordenadores, cuando lo diseña — la necesidad era práctica. El patrón divide-and-conquer se convierte en técnica fundamental de diseño de algoritmos, de Mergesort a FFT.

**Conduce a:** TAOCP de Knuth (1968) — Quicksort es uno de los algoritmos que Knuth analiza formalmente · **Depende de:** Minimax (1928) — cadena de formalización algorítmica.

---

### 1968 · Knuth · TAOCP Vol 1 — Donald Knuth

**Donald Knuth** publica el Vol. 1 de *The Art of Computer Programming* (TAOCP) en 1968, en Stanford. Antes de Knuth, los algoritmos se describían informalmente, sin análisis de coste. Knuth formaliza la notación O() (aunque Landau la había introducido en 1909, Knuth la populariza en CS), el análisis amortizado, y el análisis probabilístico. Inventa MIX, un computador hipotético estándar para análisis comparativo. El Vol. 4B (el más reciente) se publicó en 2022 — el proyecto lleva más de 50 años activo. Knuth interrumpió la redacción en 1977 para crear TeX porque la composición tipográfica de los manuscritos era inaceptable. TeX es ahora el estándar de publicación científica.

**Conduce a:** Cook-Levin (1971), Lean 4 (2021) — antecedente de la formalización matemática como práctica · **Depende de:** Quicksort (1962) y los algoritmos que analiza; Lógica formal como fundamento.

---

### 1971 · Cook-Levin · NP — Stephen Cook / Leonid Levin

**Stephen Cook** (Universidad de Toronto) y **Leonid Levin** (Moscú, independientemente) demuestran en 1971 el teorema Cook-Levin: el problema de satisfacibilidad booleana (SAT) es NP-completo. Consecuencia: si SAT es resoluble en tiempo polinomial, entonces todos los problemas de NP también lo son. Define la frontera entre P (tratable) y NP (verificable en tiempo polinomial). La pregunta P=NP sigue abierta en 2026 — el Clay Mathematics Institute ofrece 1 millón de dólares por su resolución. Cook recibe el Premio Turing en 1982. La teoría de la complejidad se vuelve herramienta para demostrar que ciertos problemas (viajante, coloración de grafos, scheduling) no tienen solución eficiente general conocida.

**Conduce a:** Criptografía de clave pública (RSA depende de que factorizar sea difícil, es decir, que ciertos problemas sean "NP-hard") · DNA computing de Adleman (1994) — resolver un NP-completo con DNA · **Depende de:** TAOCP de Knuth (1968) — formalización del análisis; Gödel (1931) — los límites de lo demostrable inspiran los límites de lo computable.

---

### 1976 · Diffie-Hellman — Whitfield Diffie / Martin Hellman

**Whitfield Diffie** y **Martin Hellman** publican "New Directions in Cryptography" en noviembre de 1976. Proponen el primer protocolo de intercambio de claves sin canal seguro previo: dos partes que nunca se han comunicado antes pueden establecer un secreto compartido en presencia de un adversario que escucha todo. La seguridad descansa en la dificultad del logaritmo discreto. Antes de Diffie-Hellman, para comunicarte cifrado necesitabas haber intercambiado la clave en persona previamente. Con Diffie-Hellman, la web cifrada es posible. Sin este paper no hay HTTPS, no hay e-commerce, no hay mensajería cifrada moderna. Reciben el Premio Turing en 2015.

**Conduce a:** RSA (1977) — primer sistema de cifrado asimétrico completo · **Depende de:** Cook-Levin (1971) — la dureza computacional de ciertos problemas es el fundamento de la seguridad.

---

### 1977 · RSA — Ron Rivest / Adi Shamir / Leonard Adleman

**Ron Rivest**, **Adi Shamir** y **Leonard Adleman** (MIT) publican RSA en 1977. Primer sistema de cifrado de clave pública completamente funcional: mensaje cifrado con clave pública, descifrado solo con clave privada. La seguridad descansa en la dificultad de factorizar el producto de dos primos grandes. Rivest inventa RSA en una noche de insomnio tras una fiesta de Pésaj, según su propio relato. El algoritmo estaba clasificado en el Reino Unido (GCHQ lo había desarrollado independientemente en 1973, clasificado) hasta que Clifford Cocks lo desclasificó en 1997. RSA es hoy el algoritmo de clave pública más desplegado del mundo — y está directamente bajo amenaza del algoritmo de Shor (1994), que lo rompe en tiempo polinomial con un ordenador cuántico suficientemente grande.

**Conduce a:** MapReduce (2004) — siguiente eslabón en la cadena algorítmica; bajo amenaza directa de Shor · **Depende de:** Diffie-Hellman (1976) — el marco conceptual de la criptografía asimétrica.

---

### 1994 · DNA computing — Leonard Adleman

**Leonard Adleman** (USC) publica "Molecular Computation of Solutions To Combinatorial Problems" en *Science* en noviembre de 1994. Resuelve el problema del camino hamiltoniano para un grafo de 7 nodos usando cadenas de DNA: cada posible camino se codifica como una cadena de nucleótidos, las cadenas se mezclan en un tubo de ensayo, y la bioquímica selecciona por complementariedad las que son válidas. El cómputo tarda días, pero funciona. El mismo Adleman de RSA aplica ahora la dureza computacional de NP a un sustrato biológico. Demuestra el principio fundamental: la computación no requiere silicio — cualquier sustrato que procese información puede computar.

**Conduce a:** investigación en computación molecular y no convencional · **Depende de:** Cook-Levin (1971) — Adleman ataca un problema NP-completo (camino hamiltoniano).

---

### 1998 · PageRank — Larry Page / Sergey Brin

**Larry Page** y **Sergey Brin** (Stanford) publican "The Anatomy of a Large-Scale Hypertextual Web Search Engine" en enero-abril de 1998. Trabajo iniciado en 1996 como "BackRub". PageRank calcula la importancia de una página web como el eigenvector dominante del grafo de hiperenlaces: una página es importante si páginas importantes enlazan a ella. El algoritmo convierte un problema de búsqueda en un problema de álgebra lineal sobre un grafo de miles de millones de nodos. Page y Brin fundan Google ese mismo año. Sin PageRank, el directorio Yahoo o el AltaVista basado en keywords seguirían siendo la norma.

**Conduce a:** Google (NET) — aplicación directa; búsqueda semántica · **Depende de:** Dijkstra (1956) — algoritmia sobre grafos como antecedente; TAOCP — cultura del análisis algorítmico riguroso.

---

### 2004 · MapReduce — Jeffrey Dean / Sanjay Ghemawat

**Jeffrey Dean** y **Sanjay Ghemawat** (Google) publican el paper de MapReduce en 2004, en OSDI. El patrón: distribuir un cómputo masivo en dos fases — map (aplicar una función a cada elemento en paralelo) y reduce (agregar los resultados). La elegancia está en que el programador escribe solo esas dos funciones; el sistema se encarga de la distribución, la tolerancia a fallos y el balanceo de carga en miles de máquinas. Inspira Hadoop (2006, Yahoo/Doug Cutting), Spark (2009, AMPLab Berkeley), y todo el ecosistema big data de la siguiente década. Google usaba MapReduce para construir el índice web completo — el problema que PageRank resuelve teóricamente, MapReduce lo ejecuta a escala.

**Conduce a:** NoSQL y bases de datos distribuidas (cadena ALG → DATA); AWS cloud pública · **Depende de:** RSA y la infraestructura computacional que habilita el cómputo distribuido seguro.

---

### 2008 · Nakamoto consensus — Satoshi Nakamoto

**Satoshi Nakamoto** — identidad desconocida — publica "Bitcoin: A Peer-to-Peer Electronic Cash System" en octubre de 2008. Resuelve el problema del teniente bizantino a escala global: ¿cómo llegan a un consenso N nodos desconfiados sin autoridad central? La solución: proof-of-work como mecanismo de selección aleatoria pesado por poder computacional. El primero en resolver un puzzle criptográfico impone el siguiente bloque; la cadena más larga es la válida. Primera vez que un sistema distribuido sin administrador central mantiene estado consistente entre millones de nodos desconocidos entre sí. Funda la era cripto y abre la pregunta sobre consenso descentralizado más allá de la moneda.

**Conduce a:** Mecanismo de atención (2017) — siguiente eslabón en la cadena ALG; aplicaciones en identidad, contratos, votación · **Depende de:** RSA y criptografía de clave pública — Bitcoin usa ECDSA para firmas.

---

### 2017 · Attention — Ashish Vaswani et al.

**Ashish Vaswani**, **Noam Shazeer**, **Niki Parmar**, **Jakob Uszkoreit**, **Llion Jones**, **Aidan N. Gomez**, **Łukasz Kaiser** y **Illia Polosukhin** (Google Brain / Google Research) publican "Attention Is All You Need" en junio de 2017. El mecanismo de atención escalado por producto-punto ya existía en formas previas (Bahdanau 2015), pero este paper lo convierte en la primitiva central: reemplaza convolucioon y recurrencia por atención multi-cabeza, posibilitando paralelización completa durante el entrenamiento. Sin esto no hay Transformer; sin Transformer no hay GPT, Claude, Gemini ni Llama.

**Conduce a:** Transformer (2017) — el paper es simultáneo y sinónimo; Algoritmos agénticos (2024) · **Depende de:** Word2Vec (2013) — embeddings como representación que el attention opera; Nakamoto (2008) — cadena algorítmica formal.

---

### 2024 · Algoritmos agénticos — Múltiples autores

La cadena que va de **ReAct** (Yao et al., Princeton/Google, 2022) a **Tree-of-Thoughts** (Yao et al., 2023), **MCTS sobre LLMs**, **tool use estructurado** (Anthropic, OpenAI, 2023-2024) y **planning con verificación** (múltiples equipos). El patrón que emerge: los LLMs actúan como heurísticas dentro de bucles de búsqueda clásica. Tree-of-Thoughts aplica búsqueda en árbol (el minimax de Von Neumann, 1928) pero con un LLM evaluando los nodos. MCTS (Monte Carlo Tree Search) — el mismo algoritmo que AlphaGo usó en Go — se combina con modelos de lenguaje para razonamiento complejo. La IA generativa regresa a los algoritmos de búsqueda clásica como estructura; el LLM aporta la heurística que antes tenía que programarse a mano.

**Conduce a:** Claude Opus 4.7 y los agentes IA de 2025-2026 — aplicación directa · **Depende de:** Attention/Transformer (2017) — el LLM que actúa como heurística; AlphaGo (2016) — MCTS ya demostrado en juegos.

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1928 | John von Neumann | Teorema minimax; fundación de la teoría de juegos | Hungría / EE.UU. / Princeton |
| 1956 | Edsger Dijkstra | Algoritmo de camino más corto en grafos | Países Bajos / Mathematisch Centrum Ámsterdam |
| 1962 | C. A. R. Hoare (Tony Hoare) | Quicksort; patrón divide-and-conquer | Reino Unido / Elliott Brothers |
| 1968 | Donald Knuth | TAOCP; notación O(); análisis formal de algoritmos; TeX | EE.UU. / Stanford |
| 1971 | Stephen Cook | Teorema Cook-Levin; NP-completitud | Canadá / Universidad de Toronto |
| 1971 | Leonid Levin | Teorema Cook-Levin (independiente) | URSS / Moscú |
| 1976 | Whitfield Diffie | Protocolo de intercambio de claves Diffie-Hellman | EE.UU. / Stanford |
| 1976 | Martin Hellman | Protocolo de intercambio de claves Diffie-Hellman | EE.UU. / Stanford |
| 1977 | Ron Rivest | RSA; criptografía de clave pública práctica | EE.UU. / MIT |
| 1977 | Adi Shamir | RSA | EE.UU. / MIT |
| 1977 | Leonard Adleman | RSA; DNA computing (1994) | EE.UU. / MIT / USC |
| 1994 | Leonard Adleman | DNA computing; computación con sustrato biológico | EE.UU. / USC |
| 1998 | Larry Page | PageRank; fundación de Google | EE.UU. / Stanford |
| 1998 | Sergey Brin | PageRank; fundación de Google | EE.UU. / Stanford |
| 2004 | Jeffrey Dean | MapReduce; computación distribuida masiva | EE.UU. / Google |
| 2004 | Sanjay Ghemawat | MapReduce | EE.UU. / Google |
| 2006 | Doug Cutting | Hadoop (implementación open source de MapReduce) | EE.UU. / Yahoo |
| 2008 | Satoshi Nakamoto | Protocolo Bitcoin; consenso distribuido sin autoridad central | Identidad desconocida |
| 2017 | Ashish Vaswani | Mecanismo de atención escalado; paper "Attention Is All You Need" | EE.UU. / Google Brain |
| 2017 | Noam Shazeer | Co-autor del mecanismo de atención | EE.UU. / Google Brain |

---

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[01_LOGICA#1879 · Lógica de predicados]] → Frege influye en Minimax y en Von Neumann
- ↗ De [[01_LOGICA#1931 · Incompletitud · Entscheidungsproblem]] → Gödel habilita Cook-Levin (los límites de lo demostrable inspiran los límites de lo computable)
- ↗ De [[04_ELECTRONICA#1946 · ENIAC]] → ENIAC hace viable el Monte Carlo (simulación); hardware que ejecuta los algoritmos
- ↗ De [[05_SOFTWARE#1958 · LISP]] → Word2Vec hereda representación simbólica; ecosistema que ejecuta algoritmos
- ↗ De [[IA#2013 · Word2Vec]] → embeddings que el mecanismo de atención opera
- ↗ De [[IA#2016 · AlphaGo]] → MCTS demostrado, base de algoritmos agénticos

Lo que esta columna **aporta** a otras columnas:

- ↘ De Dijkstra (1956) → habilita [[NET#1969 · ARPANET]] — routing de internet
- ↘ De Cook-Levin (1971) → habilita [[CUA#1994 · Algoritmo de Shor]] — complejidad computacional de la factorización
- ↘ De RSA (1977) → bajo amenaza de [[CUA#1994 · Algoritmo de Shor]]
- ↘ De MapReduce (2004) → habilita [[DATA#2007 · NoSQL · BigTable · Dynamo]]; [[NET#2006 · AWS · cloud pública]]
- ↘ De Attention (2017) → parallel con [[IA#2017 · Transformer]] — mismo paper, primitiva algorítmica
- ↘ De Algoritmos agénticos (2024) → parallel con [[IA#2026 · Claude Opus 4.7 · 1M]]
- ↘ De TAOCP (1968) → habilita [[01_LOGICA#2021 · Lean 4 + mathlib]] (formalización como práctica)

---

## Lectura siguiente

- Si te interesa cómo los algoritmos de búsqueda se aplican en IA (Deep Blue, AlphaGo, agentes) → [[IA]] en el grafo
- Si quieres ver cómo RSA y Diffie-Hellman quedan bajo amenaza cuántica → [[CUA]] en el grafo
- Si quieres la cadena que convierte MapReduce en infraestructura cloud → [[NET]] en el grafo
- Si quieres la cadena lógica que da fundamento a Cook-Levin → [[01_LOGICA]]

---

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
