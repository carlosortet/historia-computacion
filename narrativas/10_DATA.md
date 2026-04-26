---
columna: DATA
cat: DATA
nodos_cubiertos: 10
periodo: 1970 → 2027
---

# DATA · Del modelo relacional a la memoria de los agentes

> Las bases de datos no almacenan datos: almacenan la forma en que los humanos modelan el mundo. Cada nuevo modelo de datos refleja un cambio en qué tipo de preguntas queremos hacer.

## El arco

En 1970, un matemático de IBM publica 13 páginas que fundan la teoría de las bases de datos relacionales. En 2027, se espera la convergencia de múltiples paradigmas de almacenamiento —relacional, vectorial, episódico, grafos— en plataformas diseñadas para que los agentes IA mantengan memoria persistente entre sesiones. Entre ambos extremos, la columna DATA narra cuatro transiciones: de la teoría al producto comercial (Codd a Oracle), del monopolio relacional a la escala web (SQL a NoSQL), de la búsqueda exacta a la similitud semántica (RDBMS a vector DBs), y del almacenamiento como commodity al dato como contexto activo de la IA. La columna recibe de INTERNET y de IA sus presiones transformadoras.

## La cadena

### 1970 · Modelo relacional — E.F. Codd

**Edgar F. Codd** (IBM Research, San José) publica "A Relational Model of Data for Large Shared Data Banks" en junio de 1970 en *Communications of the ACM*. 13 páginas. La propuesta: representar datos como tuplas en relaciones (tablas), operar sobre ellas con álgebra relacional (selección, proyección, producto, unión, diferencia) y separar la estructura lógica de los datos de su implementación física.

En 1970, los datos se almacenaban con modelos jerárquicos o de red (IMS de IBM, CODASYL) donde las relaciones entre registros eran punteros físicos. Cambiar la estructura física de los datos requería reescribir las aplicaciones. Codd propone una capa de abstracción: el modelo lógico es independiente del almacenamiento.

IBM tarda 8 años en implementar la idea. Irónicamente, Oracle la implementa primero.

