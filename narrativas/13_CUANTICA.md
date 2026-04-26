---
columna: CUANTICA
cat: CUA
nodos_cubiertos: 13
periodo: 1980 → 2027
---

# CUÁNTICA · Del qubit teórico al chip que corrige sus propios errores

> Cuarenta y siete años de distancia entre la primera propuesta teórica y el primer hardware que demuestra corrección de errores cuánticos escalable — el problema más difícil del campo.

## El arco

La computación cuántica tiene tres fases distintas. Primera: teoría fundacional (1980-1994) — se demuestra que un ordenador cuántico puede existir y que tendría ventajas matemáticas verificables sobre los clásicos. Segunda: demostración experimental (1995-2019) — desde los primeros 2 qubits hasta el primer chip de 53 qubits que reclama "supremacía cuántica". Tercera: la fase actual (2019-2027) — el campo pivota de "cuántos qubits" a "cuántos qubits lógicos", porque un qubit físico con ruido vale poco; necesitas muchos qubits físicos coordinados + corrección de errores para construir uno lógico fiable. El Fault-Tolerant Quantum Computer (FTQC) — capaz de romper RSA y de simular moléculas complejas — sigue siendo el horizonte. Los chips actuales demuestran los componentes. No el sistema completo.

## La cadena

### 1980 · Modelo cuántico — Paul Benioff

**Paul Benioff** (Argonne National Laboratory) publica el primer modelo matemático de una máquina de Turing cuántica: un sistema cuántico de dos estados (qubit) que implementa los pasos de una máquina de Turing mediante evolución unitaria. El paper muestra que la mecánica cuántica no impide construir un ordenador — no que construir uno sea práctico.

Benioff trabaja en física teórica, no en ingeniería informática. El paper pasa desapercibido durante dos años.

**Conduce a:** Simulación cuántica (Feynman, 1982)

---

### 1982 · Simulación cuántica — Richard Feynman

**Richard Feynman** (Caltech) presenta *Simulating Physics with Computers* en una conferencia del MIT (dic 1981, publicado 1982). El argumento: simular un sistema cuántico con un ordenador clásico requiere tiempo exponencial en el número de partículas. Un ordenador que usa mecánica cuántica podría hacerlo en tiempo polinómico.

Feynman no sabe construir un ordenador cuántico. Da la motivación aplicada más poderosa del campo: si quieres simular la naturaleza con exactitud, necesitas una máquina que sea cuántica.

**Conduce a:** Computador universal (Deutsch, 1985), 2 qubits NMR (1998) · **También conecta a:** Monte Carlo (1947 en SIM) de manera paralela — ambos abordan la simulación física con diferentes herramientas

---

### 1985 · Computador universal — David Deutsch

**David Deutsch** (Universidad de Oxford) publica *Quantum Theory, the Church-Turing Principle and the Universal Quantum Computer* (1985). Formaliza el modelo del computador cuántico universal: análogo cuántico de la máquina de Turing universal. El algoritmo de Deutsch es el primero que demuestra ventaja cuántica para un problema específico (trivial, pero la prueba de principio existe).

La tesis Church-Turing cuántica: cualquier función computable puede simularse eficientemente por un computador cuántico universal. No demostrada, pero es el marco teórico que guía el campo.

**Conduce a:** Algoritmo de Shor (1994) · **Depende de:** Simulación cuántica (1982)

---

### 1994 · Algoritmo de Shor — Peter Shor

**Peter Shor** (Bell Labs) publica el algoritmo de factorización cuántica en tiempo polinómico. La factorización de un número de n bits lleva tiempo O(n³) en un ordenador cuántico frente a tiempo subexponencial en los mejores algoritmos clásicos conocidos. RSA-2048 — el cifrado que protege gran parte de las comunicaciones actuales — se basa en que factorizar es computacionalmente imposible en tiempo práctico.

