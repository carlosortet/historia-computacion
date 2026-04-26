---
columna: LÓGICA
cat: LOG
nodos_cubiertos: 10
periodo: 1673 → 2024
---

# LÓGICA · Del binario a la prueba automática

> Tres siglos de reducción: el razonamiento humano convertido en símbolo, el símbolo en circuito, el circuito en lenguaje, el lenguaje en máquina que prueba matemáticas sola.

## El arco

La columna LÓGICA arranca con Leibniz y su obsesión de convertir el pensamiento en cálculo. Durante dos siglos, la lógica avanza dentro de la filosofía y las matemáticas puras, sin tocar ninguna máquina. El giro llega en 1937, cuando Shannon demuestra que los operadores de Boole son el plano eléctrico de un circuito. A partir de ahí, la lógica deja de ser abstracción y se convierte en ingeniería. El segundo arco, que empieza en Gödel y Turing, traza los límites de lo que puede demostrarse: y esos límites fuerzan la aparición del ordenador. El tercer arco, abierto en 2013 con HoTT, pregunta si las máquinas pueden hacer matemáticas formales por sí solas. En 2024, AlphaProof responde que sí, al nivel de olimpiada.

## La cadena

### 1673 · Leibniz · binario — Gottfried Wilhelm Leibniz

**Gottfried Wilhelm Leibniz** construye la Stepped Reckoner entre 1672 y 1674 en París: primera calculadora mecánica capaz de las cuatro operaciones. En paralelo, formaliza el sistema binario en *Explication de l'Arithmétique Binaire* (1679). Su motivación es explícita: "Es indigno que hombres excelentes pierdan horas como esclavos en la labor de cálculos." El aparato no es confiable en la práctica, pero la notación binaria que publica es perfecta. Pasarán 168 años antes de que Boole le dé estructura algebraica.

**Conduce a:** Álgebra booleana (1847) · **Depende de:** Pascalina de Pascal (1642) — primer escalón mecánico que Leibniz mejora.

---

### 1847 · Álgebra booleana — George Boole

**George Boole** publica *The Mathematical Analysis of Logic* (1847) y *Laws of Thought* (1854) desde Cork (Irlanda). Sin doctorado, enseña en el Queen's College. Formaliza la lógica clásica como un álgebra de dos valores: AND, OR, NOT como operaciones cerradas. La motivación es teológica y filosófica — busca "las leyes del pensamiento" — pero el armazón matemático es ajedrez puro. No hay máquina que lo ejecute. Muere en 1864 a los 49 años sin ver ninguna aplicación técnica.

**Conduce a:** Lógica de predicados de Frege (1879) · **Depende de:** sistema binario de Leibniz (1673) — sin notación de dos valores no hay álgebra de dos valores.

---

### 1879 · Lógica de predicados — Gottlob Frege

**Gottlob Frege** publica *Begriffsschrift* ("escritura conceptual") en 1879, con 31 años, en Jena. Es la primera notación lógica que incluye cuantificadores (∀, ∃) y permite expresar enunciados sobre objetos y sus propiedades con precisión matemática completa. Boole podía formalizar "A y B implica C"; Frege puede formalizar "para todo x, si x es par entonces x no es primo (salvo el 2)". La notación bidimensional de *Begriffsschrift* es ilegible — Russell y Peano ignoran el formato pero absorben las ideas. El trabajo directo de Frege influye en Hilbert, en Russell y, a través de ellos, en Gödel y Turing.

**Conduce a:** Incompletitud de Gödel (1931) · **Depende de:** Álgebra booleana (1847) — Frege conoce el trabajo de Boole y lo considera insuficiente.

---

### 1931 · Incompletitud · Entscheidungsproblem — Kurt Gödel / David Hilbert

**David Hilbert** plantea el Entscheidungsproblem en 1928: ¿existe un procedimiento mecánico capaz de decidir, para cualquier enunciado matemático, si es verdadero o falso? **Kurt Gödel** responde en 1931, desde Viena, con dos teoremas de incompletitud: en cualquier sistema formal suficientemente potente, hay verdades que no se pueden probar dentro de ese sistema. El edificio que Hilbert quería construir tiene fisuras estructurales por definición. El resultado de Gödel no destruye las matemáticas, pero traza un perímetro: hay preguntas que ningún axioma resuelve desde dentro.

**Conduce a:** Lambda calculus de Church (1936), Máquina de Turing (1936) — ambos responden directamente al Entscheidungsproblem · **Depende de:** Lógica de predicados de Frege (1879) — sin notación formal precisa, Gödel no puede construir su argumento de autoref.

---

