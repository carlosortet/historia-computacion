---
columna: ROBÓTICA
cat: ROBOT
nodos_cubiertos: 9
periodo: 1961 → 2027
---

# ROBÓTICA · Del brazo de soldadura al agente físico generalista

> La robótica empieza como automatización industrial ciega y termina como plataforma física para modelos de fundación: el mismo arco que la IA, pero en el espacio físico.

## El arco

En 1961, un brazo hidráulico mueve piezas calientes en una cadena de montaje de GM en New Jersey. En 2027, se espera el primer modelo de fundación robótica capaz de habitar cualquier cuerpo físico —humanoide, brazo industrial, dron, vehículo— sin reentrenamiento. Entre ambos extremos, la columna ROBÓTICA narra tres transiciones: de manipulación programada a percepción autónoma, de laboratorio a producto de consumo, y de programación por tarea a aprendizaje generalista. La columna recibe de IA (el perceptrón, el Transformer) y de PC (Raspberry Pi, iPhone) sus habilitadores clave.

## La cadena

### 1961 · Unimate — George Devol, Joseph Engelberger

**George Devol** patenta el concepto en 1954; **Joseph Engelberger** (llamado "padre de la robótica industrial") negocia la implementación con General Motors. Unimate se instala en la planta de GM en Ewing Township, New Jersey, en 1961: manipula piezas metálicas calientes (die castings) en la línea de montaje, una tarea peligrosa para humanos.

El robot pesa 1.800 kg, tiene 6 grados de libertad hidráulicos y sigue instrucciones almacenadas en un tambor magnético. Sin sensores de visión, sin IA: pura programación de trayectoria. Las fábricas de automóviles de GM, Ford y Chrysler lo adoptan en los años 60 y 70. Es la fundación de 60 años de robótica industrial.

