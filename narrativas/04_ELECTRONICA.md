---
columna: ELECTRÓNICA
cat: ELE
nodos_cubiertos: 11
periodo: 1938 → 2022
---

# ELECTRÓNICA · De los relés a los transistores de 3 nm

> Ochenta años de una misma pregunta: ¿cómo hacer el interruptor más pequeño, más rápido y más barato?

## El arco

La columna ELECTRÓNICA convierte los modelos teóricos en máquinas físicas. Arranca en la Segunda Guerra Mundial con tres proyectos independientes — Zuse en Berlín, Atanasoff en Iowa, y Flowers en Bletchley — que todos alcanzan el mismo punto desde ángulos distintos: el circuito electrónico como elemento de cómputo. ENIAC en 1946 consolida el paradigma. Entonces llega el transistor (1947), que elimina las válvulas de vacío. El circuito integrado (1959) pone miles de transistores en un solo chip. Moore (1965) observa la tasa de duplicación y la convierte en hoja de ruta industrial. Durante 50 años, la ley de Moore es la fuerza organizadora de toda la industria tecnológica. En 2019 se declara muerta en su forma clásica. La respuesta: nuevas geometrías del transistor (GAA), nuevos sustratos (cristal óptico 5D), nuevos enfoques de packging. La electrónica nunca se detiene; solo cambia de palanca.

## La cadena

### 1938 · Zuse Z1 — Konrad Zuse

**Konrad Zuse** construye el Z1 en el salón de su casa en Berlin-Kreuzberg entre 1935 y 1938, sin financiación oficial, con apoyo de amigos y familia. El Z1 es la primera máquina mecánica programable binaria con representación de coma flotante. Tiene 30.000 piezas metálicas cortadas a mano por Zuse. Funcionaba mal — las tolerancias mecánicas eran demasiado estrechas — pero el diseño era correcto. Las instrucciones se leían de cinta de película perforada de 35 mm. Zuse trabajaba como ingeniero aeronáutico y usaba la máquina para cálculos de ingeniería. No conocía a Turing ni a Atanasoff; llegó al mismo punto de forma independiente. En 1944, los bombardeos aliados destruyen el Z1 en Berlín.

**Conduce a:** Z3 (1941) · **Depende de:** Shannon 1937 — aunque Zuse no conocía el paper de Shannon, reinventa el mismo principio de lógica binaria para circuitos.

---

### 1939 · Atanasoff-Berry (ABC) — John Atanasoff / Clifford Berry

**John Atanasoff** (Iowa State College) empieza el diseño de la ABC en invierno de 1937-38 durante un viaje en coche de cuatro horas de Des Moines a Illinois, según su relato. En 1939, con la ayuda de su doctorando **Clifford Berry**, construyen el prototipo. La ABC (*Atanasoff-Berry Computer*) usa tubos de vacío para la lógica y condensadores rotatorios como memoria. Puede resolver sistemas de ecuaciones lineales simultáneas — un único propósito, no programable. En 1973, el juez Earl Larson dictamina en el caso *Honeywell Inc. v. Sperry Rand Corp.* que la ABC fue el primer ordenador electrónico, invalidando la patente de ENIAC. El fallo sigue siendo controvertido — Berry había muerto en 1963 y no pudo testificar.

**Conduce a:** ENIAC (1946) — paralelo en tecnología; el fallo legal vincula directamente ambas máquinas · **Depende de:** Shannon 1937 — misma lógica de circuitos binarios.

---

### 1941 · Z3 — Konrad Zuse

**Konrad Zuse** completa el Z3 el 12 de mayo de 1941, de nuevo en Berlín. A diferencia del Z1 mecánico, el Z3 usa 2.600 relés electromecánicos. Es el primer ordenador programable y automático que funciona de forma confiable. Lee el programa de cinta perforada de película. Aritmética de coma flotante binaria. Velocidad: 3-4 operaciones por segundo. Zuse lo usa para calcular deflexiones de superficies alas de avión para la empresa Henschel. El gobierno nazi no financia el proyecto adecuadamente — no comprenden su potencial. Destruido en los bombardeos de Berlín en 1943. Una reconstrucción funciona hoy en el Deutsches Technikmuseum de Berlín.