### 1936 · Lambda calculus — Alonzo Church

**Alonzo Church** publica el cálculo lambda en 1936 en Princeton. Define una notación formal para funciones y su aplicación: cualquier función computable puede expresarse como combinación de abstracciones lambda. Ese mismo año, simultáneamente e independientemente de Turing, demuestra que el Entscheidungsproblem es indecidible. Church y Turing trabajan en el mismo departamento; Turing lee el paper de Church antes de publicar el suyo. La tesis Church-Turing: cualquier función computable por un proceso mecánico es computable por una Máquina de Turing, y también por el cálculo lambda — son equivalentes.

**Conduce a:** LISP (1958) — McCarthy construye LISP directamente sobre el cálculo lambda · Programación funcional moderna · **Depende de:** Gödel (1931) — la incompletitud es el problema que Church ataca.

---

### 1937 · Lógica → circuitos — Claude Shannon

**Claude Shannon**, con 21 años, escribe su tesis de máster en el MIT en 1937. Título: *A Symbolic Analysis of Relay and Switching Circuits*. La tesis central: los relés eléctricos se comportan exactamente como los operadores del álgebra de Boole. Un relé abierto = 0, un relé cerrado = 1. AND = relés en serie, OR = relés en paralelo. Llevó 90 años desde Boole (1847) hasta que alguien hiciera esta conexión. Shannon lo vio porque trabajaba simultáneamente con circuitos físicos en Bell Labs y con lógica matemática en sus clases del MIT. La tesis no tiene más de 60 páginas. Es posiblemente la tesis de máster más influyente del siglo XX.

**Conduce a:** Z3 de Zuse (1941), Colossus (1944), ENIAC (1946) — puente directo entre lógica y electrónica · **Depende de:** Álgebra booleana de Boole (1847) — aplicación directa al dominio eléctrico.

---

### 1948 · Teoría de la Información — Claude Shannon

**Claude Shannon** publica *A Mathematical Theory of Communication* en julio-octubre de 1948, en el Bell System Technical Journal. Dos artículos en dos entregas. Define el **bit** como unidad de información, establece la entropía de Shannon como medida de incertidumbre, y prueba los límites teóricos de transmisión sobre cualquier canal con ruido. La *Scientific American* lo llamará "la Magna Carta de la era de la información". El biólogo **James Gleick** sostiene que este paper es más importante que el transistor. Sin él no hay compresión de datos, no hay criptografía moderna, no hay codificación de canal, no hay cálculo de capacidad de redes neuronales.

**Conduce a:** TCP/IP y toda la comunicación digital — la teoría del canal es el sustrato matemático · **Depende de:** Tesis Shannon 1937 — misma mente, aplicación extendida al dominio de la comunicación.

---

### 2013 · HoTT Book · Univalent Foundations — Vladimir Voevodsky et al.

**The Univalent Foundations Program** — 40 autores reunidos en el Institute for Advanced Study (IAS) de Princeton — publica el *HoTT Book* en 2013. **Vladimir Voevodsky** (ganador de la Medalla Fields en 2002, ahora en IAS) aporta el axioma de univalencia: dos estructuras matemáticamente equivalentes son, en este sistema, literalmente idénticas. HoTT conecta la teoría de tipos de Martin-Löf con la topología algebraica. El resultado práctico: un sistema donde las pruebas matemáticas pueden verificarse automáticamente por ordenador. Voevodsky se convierte al HoTT tras encontrar un error en uno de sus propios teoremas que pasó años sin detectarse — la formalización mecánica como corrector de errores humanos.

**Conduce a:** Lean 4 + mathlib (2021) · **Depende de:** Teoremas de incompletitud de Gödel (1931) — el debate fundacional que HoTT reabre; Lambda calculus de Church (1936) — teoría de tipos como descendiente.

---

### 2021 · Lean 4 + mathlib — Leonardo de Moura et al.

**Leonardo de Moura** (Microsoft Research) lanza Lean 4 en 2021: lenguaje de programación y asistente de pruebas simultáneamente. La clave es **mathlib**: una biblioteca matemática colaborativa mantenida por cientos de matemáticos. En 2022-2023, **Peter Scholze** (Medalla Fields 2018) pide ayuda para formalizar su "liquid tensor experiment" — una prueba de 100+ páginas que él mismo no está seguro de que sea correcta. La comunidad Lean la formaliza en meses. El ordenador confirma: la prueba es correcta. Herramientas similares: Isabelle, Coq, Agda. Lean domina por su ergonomía y por mathlib.