El paper de Shor convierte la computación cuántica de curiosidad teórica en amenaza estratégica para las comunicaciones seguras. DARPA y NSA empiezan a financiar el campo seriamente.

**Conduce a:** QEC (1995), Algoritmo de Grover (1996), estimación ruptura RSA (2024) · **Depende de:** Computador universal (1985)

---

### 1995 · QEC · qubit lógico — Shor, Steane, Kitaev

**Peter Shor** (1995) publica los primeros códigos de corrección de errores cuánticos — el equivalente cuántico del código de paridad clásico, pero mucho más complejo porque medir destruye el estado cuántico. **Andrew Steane** (Oxford, 1996) simplifica el esquema con los códigos CSS (Calderbank-Shor-Steane). **Alexei Kitaev** (Caltech / Microsoft, 1997-2003) propone los surface codes: la disposición 2D de qubits físicos donde el error se detecta midiendo los vecinos sin colapsar los qubits de datos.

El concepto fundamental: un qubit lógico = N qubits físicos entrelazados + corrección continua de errores. Se comporta como un qubit "perfecto" aunque cada componente sea ruidoso. La métrica más importante del campo desde entonces: ¿cuántos qubits lógicos tiene el chip?

**Conduce a:** 2 qubits NMR (1998) como primer hardware, Willow (2024), IBM Heron (2023)

---

### 1996 · Algoritmo de Grover — Lov Grover

**Lov Grover** (Bell Labs) publica el algoritmo de búsqueda cuántica no estructurada. Dado un conjunto de N elementos sin ordenar, un algoritmo clásico necesita O(N) evaluaciones para encontrar el elemento objetivo. Grover necesita O(√N).

La ventaja es cuadrática, no exponencial como la de Shor. Para bases de datos de 1 billón de entradas: clásico necesita 1 billón de pasos, Grover necesita 1 millón. Aplicaciones: criptografía (rompe cifrados simétricos con la mitad de bits de seguridad efectiva), búsqueda en bases de datos.

**Conduce a:** contexto de amenaza criptográfica junto a Shor · **Depende de:** Algoritmo de Shor (1994) en paralelo

---

### 1998 · 2 qubits (NMR) — Chuang, Gershenfeld, Kubinec

**Isaac Chuang** (IBM), **Neil Gershenfeld** (MIT) y **Mark Kubinec** (UC Berkeley) demuestran un ordenador cuántico de 2 qubits usando Resonancia Magnética Nuclear (NMR): moléculas en solución actúan como qubits, manipuladas con pulsos de radiofrecuencia. Ejecutan el algoritmo de Deutsch en hardware real.

NMR tiene un límite inherente: a temperatura ambiente, el número de qubits que se pueden controlar coherentemente es pequeño. La vía NMR se abandona gradualmente. Pero esta demostración de 1998 es la primera prueba experimental de que los algoritmos cuánticos se pueden ejecutar.

**Conduce a:** Sycamore (2019) · **Depende de:** QEC (1995) — motiva el hardware experimental, Feynman (1982)

---

### 2019 · Sycamore — Google AI Quantum

**Google** anuncia "supremacía cuántica" con Sycamore (oct 2019): 53 qubits superconductores. La tarea: muestrear la distribución de probabilidad de un circuito cuántico aleatorio. Google afirma que Sycamore lo hace en 200 segundos; un superordenador clásico tardaría 10.000 años.

**IBM** disputa el resultado el mismo día: estimaciones más optimistas de la simulación clásica sitúan el tiempo en 2.5 días, no 10.000 años. La controversia sobre "supremacía vs ventaja cuántica" define el debate público del campo.

El nombre "supremacía cuántica" fue propuesto por **John Preskill** (Caltech) en 2012. El equipo de hardware lo lidera **Julian Kelly**.

**Conduce a:** Willow (2024) · **Depende de:** 2 qubits NMR (1998)

---

### 2023 · IBM Heron + System Two — IBM Quantum

