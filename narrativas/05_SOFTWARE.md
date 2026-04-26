---
columna: SOFTWARE
cat: SOF
nodos_cubiertos: 17
periodo: 1945 → 2024
---

# SOFTWARE · Del primer lenguaje olvidado al agente que programa

> Setenta años de reducir la distancia entre lo que el ser humano piensa y lo que la máquina ejecuta.

## El arco

La columna SOFTWARE es la historia de la abstracción como herramienta. Cada generación de esta columna hace lo mismo: añade una capa entre el programador y el hardware para que el programador piense en términos más cercanos al problema y más lejanos al silicio. Zuse lo intenta en 1945 con Plankalkül, y nadie le hace caso. Hopper lo consigue en 1952 con el compilador A-0: por primera vez, el ordenador traduce su propio lenguaje. Entonces viene la proliferación — FORTRAN para ciencia, COBOL para negocio, LISP para IA simbólica, ALGOL como gramática madre de casi todo lo que viene. Unix en 1969 unifica con una filosofía: archivos como interfaz universal, herramientas pequeñas encadenables. C es la lengua que Unix habla. GNU y Linux convierten esa filosofía en sistema distribuido libre. Git convierte la colaboración en grafo de versiones. Docker convierte el entorno en dato. Copilot añade la IA como interlocutor. Los agentes de 2024 cierran el ciclo: el software que programa software.

## La cadena

### 1945 · Plankalkül — Konrad Zuse

**Konrad Zuse** escribe el Plankalkül entre 1942 y 1945 mientras trabaja en los Z3 y Z4, en la Alemania de la guerra. Es el primer lenguaje de programación de alto nivel del mundo: incluye tipos de datos estructurados, estructuras de control (condicionales, bucles), expresiones lógicas y matriciales. Zuse diseña Plankalkül para ser compilado a lenguaje de máquina, pero nunca lo implementa — Alemania posguerra no tiene infraestructura computacional para ejecutarlo. El lenguaje se publica en 1972 y se compila por primera vez en 1975. Para entonces, FORTRAN tiene 18 años y ALGOL 15. Los conceptos de Plankalkül — tipos, estructuras, asignación — se reinventan independientemente en todos esos lenguajes. Zuse los había visto primero.

**Conduce a:** FORTRAN (1957) — paralelo en concepto (lenguaje de alto nivel) aunque ignorado · **Depende de:** Z3 (1941) — la máquina para la que diseña el lenguaje.

---

### 1952 · Compilador A-0 — Grace Hopper

**Grace Hopper** desarrolla el compilador A-0 (*Arithmetic Language, version 0*) en UNIVAC en 1952. El A-0 no es un compilador en el sentido moderno — es más un linker de subrutinas — pero establece el principio: el ordenador puede traducir instrucciones simbólicas a código de máquina. Hopper tiene que superar la resistencia de sus jefes y colegas ("los ordenadores no pueden hacer eso"). Su argumento: si le enseñas al ordenador a entender código próximo al inglés, puedes tener cien programadores en lugar de uno. El A-0 habilita el MATH-MATIC y luego el FLOW-MATIC, que es la base directa de COBOL. Hopper había aprendido a programar en el Harvard Mark I en 1944 — de máquinas electromecánicas a compiladores en 8 años.

**Conduce a:** FORTRAN (1957), COBOL (1959) · **Depende de:** EDSAC (1949) — arquitectura que hace posible el compilador; Harvard Mark I (1944) — donde Hopper aprende.

---

### 1957 · FORTRAN — John Backus

**John Backus** (IBM) lidera el equipo que publica FORTRAN (*FORmula TRANslation*) en abril de 1957 para el IBM 704. La apuesta era arriesgada: muchos creían que un compilador nunca podría generar código tan eficiente como el ensamblador escrito a mano. El equipo de Backus dedica 18 meses. El resultado: código casi tan eficiente como el ensamblador, y un lenguaje que los científicos e ingenieros pueden usar directamente. FORTRAN introduce el array multidimensional, las funciones matemáticas nativas, y el bucle DO. Backus luego crea la notación BNF (*Backus-Naur Form*) para describir la gramática de lenguajes formales — fundamento de todos los parsers modernos. FORTRAN 77, 90, 2003, 2018: el lenguaje sigue activo en computación científica y de alto rendimiento.

**Conduce a:** ALGOL 60 (1960), COBOL (1959) · **Depende de:** Compilador A-0 (1952) — Hopper demuestra que es posible.

---

### 1958 · LISP — John McCarthy

