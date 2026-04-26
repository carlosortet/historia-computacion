---
columna: SIMULACION
cat: SIM
nodos_cubiertos: 11
periodo: 1947 → 2027
---

# SIMULACIÓN · Del dado de von Neumann al mundo sintético

> Desde la primera predicción meteorológica numérica hasta los modelos generativos que aprenden física al ver vídeos del mundo real: la simulación pasa de programarse a aprenderse.

## El arco

La simulación como disciplina computacional nace en el Manhattan Project con Monte Carlo: usar la aleatoriedad para aproximar integrales que no tienen solución analítica. En 50 años recorre el camino completo: meteorología (1950), diseño de circuitos (1973), dinámica de fluidos en la ingeniería aeronáutica (1989), física en tiempo real para videojuegos que luego entrenan robots (2008), gemelos digitales industriales (2021-2022), y modelos de fundación que sintetizan entornos físicos completos sin necesidad de programarlos explícitamente (2025). El patrón: cada vez que la potencia de cómputo da un salto de orden de magnitud, una nueva clase de fenómenos pasa de "imposible de simular" a "simulable en tiempo útil". El problema que resuelve esta columna es epistemológico además de técnico: permite experimentar en mundos que no existen todavía antes de construirlos.

## La cadena

### 1947 · Monte Carlo — Ulam y von Neumann

**Stanislaw Ulam** (Los Alamos) concibe el método Monte Carlo recuperándose de una enfermedad en 1946. Estudiando solitario, se pregunta: ¿cuál es la probabilidad de que salga un cierto orden de cartas? En lugar de calcularlo combinatoriamente, propone muestrear el espacio aleatoriamente. **John von Neumann** lo formaliza y lo aplica a cálculos de difusión de neutrones para la bomba. El nombre "Monte Carlo" lo elige Ulam en honor al casino de Mónaco.

El método: si no puedes integrar una función analíticamente, muestrea muchos puntos aleatorios y promedia. Con suficientes muestras, el promedio converge al valor real. Funciona en 100 dimensiones igual que en 2.