**Conduce a:** Colossus (1944) — cadena de máquinas funcionales; demuestra viabilidad práctica antes que los aliados · **Depende de:** Z1 (1938) — versión anterior; Shannon 1937 — lógica binaria.

---

### 1944 · Colossus — Tommy Flowers

**Tommy Flowers**, ingeniero de telecomunicaciones de la GPO (General Post Office) británica, diseña y construye Colossus en Bletchley Park para el criptoanálisis de los mensajes Lorenz de los alemanes. El Colossus Mark 1 opera en febrero de 1944; el Mark 2 (con 5× más velocidad) está listo para el D-Day en junio de 1944. Usa 1.500 válvulas de vacío (el Mark 2, 2.400). Es el primer ordenador electrónico programable de la historia, pero "programable" de forma limitada: el operador cambia cables y conmutadores, no ejecuta un programa almacenado. Diez unidades se construyen en total. Churchill ordena destruirlos todos en 1945; el trabajo de Bletchley permanece clasificado hasta los 70. Flowers murió sin el reconocimiento que merecía.

**Conduce a:** ENIAC (1946) — siguiente escalón en ordenadores electrónicos · **Depende de:** Shannon 1937 — lógica de circuitos; Z3 (1941) — cadena de máquinas funcionales.

---

### 1946 · ENIAC — J. Presper Eckert / John Mauchly

**J. Presper Eckert** y **John Mauchly** (Universidad de Pensilvania) presentan el ENIAC (*Electronic Numerical Integrator and Computer*) el 14 de febrero de 1946. 17.468 válvulas de vacío. 27 toneladas. 167 m². Consume 150 kW. Realiza 5.000 adiciones por segundo — 1.000 veces más rápido que cualquier calculadora electromecánica. El primer problema que calcula: tablas de artillería para el ejército americano. En la demostración pública, también ejecuta un cálculo del proyecto Manhattan. El ENIAC no tiene programa almacenado — se "programa" recableando paneles físicos — pero consolida definitivamente el paradigma electrónico sobre el electromecánico. El debate legal con Atanasoff sobre la prioridad se resuelve en 1973 contra Eckert y Mauchly.

**Conduce a:** Transistor (1947) — el ENIAC hace visible el cuello de botella de las válvulas · **Depende de:** Shannon 1937 — justificación teórica; Z3, Colossus — antecedentes funcionales.

---

### 1947 · Transistor — John Bardeen / Walter Brattain / William Shockley

**John Bardeen**, **Walter Brattain** y **William Shockley** (Bell Labs, Murray Hill, New Jersey) demuestran el transistor de punto de contacto el 16 de diciembre de 1947. El transistor de unión bipolar, más robusto, llega en 1948. El principio: una pequeña corriente en la base controla una corriente mucho mayor entre colector y emisor. Mismo comportamiento lógico que una válvula de vacío, pero sin filamento que calentar, sin fragilidad de vidrio, sin tiempo de calentamiento. Un transistor ocupa 1 cm³ en 1947; el chip de 3 nm de Samsung en 2022 tiene 40 millones de transistores por milímetro cuadrado. Bardeen, Brattain y Shockley reciben el Nobel de Física en 1956. Shockley funda Shockley Semiconductor Laboratory en 1956 en Mountain View, California — el primer eslabón del Silicon Valley.

**Conduce a:** Circuito integrado (1959) · **Depende de:** ENIAC (1946) — la escala de las válvulas hace urgente la miniaturización.

---

### 1959 · Circuito integrado — Jack Kilby / Robert Noyce