**John McCarthy** diseña LISP (*LISt Processor*) en el MIT en 1958, publicado en 1960. Dos ideas fundacionales: el código es datos (homoiconicidad — un programa LISP es una lista, y las listas son el tipo de datos nativo) y el cálculo lambda de Church como sustrato matemático. McCarthy inventa también el *garbage collector* — la gestión automática de memoria. LISP es la lengua franca de la IA simbólica durante cuatro décadas. Todos los sistemas expertos de los 70 y 80 se escriben en LISP. La función map(), filter() y reduce() que hoy usa Python heredan directamente de LISP. Macros, metaprogramación, programación funcional: todo pasa por LISP antes de llegar a los lenguajes modernos.

**Conduce a:** Sistemas expertos (IA simbólica); Word2Vec (la representación simbólica como antecedente); programación funcional moderna · **Depende de:** Lambda calculus de Church (1936) — sustrato matemático directo; Conferencia Dartmouth (1956) — contexto IA.

---

### 1960 · ALGOL 60 — Comité internacional

**ALGOL 60** (*Algorithmic Language 1960*) es el resultado de un comité internacional — europeos y americanos — que incluye a **Peter Naur**, **John Backus**, **Alan Perlis** y **Adriaan van Wijngaarden**. ALGOL 60 introduce la estructura de bloques (begin/end), el alcance léxico, los procedimientos recursivos y la notación BNF para describir su propia gramática. Nunca fue adoptado comercialmente a escala masiva (IBM apostó por FORTRAN y COBOL), pero se convierte en el lenguaje de referencia para describir algoritmos en papers académicos durante 20 años. De ALGOL descienden directamente Pascal, C, Java, y prácticamente todos los lenguajes de programación modernos con sintaxis de llaves o palabras clave de bloque.

**Conduce a:** Programación estructurada de Dijkstra (1968) — ALGOL es el lenguaje que Dijkstra usa · **Depende de:** FORTRAN (1957) — ALGOL responde a las limitaciones de FORTRAN.

---

### 1959 · COBOL — Grace Hopper / CODASYL

**CODASYL** (*Conference on Data Systems Languages*, convocada por el DoD americano) define COBOL (*COmmon Business-Oriented Language*) en 1959. El primer compilador funciona en 1960. **Grace Hopper** es la influencia técnica central — su FLOW-MATIC es el antecedente directo. COBOL tiene una sintaxis deliberadamente cercana al inglés: `MOVE SALARY TO GROSS-PAY` en lugar de operadores matemáticos. El objetivo: que los directivos de empresa puedan leer (si no escribir) los programas. En 2026, COBOL procesa el 70% de las transacciones bancarias mundiales. Se estiman más de 200.000 millones de líneas de COBOL en producción. El banco que intenta migrarlo a Java normalmente aborta y vuelve a COBOL.

**Conduce a:** Software empresarial durante décadas; sustrato del IBM System/360 · **Depende de:** Compilador A-0 (1952) de Hopper; FORTRAN (1957) — paralelo contemporáneo; LEO I (1951) — primero en demostrar que el negocio necesita su propio software.

---

### 1961 · CTSS · timesharing — Fernando Corbató

**Fernando Corbató** (MIT) implementa el CTSS (*Compatible Time-Sharing System*) en el IBM 7090 en 1961. Antes del CTSS, un ordenador ejecutaba un trabajo a la vez — batch processing. Corbató demuestra que un único mainframe puede atender a múltiples usuarios simultáneos, intercalando sus trabajos con conmutación rápida de contexto. Cada usuario tiene la ilusión de que el ordenador es suyo. El CTSS también introduce las contraseñas en 1962 — la primera vez que un sistema informático tiene cuentas de usuario con credenciales. Corbató recibe el Premio Turing en 1990. El CTSS es el padre conceptual de Multics (1969), que es el padre de Unix.

**Conduce a:** Unix (1969) — cadena CTSS → Multics → Unix · **Depende de:** Harvard Mark I (1944) — contexto MIT de computación.

---

### 1968 · Programación estructurada — Edsger Dijkstra

**Edsger Dijkstra** publica la carta al editor *Go To Statement Considered Harmful* en *Communications of the ACM* en marzo de 1968. El argumento: el `GOTO` hace que el código sea imposible de razonar — el flujo de ejecución puede saltar a cualquier línea desde cualquier otra, sin estructura. La alternativa: secuencia, selección (if/else), iteración (while/for). Estas tres estructuras son suficientes para cualquier cómputo (teorema de Böhm-Jacopini, 1966). La programación estructurada no es un lenguaje específico sino una disciplina. Dijkstra también escribe las primeras notas sobre verificación formal de programas — demostrar matemáticamente que un programa es correcto. Funda la idea de que programar es una actividad intelectual que puede hacerse bien o mal de forma sistemática.

