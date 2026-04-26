---
columna: ARQUITECTURA
cat: ARQ
nodos_cubiertos: 14
periodo: 1642 → 1964
---

# ARQUITECTURA · De la calculadora mecánica al programa almacenado

> Trescientos años para responder a una pregunta: ¿cómo construir una máquina que procese información de forma general, no solo para un problema fijo?

## El arco

La columna ARQUITECTURA es la historia de cómo la máquina de calcular se convierte en máquina de propósito general. Pascal construye una calculadora para su padre en 1642; no es programable. Babbage diseña la primera arquitectura general en 1837, pero no la termina — Ada Lovelace documenta el primer programa para esa máquina conceptual. El salto a la electrónica llega con la Segunda Guerra Mundial. Von Neumann sintetiza las ideas en 1945 en el modelo que sigue siendo el dominante: CPU + memoria + programa almacenado en la misma RAM que los datos. El Manchester Baby lo ejecuta por primera vez en 1948. El IBM System/360 en 1964 convierte la arquitectura en contrato estable entre hardware y software. Esta columna alimenta todo lo demás: sin máquina general no hay software, sin programa almacenado no hay sistema operativo, sin la abstracción de Von Neumann no hay IA moderna.

## La cadena

### 1642 · Pascalina — Blaise Pascal

**Blaise Pascal**, con 19 años, construye la Pascalina en Rouen (Francia) entre 1642 y 1645. La razón: su padre, Étienne Pascal, era recaudador de impuestos en Normandía y pasaba horas sumando columnas de cifras. Blaise le construye una máquina. La Pascalina tiene entre 6 y 8 ruedas dentadas, cada una representando un dígito de 0 a 9; el arrastre entre ruedas implementa el "llevo uno". Fabrica aproximadamente 50 unidades. Solo suma y resta directamente (la multiplicación requiere sumas repetidas manuales). Es la primera calculadora mecánica de la historia. Leibniz la conoce, la critica por sus limitaciones, y construye su propia máquina capaz de las cuatro operaciones.

**Conduce a:** Stepped Reckoner de Leibniz (1673) — Leibniz parte de la Pascalina para superarla; Máquina Analítica de Babbage (1837) · **Depende de:** artesanía mecánica del siglo XVII — no hay antecedente computacional directo.

---

### 1804 · Telar de Jacquard — Joseph Marie Jacquard

**Joseph Marie Jacquard** presenta su telar automatizado en Lyon en 1804. El mecanismo: tarjetas de cartón perforado controlan cuáles hilos de urdimbre se levantan en cada pasada de la lanzadera. Si el agujero está presente, el hilo sube; si no, baja. Un patrón complejo de tela resulta de la secuencia de tarjetas. Las tarjetas se encadenan y se ejecutan en orden: son un programa. Jacquard no inventó el telar automatizado (Basile Bouchon y Jean-Baptiste Falcon lo habían precedido), pero su sistema es el primero en funcionar de forma confiable a escala industrial. Para 1812 había 11.000 telares Jacquard en Lyon. Babbage cita el telar de Jacquard como inspiración directa para la Máquina Analítica. Hollerith lo cita para las tarjetas del censo.

**Conduce a:** Máquina Analítica de Babbage (1837); Tabuladora Hollerith (1890) · **Depende de:** artesanía mecánica textil — no hay antecedente computacional.

---

### 1837 · Máquina Analítica — Charles Babbage

**Charles Babbage** diseña la Máquina Analítica a partir de 1837 en Londres, apoyado financieramente durante años por el gobierno británico. La arquitectura: un "molino" (unidad aritmética), un "almacén" (memoria de 1.000 números de 50 dígitos), tarjetas perforadas para el programa (inspiradas en Jacquard), y un mecanismo de control de flujo (saltos condicionales). Es la primera arquitectura conceptual de un ordenador de propósito general. Babbage nunca termina la máquina — la complejidad mecánica excede la capacidad de fabricación de la época, y los fondos del gobierno se agotan. La replica que construye el Science Museum de Londres en 1991 (solo la "diferencia", no la analítica) funciona correctamente, probando que el diseño era sólido.

