---
columna: MICRO+PC
cat: PC
nodos_cubiertos: 24
periodo: 1963 → 2027
---

# MICRO+PC · Del chip de 4 bits al paquete CPU+GPU+NPU

> La columna PC narra cómo el transistor se convirtió en microprocesador, el microprocesador en ordenador personal y el ordenador personal en el dispositivo que cabe en el bolsillo y razona con IA on-device.

## El arco

El relato empieza con un lápiz óptico sobre una pantalla en el MIT en 1963 y termina en 2027 con un paquete de silicio que integra CPU, GPU y NPU en una sola pieza para servir modelos de IA de miles de millones de parámetros. Entre ambos extremos: el circuito integrado como detonador, la GUI como interfaz que lleva el cómputo a no-técnicos, la arquitectura RISC como modelo de eficiencia, ARM como paradigma móvil y Apple Silicon como su culminación. La columna recibe la lógica de los transistores de ELECTRÓNICA y alimenta SOFTWARE, IA y INTERNET.

## La cadena

### 1963 · Sketchpad — Ivan Sutherland

**Ivan Sutherland** presenta su tesis doctoral en el MIT en 1963: Sketchpad, el primer sistema gráfico interactivo de la historia. Un lápiz óptico sobre el ordenador TX-2 (22 bits, transistores, Instituto Lincoln) permite dibujar figuras, aplicar restricciones geométricas y agrupar objetos en jerarquías.

Sketchpad inventa la GUI, las restricciones declarativas, la herencia visual y la programación interactiva en un solo trabajo. Sutherland recibe el Turing Award en 1988. Sin Sketchpad no existe el concepto de interacción visual con ordenadores.

