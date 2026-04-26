---
columna: PARALELISMO
cat: GPU
nodos_cubiertos: 16
periodo: 1999 → 2027
---

# PARALELISMO · De los píxeles al silicio de la inteligencia

> La GPU nació para dibujar triángulos; en 25 años se convirtió en el motor de toda la IA moderna, y los hyperscalers empezaron a diseñar sus propios chips para no depender de NVIDIA.

## El arco

El paralelismo masivo tiene una prehistoria en la supercomputación vectorial (Cray, 1976), pero esta columna arranca en 1999 con la GPU comercial y sigue hasta los chips especializados de 2027. El patrón es siempre el mismo: un hardware diseñado para un propósito (gráficos, luego IA, luego modelos de lenguaje) se generaliza hasta dominar el cómputo científico. CUDA (2006) es el bisagra: convierte la GPU de acelerador gráfico a plataforma de cómputo general. Desde ahí, la cadena produce Tensor Cores para entrenamiento, TPUs para los propios modelos de Google, ASICs de todos los hyperscalers, y arquitecturas especializadas al límite (Etched Sohu, diseñado solo para Transformers). Lo que resuelve esta columna: el problema de la latencia frente al throughput — cuando procesas en paralelo millones de operaciones simultáneas, el tiempo total cae aunque cada operación individual sea más lenta.

## La cadena

### 1999 · GeForce 256 — NVIDIA

**NVIDIA** lanza la GeForce 256 (ago 1999): primera GPU comercial con Transform and Lighting (T&L) acelerado por hardware. Antes, la CPU calculaba la posición y color de cada vértice 3D; ahora lo hace el chip gráfico. 23 millones de transistores. 15M vértices/segundo.

**Jensen Huang** (co-fundador y CEO de NVIDIA desde 1993) apuesta por el término "GPU" para distinguirse de las tarjetas de vídeo anteriores. La apuesta: si el hardware de juegos crece, NVIDIA crece con él.

**Conduce a:** Shaders programables (2001)

---

### 2001 · Shaders programables — NVIDIA GeForce 3

**NVIDIA** lanza la GeForce 3 (feb 2001): introduce vertex shaders y pixel shaders programables. El programador puede escribir código arbitrario que se ejecuta en la GPU para cada vértice o pixel.

Investigadores de cómputo científico observan la GeForce 3 y ven algo diferente: un procesador paralelo de propósito general disfrazado de acelerador gráfico. Los primeros experimentos GPGPU (General-Purpose Computing on GPU) usan shaders para resolver ecuaciones diferenciales.

**Conduce a:** CUDA (2006) · **Depende de:** GeForce 256 (1999)

---

### 2006 · CUDA — NVIDIA

**NVIDIA** lanza CUDA (Compute Unified Device Architecture) en noviembre 2006 con la arquitectura Tesla. **Ian Buck** (previamente en Stanford con el proyecto Brook) lidera el desarrollo. CUDA expone la GPU como plataforma de cómputo general en C/C++: memoria del dispositivo, kernels, threads organizados en bloques y grids.

El primer paper significativo usando CUDA es de **John Owens** y equipo. El impacto real llega cuando los grupos de IA descubren que pueden entrenar redes neuronales: lo que tardaba semanas en CPU tarda días en GPU.

**Conduce a:** Tensor Cores (2017), AlexNet (2012 en IA), Frontier (2022 en supercomp), TPU v1 (2015) · **Depende de:** Shaders programables (2001)

---

### 2009 · OpenCL — Khronos Group

**Apple** diseña OpenCL en 2008 y lo dona al **Khronos Group**, que publica la especificación 1.0 (dic 2008). Estándar abierto para cómputo paralelo cross-vendor: funciona en CPU + GPU + FPGA + DSP de cualquier fabricante. Apoyado por Apple, AMD, Intel, IBM, ARM.

OpenCL pierde la guerra del ecosistema frente a CUDA. Las razones: CUDA tiene compilador propio maduro, debugging, profiling, y una comunidad de investigación consolidada. OpenCL es más portable pero más difícil de optimizar.

**Conduce a:** Hyperscaler Silicon (2024) como motivación de independencia de NVIDIA · **Depende de:** CUDA (2006) como rival

---

### 2015 · TPU v1 — Google

**Google** diseña en secreto el TPU v1 (Tensor Processing Unit) y lo despliega en sus propios datacenters en 2015. El chip está diseñado exclusivamente para inferencia: operaciones de multiplicación de matrices en 8 bits. Seis veces más eficiente energéticamente que una GPU de gama alta para redes neuronales. Lo usan internamente en Search, Translate y Photos.

La decisión de fabricarlo viene de **Jeff Dean** y **Norm Jouppi**: un cálculo de back-of-the-envelope muestra que si los usuarios de Google usan reconocimiento de voz 3 minutos/día, necesitarían el doble de los datacenters existentes con CPUs.

