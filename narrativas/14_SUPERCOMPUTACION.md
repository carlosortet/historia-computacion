---
columna: SUPERCOMP
cat: SUP
nodos_cubiertos: 8
periodo: 1976 → 2025
---

# SUPERCOMPUTACIÓN · Del teraflop al exaflop en 26 años

> Cada salto de un orden de magnitud en potencia de cómputo abre una nueva clase de problemas: predicción climática, diseño nuclear, simulación de proteínas, entrenamiento de modelos de IA a escala.

## El arco

La supercomputación tiene un patrón claro: cada 10-15 años un nuevo hito de velocidad (tera → peta → exa) y con él una nueva tecnología de aceleración (vectorial → escalar cluster → híbrido CPU+GPU → GPU dominante). El Cray-1 define el género en 1976. El ASCI Red en 1997 demuestra que los clusters de chips de PC pueden desplazar a la arquitectura vectorial propietaria. El Roadrunner en 2008 introduce la arquitectura híbrida. Frontier en 2022 confirma que la GPU ya no es accesoria sino la columna vertebral. El nodo con Folding@home es singular: un superordenador distribuido de 500 petaflops construido con millones de PCs domésticos voluntarios, que demuestra que la centralización no es la única vía. La columna conecta directamente con el paralelismo masivo de GPUs y con la simulación, que es su aplicación más importante.

## La cadena

### 1976 · Cray-1 — Seymour Cray

**Seymour Cray** diseña el Cray-1 (instalado en Los Alamos National Laboratory, mar 1976): arquitectura vectorial, 80 MHz, 160 MFLOPS (160 millones de operaciones de coma flotante por segundo). Refrigeración por freón. Diseño circular con asientos de cuero bordeando el chasis — Cray quería que los cables fueran lo más cortos posible.

El Cray-1 define el concepto moderno de supercomputadora: hardware propietario, diseño radicalmente diferente al hardware comercial, propósito científico específico. **Seymour Cray** fundó Cray Research en 1972 tras años en Control Data Corporation.

**Conduce a:** ASCI Red (1997)

---

### 2000 · Folding@home — Vijay Pande

**Vijay Pande** (Stanford) lanza Folding@home (oct 2000): cómputo distribuido voluntario para simulación molecular de plegamiento de proteínas. Cualquier persona puede instalar el cliente y ceder ciclos de CPU/GPU inactivos. En marzo 2020, durante el pico de COVID-19, Folding@home alcanza 470 petaflops — más potente que el número 1 del TOP500 en ese momento.

El proyecto funciona durante 21 años en paralelo a AlphaFold — el mismo problema del plegamiento de proteínas atacado con fuerza bruta distribuida frente a IA.

**Conduce a:** Frontier (2022) en paralelo conceptual — centralizado vs distribuido · **Depende de:** ningún nodo de la columna; es entrada lateral desde la simulación distribuida

---

### 1997 · ASCI Red · 1 TF — Intel / Sandia

**Intel** construye el ASCI Red para **Sandia National Laboratories** (entregado dic 1996, operativo 1997): 9.152 nodos con procesadores Pentium Pro interconectados. Primer superordenador en superar 1 teraflop (1.06 TFLOPS Linpack). Coste: 55 millones de dólares.

La lección estratégica: el hardware de PC en cluster supera a las arquitecturas vectoriales propietarias en coste/rendimiento. El paradigma "clusters de x86" gana la guerra del TOP500 durante 20 años.

**Conduce a:** Roadrunner (2008) · **Depende de:** Cray-1 (1976) como punto de partida del género

---

### 2008 · Roadrunner · 1 PF — IBM / Los Alamos

**IBM** construye Roadrunner para **Los Alamos National Laboratory**: 6.480 nodos cada uno con un procesador AMD Opteron + dos chips IBM Cell (el procesador del PS3). Primer superordenador en superar 1 petaflop (1.026 PFLOPS, jun 2008). Primer uso masivo de arquitectura heterogénea: CPU de propósito general + acelerador especializado.

El Cell processor fue diseñado por IBM, Sony y Toshiba para el PlayStation 3. Roadrunner reutilizó hardware de consumo masivo como acelerador científico — exactamente la misma lógica que llevará a las GPUs a dominar el campo.

**Conduce a:** Fugaku (2020) · **Depende de:** ASCI Red (1997)

---

### 2020 · Fugaku — RIKEN / Fujitsu

**RIKEN** (instituto japonés de ciencias) y **Fujitsu** construyen Fugaku: 158.976 nodos con procesadores Fujitsu A64FX (ARM, 48 núcleos cada uno). Número 1 del TOP500 desde junio 2020 hasta noviembre 2021: 442 petaflops Linpack. Primer sistema ARM en lo más alto del ranking.

El A64FX incluye High Bandwidth Memory (HBM) integrada. La clave de rendimiento no es la velocidad de reloj sino el ancho de banda memoria-cómputo. En aplicaciones de simulación climática y molecular, Fugaku supera a sistemas nominalmente más rápidos.

