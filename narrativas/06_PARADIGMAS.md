---
columna: PARADIGMAS
cat: POO
nodos_cubiertos: 13
periodo: 1967 → 2025
---

# PARADIGMAS · Del objeto al agente que vibra

> La historia de los paradigmas de programación es la historia de cómo los humanos negocian con la complejidad: cada nuevo modelo aparece cuando el anterior colapsa bajo su propio peso.

## El arco

En 1967, dos noruegos inventan la clase y el objeto para simular barcos en un puerto. En 2025, un físico convertido en OpenAI-researcher acuña "vibe coding" y describe programar sin escribir código. Entre ambos extremos, la columna PARADIGMAS narra cómo el software organiza su propia complejidad: la POO primero como metáfora, luego como industria, luego como dogma que genera su propia reacción funcional, y finalmente como sustrato que la IA disuelve. Esta columna depende de SOFTWARE (C, Unix, LISP) y alimenta directamente la infraestructura cloud de INTERNET.

## La cadena

### 1967 · Simula 67 — Ole-Johan Dahl, Kristen Nygaard

**Ole-Johan Dahl** y **Kristen Nygaard** (Universidad de Oslo) publican Simula 67: el primer lenguaje con clases, objetos y herencia. El contexto es operativo: Nygaard modelaba sistemas de simulación discreta (barcos en un puerto, pacientes en un hospital) y necesitaba agrupar estado + comportamiento en una unidad. La solución fue la clase.

Simula corre sobre un UNIVAC 1107 en Oslo. No llega a ser popular fuera de Escandinavia, pero **Alan Kay** lo leerá en Xerox PARC y acuñará el término "object-oriented" para describir lo que quiere construir.