**IBM** presenta el procesador Heron R1 (4 dic 2023): 133 qubits, tasa de error de gate 2-qubit 3× mejor que el procesador Eagle anterior. La novedad arquitectónica: acopladores fijos que permiten menor crosstalk entre qubits. Integrado en IBM Quantum System Two: primer sistema cuántico modular de IBM, que combina varios procesadores.

Heron R2 (jul 2024) escala a 156 qubits. El roadmap de IBM es público desde 2020 y se sigue con notable precisión: Eagle (127 qubits, 2021) → Osprey (433, 2022) → Condor (1.121, 2023) → Heron (133 qubits con mejor fidelidad, 2023).

**Conduce a:** IBM Loon + Nighthawk (2025), IBM Cockatoo (2027) · **Depende de:** QEC (1995) como teoría subyacente a la mejora de fidelidad

---

### 2024 · Willow — Google Quantum AI

**Google Quantum AI** presenta Willow (dic 2024): 105 qubits. El resultado técnico clave: por primera vez, añadir más qubits físicos al sistema de corrección de errores reduce el error total — en lugar de acumularlo. Este es el umbral necesario para la computación cuántica tolerante a fallos: demostrar que la corrección de errores escala en la dirección correcta.

En el benchmark de referencia del campo, Willow realiza un cálculo en 5 minutos que llevaría 10^25 años a un superordenador clásico (10.000 veces más que la edad del universo). El equipo lo lidera **Hartmut Neven** y **Julian Kelly**.

**Conduce a:** MS Majorana 1 (2025) en paralelo, IBM Cockatoo (2027) · **Depende de:** Sycamore (2019), QEC (1995)

---

### 2024 · Estimación ruptura RSA — Gidney, Ekerå

**Craig Gidney** (Google) y **Martin Ekerå** (Royal Institute of Technology, KTH) publican en 2019 la estimación de recursos para romper RSA-2048: ~20 millones de qubits físicos en 8 horas. Optimizaciones de Gidney (2024) reducen la estimación a ~1.300 qubits lógicos × 1 semana de cómputo.

La traducción práctica: con los chips actuales (Willow demuestra qubits lógicos pero a pequeña escala, Heron sin qubits lógicos demostrados en número suficiente), la amenaza efectiva a RSA está a más de una década. Pero "harvest now, decrypt later" es la amenaza real: adversarios pueden capturar tráfico cifrado hoy y descifrarlo cuando tengan el hardware. Esto justifica migrar a criptografía post-cuántica (PQC, NIST ha estandarizado las primeras primitivas en 2024) antes de que el hardware madure.