**Jack Kilby** (Texas Instruments) demuestra el primer circuito integrado en germanio en julio de 1958 — múltiples componentes en un mismo sustrato. **Robert Noyce** (Fairchild Semiconductor) patenta independientemente en enero de 1959 la versión planar sobre silicio, fabricable industrialmente con fotolitografía. Kilby recibe el Nobel de Física en 2000 (Noyce había muerto en 1990). La versión de Noyce es la que industrializa el IC. Noyce cofundará Intel con **Gordon Moore** en 1968. El primer IC de Kilby: 4 transistores y 1 resistencia. El chip M3 de Apple en 2023: 35.000 millones de transistores.

**Conduce a:** Ley de Moore (1965); Intel 4004 (1971) y toda la cadena de microprocesadores · **Depende de:** Transistor (1947) — el componente que el IC integra a escala.

---

### 1965 · Ley de Moore — Gordon Moore

**Gordon Moore** (cofundador de Fairchild, futuro cofundador de Intel) publica un artículo en *Electronics* en abril de 1965. Observación: el número de transistores por chip se había duplicado cada año desde 1959. Predice que la tendencia continuará durante al menos 10 años. En 1975, revisa la predicción a duplicación cada 2 años. Lo que empieza como observación empírica se convierte en objetivo industrial: la industria semiconductora planifica inversiones, ciclos de producto y obsolescencia programada sobre la base de que la duplicación ocurrirá, porque si no ocurre, el competidor que sí la logre te desplaza. La ley de Moore no es una ley física — es una profecía autocumplida sostenida por inversión coordinada durante 50 años.

**Conduce a:** Fin de la ley de Moore clásica (2019) · **Depende de:** Circuito integrado (1959) — el hecho empírico que Moore observa.

---

### 2019 · Fin Moore clásico — Jensen Huang

**Jensen Huang** (NVIDIA) declara "Moore's Law is dead" en la GTC 2019. La cadencia de 2 años para doblar transistores se rompe: Intel tardó más de 5 años en pasar de 14 nm a 10 nm. El *Dennard scaling* — la otra mitad de la ecuación, que garantizaba que un transistor más pequeño consumía menos energía — había muerto antes, alrededor de 2006. La industria pivota: chiplets (múltiples dies en un mismo package, AMD Ryzen 2017), apilado 3D (Samsung HBM, TSMC SoIC), *advanced packaging* (CoWoS de TSMC). El nodo "nm" deja de ser una medida física real — es una marca de marketing que distintos fabricantes usan de forma inconsistente.

**Conduce a:** Transistor GAA (2022) — respuesta tecnológica · **Depende de:** Ley de Moore (1965) — lo que se declara terminado; AMD Ryzen/chiplets (2017) — la alternativa que ya está en marcha.

---

### 2019 · Project Silica · cristal 5D — Microsoft Research

**Microsoft Research** (Cambridge) demuestra Project Silica: almacenamiento óptico en cristal de cuarzo usando pulsos láser de femtosegundos que escriben datos en estructuras tridimensionales internas (5 dimensiones: 3 espaciales + polarización + intensidad). Los datos son durables durante miles de años en condiciones normales. En 2023, colaboración con Hitachi para demostración comercial: almacenar el archivo completo de *Superman* (1978) en un chip de cristal del tamaño de un posavasos. Sin partes móviles, inmune a campos electromagnéticos, no requiere energía para mantener los datos.

**Conduce a:** Memoria agéntica a largo plazo (DATA) · **Depende de:** Circuito integrado (1959) — cadena de sustratos alternativos al silicio; DNA computing (Adleman 1994) — exploración de sustratos no convencionales.

---

### 2022 · Transistor GAA — Samsung