**Conduce a:** AlphaProof (2024) · **Depende de:** HoTT Book (2013) — sustrato teórico; TAOCP de Knuth (1968) — formalización del análisis algorítmico como antecedente cultural.

---

### 2024 · AlphaProof / AlphaGeometry — DeepMind

**DeepMind** publica AlphaProof y AlphaGeometry en julio de 2024. En la IMO 2024 (International Mathematical Olympiad), el sistema resuelve 4 de 6 problemas, incluyendo dos de los tres más difíciles. Medalla de plata equivalente — el primer resultado de plata para un sistema automatizado en la olimpiada más exigente del mundo. AlphaProof combina un modelo de lenguaje con el asistente de pruebas Lean: el LLM propone pasos de prueba, Lean verifica cada uno formalmente. AlphaGeometry usa un sistema diferente (cálculo simbólico + LLM) para los problemas de geometría.

**Conduce a:** era de formalización matemática asistida por IA — el círculo Boole → Hilbert → Gödel → Turing → IA razonando en lógica formal se cierra. · **Depende de:** Lean 4 (2021) — motor de verificación; Transformer (2017) — LLM que propone los pasos.

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1673 | Gottfried Wilhelm Leibniz | Sistema binario formalizado; primera calculadora de 4 operaciones | Alemania / París |
| 1847 | George Boole | Álgebra lógica AND/OR/NOT sobre dos valores | Irlanda / Queen's College Cork |
| 1879 | Gottlob Frege | Lógica de predicados con cuantificadores; primera notación formal completa | Alemania / Universidad de Jena |
| 1928 | David Hilbert | Entscheidungsproblem — el problema que Gödel y Turing resuelven | Alemania / Universidad de Gotinga |
| 1931 | Kurt Gödel | Teoremas de incompletitud — límites formales de los sistemas matemáticos | Austria / Universidad de Viena |
| 1936 | Alonzo Church | Cálculo lambda; indecidibilidad del Entscheidungsproblem | EE.UU. / Princeton |
| 1937 | Claude Shannon | Aplicación del álgebra de Boole a circuitos eléctricos | EE.UU. / MIT / Bell Labs |
| 1948 | Claude Shannon | Teoría de la información; definición del bit; entropía | EE.UU. / Bell Labs |
| 2013 | Vladimir Voevodsky | Axioma de univalencia; Univalent Foundations | Rusia / EE.UU. / IAS Princeton |
| 2021 | Leonardo de Moura | Lean 4; asistente de pruebas práctico para matemáticos | Brasil / Microsoft Research |
| 2021 | Peter Scholze | Formalización del liquid tensor experiment en Lean | Alemania / Universidad de Bonn |

---

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[03_ARQUITECTURA#1642 · Pascalina]] → Leibniz mejora el cálculo mecánico de Pascal para construir la Stepped Reckoner
- ↗ De [[03_ARQUITECTURA#1936 · Máquina universal]] → Turing responde directamente al Entscheidungsproblem (paralelo a Church 1936)
- ↗ De [[02_ALGORITMOS#1968 · Knuth · TAOCP Vol 1]] → antecedente cultural de la formalización algorítmica que habilita Lean 4
- ↗ De [[05_SOFTWARE#2021 · GitHub Copilot]] / [[03_ARQUITECTURA]] Transformer → AlphaProof usa un LLM como generador de pasos de prueba

Lo que esta columna **aporta** a otras columnas:

- ↘ De Shannon 1937 → habilita [[04_ELECTRONICA#1941 · Z3]], [[04_ELECTRONICA#1944 · Colossus]], [[04_ELECTRONICA#1946 · ENIAC]] — puente lógica-electrónica
- ↘ De Church (lambda calculus) → habilita [[05_SOFTWARE#1958 · LISP]] y toda la programación funcional
- ↘ De Gödel → habilita [[02_ALGORITMOS#1971 · Cook-Levin · NP]] (vía cadena Gödel → Turing → complejidad)
- ↘ De Shannon 1948 → habilita TCP/IP y toda la comunicación digital — sustrato matemático de [[NET]]
- ↘ De Lean 4 → habilita [[#2024 · AlphaProof / AlphaGeometry]]

---

## Lectura siguiente

- Si te interesa cómo la lógica se convierte en hardware físico → [[04_ELECTRONICA]]
- Si quieres ver cómo el cálculo lambda se convierte en lenguajes de programación → [[05_SOFTWARE]]
- Si quieres la cadena de algoritmos que nace de los límites lógicos (Cook-Levin, Shor) → [[02_ALGORITMOS]]
- Si quieres ver cómo se construyen las máquinas que ejecutan la lógica → [[03_ARQUITECTURA]]

---

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