**Conduce a:** Primer programa de Ada Lovelace (1843) · **Depende de:** Telar de Jacquard (1804) — tarjetas perforadas como modelo de programa; Pascalina (1642) — cadena mecánica.

---

### 1843 · Primer programa — Ada Lovelace

**Ada Lovelace** publica sus notas sobre la Máquina Analítica en 1843 como traducción anotada de un artículo de Luigi Menabrea (transcripción de una conferencia de Babbage en Turín). Las notas triplican en extensión el artículo original. La Nota G contiene el primer algoritmo publicado destinado a ser ejecutado por una máquina: el cálculo de los números de Bernoulli mediante la Máquina Analítica. Lovelace también articula, por primera vez, la distinción entre la máquina (lo que hace) y el programa (lo que se le dice que haga) — la distinción hardware/software. Señala que la máquina solo puede hacer lo que se le ordena: nunca "originará" nada por sí misma. El debate sobre qué significa "originalidad" en las máquinas llegará 107 años después con Turing.

**Conduce a:** Máquina de Turing (1936) — Turing conoce el trabajo de Lovelace y debate explícitamente su afirmación · **Depende de:** Máquina Analítica (1837) — el hardware para el que escribe el algoritmo.

---

### 1890 · Hollerith → IBM — Herman Hollerith

**Herman Hollerith** (MIT, 1879) inventa la tabuladora eléctrica con tarjetas perforadas para el censo de EE.UU. de 1890. El problema: el censo de 1880 tardó 8 años en procesarse — para cuando terminó, el siguiente ya estaba llegando. Hollerith codifica cada persona en una tarjeta perforada y usa contactos eléctricos para contar. El resultado: el conteo básico del censo de 1890 se completa en 6 meses. Hollerith funda la Tabulating Machine Company en 1896. En 1911, la empresa se fusiona con otras tres para formar CTR (Computing-Tabulating-Recording Company). En 1924, CTR se renombra **International Business Machines — IBM**. Las tarjetas perforadas Hollerith dominan el procesamiento de datos durante 70 años, hasta que los discos magnéticos las desplazan en los 70.

**Conduce a:** IBM System/360 (1964) — la misma empresa que Hollerith fundó · **Depende de:** Telar de Jacquard (1804) — tarjetas perforadas como mecanismo.

---

### 1936 · Máquina universal — Alan Turing

**Alan Turing** publica *On Computable Numbers, with an Application to the Entscheidungsproblem* en 1936, con 24 años, en Cambridge. Define la Máquina de Turing: una cinta infinita, un cabezal de lectura/escritura, un conjunto finito de estados y reglas de transición. Simple al extremo, universal en poder: cualquier función computable puede ser ejecutada por alguna Máquina de Turing. La "Máquina Universal" de Turing puede simular cualquier otra Máquina de Turing — es el primer concepto de ordenador de propósito general expresado con precisión matemática. El paper responde directamente al Entscheidungsproblem de Hilbert: no, no existe tal procedimiento de decisión general.

**Conduce a:** Von Neumann (1945) — la arquitectura de programa almacenado es la realización física del modelo Turing; Church (1936) — tesis Church-Turing · **Depende de:** Gödel (1931) — el problema que Turing ataca; Lovelace (1843) — la distinción hardware/software que Turing elabora.

---

### 1944 · Harvard Mark I — Howard Aiken

**Howard Aiken** (Harvard + IBM) entrega el ASCC (*Automatic Sequence Controlled Calculator*), renombrado Harvard Mark I, en agosto de 1944. Características: electromecánico (relés, no válvulas), aproximadamente 4.300 kg, 765.000 piezas. Ejecuta secuencias de instrucciones codificadas en cinta de papel perforada. No es un ordenador de programa almacenado — el programa y los datos están separados — pero es el primer ordenador automático de propósito general en EE.UU. **Grace Hopper** aprende a programar en el Mark I. El famoso "bug" (la polilla) lo encontró Hopper en el Mark II (sucesor, 1947), no en el Mark I — pero la anécdota dio nombre al concepto de "bug de software".