**Conduce a:** Unix (1969) — el estilo de programación que Thompson y Ritchie adoptan; ALGOL 60 como lenguaje que Dijkstra usa para demostrar sus ideas · **Depende de:** ALGOL 60 (1960).

---

### 1969 · Hamilton · Apollo 11 — Margaret Hamilton

**Margaret Hamilton** dirige el equipo de software de vuelo del Apollo 11 en el MIT Instrumentation Lab. El momento clave: el 20 de julio de 1969, a 3 minutos del alunizaje, el AGC (*Apollo Guidance Computer*) genera alarmas de sobrecarga (códigos 1202, 1201). El sistema operativo de Hamilton tiene un sistema de prioridades que descarta tareas de baja prioridad y protege las críticas — el radar de encuentro genera datos basura, el SO los tira, y el proceso de alunizaje continúa. Sin ese mecanismo de prioridades, la misión se aborta. Hamilton acuña el término "software engineering" para describir su disciplina y forzar su reconocimiento institucional como ingeniería. Recibe la Medalla Presidencial de la Libertad de Obama en 2016.

**Conduce a:** Programación estructurada — paralelo en tiempo; funda la ingeniería del software como profesión · **Depende de:** Von Neumann (1945) — arquitectura del AGC; programación estructurada — misma era.

---

### 1969 · Unix — Ken Thompson / Dennis Ritchie

**Ken Thompson** y **Dennis Ritchie** crean Unix en Bell Labs (Murray Hill, New Jersey) en 1969, empezando con un PDP-7 que nadie más quería. La filosofía: cada herramienta hace una sola cosa bien; la composición de herramientas resuelve problemas complejos; todo es un archivo. Thompson escribe el kernel inicial en ensamblador; Ritchie diseña C para reescribirlo. Unix introduce la *pipeline* (la salida de un programa es la entrada del siguiente), el filesystem jerárquico con inodes, y los procesos como abstracción. En 1973, Unix se reescribe completamente en C — primer sistema operativo portátil entre arquitecturas de hardware distintas. La cadena Unix → BSD → macOS → iOS y Unix → Linux → Android → servidores cubre el 90%+ del cómputo moderno.

**Conduce a:** C (1973), GNU (1983); sustrato de macOS, Linux, Android, iOS · **Depende de:** Programación estructurada (1968) — filosofía; CTSS (1961) — modelo multiusuario; Manchester Atlas (1962) — memoria virtual como prerequisito.

---

### 1973 · Lenguaje C — Dennis Ritchie

**Dennis Ritchie** diseña C entre 1969 y 1973 en Bell Labs, inicialmente como herramienta para reescribir Unix. C es de bajo nivel suficiente para controlar hardware (punteros, manipulación de bits) pero de alto nivel suficiente para ser portátil entre arquitecturas. En 1978, Ritchie y **Brian Kernighan** publican *The C Programming Language* ("K&R") — uno de los libros técnicos más influyentes del siglo XX. El estándar ANSI C llega en 1989. C es el padre directo de C++ (1985), Java (1995), C# (2000), y el abuelo de prácticamente todos los lenguajes de sistemas modernos. Rust y Go, en 2010-2015, se definen explícitamente como alternativas a C para sistemas seguros.

**Conduce a:** C++ (1985) — suma POO sobre C; Go y Rust (2010) — sucesores de sistemas · **Depende de:** Unix (1969) — C nace para escribir Unix.

---

### 1983 · GNU Project — Richard Stallman