**Conduce a:** [[#1980 · Smalltalk-80]] · **Depende de:** [[04_SOFTWARE#1973 · Lenguaje C]] (influencia indirecta vía la comunidad de lenguajes)

---

### 1980 · Smalltalk-80 — Alan Kay, Dan Ingalls, Adele Goldberg

Xerox PARC. **Alan Kay** (visión), **Dan Ingalls** (implementación) y **Adele Goldberg** (lenguaje, libros, evangelización) construyen Smalltalk-80: el primer entorno donde todo es objeto, incluido el propio entorno. El sistema puede inspeccionarse y modificarse desde dentro.

**Adele Goldberg** presenta el sistema a Steve Jobs durante su visita a PARC en 1979. Jobs ve la GUI y el ratón; lo que no copia es el modelo de objetos puro. Smalltalk recibe el ACM Software System Award en 1987. No domina el mercado, pero dicta la gramática que C++ y Java seguirán.

**Conduce a:** [[#1985 · C++]] · [[07_MICRO_PC#1984 · Macintosh]] · **Depende de:** [[07_MICRO_PC#1973 · Xerox Alto]] (mismo equipo PARC)

---

### 1985 · C++ — Bjarne Stroustrup

**Bjarne Stroustrup** (Bell Labs) suma clases y herencia sobre C. El objetivo es claro: los sistemas de telecomunicaciones de Bell necesitaban modelado orientado a objetos sin sacrificar el control de memoria que C ofrecía. La primera edición comercial aparece en 1985 como "C with Classes"; el nombre C++ llega después.

C++ lleva la POO al software de sistemas, a los juegos, a los compiladores. Define el trade-off que marcará dos décadas: poder expresivo a cambio de complejidad de gestión de memoria. Stroustrup dirá más tarde que C++ fue diseñado para ser aprendido gradualmente, no de golpe.

**Conduce a:** [[#1995 · Java]] · **Depende de:** [[04_SOFTWARE#1973 · Lenguaje C]] (habilitante directo)

---

### 1991 · Python — Guido van Rossum

**Guido van Rossum** diseña Python durante las vacaciones de Navidad de 1989 (primera versión pública en febrero 1991). El objetivo declarado: un lenguaje que fuera legible como pseudocódigo. Van Rossum trabajaba en el CWI de Ámsterdam y estaba insatisfecho con ABC.

Python combina scripting, POO y funcional sin forzar ninguno de los tres. La versión 2.0 (2000) introduce list comprehensions; la 3.0 (2008) rompe compatibilidad para limpiar el diseño. Tres décadas después es la lengua franca de la IA, el data science y la automatización. El momento en que PyPI supera 500.000 paquetes (2023) cierra el argumento.

**Conduce a:** [[#2025 · Vibe Coding]] (paralelo via coding agents) · **Depende de:** [[04_SOFTWARE#1958 · LISP]] (herencia funcional) · [[03_IA#2012 · AlexNet]] (python como puente a IA)

---

### 1995 · Java — James Gosling

**James Gosling** (Sun Microsystems) lanza Java con la promesa "write once, run anywhere" sobre la Java Virtual Machine. El contexto: la fragmentación de plataformas (Solaris, Windows, Mac, HP-UX) hacía imposible distribuir software binario. La JVM abstrae el hardware.

Java masifica la POO en entornos corporativos. J2EE (1999) la lleva a los servidores de aplicaciones bancarios y de telecomunicaciones. En 2010 Oracle compra Sun. Android adopta Java (después Kotlin sobre JVM) y le da 15 años adicionales de dominio. Gosling recibe el premio Draper en 2022.

**Conduce a:** [[#2001 · TDD + Manifiesto Ágil]] · [[#2014 · Swift + TypeScript]] (paralelo)

---

### 1995 · JavaScript — Brendan Eich

**Brendan Eich** diseña JavaScript en 10 días en Netscape, mayo 1995. Originalmente "Mocha", luego "LiveScript", renombrado JavaScript para aprovechar el hype de Java (sin relación técnica). Estandarizado como ECMAScript en 1997.

Durante su primera década, JavaScript es el lenguaje que nadie confiesa usar. Node.js (2009, Ryan Dahl) lo saca del navegador y lo instala en servidores. Con el tiempo pasa a ser el lenguaje más usado del mundo. Es el único lenguaje nativo del navegador hasta que WebAssembly llega en 2019.

**Conduce a:** [[#2014 · Swift + TypeScript]] · [[#2007 · Renacimiento funcional]] (paralelo)

---

### 2001 · TDD + Manifiesto Ágil — Kent Beck, Ward Cunningham, Martin Fowler

**Kent Beck** publica *Extreme Programming Explained* (octubre 1999). En febrero de 2001, diecisiete desarrolladores se reúnen en Snowbird, Utah, y firman el Manifiesto Ágil: individuos sobre procesos, software funcionando sobre documentación exhaustiva, colaboración con el cliente sobre contratos. Beck publica *TDD: By Example* en noviembre 2002.

El Manifiesto desplaza el modelo waterfall (dominante en contratos de defensa y bancarios desde los 70) como marco de referencia. Scrum y XP se convierten en estándar de facto en startups y luego en empresas grandes. **Martin Fowler** y **James Lewis** sistematizarán la siguiente transformación: los microservicios (2014).

**Conduce a:** [[#2014 · Microservicios]]

---

### 2007 · Renacimiento funcional — Rich Hickey, Martin Odersky

**Rich Hickey** lanza Clojure (2007): Lisp sobre la JVM, inmutabilidad radical, datos como valores. **Martin Odersky** publica Scala (primera versión 2004, popularidad desde 2007): objetos + tipos + funcional sobre JVM.

El contexto es el problema de la concurrencia: con los procesadores multi-núcleo (Intel Core 2 Duo, 2006), el estado mutable compartido se convierte en una fuente constante de bugs imposibles de depurar. Las funciones puras y los datos inmutables no tienen ese problema. Clojure + Scala influyen en Java (lambdas en Java 8, 2014), en JavaScript (React/Redux, 2015) y en Python (functools, itertools).

**Conduce a:** [[#2010 · Go + Rust]] (paralelo)

---

### 2010 · Go + Rust — Rob Pike, Robert Griesemer, Ken Thompson / Graydon Hoare

**Go**: anunciado por **Rob Pike**, **Robert Griesemer** y **Ken Thompson** (Google) en noviembre 2009; versión 1.0 en marzo 2012. Concurrencia nativa con goroutines, garbage collector, compilación rápida. Docker (Go, 2013) y Kubernetes (Go, 2014) lo consagran.

**Rust**: proyecto personal de **Graydon Hoare** desde 2006; Mozilla lo patrocina en 2009; anuncio público en 2010; versión 1.0 en mayo 2015. Memory safety sin garbage collector mediante el sistema de ownership. Cloudflare Workers y el kernel Linux lo adoptan.

Ambos comparten el objetivo de reemplazar C/C++ en infraestructura, pero con garantías de seguridad que C nunca tuvo.

**Conduce a:** [[09_INTERNET#2014 · Kubernetes]] (Go como sustrato)

---

### 2014 · Microservicios — Martin Fowler, James Lewis

**Martin Fowler** y **James Lewis** popularizan el término "microservices" en marzo 2014 (artículo en martinfowler.com). La idea no es nueva — SOA llevaba una década — pero la combinación con contenedores Docker (2013) y cloud hace que el modelo sea por primera vez económicamente viable para equipos medianos.

La arquitectura de microservicios descompone el monolito en servicios desplegables independientemente, cada uno con su propia base de datos y ciclo de release. Permite que Netflix, Amazon y Spotify escalen con cientos de equipos en paralelo. La complejidad operativa que genera (service mesh, distributed tracing, eventual consistency) alimentará la demanda de Kubernetes.

**Conduce a:** [[09_INTERNET#2014 · Kubernetes]] · **Depende de:** [[04_SOFTWARE#2013 · Docker]]

---

### 2014 · Swift + TypeScript — Chris Lattner / Anders Hejlsberg

**Apple Swift** (junio 2014): diseñado por **Chris Lattner** (creador también de LLVM y Clang) como sucesor de Objective-C. Sucesor directo de la plataforma iOS/macOS.

**Microsoft TypeScript** (anunciado 2012, mainstream 2014): diseñado por **Anders Hejlsberg** (también creador de Turbo Pascal y C#). Añade tipos estáticos opcionales sobre JavaScript. En 2024, TypeScript supera a JavaScript en repos activos en GitHub.

Ambos modernizan plataformas masivas sin romperlas: Swift convive con Objective-C, TypeScript es JavaScript válido.

---

### 2024 · Algoritmos agénticos — múltiples autores

ReAct (2022, **Shunyu Yao** et al., Princeton+Google) → Tree-of-Thoughts (2023, **Shunyu Yao** et al.) → MCTS sobre LLMs → tool use estructurado → planning con verificación. La IA vuelve a abrazar la búsqueda algorítmica clásica, pero con LLMs como heurística.

No es una persona ni una empresa: es un patrón que emerge en paralelo en múltiples laboratorios. El resultado: agentes capaces de descomponer tareas, usar herramientas, verificar resultados e iterar. Base de Cursor, Claude Code, Devin.

**Conduce a:** [[#2025 · Vibe Coding]] · **Depende de:** [[03_IA#2017 · Transformer]]

---

### 2025 · Vibe Coding — Andrej Karpathy

**Andrej Karpathy** acuña *vibe coding* en febrero de 2025: programar describiendo la intención en lenguaje natural y dejar que un agente IA escriba e itere el código. Karpathy era Director de IA en Tesla y cofundador de OpenAI; el término aparece en un post de X el 2 de febrero de 2025.

El nombre es provocador y preciso a la vez: el programador no necesita saber el nombre de la función, solo la intención. Es el cierre del arco que empieza con el compilador A-0 de Hopper (1952): cada salto de abstracción aleja al humano un paso más de los bits.

**Depende de:** [[04_SOFTWARE#2024 · Coding agents]] · [[03_IA#2026 · Claude Opus 4.7 · 1M]] (como soporte de razonamiento)

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1967 | Ole-Johan Dahl | Coinventor de Simula 67, clases y objetos | Universidad de Oslo, Noruega |
| 1967 | Kristen Nygaard | Coinventor de Simula 67, diseño del modelo de simulación | Universidad de Oslo, Noruega |
| 1980 | Alan Kay | Visión de Smalltalk, acuña "object-oriented" | Xerox PARC, EE.UU. |
| 1980 | Dan Ingalls | Implementación de Smalltalk-80 | Xerox PARC, EE.UU. |
| 1980 | Adele Goldberg | Lenguaje Smalltalk, libros, evangelización, demo a Jobs | Xerox PARC, EE.UU. |
| 1985 | Bjarne Stroustrup | Diseñador de C++ | Bell Labs, EE.UU. |
| 1991 | Guido van Rossum | Diseñador de Python | CWI, Países Bajos |
| 1995 | James Gosling | Diseñador de Java | Sun Microsystems, EE.UU. |
| 1995 | Brendan Eich | Diseñador de JavaScript | Netscape, EE.UU. |
| 1999 | Kent Beck | Extreme Programming, TDD | Independiente, EE.UU. |
| 2001 | Martin Fowler | Manifiesto Ágil, microservicios | ThoughtWorks, EE.UU. |
| 2001 | James Lewis | Coautor del término "microservicios" | ThoughtWorks, UK |
| 2007 | Rich Hickey | Diseñador de Clojure | Independiente, EE.UU. |
| 2004 | Martin Odersky | Diseñador de Scala | EPFL, Suiza |
| 2009 | Rob Pike | Codiseñador de Go | Google, EE.UU. |
| 2009 | Robert Griesemer | Codiseñador de Go | Google, EE.UU. |
| 2009 | Ken Thompson | Codiseñador de Go (también Unix, C) | Google, EE.UU. |
| 2006 | Graydon Hoare | Diseñador de Rust | Mozilla, Canadá |
| 2014 | Chris Lattner | Diseñador de Swift (también LLVM, Clang) | Apple, EE.UU. |
| 2012 | Anders Hejlsberg | Diseñador de TypeScript (también Turbo Pascal, C#) | Microsoft, EE.UU. |
| 2025 | Andrej Karpathy | Acuña "vibe coding" | Ex-Tesla/OpenAI, EE.UU. |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[04_SOFTWARE#1958 · LISP]] → habilita Python (herencia funcional) y el renacimiento funcional via Church-lambda
- ↗ De [[04_SOFTWARE#1973 · Lenguaje C]] → habilita C++ (C es el sustrato directo)
- ↗ De [[07_MICRO_PC#1973 · Xerox Alto]] → habilita Smalltalk-80 (mismo equipo PARC, entorno paralelo)
- ↗ De [[04_SOFTWARE#2013 · Docker]] → habilita Microservicios (contenedores hacen el modelo viable)
- ↗ De [[03_IA#2017 · Transformer]] → habilita Coding agents y Vibe Coding
- ↗ De [[04_SOFTWARE#2024 · Coding agents]] → habilita Vibe Coding

Lo que esta columna **aporta** a otras columnas:

- ↘ Smalltalk-80 → habilita [[07_MICRO_PC#1984 · Macintosh]] (la GUI de Mac hereda conceptos PARC/Smalltalk)
- ↘ Microservicios → habilita [[09_INTERNET#2014 · Kubernetes]] (la demanda de orquestación nace de los microservicios)
- ↘ Python → habilita [[03_IA#2012 · AlexNet]] (puente crítico al ecosistema IA)
- ↘ Vibe Coding → habilita [[03_IA#2026 · Claude Opus 4.7 · 1M]] (relación recíproca de soporte)

## Lectura siguiente

- Si te interesa cómo se ejecutan estos paradigmas en hardware → [[07_MICRO_PC]]
- Si quieres seguir la rama del software de sistemas (compiladores, kernels) → [[04_SOFTWARE]]
- Si quieres ver cómo los agentes IA convierten estos lenguajes en herramientas → [[03_IA]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