**Conduce a:** Meteorología numérica en ENIAC (1950) · **Depende de:** [[03_ARQUITECTURA#1945 · Von Neumann]] — es el mismo equipo del Manhattan Project

---

### 1950 · Weather (ENIAC) — Charney, Fjørtoft, von Neumann

**Jules Charney** (MIT), **Ragnar Fjørtoft** (meteorólogo noruego) y **John von Neumann** ejecutan la primera predicción meteorológica numérica en ENIAC (abril 1950, Princeton). Calculan un pronóstico de 24 horas para Norteamérica usando ecuaciones de cuasi-geostrofía simplificadas. El cálculo tarda 24 horas — el mismo tiempo que predice.

En 1955, la **Joint Numerical Weather Prediction Unit** (USAF + USNavy + USWB) ya produce predicciones operacionales diarias. El tiempo de cómputo cae por debajo del tiempo real a finales de los 50.

**Conduce a:** CFD industrial (1989) · **Depende de:** Monte Carlo (1947), [[02_ELECTRONICA#1946 · ENIAC]] como hardware

---

### 1973 · SPICE — Donald Pederson

**Donald Pederson** y equipo en **UC Berkeley** crean SPICE (Simulation Program with Integrated Circuit Emphasis): simulador de circuitos analógicos y digitales. Open source desde el primer día — Pederson insiste en que el código sea público para facilitar la adopción universitaria.

SPICE resuelve las ecuaciones diferenciales de los componentes electrónicos (transistores, condensadores, resistencias) y predice el comportamiento del circuito antes de fabricarlo. Antes de SPICE, los diseñadores de chips construían prototipos físicos para cada iteración — proceso lento y caro.

Sin SPICE no se diseña ningún chip moderno. Todos los EDA tools (Electronic Design Automation) de la industria descienden o compiten con SPICE.

**Conduce a:** CFD industrial (1989) como paralelo de simulación especializada · **Depende de:** [[02_ELECTRONICA#1959 · Circuito integrado]] — SPICE nace para simular ICs

---

### 1989 · CFD industrial — Boeing y aeronáutica

**Computational Fluid Dynamics** se vuelve estándar industrial en la aeronáutica y el automóvil. El hito canónico: el **Boeing 777** (certificado 1995) es el primer avión "100% diseñado en ordenador" sin maqueta física a escala completa. El gemelo digital computacional reemplaza el túnel de viento de madera.

Los grupos de investigación clave: **NASA Ames**, grupos en Oxford, ONERA (Francia). Los códigos: FLUENT, OVERFLOW, CFL3D. La GPU todavía no existe como acelerador — estos cálculos corren en estaciones de trabajo SGI y superordenadores Cray.

**Conduce a:** PhysX/Bullet (2008) · **Depende de:** Weather/ENIAC (1950) como precursor metodológico

---

### 2002 · A New Kind of Science — Stephen Wolfram

**Stephen Wolfram** publica *A New Kind of Science* (may 2002): 1.197 páginas con la tesis de que reglas computacionales simples (autómatas celulares) generan complejidad arbitraria. La regla 30, un autómata de 3 colores con una regla de 3 bits, produce patrones que superan el test de aleatoriedad de NIST.

La tesis central: el universo es un autómata computacional. El cómputo es el lenguaje fundamental de la naturaleza, no la matemática diferencial.

El libro es polémico (Wolfram no cita suficiente trabajo previo, incluyendo el de **John Conway** con Game of Life). Pero conecta la tradición de autómatas autoreplicantes de **von Neumann** (1948) con la simulación moderna: si las reglas simples generan complejidad, quizá la realidad es una simulación de bajo nivel.

**Conduce a:** PhysX (2008) en paralelo · **Depende de:** [[03_ARQUITECTURA#1948 · Autómatas autoreplicantes]] (von Neumann)

---

### 2008 · PhysX · Bullet — NVIDIA / Erwin Coumans

**NVIDIA** adquiere Ageia Technologies (4 feb 2008) y libera PhysX como SDK gratuito. **Erwin Coumans** desarrolla **Bullet Physics** (open source, desde 2003): rigid bodies, soft bodies, colisiones. PhysX se ejecuta en GPU; Bullet corre en CPU.

El impacto no es el videojuego en sí — es que los motores de juego (Unreal Engine, Unity) los integran como infraestructura estándar. Esto convierte los motores de juego en simuladores físicos de propósito general. Años después, Boston Dynamics, Waymo y todos los proyectos de robótica autónoma usarán derivados de esta infraestructura para entrenar sus sistemas.

**Conduce a:** NVIDIA Omniverse (2021) · **Depende de:** CFD industrial (1989), A New Kind of Science (2002)

---

### 2021 · NVIDIA Omniverse — NVIDIA

**NVIDIA** lanza Omniverse en versión general (dic 2021): plataforma de gemelos digitales en tiempo real basada en **USD** (Universal Scene Description), el formato de escenas 3D creado por **Pixar**. Multi-usuario: varios ingenieros de lugares distintos colaboran en la misma simulación simultáneamente. Físicamente correcta: materiales PBR, iluminación ray-traced, simulación de fluidos integrada.

Los primeros adoptantes industriales: **BMW** simula la fábrica completa antes de mover una máquina real. **Boeing** simula el ensamblaje de aviones. **Foxconn** planifica la reorganización de líneas de producción.

**Conduce a:** Digital Twins mainstream (2022) · **Depende de:** PhysX (2008), [[12_PARALELISMO]] para el hardware de renderizado físico

---

### 2022 · Digital Twins mainstream — BMW, Boeing, Singapore

Los gemelos digitales pasan de proyecto piloto a práctica industrial estándar. **BMW iFactory**: cada fábrica tiene su clon digital completo actualizado en tiempo real — líneas de montaje, robots, flujo de materiales. Si se reorganiza la planta virtual, el sistema predice cuellos de botella antes de mover nada físico.

**Digital Singapore**: el gobierno de Singapur crea un gemelo digital de toda la isla — edificios, infraestructura, datos de sensores urbanos en tiempo real — para planificación urbanística y gestión de emergencias.

La fusión: el gemelo digital no es ya una visualización sino un entorno en el que se toman decisiones que después se ejecutan en el mundo físico.

**Conduce a:** World Models / Sora (2024) · **Depende de:** NVIDIA Omniverse (2021)

---

### 2024 · World Models · Sora — OpenAI, DeepMind

**OpenAI** presenta Sora (15 feb 2024): modelo de difusión latente entrenado sobre vídeo masivo que genera clips de hasta 1 minuto físicamente consistentes. Sora no programa física explícitamente — aprende la dinámica del mundo al ver cómo se mueven las cosas en miles de millones de frames.

**DeepMind** publica Genie (paper arXiv, 23 feb 2024): modelo generativo entrenado en plataformers 2D que aprende las reglas del mundo físico de videojuegos sin supervisión explícita. Con un solo frame como prompt, genera el videojuego completo.

La transición conceptual: la simulación deja de programarse con ecuaciones diferenciales y comienza a aprenderse de observaciones del mundo.

**Conduce a:** NVIDIA Cosmos (2025) · **Depende de:** Digital Twins (2022), [[11_IA#2023 · GPT-4]] y Transformer como motor generativo

---

### 2025 · NVIDIA Cosmos · Genesis 2 — NVIDIA

**NVIDIA** anuncia Cosmos en CES (6 ene 2025): plataforma de "world foundation models" específicamente diseñados para entrenar robots y vehículos autónomos en entornos sintéticos. Los modelos de Cosmos generan escenas físicamente coherentes desde descripciones textuales o imágenes de referencia.

**Genesis 2** (sucesor open source del simulador Genesis): simulador de propósito general para robótica y física, compatible con los modelos de Cosmos como backend.

La lógica operativa: si necesitas millones de trayectorias de robot para entrenar una política robótica y el mundo real solo genera miles, la simulación genera los millones restantes. El ratio simulación/realidad pasa de 1:1 a 1000:1.

**Conduce a:** Foundation Simulation (2027) · **Depende de:** World Models (2024), [[10_ROBOTICA#Robot Foundation Models]]

---

### 2027 · Foundation simulation (esp.) — convergencia

Convergencia esperada: un único modelo de fundación capaz de simular cualquier entorno físico — mecánico, fluido, biológico, social — con prompts en lenguaje natural. Sora + AlphaFold + Cosmos en una capa unificada. Si describes "simula el plegamiento de esta proteína en un solvente acuoso a 37°C durante 10 microsegundos", el modelo genera la trayectoria.

La clave técnica habilitante: los modelos de fundación unificados aprenden física transferible entre dominios — la dinámica de fluidos comparte estructura matemática con la dinámica molecular que comparte estructura con los mercados financieros.

**Conduce a:** realidad como query; el mundo físico como dataset de validación · **Depende de:** NVIDIA Cosmos (2025), [[11_IA#2021 · AlphaFold 2]] como caso de demostración, [[10_ROBOTICA#Robot FM cross-embodiment]] en paralelo

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1947 | Stanislaw Ulam | Concepción del método Monte Carlo | Los Alamos / Polonia-USA |
| 1947 | John von Neumann | Formalización matemática de Monte Carlo | Los Alamos / Princeton |
| 1950 | Jules Charney | Primera predicción meteorológica numérica | MIT |
| 1950 | Ragnar Fjørtoft | Predicción meteorológica ENIAC (meteorólogo) | Instituto Meteorológico Noruego |
| 1973 | Donald Pederson | Creó SPICE, simulación de circuitos | UC Berkeley |
| 2002 | Stephen Wolfram | A New Kind of Science, autómatas y complejidad | Wolfram Research |
| 2008 | Erwin Coumans | Bullet Physics (open source) | Sony / Google |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:
- ↗ De [[03_ARQUITECTURA#1948 · Autómatas autoreplicantes]] → von Neumann conecta autómatas con A New Kind of Science
- ↗ De [[02_ELECTRONICA#1946 · ENIAC]] → hardware para la primera predicción meteorológica (1950)
- ↗ De [[02_ELECTRONICA#1959 · Circuito integrado]] → SPICE nace para simular ICs
- ↗ De [[11_IA#2023 · GPT-4]] → habilita los World Models como modelos generativos de física
- ↗ De [[11_IA#2021 · AlphaFold 2]] → demuestra que la IA puede resolver problemas de simulación científica
- ↗ De [[13_CUANTICA#1982 · Simulación cuántica]] → Feynman propone simular física con física (paralelo conceptual con Monte Carlo)
- ↗ De [[12_PARALELISMO]] → GPUs como acelerador de CFD, Omniverse, Cosmos
- ↗ De [[10_ROBOTICA#Robot Foundation Models]] → π0 y RT-2 consumen simulación como fuente de datos de entrenamiento

Lo que esta columna **aporta** a otras columnas:
- ↘ De Omniverse/Digital Twins → habilita [[10_ROBOTICA#Humanoides comerciales]] (entrenamiento en entornos sintéticos)
- ↘ De NVIDIA Cosmos (2025) → habilita [[10_ROBOTICA#Robot FM cross-embodiment]] (datos sintéticos a escala)
- ↘ De Foundation Simulation (2027) → paralelo con [[10_ROBOTICA#Robot FM cross-embodiment]] (misma frontera)
- ↘ De PhysX/Bullet → motores de juego como infraestructura de simulación física general

## Lectura siguiente

- Si te interesa la robótica que usa estas simulaciones → [[10_ROBOTICA]]
- Si te interesa la IA que aprende a simular mundos → [[11_IA]]
- Si te interesa la supercomputación que ejecuta estas simulaciones → [[14_SUPERCOMPUTACION]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