**Conduce a:** [[#1974 · IBM System R]] · **Depende de:** [[04_SOFTWARE#1969 · Unix]] (el ecosistema Unix/C es el entorno de desarrollo de los primeros RDBMS)

---

### 1974 · IBM System R — Donald Chamberlin, Raymond Boyce

IBM Research (San José) desarrolla System R entre 1974 y 1979. **Donald Chamberlin** y **Raymond Boyce** diseñan SEQUEL (Structured English Query Language) para acceder a los datos del modelo de Codd; SEQUEL se renombra SQL para evitar un conflicto de marca.

System R demuestra que el modelo relacional de Codd es implementable con rendimiento aceptable. Dos contribuciones clave: el optimizador de consultas (decide automáticamente cómo ejecutar una consulta) y el protocolo de control de concurrencia. Ambos siguen siendo el núcleo de cualquier RDBMS moderno.

**Conduce a:** [[#1979 · Oracle V2]]

---

### 1979 · Oracle V2 — Larry Ellison

**Larry Ellison** lee el paper de Codd en 1977 e invierte 2.000 USD en fundar SDL (Software Development Labs) con **Bob Miner** y **Ed Oates**. Oracle V2 se lanza en 1979 (V1 nunca salió de pruebas) para el minicomputador PDP-11. Es el primer RDBMS comercial funcional.

Oracle se adelanta a IBM en comercializar la idea que IBM había inventado. Ellison convence a la CIA como primer cliente. El nombre "Oracle" viene del proyecto CIA para el que IBM había contratado a Ellison antes de su empresa. Oracle domina el mercado de bases de datos empresariales durante 30 años.

**Conduce a:** [[#1996 · PostgreSQL · MySQL]]

---

### 1990 · BLAST · bioinformática — Stephen Altschul

**Stephen Altschul**, **Warren Gish**, **Webb Miller**, **Eugene Myers** y **David Lipman** (NCBI, NIH) publican BLAST (Basic Local Alignment Search Tool) en 1990: búsqueda heurística de similitud entre secuencias biológicas (DNA, RNA, proteínas) a velocidad práctica. Resuelve un problema de búsqueda por similitud en espacios de alta dimensión biológica.

BLAST es el algoritmo más citado de la biología computacional. Es el sustrato técnico del Human Genome Project (1990-2003). Conceptualmente, BLAST es el precursor de la búsqueda vectorial: encontrar el elemento más similar en un espacio de alta dimensión, no el elemento exacto.

**Conduce a:** [[#2017 · FAISS (Meta)]] (puente conceptual) · [[03_IA#2018 · AlphaFold 1]] (la bioinformática habilita la IA biológica)

---

### 1996 · PostgreSQL · MySQL — Michael Stonebraker / Monty Widenius

**MySQL 1.0** (mayo 1995, **Michael "Monty" Widenius** y **David Axmark**, Suecia). **PostgreSQL**: sucesor del proyecto Postgres de **Michael Stonebraker** (UC Berkeley, 1986); renombrado en 1996; PostgreSQL 6.0 lanzado en enero de 1997.

Ambos democratizan el RDBMS a coste cero. Hasta entonces, Oracle DB costaba decenas de miles de dólares por servidor. MySQL y PostgreSQL bajan la barrera a cero. MySQL se convierte en el estándar de la web 2.0 (LAMP stack: Linux + Apache + MySQL + PHP). PostgreSQL gana reputación de corrección y extensibilidad.

**Conduce a:** [[#2007 · NoSQL · BigTable · Dynamo]] · [[#2024 · pgvector + Iceberg]] (PostgreSQL como sustrato de la convergencia)

---

### 2007 · NoSQL · BigTable · Dynamo — Jeff Dean, Werner Vogels

**Google** publica el paper de BigTable en 2006 (**Fay Chang**, **Jeffrey Dean** et al.): almacenamiento distribuido orientado a columnas para datos esparsos a escala web. **Amazon** publica Dynamo en 2007 (**Giuseppe DeCandia**, **Werner Vogels** et al.): almacenamiento clave-valor distribuido para alta disponibilidad con consistencia eventual.

El problema: MySQL no escala horizontalmente. Cuando tienes 1.000 servidores y petabytes de datos, las garantías ACID del modelo relacional son demasiado caras. El movimiento NoSQL produce CouchDB (2005), Cassandra (Facebook, 2008, open source 2009), MongoDB (2009). El patrón MapReduce de Google (2004) habilita el procesamiento masivo sobre estos almacenes.

**Conduce a:** [[#2019 · Vector DBs · Pinecone+]] · **Depende de:** [[09_INTERNET#2006 · AWS · cloud pública]] (Amazon Dynamo nace de las necesidades de AWS) · [[08_ALG#2004 · MapReduce]] (el procesamiento distribuido masivo habilita el modelo NoSQL)

---

### 2017 · FAISS (Meta) — Hervé Jégou, Matthijs Douze

**Meta** (entonces Facebook) abre **FAISS** (Facebook AI Similarity Search) en 2017. **Hervé Jégou** y **Matthijs Douze** lideran el desarrollo. FAISS resuelve un problema específico: dado un vector de 1.024 dimensiones (un embedding de imagen o texto), encontrar los K vectores más similares entre mil millones de vectores en milisegundos.

El algoritmo usa quantización de productos e índices HNSW (Hierarchical Navigable Small World). FAISS hace prácticas las búsquedas de similitud a escala. Sin FAISS, las bases de datos vectoriales y el RAG (Retrieval-Augmented Generation) no existirían en su forma actual.

**Conduce a:** [[#2019 · Vector DBs · Pinecone+]] · **Depende de:** [[03_IA#2017 · Transformer]] (los embeddings del Transformer son lo que se indexa)

---

### 2019 · Vector DBs · Pinecone+ — múltiples fundadores

**Weaviate** (open source, **Bob van Luijt**, Ámsterdam, 2019) y **Milvus** (open source, **Charles Xie**, Zilliz, China, 2019) son los primeros. **Pinecone** fundada en 2019 por **Edo Liberty** (ex-Yahoo Research); lanzamiento público en enero 2021.

El producto: una base de datos cuya primitiva de búsqueda no es "dame el registro donde id=5" sino "dame los 10 registros más similares a este vector". El caso de uso que las lanza a la fama es RAG (Retrieval-Augmented Generation) con LLMs: el embedding de la pregunta del usuario se compara con el embedding de los documentos almacenados para recuperar contexto relevante.

**Conduce a:** [[#2024 · pgvector + Iceberg]]

---

### 2024 · pgvector + Iceberg — Andrew Kane / Apache community

**pgvector** (creado por **Andrew Kane**, primera versión en abril 2021) se vuelve estándar de facto en PostgreSQL en 2023-2024: un índice vectorial dentro del RDBMS más maduro. Las bases vectoriales aisladas (Pinecone, Weaviate como servicio independiente) pierden parte de su razón de ser.

**Apache Iceberg** (open source, creado por **Ryan Blue** en Netflix, 2018) gana la guerra de open table formats en 2023-2024: Snowflake, Databricks y AWS adoptan Iceberg como formato interoperable para tablas analíticas. La convergencia OLAP/OLTP/vector en un solo motor empieza a ser real.

**Conduce a:** [[#2024 · MCP (Anthropic)]] · [[#2027 · Agentic memory (esp.)]]

---

### 2024 · MCP (Anthropic) — equipo Anthropic

**Anthropic** libera el **Model Context Protocol** (MCP) en noviembre de 2024: un estándar abierto de comunicación entre agentes IA y fuentes de datos arbitrarias (bases de datos, APIs, sistemas de archivos, servicios web). En 2025, OpenAI, Google y Microsoft lo adoptan; decenas de bases de datos publican conectores MCP.

MCP es el "USB-C para IA": antes de MCP, cada LLM tenía su propio método propietario de acceder a herramientas y datos. Con MCP, cualquier fuente de datos que implemente el protocolo es accesible desde cualquier agente.

**Conduce a:** [[#2027 · Agentic memory (esp.)]] · **Depende de:** [[03_IA#2022 · ChatGPT]] (ChatGPT genera la demanda masiva que hace necesario el protocolo) · [[03_IA#2026 · Claude Opus 4.7 · 1M]] (Opus 4.7 como caso de uso avanzado de MCP)

---

### 2027 · Agentic memory (esp.) — convergencia esperada

Plataformas diseñadas para agentes IA con memoria persistente: **Mem0** (vectorial + episódica), **Zep** (memoria de larga duración para agentes), próxima generación de Snowflake, Databricks y MongoDB con índices auto-gestionados.

La convergencia esperada: vector + grafo + memoria episódica + SQL en un motor unificado que se auto-indexa según los patrones de acceso del agente. El agente no solo ejecuta tareas: recuerda, actualiza su conocimiento y adapta su comportamiento basándose en experiencias pasadas.

**Depende de:** [[#2024 · pgvector + Iceberg]] · [[#2024 · MCP (Anthropic)]] · [[02_ELE#2019 · Project Silica · cristal 5D]] (almacenamiento a largo plazo para la capa de archivo)

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1970 | E.F. Codd | Modelo relacional de datos | IBM Research, EE.UU. |
| 1974 | Donald Chamberlin | Codiseñador de SQL (SEQUEL) | IBM Research, EE.UU. |
| 1974 | Raymond Boyce | Codiseñador de SQL (SEQUEL) | IBM Research, EE.UU. |
| 1979 | Larry Ellison | Fundador de Oracle, primer RDBMS comercial | Oracle, EE.UU. |
| 1979 | Bob Miner | Cofundador de Oracle | Oracle, EE.UU. |
| 1979 | Ed Oates | Cofundador de Oracle | Oracle, EE.UU. |
| 1990 | Stephen Altschul | Codiseñador de BLAST | NCBI/NIH, EE.UU. |
| 1990 | Eugene Myers | Codiseñador de BLAST | NCBI/NIH, EE.UU. |
| 1990 | David Lipman | Codiseñador de BLAST | NCBI/NIH, EE.UU. |
| 1986 | Michael Stonebraker | Creador de Postgres (luego PostgreSQL) | UC Berkeley, EE.UU. |
| 1995 | Michael "Monty" Widenius | Creador de MySQL | MySQL AB, Suecia |
| 1995 | David Axmark | Cofundador MySQL | MySQL AB, Suecia |
| 2006 | Fay Chang | Codiseñadora de BigTable (Google) | Google, EE.UU. |
| 2006 | Jeffrey Dean | Codiseñador de BigTable (y MapReduce) | Google, EE.UU. |
| 2007 | Giuseppe DeCandia | Codiseñador de Amazon Dynamo | Amazon, EE.UU. |
| 2007 | Werner Vogels | CTO Amazon, impulsor de Dynamo | Amazon, EE.UU. |
| 2017 | Hervé Jégou | Codiseñador de FAISS | Meta (Facebook AI), Francia |
| 2017 | Matthijs Douze | Codiseñador de FAISS | Meta (Facebook AI), Francia |
| 2019 | Bob van Luijt | Fundador de Weaviate | Weaviate, Países Bajos |
| 2019 | Charles Xie | Fundador de Milvus/Zilliz | Zilliz, China |
| 2021 | Edo Liberty | Fundador de Pinecone | Pinecone, EE.UU. |
| 2021 | Andrew Kane | Creador de pgvector | Independiente, EE.UU. |
| 2018 | Ryan Blue | Creador de Apache Iceberg (en Netflix) | Netflix / Apache, EE.UU. |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[04_SOFTWARE#1969 · Unix]] → habilita el modelo relacional (el ecosistema Unix/C es el entorno de desarrollo de los primeros RDBMS)
- ↗ De [[09_INTERNET#2006 · AWS · cloud pública]] → habilita NoSQL (Amazon Dynamo nace de las necesidades de AWS; BigTable de Google)
- ↗ De [[08_ALG#2004 · MapReduce]] → habilita NoSQL (el procesamiento distribuido masivo da sentido al modelo NoSQL)
- ↗ De [[03_IA#2017 · Transformer]] → habilita FAISS y Vector DBs (los embeddings del Transformer son lo que se indexa en vectorial)
- ↗ De [[03_IA#2022 · ChatGPT]] → habilita MCP (ChatGPT genera la demanda masiva que hace necesario el protocolo estándar)
- ↗ De [[03_IA#2026 · Claude Opus 4.7 · 1M]] → habilita Agentic memory (Opus 4.7 es el caso de uso avanzado que presiona la arquitectura de memoria)
- ↗ De [[02_ELE#2019 · Project Silica · cristal 5D]] → habilita Agentic memory (almacenamiento de largo plazo para la capa de archivo)

Lo que esta columna **aporta** a otras columnas:

- ↘ BLAST → habilita [[03_IA#2018 · AlphaFold 1]] (la bioinformática computacional habilita la IA biológica)
- ↘ Vector DBs + MCP → habilita la era de agentes con memoria ([[08_ROBOT#2027 · Robot FM cross-embodiment]])
- ↘ NoSQL → relacionado con [[08_ALG#2004 · MapReduce]] (el patrón MapReduce y los almacenes NoSQL se co-habilitan)

## Lectura siguiente

- Si te interesa cómo los agentes IA consumen estos datos → [[03_IA]]
- Si quieres ver la red sobre la que viajan los datos → [[09_INTERNET]]
- Si te interesa la bioinformática y la ciencia computacional → [[03_IA]] (vía AlphaFold)

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