**Conduce a:** TPU v2 (2017) · **Depende de:** CUDA (2006) como motivación para construir alternativa; Tensor Cores (2017) en paralelo como rival

---

### 2017 · Tensor Cores — NVIDIA Volta

**NVIDIA** lanza la arquitectura Volta (V100, ago 2017) con los primeros Tensor Cores: unidades de hardware diseñadas para multiplicaciones de matrices en precisión mixta (FP16 × FP16 = FP32). 640 Tensor Cores en el V100. Throughput de 120 TFLOPS en operaciones tensor vs 15 TFLOPS FP32 convencionales.

Las arquitecturas posteriores escalan el concepto: Turing (2018) añade RT Cores, Ampere (2020) multiplica los Tensor Cores, Hopper (2022) introduce FP8 y el Transformer Engine, Blackwell (2024) añade NVLink 5 y HBM3e.

**Conduce a:** NVIDIA Rubin (2026) · **Depende de:** CUDA (2006), Transformer (2017 en IA)

---

### 2017 · TPU v2 · cloud — Google

**Google** lanza TPU v2 como producto público en Google Cloud (may 2017). Primer TPU capaz de entrenar, no solo inferir. 180 TFLOPS en bfloat16. Los TPU pods combinan 64 chips con interconexión de alta velocidad propia.

bfloat16 es una innovación de Google: el mismo rango de exponentes que FP32 pero con menos bits de mantisa. Más estable para entrenamiento que FP16. La industria lo adopta masivamente después.

**Conduce a:** TPU v5p (2023) · **Depende de:** TPU v1 (2015), Tensor Cores (2017) en competencia

---

### 2019 · Cerebras WSE-1 — Cerebras Systems

**Cerebras Systems** (fundada por **Andrew Feldman** y **Gary Lauterbach**) anuncia el Wafer-Scale Engine (WSE-1): un chip del tamaño de una oblea de silicio completa (462 cm², 1.2 billones de transistores, 400.000 núcleos). La comparación: el mayor chip anterior de NVIDIA era ~815 mm².

El diseño sacrifica el yield (probabilidad de que un chip funcione sin defectos) a cambio de densidad de memoria on-chip: 18 GB de SRAM directamente en el chip. Para LLMs, el cuello de botella es mover pesos entre memoria y cómputo. WSE-1 lo minimiza.

**Conduce a:** Etched Sohu (2024) como variante del concepto · **Depende de:** CUDA (2006) como contexto de mercado

---

### 2023 · TPU v5p — Google

**Google** lanza TPU v5p (nov 2023): producción a escala para el entrenamiento de Gemini. Pods de 8.960 chips interconectados con ICI (Inter-Chip Interconnect) de alta velocidad. Cada chip: 459 TFLOPS bfloat16.

El TPU v5p es el sustrato del entrenamiento de Gemini Ultra. Google no necesita NVIDIA para entrenar su modelo más grande. La pila completa: datos → TPU → modelo → servicio.

**Conduce a:** TPU v6 Trillium (2024) · **Depende de:** TPU v2 (2017)

---

### 2024 · TPU v6 Trillium — Google

**Google** anuncia TPU v6 "Trillium" (may 2024): 4.7× el rendimiento por chip respecto a v5e (la variante eficiente del v5). Backbone de Gemini 1.5 y Gemini 2.

**Conduce a:** TPU v7 Ironwood (2025) · **Depende de:** TPU v5p (2023)

---

### 2024 · Hyperscaler Silicon — AWS, Microsoft, Meta

**AWS Trainium 2** · **Microsoft Maia** · **Meta MTIA** (Meta Training and Inference Accelerator). Los tres principales competidores de Google diseñan sus propios chips de IA para reducir dependencia de NVIDIA.

La lógica económica: a escala de hyperscaler, ahorrar 30% en cómputo representa miles de millones de dólares anuales. Diseñar el chip propio tarda 3-4 años y cuesta cientos de millones — pero la amortización se consigue en 1-2 años de operación.

**Conduce a:** TPU v8 (2027) · **Depende de:** OpenCL (2009) como precedente de independencia de NVIDIA, TPU v2 (2017) como modelo de referencia

---

### 2024 · Etched Sohu — Etched

**Etched** (startup californiana, fundada por **Gavin Uberti** y **Chris Zhu**) lanza Sohu: ASIC diseñado exclusivamente para ejecutar Transformers. Sin generalidad. Sin soporte para otras arquitecturas. La apuesta: si el Transformer es la arquitectura dominante indefinidamente, este chip es ~10× más eficiente que una GPU de propósito general para inferencia de LLMs.