**Conduce a:** Compilador A-0 de Grace Hopper (1952) — ella aprende aquí · **Depende de:** cálculo diferencial de Babbage — Aiken conoce el diseño de la Máquina Analítica.

---

### 1945 · Programa almacenado — John von Neumann

**John von Neumann** circula el *First Draft of a Report on the EDVAC* en junio de 1945. El documento describe la arquitectura de programa almacenado: el programa se guarda en la misma memoria que los datos, representado como números binarios. La CPU lee instrucciones y datos del mismo bus, las ejecuta secuencialmente, modifica memoria. La simplicidad revolucionaria del modelo: al ser el programa un dato más, puede modificarse a sí mismo. Von Neumann escribe el documento solo (con créditos a Eckert y Mauchly implícitos, lo que genera controversia), pero las ideas vienen de múltiples conversaciones con Eckert, Mauchly, y el equipo de Turing en Bletchley. Este modelo — CPU + memoria + bus — sigue siendo el dominante en 2026.

**Conduce a:** Manchester Baby (1948), EDSAC (1949) — primeras realizaciones físicas · Autómatas autoreplicantes (1948) — Von Neumann extiende las implicaciones · **Depende de:** Máquina de Turing (1936) — sustrato teórico; Shannon 1937 — puente lógica-electrónica.

---

### 1948 · Manchester Baby (SSEM) — Freddie Williams / Tom Kilburn

La *Small-Scale Experimental Machine* se ejecuta en Manchester el **21 de junio de 1948**: es el primer ordenador del mundo que ejecuta un programa almacenado en memoria electrónica. **Freddie Williams** y **Tom Kilburn** (Universidad de Manchester) construyen el SSEM sobre tubos Williams-Kilburn (tubos de rayos catódicos modificados) como memoria RAM electrónica. 32 palabras de 32 bits. El primer programa — escrito por Kilburn — busca el factor más grande de un número entero. Tarda 52 minutos en ejecutarse. Pequeño, lento, inestable — pero funciona, y anticipa al EDSAC por casi un año.

**Conduce a:** EDSAC (1949) — primer Von Neumann plenamente operativo · **Depende de:** Von Neumann (1945) — la arquitectura que implementa.

---

### 1948 · Autómatas autoreplicantes — John von Neumann

**John von Neumann** formula la teoría de los autómatas autoreplicantes a partir de 1948. La pregunta: ¿puede una máquina construir una copia de sí misma? Von Neumann demuestra que sí, y describe un "constructor universal" capaz de fabricar cualquier máquina cuyas instrucciones se le proporcionen — incluyéndose a sí mismo. El trabajo se publica póstumamente en 1966 como *Theory of Self-Reproducing Automata*, editado por Arthur Burks. Von Neumann trabaja en esto simultáneamente con McCulloch y Pitts (neuronas artificiales) y con Shannon (teoría de la información). Predice la lógica del ADN antes de que Watson y Crick la descubran en 1953: el código genético es instrucción + datos en el mismo sustrato.

**Conduce a:** *A New Kind of Science* de Wolfram (2002) — autómatas celulares; algoritmos evolutivos · **Depende de:** McCulloch-Pitts (neuronas artificiales, 1943) — mismo contexto intelectual.

---

### 1949 · EDSAC operativo — Maurice Wilkes