**Samsung** lanza en 2022 el primer chip producido en masa con transistores **Gate-All-Around** (GAA) a 3 nm. El FinFET (que Intel introdujo en 2011 a 22 nm) tiene la puerta del transistor en tres lados del canal. El GAA la tiene en los cuatro — mayor control del canal, mejor eficiencia energética, mejor comportamiento a escala sub-5 nm. La geometría del canal pasa de aleta (FinFET) a nanohoja (*nanosheet* o *nanoribbon*). TSMC adopta GAA en su nodo N2 (2 nm) en 2025. Intel lo llama "RibbonFET" en su nodo 18A.

**Conduce a:** Apple M5 (2026) — primer chip de consumo en nodo GAA masivo · **Depende de:** Fin Moore clásico (2019) — GAA es la respuesta a que el FinFET ya no escala.

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1938 | Konrad Zuse | Z1, Z3; primeras máquinas programables binarias | Alemania / Berlín |
| 1939 | John Atanasoff | ABC; primer ordenador electrónico (fallo legal 1973) | EE.UU. / Iowa State |
| 1939 | Clifford Berry | Construcción de la ABC; colaborador de Atanasoff | EE.UU. / Iowa State |
| 1944 | Tommy Flowers | Colossus; primer ordenador electrónico programable | Reino Unido / GPO / Bletchley Park |
| 1946 | J. Presper Eckert | ENIAC; primer ordenador electrónico de propósito general | EE.UU. / Universidad de Pensilvania |
| 1946 | John Mauchly | ENIAC | EE.UU. / Universidad de Pensilvania |
| 1947 | John Bardeen | Transistor de punto de contacto | EE.UU. / Bell Labs |
| 1947 | Walter Brattain | Transistor de punto de contacto | EE.UU. / Bell Labs |
| 1947 | William Shockley | Transistor de unión bipolar; fundador Shockley Semiconductor | EE.UU. / Bell Labs → Silicon Valley |
| 1958 | Jack Kilby | Primer circuito integrado (germanio); Nobel 2000 | EE.UU. / Texas Instruments |
| 1959 | Robert Noyce | IC planar fabricable; cofundador de Intel | EE.UU. / Fairchild Semiconductor |
| 1965 | Gordon Moore | Observación de la ley de Moore; cofundador de Intel | EE.UU. / Fairchild → Intel |
| 2019 | Jensen Huang | Declaración del fin de la ley de Moore clásica | EE.UU. / NVIDIA (GTC 2019) |

---

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[01_LOGICA#1937 · Lógica → circuitos]] → Shannon demuestra que la lógica booleana se implementa en relés — esto es la licencia teórica de Z3, Colossus y ENIAC
- ↗ De [[03_ARQUITECTURA#1945 · Programa almacenado]] → Von Neumann proporciona la arquitectura que ENIAC parcialmente precede y que el Manchester Baby implementa
- ↗ De [[02_ALGORITMOS#2017 · AMD Ryzen / Zen]] (PC) → chiplet architecture que influye en el pivote post-Moore

Lo que esta columna **aporta** a otras columnas:

- ↘ De ENIAC (1946) → habilita Monte Carlo (simulación), backpropagation práctica, y toda la computación científica
- ↘ De IC (1959) → habilita [[PC]] completo — Intel 4004, la cadena de microprocesadores
- ↘ De IC (1959) → habilita [[NET#1969 · ARPANET]] — el circuito integrado hace factible la miniaturización de routers
- ↘ De IC (1959) → habilita SPICE (simulación de circuitos integrados)
- ↘ De Transistor (1947) → habilita toda la industria semiconductora; sustrato de GPU, CPU, TPU
- ↘ De GAA (2022) → habilita [[PC]] — Apple M5 (2026), Intel 18A

---

## Lectura siguiente

- Si te interesa cómo los circuitos integrados se convierten en microprocesadores y PCs → PC en el grafo
- Si quieres ver la GPU como extensión de la electrónica hacia el cómputo paralelo → GPU en el grafo
- Si quieres la lógica teórica que precede a los circuitos → [[01_LOGICA]]
- Si quieres ver cómo la electrónica se convierte en software de sistemas → [[05_SOFTWARE]]

---

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