**Conduce a:** [[#1968 · Mother of All Demos]] · **Depende de:** [[02_ELE#1959 · Circuito integrado]] (hardware que hace posible el TX-2)

---

### 1968 · Mother of All Demos — Douglas Engelbart

**Douglas Engelbart** (SRI Stanford) presenta el 9 de diciembre de 1968 en el Civic Auditorium de San Francisco, ante 1.000 ingenieros, en 90 minutos: el ratón, el hipertexto, la edición colaborativa en tiempo real, la videoconferencia, las ventanas en pantalla y el control por voz. Todo operativo, todo en una sola demo.

El sistema NLS (oN-Line System) corre en un SDS 940 en Menlo Park; la conexión al escenario va por una línea de telecomunicaciones especial. Engelbart lleva 10 años trabajando en estas ideas. La audiencia aplaude de pie. Xerox PARC se fundará al año siguiente para continuar esta visión.

**Conduce a:** [[#1973 · Xerox Alto]] · **Depende de:** [[#1963 · Sketchpad]] (la cadena de visión de la interfaz gráfica)

---

### 1971 · Intel 4004 — Federico Faggin, Ted Hoff, Stan Mazor, Masatoshi Shima

**Federico Faggin**, **Ted Hoff** (Marcian Hoff), **Stan Mazor** y **Masatoshi Shima** diseñan el Intel 4004: 4 bits, 2.300 transistores, 740 kHz, fabricado en 10 micrones. Lanzado el 15 de noviembre de 1971. El encargo original era un chipset para calculadoras de escritorio de Busicom; Hoff propuso integrar todo en un chip programable de propósito general.

Primer microprocesador comercial. Inaugura el modelo "ordenador en un chip" y la posibilidad de que cualquier dispositivo tenga lógica programable. La factura de diseño la paga Busicom; Intel negocia quedarse los derechos para otros usos.

**Conduce a:** [[#1972 · Intel 8008]] · **Depende de:** [[02_ELE#1959 · Circuito integrado]] (el IC es la condición de posibilidad del micro)

---

### 1972 · Intel 8008 — Intel

Intel lanza el **8008**: primer microprocesador de 8 bits. 3.500 transistores, 200 kHz a 800 kHz. Diseñado originalmente para un terminal CRT (Datapoint 2200); Intel lo adquiere y lo generaliza.

El salto de 4 a 8 bits parece pequeño pero es cualitativo: 8 bits permiten codificar caracteres ASCII directamente, abrir la puerta al procesamiento de texto.

**Conduce a:** [[#1974 · Intel 8080]]

---

### 1973 · Xerox Alto — Equipo Xerox PARC

Xerox PARC construye el **Alto**: primer ordenador personal con GUI completa, ethernet, ratón, editor WYSIWYG, pantalla de mapa de bits. El equipo incluye a **Butler Lampson**, **Charles Thacker**, **Alan Kay**, **Dan Ingalls** y **Adele Goldberg**, entre otros. Se fabrican aproximadamente 2.000 unidades; ninguna se comercializa.

Steve Jobs visita PARC en diciembre de 1979 con un grupo de Apple. Ve el ratón y la interfaz gráfica. Lo que no ve —o no entiende entonces— es el modelo de objetos de Smalltalk que corre sobre el Alto. La metáfora del escritorio nace en PARC, no en Apple.

**Conduce a:** [[#1984 · Macintosh]] · [[06_PARADIGMAS#1980 · Smalltalk-80]] (paralelo, mismo equipo)

---

### 1974 · Intel 8080 — Intel

El **Intel 8080**: 8 bits ampliado, 6.000 transistores, 2 MHz. Primer microprocesador con bus de 8 bits separado de datos y direcciones. Digital Research escribe CP/M para él.

Con el 8080 arrancan los primeros microordenadores útiles: el IMSAI 8080 (1975) y, sobre todo, el Altair 8800. Es también el antecesor arquitectónico del 8086 (1978) y de toda la familia x86.

**Conduce a:** [[#1975 · Altair 8800 + BASIC]] · [[#1980 · RISC]] (paralelo, crítica al CISC)

---

### 1975 · Altair 8800 + BASIC — Ed Roberts / Bill Gates, Paul Allen

**Ed Roberts** (MITS, Albuquerque) lanza el Altair 8800 en portada de *Popular Electronics* en enero de 1975: kit de 397 USD, sin teclado, sin pantalla, sin software. **Bill Gates** y **Paul Allen** leen el artículo en Harvard y escriben un intérprete BASIC para él en 8 semanas, desde cero, sin haber visto el hardware. Lo prueban por primera vez en el Altair real el día que lo entregan.

La transacción funda Microsoft y lanza la industria del software para PC. Antes del Altair, el software venía con el hardware. Después, el software es un negocio independiente.

**Conduce a:** [[#1976 · Apple I]]

---

### 1976 · Apple I — Steve Wozniak, Steve Jobs

**Steve Wozniak** diseña el Apple I en el garaje de Jobs (Los Altos, California): placa con CPU MOS 6502, 4 KB RAM (ampliable), video de texto. Jobs actúa como cofundador comercial: convence al Homebrew Computer Club y vende 200 unidades a 666,66 USD.

El Apple I es rudimentario pero elegante en su arquitectura mínima. Wozniak hace todo con menos chips de los que la competencia creía posible.

**Conduce a:** [[#1977 · Apple II]]

---

### 1977 · Apple II — Steve Wozniak, Steve Jobs

**Apple II** (junio 1977): color (6 colores en modo hi-res), sonido, 8 slots de expansión, 4 KB a 48 KB RAM. El primer microordenador pensado para el usuario no técnico. **VisiCalc** (1979, Dan Bricklin y Bob Frankston) lo convierte en herramienta empresarial y vende la plataforma a directivos de empresa que no habían tocado un ordenador.

Más de 5 millones de unidades vendidas entre 1977 y 1993. Primer producto de consumo masivo de la categoría.

**Conduce a:** [[#1981 · IBM PC 5150]] · [[#2012 · Raspberry Pi]] (paralelo)

---

### 1980 · RISC — John Cocke, David Patterson, John Hennessy

Tres grupos en paralelo: **IBM 801** (**John Cocke**, ~1975-1980), **Berkeley RISC** (**David Patterson**, 1980 —acuña el término—) y **Stanford MIPS** (**John Hennessy**, 1981). La tesis: pocas instrucciones simples, ejecutadas en un solo ciclo, son más rápidas que muchas instrucciones complejas porque el compilador puede optimizarlas mejor.

RISC da origen a SPARC (Sun, 1987), MIPS, PowerPC y ARM (1985). Treinta años después, ARM domina el móvil y empieza el desktop con M1. Patterson y Hennessy reciben el Turing Award en 2017.

**Conduce a:** [[#2007 · iPhone (ARM mobile)]] · [[#2020 · Apple M1 · ARM]] · [[#2010 · RISC-V]]

---

### 1981 · IBM PC 5150 — IBM / Microsoft

IBM lanza el **PC 5150** el 12 de agosto de 1981: CPU Intel 8088, hasta 640 KB RAM, MS-DOS (Microsoft compra QDOS a Seattle Computer Products por 75.000 USD). La decisión de IBM de usar componentes estándar y publicar los esquemas crea la arquitectura abierta.

Los clones llegan en 1982 (Compaq, con un IBM PC portátil). En 1984 hay ya cientos de fabricantes. IBM cede el control del estándar a Intel (chips) y Microsoft (sistema operativo) sin saberlo. La arquitectura x86 domina el ordenador personal durante 40 años.

**Conduce a:** [[#1984 · Macintosh]] (paralelo)

---

### 1984 · Macintosh — Steve Jobs, Jef Raskin, Andy Hertzfeld

El **Macintosh** (24 de enero de 1984, presentado con el anuncio "1984" de Ridley Scott en la Super Bowl) es el primer ordenador con GUI de éxito masivo. **Jef Raskin** concibió el proyecto; **Steve Jobs** tomó el control y lo reorientó hacia lo que había visto en Xerox PARC; **Andy Hertzfeld** y el equipo de software lo implementaron. Motorola 68000 a 8 MHz, 128 KB RAM, pantalla de 512×342 píxeles.

Llevar Smalltalk/PARC al mercado de consumo. El sistema de ficheros, el Finder y el sistema de fuentes tipográficas de calidad imprenta que Jobs impone (tras su clase de caligrafía en Reed College) cambian la comunicación visual en pantalla.

**Conduce a:** [[#1985 · Intel 80386]] · [[#1993 · Mosaic browser]] (dependencia cruzada)

---

### 1985 · Intel 80386 — Intel

Intel lanza el **386** (17 de octubre de 1985): primer x86 de 32 bits, 275.000 transistores, memoria protegida, modo virtual 8086. Permite ejecutar múltiples tareas en sistemas operativos multitarea (Windows NT, OS/2, Linux).

Sin el 386 no hay desktops ni servidores modernos. Es el hito que transforma el PC de "juguete sofisticado" en "máquina de trabajo seria".

**Conduce a:** [[#1993 · Intel Pentium]]

---

### 1993 · Intel Pentium — Intel

Intel **Pentium** (P5, 22 de marzo de 1993): arquitectura superescalar con doble pipeline. 60–66 MHz iniciales; llega a 200 MHz en 1996. La marca "Pentium" domina durante una década. El famoso bug del FPU (noviembre 1994, **Thomas Nicely**, Lynchburg College) obliga a IBM a suspender las ventas y a Intel a asumir 475 M USD en reemplazos.

**Conduce a:** [[#2003 · AMD Athlon 64]]

---

### 2003 · AMD Athlon 64 — Dirk Meyer, Fred Weber

**AMD** lanza el Opteron (abril 2003) y el Athlon 64 (septiembre 2003): primer x86 de 64 bits comercial. **Dirk Meyer** y **Fred Weber** lideran la arquitectura K8/AMD64. AMD se adelanta a Intel en el salto a 64 bits y obliga a toda la industria a migrar. Intel adopta el ISA AMD64 bajo el nombre "EM64T".

**Conduce a:** [[#2006 · Intel Core 2 Duo]]

---

### 2006 · Intel Core 2 Duo — Intel

Intel lanza el **Core 2 Duo** (Conroe, julio 2006): multi-core mainstream. 65nm, dos núcleos físicos, 4 MB L2 compartida. Fin de la guerra de GHz (el Pentium 4 a 3,8 GHz consumía 115 W); empieza la guerra de núcleos.

Recupera el liderazgo para Intel y define el modelo dominante durante 5 años, hasta Sandy Bridge (2011).

**Conduce a:** [[#2007 · iPhone (ARM mobile)]] (paralelo) · [[#2017 · AMD Ryzen / Zen]]

---

### 2007 · iPhone (ARM mobile) — Steve Jobs, Tony Fadell, Scott Forstall

**Apple** lanza el iPhone el 29 de junio de 2007. La CPU es la Samsung S5L8900 (ARM11 a 412 MHz). Jobs lo presenta en enero como "iPod + teléfono + internet communicator". El primer Apple Silicon propio (A4, ARM Cortex-A8) llega en 2010 con el iPad y el iPhone 4.

El iPhone es la inflexión de plataforma más grande desde el IBM PC. ARM pasa a dominar el móvil en 18 meses. **Tony Fadell** (hardware) y **Scott Forstall** (software iOS) son las piezas clave del equipo.

**Conduce a:** [[#2020 · Apple M1 · ARM]] · [[08_ROBOTICA#2024 · Humanoides comerciales]] (vía Raspberry Pi como puente)

---

### 2008 · Android 1.0 — Andy Rubin, Google

**Google** libera Android 1.0 en septiembre de 2008 en el HTC Dream. Sistema operativo móvil open source basado en el kernel Linux. Google adquiere la empresa de **Andy Rubin** en 2005 por 50 millones de USD.

Android funda el duopolio iOS/Android. En 2024 supera el 70% del mercado global de smartphones. Demuestra que open source puede liderar en consumo masivo. La decisión de liberarlo sin royalties obliga a todos los fabricantes a abandonar Symbian y Windows Mobile.

**Conduce a:** [[#2024 · NPU mainstream]] · **Depende de:** [[04_SOFTWARE#1991 · Linux kernel]]

---

### 2010 · RISC-V — Krste Asanović, David Patterson

**Berkeley RISC-V**: proyecto iniciado en 2010 por **Krste Asanović** y **David Patterson**; especificación ratificada en 2014. ISA abierto y libre de royalties. Sin dependencia de propietarios.

SiFive, Western Digital, Alibaba y NVIDIA (en microcontroladores de GPU) lo adoptan. La Unión Europea lo usa como apuesta estratégica de soberanía tecnológica. En 2024, el parque de chips RISC-V supera los 10.000 millones de unidades.

**Depende de:** [[#1980 · RISC]] (es su heredero arquitectónico directo)

---

### 2012 · Raspberry Pi — Eben Upton

**Eben Upton** (Universidad de Cambridge) lanza la Raspberry Pi en febrero de 2012: single-board computer con Linux, 35 USD. Pensado para educación en países con poco presupuesto, adoptado masivamente por makers, IoT y retro-gaming.

Más de 50 millones de unidades vendidas en 2024. Estándar de facto para prototipos hardware/software. La placa base más vendida de la historia en su categoría de precio.

**Conduce a:** [[08_ROBOTICA#2024 · Humanoides comerciales]] (puente: hardware barato democratiza robótica amateur)

---

### 2017 · AMD Ryzen / Zen — Lisa Su, Mike Clark

**AMD Zen 1** (Ryzen, marzo 2017): renacimiento de AMD tras una década de irrelevancia. Arquitectura chiplet: múltiples dies en un solo package conectados por Infinity Fabric. **Lisa Su** (CEO) y **Mike Clark** (arquitecto jefe de Zen) lideran el turnaround.

El chiplet rompe la lógica del die monolítico y baja el coste de fabricación al permitir mezclar nodos de proceso para distintos componentes. Intel, NVIDIA y Apple lo adoptan en los años siguientes.

**Conduce a:** [[#2024 · NPU mainstream]]

---

### 2020 · Apple M1 · ARM — Johny Srouji

**Apple M1** (noviembre 2020): primer SoC ARM en Mac, tras 15 años de Intel. 5nm TSMC, 8 núcleos CPU, GPU unificada, Neural Engine. Eficiencia disruptiva: 10 W con rendimiento de chips de escritorio de 35 W. **Johny Srouji** lidera el equipo de silicio de Apple desde 2008.

ARM llega al desktop. Desencadena Snapdragon X Elite de Qualcomm (2024) y la nueva ola de Windows-on-ARM. Intel pierde el contrato de Apple después de 15 años.

**Conduce a:** [[#2024 · NPU mainstream]]

---

### 2024 · NPU mainstream — múltiples fabricantes

Apple A17 Pro (iPhone 15 Pro, sep 2023), **Snapdragon X Elite** (Qualcomm, 2024), **Intel Core Ultra** (Meteor Lake, dic 2023), **AMD Ryzen AI** (Hawk Point, 2024): las NPU (Neural Processing Units) pasan a ser un bloque obligatorio en todo SoC de consumo. 40+ TOPS on-device.

Microsoft define la categoría "Copilot+ PC" (mayo 2024) exigiendo 40 TOPS mínimos. Modelos de lenguaje pequeños (Phi-3, Llama 3.2 de 1B) corren localmente sin conexión a cloud.

**Conduce a:** [[#2026 · Apple M5 + Intel 18A]]

---

### 2026 · Apple M5 + Intel 18A — Apple / Intel

**Apple M5** en nodo N3P de TSMC · **Intel Panther Lake** debuta el nodo 18A con backside power delivery (PowerVia) y RibbonFET (GAA, equivalente al transistor Gate-All-Around). Primera vez en una década que Intel compite en fabricación con TSMC.

La carrera de nodos se reabre. Apple mantiene la ventaja en eficiencia energética; Intel apuesta por recuperar el liderazgo de fabricación.

**Conduce a:** [[#2027 · Apple M6 + Vera (esp.)]]

---

### 2027 · Apple M6 + Vera (esp.) — Apple / NVIDIA

**Apple M6** esperado en TSMC N2 (2 nm). **NVIDIA Vera CPU**: primera CPU diseñada explícitamente como compañera de GPU para IA, con NVLink directo al chip Rubin. Vera+Rubin en un solo package.

Convergencia CPU+GPU+NPU: el "computer for AI" deja de ser un cluster de racks y se convierte en un único package que cabe en un servidor de 1U.

**Depende de:** [[05_GPU#2026 · NVIDIA Rubin]] (Rubin GPU es la pareja de Vera CPU)

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1963 | Ivan Sutherland | Sketchpad: primera GUI e interacción gráfica | MIT, EE.UU. |
| 1968 | Douglas Engelbart | Mother of All Demos: ratón, hipertexto, colaboración | SRI Stanford, EE.UU. |
| 1971 | Federico Faggin | Diseño físico del Intel 4004 | Intel, EE.UU. |
| 1971 | Ted Hoff (Marcian Hoff) | Arquitectura del Intel 4004 | Intel, EE.UU. |
| 1971 | Stan Mazor | Diseño del Intel 4004 | Intel, EE.UU. |
| 1971 | Masatoshi Shima | Diseño del Intel 4004 | Intel / Busicom, Japón |
| 1973 | Butler Lampson | Arquitectura del Xerox Alto | Xerox PARC, EE.UU. |
| 1973 | Charles Thacker | Hardware del Xerox Alto | Xerox PARC, EE.UU. |
| 1973 | Alan Kay | Visión del Xerox Alto y Smalltalk | Xerox PARC, EE.UU. |
| 1975 | Ed Roberts | Creador del Altair 8800 | MITS, EE.UU. |
| 1975 | Bill Gates | Altair BASIC, cofundador Microsoft | Microsoft, EE.UU. |
| 1975 | Paul Allen | Altair BASIC, cofundador Microsoft | Microsoft, EE.UU. |
| 1976 | Steve Wozniak | Diseñador del Apple I y Apple II | Apple, EE.UU. |
| 1976 | Steve Jobs | Cofundador comercial de Apple, visión de producto | Apple, EE.UU. |
| 1979 | Dan Bricklin | VisiCalc (junto con Frankston) | Software Arts, EE.UU. |
| 1979 | Bob Frankston | VisiCalc (junto con Bricklin) | Software Arts, EE.UU. |
| 1980 | John Cocke | IBM 801, RISC precursor | IBM Research, EE.UU. |
| 1980 | David Patterson | Berkeley RISC, acuña el término, RISC-V | UC Berkeley, EE.UU. |
| 1981 | John Hennessy | Stanford MIPS, RISC | Stanford, EE.UU. |
| 1984 | Jef Raskin | Concepto original del Macintosh | Apple, EE.UU. |
| 1984 | Andy Hertzfeld | Software del Macintosh | Apple, EE.UU. |
| 2003 | Dirk Meyer | Arquitectura AMD K8/Athlon 64 | AMD, EE.UU. |
| 2003 | Fred Weber | Codiseñador AMD K8 | AMD, EE.UU. |
| 2008 | Andy Rubin | Fundador Android | Android Inc. / Google, EE.UU. |
| 2010 | Krste Asanović | RISC-V, cofundador | UC Berkeley, EE.UU. |
| 2012 | Eben Upton | Creador de Raspberry Pi | Universidad de Cambridge, UK |
| 2017 | Lisa Su | CEO AMD, turnaround Zen/Ryzen | AMD, EE.UU. |
| 2017 | Mike Clark | Arquitecto jefe de Zen | AMD, EE.UU. |
| 2020 | Johny Srouji | Liderazgo equipo Apple Silicon | Apple, EE.UU. |
| 2007 | Tony Fadell | Hardware del iPhone | Apple, EE.UU. |
| 2007 | Scott Forstall | Software iOS del iPhone | Apple, EE.UU. |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[02_ELE#1959 · Circuito integrado]] → habilita el Intel 4004 (el IC es condición de posibilidad del microprocesador)
- ↗ De [[06_PARADIGMAS#1980 · Smalltalk-80]] → habilita el Macintosh (la GUI de Mac hereda Smalltalk/PARC)
- ↗ De [[04_SOFTWARE#1991 · Linux kernel]] → habilita Android (Android es Linux para móvil)
- ↗ De [[05_GPU#2026 · NVIDIA Rubin]] → habilita Apple M6 + Vera (convergencia CPU+GPU en un paquete)
- ↗ De [[02_ELE#2022 · Transistor GAA]] → habilita Apple M5 + Intel 18A (nuevo nodo de proceso)

Lo que esta columna **aporta** a otras columnas:

- ↘ Macintosh → habilita [[09_INTERNET#1993 · Mosaic browser]] (Mac populariza la metáfora visual que Mosaic adopta)
- ↘ iPhone → habilita [[08_ROBOTICA#2024 · Humanoides comerciales]] (plataforma ARM barata y sensores maduros)
- ↘ Raspberry Pi → habilita [[08_ROBOTICA#2024 · Humanoides comerciales]] (hardware educativo → prototipado robótico)
- ↘ Android → habilita [[#2024 · NPU mainstream]] (Android pioneer en NPU móvil con chips Kirin/Exynos)
- ↘ RISC → habilita [[#2007 · iPhone]] y [[#2020 · Apple M1]] (arquitectura que hace eficiente el silicio móvil)

## Lectura siguiente

- Si te interesa la evolución de los chips aceleradores de IA (GPU, TPU) → [[05_GPU]]
- Si quieres seguir la capa de software que corre sobre este hardware → [[04_SOFTWARE]]
- Si quieres ver cómo este hardware alimenta la robótica → [[08_ROBOTICA]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