**Maurice Wilkes** pone en marcha el EDSAC (*Electronic Delay Storage Automatic Calculator*) en Cambridge el 6 de mayo de 1949. Es el primer ordenador de arquitectura Von Neumann plenamente operativo: memoria de mercurio líquido como líneas de retardo (512 palabras de 17 bits), programa almacenado. El primer programa útil: calcula una tabla de cuadrados y números primos. Wilkes introduce el concepto de "biblioteca de subrutinas" — pequeños programas reutilizables que se llaman desde el programa principal. Es el primer antecedente de lo que será la programación modular. El EDSAC habilita al compilador A-0 de Grace Hopper (que trabaja en UNIVAC, que hereda las ideas del EDSAC).

**Conduce a:** Compilador A-0 de Hopper (1952) — la arquitectura que hace viable el compilador · **Depende de:** Von Neumann (1945) — la arquitectura que realiza; Manchester Baby (1948) — primer antecedente.

---

### 1951 · LEO I — J. Lyons & Co.

**J. Lyons & Co.**, cadena británica de salones de té y catering, encarga la construcción del LEO I (*Lyons Electronic Office*) basado directamente en el diseño del EDSAC de Wilkes. El LEO I se usa por primera vez para cómputo de negocio el 29 de noviembre de 1951: calcula nóminas y gestión de stock para la empresa. Es el primer ordenador del mundo usado con fines empresariales. Treinta años antes de la era del PC, una empresa de alimentación comprende que el ordenador no es solo para científicos. El equipo detrás del LEO incluye a **John Simmons** y **David Caminer** (primer programador de negocio profesional del mundo).

**Conduce a:** COBOL (1959) — el LEO I establece que el negocio necesita sus propios lenguajes y paradigmas · **Depende de:** EDSAC (1949) — el diseño sobre el que se construye.

---

### 1962 · Manchester Atlas — Tom Kilburn

**Tom Kilburn** (el mismo que había construido el Manchester Baby en 1948) lidera el desarrollo del Atlas en colaboración con **Ferranti**. El Atlas se opera desde 1962 en la Universidad de Manchester. Dos innovaciones fundamentales: la **memoria virtual** (el sistema puede usar más memoria de la que físicamente existe, paginando automáticamente entre RAM y drum) y el **paginado por demanda** (solo se carga en RAM la parte del programa que se necesita en ese momento). Es considerado el ordenador más potente del mundo en su lanzamiento. Un tercio del poder computacional del Reino Unido en un solo sistema.

**Conduce a:** Unix (1969) — la memoria virtual habilita los SO multitarea modernos; GNU (1983) — herencia académica · **Depende de:** Manchester Baby (1948) — mismo equipo; Von Neumann (1945) — arquitectura base.

---

### 1964 · IBM System/360 — Gene Amdahl / Fred Brooks

IBM lanza el System/360 el **7 de abril de 1964**. La inversión: 5.000 millones de dólares — más que el proyecto Manhattan, más que el programa espacial Mercury. El concepto central: una **familia** de mainframes completamente compatibles entre sí. El programa escrito para el modelo más pequeño corre sin cambios en el más grande. **Gene Amdahl** diseña la arquitectura del conjunto de instrucciones (ISA); **Fred Brooks** dirige el proyecto (y luego escribe *The Mythical Man-Month* basándose en las lecciones aprendidas). El ISA del S/360 sigue vivo en 2026 en los mainframes IBM Z — 62 años de compatibilidad binaria. El concepto de "arquitectura" como contrato estable entre hardware y software nace aquí.