**Conduce a:** urgencia migración a PQC · **Depende de:** Algoritmo de Shor (1994), RSA [[15_ALGORITMOS#1977 · RSA]]

---

### 2025 · MS Majorana 1 — Microsoft

**Microsoft** anuncia Majorana 1 (feb 2025): primer chip cuántico basado en qubits topológicos. El sustrato: heterostructura InAs/Al (arseniuro de indio / aluminio) que genera modos de Majorana cero — estados cuánticos en los extremos de un nanohilo que codifican información de forma no local.

La promesa del qubit topológico: error intrínsecamente más bajo que el superconductor (Google/IBM) porque la información no está localizada en un punto físico sino distribuida. El coste: décadas de física experimental para demostrar que los modos de Majorana son reales (la controversia scientific sobre la detección empezó en 2012 y se resolvió con este chip).

**Conduce a:** vía alternativa a los chips superconductores · **Depende de:** Willow (2024) en paralelo

---

### 2025 · IBM Loon + Nighthawk — IBM Quantum

**IBM** anuncia Loon y Nighthawk (12 nov 2025). Loon: primer chip que demuestra todos los componentes técnicos necesarios para la computación cuántica tolerante a fallos (FTQC) — couplers de larga distancia, multiplexores de señal, sin crosstalk residual. Nighthawk: 120 qubits orientados a demostrar "ventaja cuántica computacional" en problemas reales (optimización química, materiales).

**Conduce a:** IBM Cockatoo (2027) · **Depende de:** IBM Heron (2023)

---

### 2027 · IBM Cockatoo (esp.) — IBM Quantum

**IBM** prevé Cockatoo como hito de 2027: primer sistema multi-chip cuántico que acopla módulos Kookaburra mediante L-couplers (acopladores resonantes de microondas). La arquitectura modular es el camino de IBM hacia escalado: en lugar de un chip monolítico de miles de qubits (físicamente imposible con tecnología superconductora actual), múltiples chips de ~100-200 qubits conectados.

El objetivo posterior: Starling (2029) — primer sistema orientado a FTQC a gran escala.

**Conduce a:** Starling (2029, fuera del rango de este grafo) · **Depende de:** IBM Loon + Nighthawk (2025), IBM Heron (2023)

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1980 | Paul Benioff | Primer modelo matemático de computación cuántica | Argonne National Lab / USA |
| 1982 | Richard Feynman | Propuesta de simulación cuántica con hardware cuántico | Caltech / USA |
| 1985 | David Deutsch | Computador cuántico universal, algoritmo de Deutsch | Oxford / UK |
| 1994 | Peter Shor | Algoritmo de factorización cuántica polinómica | Bell Labs / USA |
| 1995 | Peter Shor | Primeros códigos de corrección de errores cuánticos | Bell Labs |
| 1996 | Andrew Steane | Códigos CSS de corrección de errores | Oxford / UK |
| 1996 | Lov Grover | Algoritmo de búsqueda cuántica √N | Bell Labs / USA |
| 1997 | Alexei Kitaev | Surface codes, topological quantum computing | Caltech / Microsoft |
| 1998 | Isaac Chuang | Primer hardware cuántico de 2 qubits (NMR) | IBM |
| 1998 | Neil Gershenfeld | 2 qubits NMR | MIT |
| 1998 | Mark Kubinec | 2 qubits NMR | UC Berkeley |
| 2012 | John Preskill | Acuña "supremacía cuántica" | Caltech |
| 2019 | Julian Kelly | Hardware Sycamore y Willow | Google Quantum AI |
| 2019 | Hartmut Neven | Director Google Quantum AI | Google |
| 2019 | Craig Gidney | Estimación recursos ruptura RSA | Google |
| 2019 | Martin Ekerå | Co-estimación recursos ruptura RSA | KTH / Suecia |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:
- ↗ De [[01_LOGICA#1931 · Incompletitud]] → Gödel y la indecidibilidad inspiran la búsqueda de los límites de la computación, contexto del que surge la computación cuántica
- ↗ De [[15_ALGORITMOS#1971 · Cook-Levin]] → la frontera NP justifica buscar ventaja cuántica en problemas intratables
- ↗ De [[15_ALGORITMOS#1977 · RSA]] → RSA es el cifrado que Shor amenaza, justificando la financiación del campo

Lo que esta columna **aporta** a otras columnas:
- ↘ De Algoritmo de Shor (1994) → amenaza directa a [[15_ALGORITMOS#1977 · RSA]] (cripto clásica)
- ↘ De Feynman (1982) → paralelo conceptual con [[15_SIMULACION#1947 · Monte Carlo]] (ambos atacan simulación física)
- ↘ De Sycamore/Willow → presión sobre [[14_SUPERCOMPUTACION]] para mantener relevancia en benchmarks
- ↘ De Estimación ruptura RSA (2024) → urge migración criptográfica, afecta a [[09_DATOS#pgvector+Iceberg]] y toda la seguridad de datos

## Lectura siguiente

- Si te interesa la computación masivamente paralela no cuántica → [[12_PARALELISMO]]
- Si quieres ver los límites matemáticos de lo computable → [[01_LOGICA]]
- Si te interesa la supercomputación clásica en el mismo período → [[14_SUPERCOMPUTACION]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