**Conduce a:** Frontier (2022) · **Depende de:** Roadrunner (2008)

---

### 2022 · Frontier · 1 EF — HPE / AMD / ORNL

**Oak Ridge National Laboratory** (ORNL, Tennessee) en colaboración con **HPE** y **AMD**: Frontier es el primer superordenador exascale oficialmente confirmado. 1.102 exaflops (1.1 exaflops) en Linpack (nov 2022). Arquitectura: 9.408 nodos AMD EPYC 7A53 (CPU, 64 núcleos) + 4× AMD Instinct MI250X (GPU) por nodo. Total: 37.632 GPUs AMD.

El salto del petaflop al exaflop tarda 14 años (2008-2022) — el mismo tiempo que del teraflop al petaflop. Pero la composición cambia radicalmente: en Roadrunner, los aceleradores eran el 15% del rendimiento total. En Frontier, las GPUs aportan el 90%.

**Conduce a:** El Capitan (2024) · **Depende de:** Fugaku (2020), [[12_PARALELISMO#2006 · CUDA]] (como tecnología habilitadora de GPU en HPC)

---

### 2024 · Aurora — Intel / Argonne

**Argonne National Laboratory** (Illinois) con **Intel** y **HPE**: Aurora es el segundo sistema exascale. 1.012 exaflops Linpack (jun 2024, tras múltiples retrasos). Arquitectura: 10.624 nodos Intel Xeon Max (Sapphire Rapids HBM) + 6× Intel Ponte Vecchio GPU por nodo. Total: 63.744 Intel GPUs.

Aurora demuestra que Intel puede construir GPUs competitivas en HPC, aunque los retrasos (estaba previsto para 2021) lo entregaron casi 2 años después de Frontier.

**Conduce a:** TPU v7 (2025) en GPU via [[12_PARALELISMO]] en paralelo de arquitecturas aceleradas · **Depende de:** Frontier (2022)

---

### 2024 · El Capitan — HPE / AMD / LLNL

**Lawrence Livermore National Laboratory** (California) con **HPE** y **AMD**: El Capitan toma el número 1 del TOP500 desde noviembre 2024. Rendimiento: >1.7 exaflops Linpack (estimado final: ~2 exaflops). Diseñado para simulaciones de armas nucleares sin pruebas físicas — programa de Stockpile Stewardship.

Arquitectura similar a Frontier pero con AMD Instinct MI300A: la primera APU (CPU + GPU en un mismo chip, con memoria unificada HBM) en un superordenador de primer nivel. Elimina el cuello de botella de la transferencia de datos entre CPU y GPU separados.

**Conduce a:** JUPITER Europa (2025) · **Depende de:** Frontier (2022)

---

### 2025 · JUPITER (EU) — EuroHPC / Jülich

**EuroHPC Joint Undertaking** instala JUPITER en el **Forschungszentrum Jülich** (Alemania): primer sistema exascale europeo. 4º en el TOP500 (jun 2025). Arquitectura modular: JUPITER Booster (nodos GPU para IA y HPC intensivo) + JUPITER Cluster (nodos CPU para trabajos con más comunicación que cómputo).

JUPITER es parte de la estrategia europea de soberanía tecnológica: no depender de infraestructura USA para investigación científica clasificada o sensible. El coste supera 500M EUR entre hardware e infraestructura.

**Depende de:** Frontier (2022) y El Capitan (2024) como referencia de diseño

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1976 | Seymour Cray | Diseñó el Cray-1 y fundó el concepto de supercomputadora | Cray Research / USA |
| 2000 | Vijay Pande | Lanzó Folding@home, cómputo distribuido voluntario | Stanford / USA |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:
- ↗ De [[12_PARALELISMO#2006 · CUDA]] → tecnología que convierte la GPU en acelerador dominante de HPC (Frontier, El Capitan, Aurora)
- ↗ De [[12_PARALELISMO#2009 · OpenCL]] → base tecnológica de las GPUs Intel en Aurora
- ↗ De [[12_PARALELISMO#TPU v7 Ironwood]] → en paralelo: arquitecturas exascale y ASICs de IA convergen en demanda energética

Lo que esta columna **aporta** a otras columnas:
- ↘ De Frontier/Aurora/El Capitan → capacidad de entrenamiento a escala para [[11_IA]] (modelos frontier)
- ↘ De Folding@home → precede conceptualmente a [[15_SIMULACION#AlphaFold]] en 21 años
- ↘ De JUPITER (2025) → paralelo con [[12_PARALELISMO#TPU v8]] como frontera de hardware 2025-2027
- ↘ De toda la columna → habilita las simulaciones científicas de [[15_SIMULACION]] (CFD, gemelos digitales, física nuclear)

## Lectura siguiente

- Si te interesa el hardware que impulsa estos sistemas → [[12_PARALELISMO]]
- Si te interesa lo que simulan → [[15_SIMULACION]]
- Si quieres ver el horizonte cuántico de la supercomputación → [[13_CUANTICA]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