**Richard Stallman** anuncia el proyecto GNU (*GNU's Not Unix*) el 27 de septiembre de 1983, en net.unix-wizards y net.usoft. El manifiesto GNU (1985) artícula la filosofía: el software debe ser libre de usar, estudiar, modificar y redistribuir. La GPL (*GNU General Public License*, 1989) implementa el *copyleft*: cualquier obra derivada de software GPL debe también ser GPL. Stallman construye el compilador GCC, el editor Emacs, el debugger GDB, y docenas de herramientas. Lo que falta en 1991 es el kernel. Stallman no es solamente ideólogo — es un ingeniero excepcional: GCC compila más lenguajes que cualquier otro compilador de su época.

**Conduce a:** Linux (1991) — GNU + Linux = sistema operativo completo · **Depende de:** Unix (1969) — GNU es una reimplementación libre de Unix; Manchester Atlas — herencia académica.

---

### 1991 · Linux kernel — Linus Torvalds

**Linus Torvalds** (Universidad de Helsinki) publica la primera versión del kernel Linux el 17 de septiembre de 1991 en comp.os.minix: "I'm doing a (free) operating system (just a hobby, won't be big and professional like GNU) for 386(486) AT clones." En 1992 adopta la GPL. En 1993, las distribuciones Slackware y Debian aparecen. Linux + herramientas GNU = sistema operativo completo y libre. Hoy Linux corre en el 96.4% de los servidores web, el 100% de las supercomputadoras del TOP500 (desde 2017), y es la base de Android (70%+ de smartphones). El modelo de desarrollo distribuido de Linux — miles de contribuidores coordinados por listas de correo y, desde 2005, por Git — es el prototipo de la colaboración open source.

**Conduce a:** Docker (2013), Android (2008) · **Depende de:** GNU (1983) — las herramientas; C (1973) — el lenguaje; Unix (1969) — la filosofía.

---

### 2005 · Git — Linus Torvalds

**Linus Torvalds** escribe Git en 10 días de abril de 2005, tras un conflicto con BitKeeper (la herramienta de control de versiones propietaria que usaba para el kernel Linux). El diseño es radical para su época: distribuido (cada clone es un repositorio completo), branches baratas (crear una rama cuesta nanosegundos), modelo de snapshots en lugar de deltas, y un grafo de commits como estructura de datos fundamental. El primer commit de Git usa Git para guardarse a sí mismo. GitHub (fundado 2008 por **Tom Preston-Werner**, **Chris Wanstrath** y **PJ Hyett**) lo populariza globalmente. En 2026, más de 100 millones de repositorios en GitHub.

**Conduce a:** Docker (2013) — Git habilita el versionado de Dockerfiles e imágenes · **Depende de:** C (1973) — Git está escrito en C; Linux (1991) — el ecosistema que lo necesita.

---

### 2013 · Docker — Solomon Hykes

**Solomon Hykes** presenta Docker en la PyCon US 2013 (13 de marzo), en una sesión de 5 minutos que termina con aplausos sostenidos. Docker populariza los contenedores Linux — una tecnología que existía (Linux namespaces desde 2002, cgroups desde 2007) pero que nadie había empaquetado de forma usable. La idea: un contenedor es una imagen (datos) + un proceso. La imagen incluye el sistema de archivos, las dependencias, la configuración. Se ejecuta igual en el portátil del desarrollador y en producción. dotCloud (la empresa de Hykes) pivota completamente a Docker y se renombra Docker Inc. Kubernetes (Google, 2014) orquesta contenedores a escala.

**Conduce a:** Kubernetes (NET) · **Depende de:** Linux (1991) — los namespaces y cgroups del kernel; Git (2005) — control de versiones de las imágenes.

---

### 2021 · GitHub Copilot — GitHub + OpenAI

**GitHub** y **OpenAI** lanzan GitHub Copilot en fase técnica preview en junio de 2021, con disponibilidad general en junio de 2022. Copilot usa Codex — un descendiente de GPT-3 ajustado en código público de GitHub — para completar código en tiempo real dentro del editor. El cambio de paradigma: el programador describe la intención en comentarios o nombres de función, y la IA genera la implementación. En el primer año de disponibilidad general, GitHub reporta que Copilot genera el 40% del código en los archivos donde está activo. Es el primer *AI pair programmer* masivo. El mercado de herramientas IA para programación no existía en 2020; en 2024 es un campo con decenas de competidores.

**Conduce a:** Agentes de código (2024) · **Depende de:** Transformer (2017) — Codex es un transformer; Linux/Git/Docker — el ecosistema de código abierto sobre el que se entrena.

---

### 2024 · Coding agents — Múltiples equipos

**Cursor** (Anysphere, fundada 2022) · **Aider** (Paul Gauthier) · **Claude Code** (Anthropic) · **Devin** (Cognition Labs) · **Cline** (open source). Los IDEs habitados por agentes IA que entienden la codebase completa, ejecutan comandos, leen errores, iteran. La diferencia con Copilot: el agente tiene contexto del repositorio entero (no solo el archivo abierto), puede ejecutar tests y leer su output, puede modificar múltiples archivos, puede buscar en la web documentación. **Andrej Karpathy** acuña el término *vibe coding* en febrero de 2025: programar describiendo la intención en lenguaje natural y dejando que el agente escriba e itere el código. El programador pasa de escribir código a revisar código — o a describir qué quiere que el código haga.

**Conduce a:** Vibe coding (Karpathy 2025); Claude Opus 4.7 y agentes autónomos · **Depende de:** GitHub Copilot (2021) — el antecedente; Transformer (2017) — el modelo subyacente; Docker/Git — el entorno que el agente ejecuta.

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1945 | Konrad Zuse | Plankalkül; primer lenguaje de alto nivel del mundo | Alemania |
| 1952 | Grace Hopper | Compilador A-0; FLOW-MATIC; influencia clave en COBOL | EE.UU. / UNIVAC / US Navy |
| 1957 | John Backus | FORTRAN; notación BNF | EE.UU. / IBM |
| 1958 | John McCarthy | LISP; garbage collector; cálculo lambda en software | EE.UU. / MIT |
| 1959 | Peter Naur | ALGOL 60; notación BNF con Backus | Dinamarca |
| 1959 | Alan Perlis | ALGOL 60; primer recipiente del Premio Turing (1966) | EE.UU. |
| 1959 | Adriaan van Wijngaarden | ALGOL 60; gramáticas van Wijngaarden | Países Bajos / CWI |
| 1961 | Fernando Corbató | CTSS; timesharing; contraseñas; Premio Turing 1990 | EE.UU. / MIT |
| 1968 | Edsger Dijkstra | Programación estructurada; Go To Considered Harmful | Países Bajos / Eindhoven |
| 1969 | Margaret Hamilton | Software Apollo 11; término "software engineering" | EE.UU. / MIT Instrumentation Lab |
| 1969 | Ken Thompson | Unix; creador del shell, del editor ed, de Go (2007) | EE.UU. / Bell Labs |
| 1969 | Dennis Ritchie | Unix; lenguaje C; *The C Programming Language* | EE.UU. / Bell Labs |
| 1973 | Brian Kernighan | Co-autor de *The C Programming Language* (K&R) | EE.UU. / Bell Labs |
| 1983 | Richard Stallman | GNU Project; GPL; copyleft; GCC, Emacs | EE.UU. / MIT |
| 1991 | Linus Torvalds | Kernel Linux; Git (2005) | Finlandia / Universidad de Helsinki |
| 2005 | Tom Preston-Werner | Cofundador de GitHub | EE.UU. |
| 2005 | Chris Wanstrath | Cofundador de GitHub | EE.UU. |
| 2013 | Solomon Hykes | Docker; contenedores Linux como modelo de empaquetado | Francia / EE.UU. / dotCloud |
| 2021 | Paul Gauthier | Aider; agente de código open source | EE.UU. |
| 2024 | Andrej Karpathy | Acuña el término "vibe coding" | EE.UU. / OpenAI → independiente |

---

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[01_LOGICA#1936 · Lambda calculus]] → McCarthy construye LISP directamente sobre el cálculo lambda
- ↗ De [[03_ARQUITECTURA#1949 · EDSAC operativo]] → Hopper tiene una arquitectura Von Neumann sobre la que construir el compilador
- ↗ De [[03_ARQUITECTURA#1944 · Harvard Mark I]] → donde Hopper aprende a programar
- ↗ De [[03_ARQUITECTURA#1962 · Manchester Atlas]] → la memoria virtual habilita los sistemas operativos multitarea (Unix)
- ↗ De [[04_ELECTRONICA#1959 · Circuito integrado]] → el hardware que hace posible que el software sea práctico
- ↗ De [[IA#2017 · Transformer]] → Copilot y los agentes de código usan transformers como motor

Lo que esta columna **aporta** a otras columnas:

- ↘ De Unix (1969) → habilita [[DATA#1970 · Modelo relacional]] (bases de datos en entornos Unix); [[NET#1969 · ARPANET]] — Unix es el SO de los servidores ARPANET
- ↘ De LISP (1958) → habilita [[IA]] — sistemas expertos, programación funcional, Word2Vec como herencia cultural
- ↘ De Linux (1991) → habilita [[NET#2006 · AWS]] — los servidores cloud corren Linux; Android (2008)
- ↘ De Docker (2013) → habilita [[NET#2014 · Kubernetes]]
- ↘ De Copilot (2021) → habilita [[IA#2024 · Coding agents]] como categoría de producto
- ↘ De COBOL (1959) → sustrato de [[ARQ#1964 · IBM System/360]] — COBOL corre en S/360 durante décadas

---

## Lectura siguiente

- Si te interesa la cadena de paradigmas de programación (POO, funcional, agile) → POO en el grafo
- Si quieres ver cómo el software de sistemas se convierte en infraestructura cloud → [[NET]] en el grafo
- Si quieres la arquitectura de las máquinas que ejecutan este software → [[03_ARQUITECTURA]]
- Si quieres ver cómo el software se encuentra con la inteligencia artificial → [[IA]] en el grafo

---

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