**Conduce a:** COBOL (software bancario que corre sobre S/360); define el modelo mainframe que domina la empresa hasta hoy · **Depende de:** Von Neumann (1945) — arquitectura; Hollerith/IBM (1890) — la empresa que lo construye.

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1642 | Blaise Pascal | Primera calculadora mecánica funcional | Francia / Rouen |
| 1804 | Joseph Marie Jacquard | Telar automático con tarjetas perforadas | Francia / Lyon |
| 1837 | Charles Babbage | Máquina Analítica; primera arquitectura de propósito general | Reino Unido / Londres |
| 1843 | Ada Lovelace | Primer algoritmo publicado; distinción hardware/software | Reino Unido / Londres |
| 1843 | Luigi Menabrea | Artículo original que Lovelace traduce y anota | Italia / Turín |
| 1890 | Herman Hollerith | Tabuladora con tarjetas perforadas; fundador de lo que será IBM | EE.UU. / MIT → Washington |
| 1936 | Alan Turing | Máquina universal; base teórica del ordenador de propósito general | Reino Unido / Cambridge |
| 1944 | Howard Aiken | Harvard Mark I; primer ordenador automático de EE.UU. | EE.UU. / Harvard + IBM |
| 1944 | Grace Hopper | Aprende a programar en el Mark I; pionera del compilador | EE.UU. / Harvard |
| 1945 | John von Neumann | Arquitectura de programa almacenado; autómatas autoreplicantes | Hungría / EE.UU. / Princeton |
| 1945 | J. Presper Eckert | ENIAC; contribuciones conceptuales al First Draft | EE.UU. / Penn |
| 1945 | John Mauchly | ENIAC; contribuciones conceptuales al First Draft | EE.UU. / Penn |
| 1948 | Freddie Williams | Manchester Baby; memoria de tubos Williams-Kilburn | Reino Unido / Universidad de Manchester |
| 1948 | Tom Kilburn | Manchester Baby; Manchester Atlas (1962) | Reino Unido / Universidad de Manchester |
| 1948 | Arthur Burks | Edita y publica póstumamente la teoría de autómatas de Von Neumann | EE.UU. |
| 1949 | Maurice Wilkes | EDSAC; concepto de biblioteca de subrutinas | Reino Unido / Cambridge |
| 1951 | David Caminer | Primer programador de negocio profesional del mundo; LEO I | Reino Unido / J. Lyons & Co. |
| 1951 | John Simmons | Director del proyecto LEO I | Reino Unido / J. Lyons & Co. |
| 1964 | Gene Amdahl | Diseño del ISA del System/360 | EE.UU. / IBM |
| 1964 | Fred Brooks | Director del proyecto S/360; *The Mythical Man-Month* | EE.UU. / IBM |

---

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[01_LOGICA#1673 · Leibniz · binario]] → Leibniz mejora la Pascalina; el binario es la notación que Turing y Von Neumann usarán
- ↗ De [[01_LOGICA#1937 · Lógica → circuitos]] → Shannon 1937 habilita directamente el puente entre lógica y hardware electrónico (Z3, Colossus, ENIAC)
- ↗ De [[04_ELECTRONICA#1943 · McCulloch-Pitts]] → neuronas artificiales en el mismo contexto intelectual que Von Neumann (autómatas)
- ↗ De [[01_LOGICA#1931 · Incompletitud]] → Gödel plantea el problema que Turing responde con la máquina universal

Lo que esta columna **aporta** a otras columnas:

- ↘ De Turing (1936) → habilita [[05_SOFTWARE]] completo — todo software presupone la máquina universal
- ↘ De Von Neumann (1945) → habilita [[04_ELECTRONICA#1948 · Manchester Baby]], EDSAC, y toda la cadena electrónica posterior
- ↘ De Manchester Atlas (1962) → habilita [[05_SOFTWARE#1969 · Unix]] — memoria virtual es prerequisito del SO moderno
- ↘ De IBM S/360 (1964) → sustrato de [[05_SOFTWARE#1959 · COBOL]] — COBOL bancario corre en S/360 durante décadas
- ↘ De Von Neumann (1948, autómatas) → habilita simulación de vida artificial, algoritmos evolutivos — [[SIM]] en el grafo

---

## Lectura siguiente

- Si te interesa el hardware electrónico que construye estas arquitecturas → [[04_ELECTRONICA]]
- Si quieres ver cómo el programa almacenado se convierte en software real → [[05_SOFTWARE]]
- Si quieres la lógica teórica que precede a la máquina universal → [[01_LOGICA]]
- Si quieres los microprocesadores y el PC personal que heredan la arquitectura Von Neumann → PC en el grafo

---

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