**Conduce a:** [[#1978 · PUMA 600]] · **Depende de:** [[02_ARQ#1948 · Autómatas autoreplicantes]] (paralelo conceptual: la idea de máquinas que se replican en fábricas)

---

### 1972 · Shakey · SRI — Charles Rosen, Nils Nilsson, Bertram Raphael

**SRI International** construye Shakey entre 1966 y 1972. El equipo, liderado por **Charles Rosen** y con contribuciones de **Nils Nilsson** y **Bertram Raphael**, combina por primera vez tres capacidades en un solo sistema: visión por computador (cámara de TV), planificación simbólica (planificador STRIPS — Stanford Research Institute Problem Solver) y movimiento físico autónomo.

Shakey se mueve a ~1 m/min, tarda minutos en planificar cada acción y solo opera en un entorno de bloques simples. Pero demuestra que un robot puede razonar sobre su entorno antes de actuar. STRIPS influye en toda la planificación en IA durante décadas. El nombre viene del temblor que producían sus motores.

**Conduce a:** [[#1978 · PUMA 600]] (paralelo) · **Depende de:** [[03_IA#1958 · Perceptrón]] (el conexionismo temprano habilita la visión)

---

### 1978 · PUMA 600 — Victor Scheinman, Unimation

**Victor Scheinman** diseña el PUMA (Programmable Universal Machine for Assembly): brazo eléctrico con 6 grados de libertad, encoder en cada articulación, controlado por minicomputador PDP-11. Unimation lo comercializa desde 1978.

PUMA define la geometría de brazo articulado que veremos en prácticamente todos los robots industriales de los 40 años siguientes: KUKA, Fanuc, ABB. La programación por teach-pendant (guiar el brazo con el operador) se convierte en estándar. Más de 100.000 unidades instaladas en los años 80.

**Conduce a:** [[#2002 · Roomba]]

---

### 2002 · Roomba — iRobot (Colin Angle, Helen Greiner, Rodney Brooks)

**iRobot** lanza el Roomba en septiembre de 2002. **Colin Angle** (CEO), **Helen Greiner** (presidenta) y **Rodney Brooks** (director técnico, también fundador de la empresa y profesor en MIT) llevan 10 años trabajando en robótica móvil. El precio inicial es 199 USD.

El Roomba no usa un mapa del hogar: navega con una combinación de sensores de infrarrojos, contacto y algoritmos probabilísticos que cubren el suelo de forma estadística. Es suficiente para limpiar. Más de 50 millones de unidades vendidas hasta 2024. Primera vez que la robótica entra al hogar como producto de serie, no como demostración de laboratorio.

**Conduce a:** [[#2007 · DARPA Urban Challenge]] (paralelo) · **Depende de:** [[#1978 · PUMA 600]]

---

### 2007 · DARPA Urban Challenge — Sebastian Thrun, Chris Urmson

**DARPA Urban Challenge** (Victorville, California, 3 de noviembre de 2007): 11 equipos de universidades y empresas compiten con vehículos que deben circular 60 millas en un entorno urbano simulado con tráfico real, señales y aparcamiento.

Ganadores: **Boss** (CMU, liderado por **Chris Urmson**) y **Junior** (Stanford, liderado por **Sebastian Thrun**). Boss completa el curso en 4h 10min. Los 6 primeros equipos lo terminan. Thrun funda Google Street View ese mismo año; en 2009 arranca Google Self-Driving Car (después Waymo). Urmson funda Aurora Innovation en 2017. Todos los proyectos de conducción autónoma actuales tienen raíces directas en este evento.

**Conduce a:** [[#2015 · Spot · Boston Dynamics]] · **Depende de:** [[#2002 · Roomba]] (paralelo: robótica autónoma entra a espacios no industriales)

---

### 2015 · Spot · Boston Dynamics — Marc Raibert

**Boston Dynamics** presenta Spot (2015), sucesor eléctrico del hidráulico BigDog (2005). **Marc Raibert** fundó Boston Dynamics como spin-off del MIT Leg Lab en 1992. Spot pesa 32 kg, sube escaleras, se recupera de empujones y corre a 1,6 m/s. Se comercializa en 2019 a 74.500 USD.

El salto de BigDog (hidráulico, ruidoso, 109 kg) a Spot (eléctrico, silencioso, 32 kg) es posible por los avances en servomotores sin escobillas y en baterías de litio: la misma tecnología que habilita el dron y el coche eléctrico. Boston Dynamics es adquirida por Hyundai en 2021.

**Conduce a:** [[#2024 · Humanoides comerciales]]

---

### 2024 · Humanoides comerciales — múltiples empresas

Primera ola comercial de robots humanoides: **Figure 01** (Figure AI, Brett Adcock), **Tesla Optimus Gen 2** (Elon Musk, liderazgo de ingeniería por **Milan Kovac**), **1X NEO** (Halodi Robotics, Norway), **Apptronik Apollo** (Jeff Cardenas, University of Texas), **Unitree H1** (Wang Xingxing, China).

El habilitador común: servomotores eléctricos económicos (costes caídos 10× en una década por la industria de los drones y los VEs) más modelos de lenguaje grandes que permiten razonamiento de sentido común. Amazon contrata 750 robots Figure para sus almacenes en 2024. BMW integra Figure en su planta de Spartanburg, Carolina del Sur.

**Conduce a:** [[#2024 · Robot Foundation Models]] · **Depende de:** [[03_IA#2017 · Transformer]] · [[07_MICRO_PC#2012 · Raspberry Pi]] (hardware barato como puente)

---

### 2024 · Robot Foundation Models — Sergey Levine, equipo Physical Intelligence

Los modelos VLA (Vision-Language-Action) se materializan en 2023-2024. Hitos:
- **Google RT-2** (julio 2023): primer modelo que combina lenguaje + visión + acción.
- **Open X-Embodiment / RT-X** (octubre 2023): dataset de 22 robots diferentes con 527 skills.
- **OpenVLA** (junio 2024, **Moo Jin Kim** et al., Stanford): modelo open source VLA.
- **π0** de Physical Intelligence (31 octubre 2024, **Sergey Levine** + **Chelsea Finn** + equipo): primer modelo generalista multi-tarea entrenado en datasets cross-embodiment. Maneja doblar ropa, cargar lavavajillas, montar cajas.

La robótica deja de programarse tarea a tarea. Un modelo único maneja miles de tareas en distintas plataformas físicas.

**Conduce a:** [[#2027 · Robot FM cross-embodiment (esp.)]] · **Depende de:** [[03_IA#2017 · Transformer]]

---

### 2027 · Robot FM cross-embodiment (esp.) — expectativa industria

Próxima frontera esperada: modelos VLA verdaderamente generalistas que transfieren entre plataformas físicas radicalmente distintas (humanoide, brazo industrial, dron, vehículo) sin fine-tuning. Los candidatos son los sucesores de π0 (π2/π3), RT-3 y sucesores de OpenVLA escalando a billion+ trayectorias de entrenamiento.

El paralelismo con los LLMs es explícito en la industria: un único modelo de lenguaje entiende inglés, francés y código; un único modelo robótico debería entender Spot, Figure y un brazo KUKA.

**Depende de:** [[#2024 · Robot Foundation Models]] · [[03_IA#2025 · NVIDIA Cosmos · Genesis 2]] (simulación sintética de datos de entrenamiento) · [[03_IA#2026 · Claude Opus 4.7 · 1M]] (razonamiento de alto nivel para planificación)

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1954 | George Devol | Patente del concepto Unimate | EE.UU. |
| 1961 | Joseph Engelberger | Comercialización de Unimate, "padre robótica industrial" | Unimation, EE.UU. |
| 1966 | Charles Rosen | Director del proyecto Shakey en SRI | SRI International, EE.UU. |
| 1968 | Nils Nilsson | Planificador STRIPS, Shakey | SRI International, EE.UU. |
| 1968 | Bertram Raphael | Contribución a Shakey | SRI International, EE.UU. |
| 1978 | Victor Scheinman | Diseñador del PUMA 600 | Unimation / Stanford, EE.UU. |
| 1992 | Marc Raibert | Fundador Boston Dynamics, BigDog, Spot | MIT / Boston Dynamics, EE.UU. |
| 2002 | Colin Angle | CEO y cofundador de iRobot / Roomba | iRobot, EE.UU. |
| 2002 | Helen Greiner | Cofundadora de iRobot | iRobot, EE.UU. |
| 2002 | Rodney Brooks | Cofundador iRobot, director técnico | MIT / iRobot, EE.UU. |
| 2007 | Sebastian Thrun | Equipo Junior (Stanford), funda Google Self-Driving Car | Stanford / Google, EE.UU. |
| 2007 | Chris Urmson | Equipo Boss (CMU), funda Aurora Innovation | CMU / Aurora, EE.UU. |
| 2024 | Brett Adcock | CEO y fundador de Figure AI | Figure AI, EE.UU. |
| 2024 | Milan Kovac | Liderazgo ingenieril de Tesla Optimus | Tesla, EE.UU. |
| 2024 | Wang Xingxing | Fundador de Unitree Robotics | Unitree, China |
| 2024 | Jeff Cardenas | CEO Apptronik | Apptronik / UT Austin, EE.UU. |
| 2024 | Sergey Levine | Physical Intelligence, π0 | UC Berkeley / Physical Intelligence, EE.UU. |
| 2024 | Chelsea Finn | Physical Intelligence, meta-learning robótico | Stanford / Physical Intelligence, EE.UU. |
| 2024 | Moo Jin Kim | OpenVLA, Stanford | Stanford, EE.UU. |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[03_IA#1958 · Perceptrón]] → habilita Shakey (visión temprana y razonamiento conexionista)
- ↗ De [[02_ARQ#1948 · Autómatas autoreplicantes]] → paralelo conceptual con Unimate (máquinas que replican tareas humanas en fábricas)
- ↗ De [[03_IA#2017 · Transformer]] → habilita Humanoides comerciales y Robot Foundation Models (el LLM como cerebro del robot)
- ↗ De [[07_MICRO_PC#2012 · Raspberry Pi]] → habilita Humanoides comerciales (hardware barato como puente para prototipado)
- ↗ De [[10_SIM#2025 · NVIDIA Cosmos · Genesis 2]] → habilita Robot FM cross-embodiment (datos sintéticos de entrenamiento)
- ↗ De [[03_IA#2026 · Claude Opus 4.7 · 1M]] → habilita Robot FM cross-embodiment (razonamiento de alto nivel)

Lo que esta columna **aporta** a otras columnas:

- ↘ No hay aristas salientes hacia otras columnas principales en el grafo: la robótica es receptora neta de habilitadores de IA, PC y simulación.

## Lectura siguiente

- Si te interesa la IA que hace razonar a los robots → [[03_IA]]
- Si quieres ver los entornos de simulación donde se entrenan → [[10_SIM]]
- Si te interesa el hardware de bajo coste que democratiza la robótica → [[07_MICRO_PC]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