El riesgo es simétrico: si emerge una arquitectura alternativa (SSMs, Mamba, etc.), el chip queda obsoleto. Etched apuesta a que no pasa.

**Conduce a:** diseño de chips especializados como tendencia · **Depende de:** Cerebras WSE-1 (2019) como precedente de especialización radical, Transformer (2017 en IA) como arquitectura objetivo

---

### 2025 · TPU v7 Ironwood — Google

**Google** anuncia TPU v7 "Ironwood" (2025): ~5× rendimiento respecto a v5p. Diseñado explícitamente para la era de extended thinking: los modelos de razonamiento como o1 y Gemini 2.5 consumen 10-100× más cómputo en inferencia que los modelos generativos anteriores.

**Conduce a:** TPU v8 (2027) · **Depende de:** TPU v6 Trillium (2024), o1 (2024 en IA) como driver de demanda

---

### 2026 · NVIDIA Rubin — NVIDIA

**NVIDIA** lanza Rubin (R100) a finales de 2026. HBM4, NVLink 6, sucesor de Blackwell (B100/B200, 2024). Continúa la cadencia anual que NVIDIA aceleró después de Hopper: Hopper (2022) → Blackwell (2024) → Rubin (2026).

NVLink 6 aumenta el ancho de banda inter-GPU, crítico para modelos que no caben en un solo chip.

**Conduce a:** Vera Rubin Ultra (2027), Apple M6 (2027 en PC) · **Depende de:** Tensor Cores (2017)

---

### 2027 · Vera Rubin Ultra (esp.) — NVIDIA

**NVIDIA** Vera Rubin Ultra: integra en un solo package la CPU Vera (arquitectura arm-compatible diseñada por NVIDIA) con la GPU Rubin Ultra. NVLink directo entre CPU y GPU elimina el cuello de botella del bus PCIe. La CPU Vera diseñada explícitamente como acompañante de la GPU — no como CPU de propósito general sino como orquestador de workloads de IA.

El concepto: una "AI factory" en un package. Ya no un servidor con CPU separada y GPU separada, sino una unidad integrada para entrenar y servir modelos.

**Conduce a:** convergencia CPU+GPU+NPU en un package · **Depende de:** NVIDIA Rubin (2026), [[08_PC#Apple M6]]

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1999 | Jensen Huang | Co-fundador y CEO NVIDIA, estrategia GPU | NVIDIA (Taiwan/California) |
| 2006 | Ian Buck | Lideró desarrollo de CUDA | NVIDIA / ex-Stanford |
| 2006 | John Owens | Primeros papers académicos con CUDA | UC Davis |
| 2015 | Jeff Dean | Impulsor del TPU v1 en Google | Google Brain |
| 2015 | Norm Jouppi | Arquitecto principal TPU v1 | Google |
| 2019 | Andrew Feldman | Co-fundador Cerebras | Cerebras Systems |
| 2019 | Gary Lauterbach | Co-fundador Cerebras | Cerebras Systems |
| 2024 | Gavin Uberti | Co-fundador Etched | Etched |
| 2024 | Chris Zhu | Co-fundador Etched | Etched |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:
- ↗ De [[11_IA#2017 · Transformer]] → impulsa el diseño de Tensor Cores y TPU v5/v7 específicos para Transformers
- ↗ De [[11_IA#2012 · AlexNet]] → primer caso de uso que justifica CUDA para IA
- ↗ De [[11_IA#2022 · ChatGPT]] → explosión de demanda que hace rentable el silicio especializado
- ↗ De [[07_SOFTWARE#1991 · Python]] → Python como frontend de CUDA; sin Python no hay ecosistema IA sobre GPU

Lo que esta columna **aporta** a otras columnas:
- ↘ De CUDA (2006) → habilita [[11_IA#2012 · AlexNet]] (entrenamiento viable en 2× GTX 580)
- ↘ De CUDA (2006) → habilita [[14_SUPERCOMPUTACION#2022 · Frontier]] (GPUs AMD como acelerador del primer exascale)
- ↘ De Tensor Cores (2017) → habilita [[08_PC#2026 · NVIDIA Rubin]] y cadena de chips avanzados
- ↘ De OpenCL (2009) → habilita [[14_SUPERCOMPUTACION#Aurora]] como arquitectura Intel alternativa
- ↘ De TPU v2 (2017) → habilita [[11_IA#2023 · Gemini Ultra]] (entrenamiento sobre hardware propio)
- ↘ De Rubin (2026) → habilita [[08_PC#Apple M6 + Vera]] como plataforma unificada

## Lectura siguiente

- Si te interesa cómo el hardware habilita la IA → [[11_IA]]
- Si te interesa la computación masivamente paralela en supercomputación → [[14_SUPERCOMPUTACION]]
- Si quieres ver el límite cuántico del paralelismo → [[13_CUANTICA]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
