---
columna: INTERNET
cat: NET
nodos_cubiertos: 8
periodo: 1969 → 2017
---

# INTERNET · De 4 nodos universitarios a la infraestructura del mundo

> Internet no fue diseñado como red global: fue diseñado para sobrevivir. Lo demás vino después.

## El arco

El 29 de octubre de 1969, dos ordenadores en UCLA y SRI Stanford intentan enviarse la palabra "LOGIN". El sistema cae tras dos caracteres: "LO". Así empieza internet. Cincuenta años después, la columna INTERNET cubre el camino desde ese primer paquete hasta el cómputo distribuido en el borde de la red, pasando por el protocolo TCP/IP, la web, el primer navegador gráfico, Google, AWS y Kubernetes. El patrón es constante: cada capa construye sobre la anterior y desplaza el poder hacia quien controla la nueva abstracción. La columna recibe de ELECTRÓNICA (el circuito integrado) y de SOFTWARE (Unix, Linux, Docker) sus habilitadores; alimenta DATA y PARADIGMAS.

## La cadena

### 1969 · ARPANET — Larry Roberts, Vinton Cerf, Bob Kahn

**Larry Roberts** lidera desde DARPA (Defense Advanced Research Projects Agency) la primera red de paquetes conmutados. El 29 de octubre de 1969, el primer mensaje viaja entre la UCLA (**Len Kleinrock**, equipo) y el SRI Stanford (**Doug Engelbart**, equipo): "LO". Pretendían enviar "LOGIN" pero el sistema IMP (Interface Message Processor) en el SRI cae tras dos caracteres.

La red crece: 4 nodos en 1969 (UCLA, SRI Stanford, UC Santa Barbara, Universidad de Utah). Los algoritmos de **Paul Baran** (RAND Corporation, 1964) sobre packet switching —redes que encaminan paquetes por múltiples rutas y resisten la destrucción de nodos— son el sustrato conceptual. Sin ARPA y sin la presión de la Guerra Fría (redes resistentes a ataque nuclear), el proyecto no habría recibido financiación.

**Conduce a:** [[#1983 · TCP/IP "flag day"]] · **Depende de:** [[02_ELE#1959 · Circuito integrado]] · [[04_SOFTWARE#1969 · Unix]] (paralelo: Unix y ARPANET nacen el mismo año, mismo ecosistema DARPA)

---

### 1983 · TCP/IP "flag day" — Vinton Cerf, Bob Kahn

**Vinton Cerf** y **Bob Kahn** especifican TCP/IP entre 1973 y 1978. El 1 de enero de 1983 es el "flag day": ARPANET completa la migración desde NCP (Network Control Protocol) a TCP/IP. Cualquier ordenador en cualquier red heterogénea puede ahora intercambiar paquetes con cualquier otro.

TCP/IP es el estándar abierto que permite la interoperación sin coordinación central. Cerf y Kahn reciben el Premio Turing en 2004. La arquitectura de capas (física, red, transporte, aplicación) que define el modelo OSI deriva de esta decisión de diseño.

**Conduce a:** [[#1989 · WWW · Berners-Lee]] · **Depende de:** [[01_LOG#1948 · Teoría de la Información]] (la teoría de Shannon sobre canales de comunicación es el sustrato matemático)

---

### 1989 · WWW · Berners-Lee — Tim Berners-Lee

**Tim Berners-Lee** (CERN, Ginebra) entrega su propuesta "Information Management: A Proposal" en marzo de 1989. Su jefe, **Mike Sendall**, escribe en el margen: "Vague but exciting". En 1990, Berners-Lee implementa el primer servidor HTTP (en una NeXT Cube) y el primer navegador/editor. El primer sitio web público es info.cern.ch, activo desde agosto de 1991.

HTTP, HTML y URL son los tres inventos en un mismo proyecto. El diseño es deliberadamente abierto: sin patentes, sin licencias. Berners-Lee rechaza enriquecerse con el invento. En 1994 funda el W3C (World Wide Web Consortium) para mantener los estándares abiertos. Sin esta decisión, la web podría haber sido un sistema propietario de una empresa.

**Conduce a:** [[#1993 · Mosaic browser]]

---

### 1993 · Mosaic browser — Marc Andreessen, Eric Bina

**Marc Andreessen** y **Eric Bina** (NCSA, Universidad de Illinois) lanzan Mosaic en enero de 1993: el primer navegador que muestra imágenes en línea con el texto (los anteriores mostraban el texto y descargaban las imágenes por separado). Gratuito. Disponible para Windows, Mac y Unix.

En 18 meses, el tráfico web en internet crece un 341.634%. Andreessen funda Netscape en 1994 con **Jim Clark**. La IPO de Netscape en agosto de 1995 (con la empresa sin beneficios) dispara el boom dotcom.

**Conduce a:** [[#1998 · Google · PageRank]] · **Depende de:** [[07_MICRO_PC#1984 · Macintosh]] (Mac populariza la interfaz visual que Mosaic adopta)

---

### 1998 · Google · PageRank — Larry Page, Sergey Brin

**Larry Page** y **Sergey Brin** lanzan Google en septiembre de 1998 desde un garaje en Menlo Park, California. El algoritmo **PageRank** (desarrollado como BackRub en 1996 en Stanford) mide la importancia de una página web como el eigenvector de la matriz de adyacencia del grafo de hiperenlaces: una página es importante si otras páginas importantes apuntan a ella.

La búsqueda web existía antes (AltaVista, Yahoo, Lycos) pero Google la resuelve con calidad sustancialmente mayor. En 2004, Google tiene el 75% del mercado de búsqueda. AdWords (2000) y AdSense (2003) convierten la búsqueda en el negocio de publicidad más eficiente de la historia.

**Conduce a:** [[#2006 · AWS · cloud pública]] · **Depende de:** [[08_ALG#1998 · PageRank]] (el algoritmo es el corazón)

---

### 2006 · AWS · cloud pública — Andy Jassy, Werner Vogels

**Amazon Web Services** lanza S3 (Simple Storage Service, marzo 2006) y EC2 (Elastic Compute Cloud, agosto 2006). **Andy Jassy** lidera AWS; **Werner Vogels** (CTO de Amazon) impulsa la arquitectura de servicios que hace posible el modelo.

La idea nace de la necesidad interna de Amazon: para los picos de Navidad, Amazon tenía que aprovisionar hardware suficiente para el máximo de demanda, que luego quedaba ocioso el resto del año. AWS ofrece ese exceso a terceros. El resultado accidental es la mayor transformación en la economía del software desde el PC: el hardware deja de ser barrera de entrada. Startups sin capital pueden escalar globalmente el mismo día de su lanzamiento.

**Conduce a:** [[#2014 · Kubernetes]] · **Depende de:** [[08_ALG#2004 · MapReduce (Google)]] (el patrón de procesamiento distribuido masivo habilita el modelo cloud)

---

### 2014 · Kubernetes — Joe Beda, Brendan Burns, Craig McLuckie

**Google** libera Kubernetes (k8s) en junio de 2014. **Joe Beda**, **Brendan Burns** y **Craig McLuckie** son los tres ingenieros que lo originan internamente. Se basa en Borg, el sistema de orquestación interno de Google que lleva más de una década en producción.

Kubernetes orquesta contenedores Docker (2013): decide en qué máquina ejecutar cada contenedor, gestiona el escalado automático, reemplaza los contenedores que fallan y expone los servicios con load balancing. En 2016 se dona a la Cloud Native Computing Foundation (CNCF). En 2024 es el estándar industrial indiscutible para despliegue cloud-native.

**Conduce a:** [[#2017 · Edge computing]] · **Depende de:** [[04_SOFTWARE#2013 · Docker]] (Docker es el formato que Kubernetes orquesta) · [[06_PARADIGMAS#2014 · Microservicios]] (la demanda de orquestación viene de los microservicios)

---

### 2017 · Edge computing — Cloudflare, Vercel, AWS

**Cloudflare Workers** (septiembre 2017): código JavaScript ejecutándose en los ~300 PoP (puntos de presencia) de Cloudflare, a menos de 50 ms de cualquier usuario del mundo. **Vercel Edge Functions** (2021). **AWS Lambda@Edge** (2016, producción desde 2017).

El modelo: en lugar de enviar la petición de un usuario en Tokyo a un servidor en us-east-1 (Virginia), la lógica corre en el PoP de Tokyo. La latencia pasa de 150 ms a 5 ms para funciones simples. 5G (despliegue masivo 2019-2021) acelera la adopción. **Matthew Prince** y **Michelle Zatlyn** (Cloudflare) y **Guillermo Rauch** (Vercel) son las caras públicas de este movimiento.

**Depende de:** [[08_ALG#2008 · Nakamoto consensus]] (blockchain como fenómeno paralelo en esta capa, Web3)

---

## Personas clave

| Año | Persona | Aportación | País/Institución |
|---|---|---|---|
| 1964 | Paul Baran | Algoritmos de packet switching | RAND Corporation, EE.UU. |
| 1969 | Larry Roberts | Dirección de ARPANET desde DARPA | DARPA, EE.UU. |
| 1969 | Len Kleinrock | Teoría de colas para redes, nodo UCLA | UCLA, EE.UU. |
| 1973 | Vinton Cerf | Codiseñador de TCP/IP | Stanford / DARPA, EE.UU. |
| 1973 | Bob Kahn | Codiseñador de TCP/IP | DARPA, EE.UU. |
| 1989 | Tim Berners-Lee | Inventor de la WWW, HTTP, HTML, URL | CERN, Suiza |
| 1993 | Marc Andreessen | Mosaic, cofundador Netscape | NCSA / Netscape, EE.UU. |
| 1993 | Eric Bina | Codesarrollador de Mosaic | NCSA, EE.UU. |
| 1994 | Jim Clark | Cofundador de Netscape | Netscape, EE.UU. |
| 1996 | Larry Page | PageRank, cofundador Google | Stanford / Google, EE.UU. |
| 1998 | Sergey Brin | PageRank, cofundador Google | Stanford / Google, EE.UU. |
| 2003 | Andy Jassy | Creador y CEO de AWS | Amazon, EE.UU. |
| 2003 | Werner Vogels | CTO Amazon, arquitectura de servicios | Amazon, EE.UU. |
| 2014 | Joe Beda | Cofundador de Kubernetes | Google, EE.UU. |
| 2014 | Brendan Burns | Cofundador de Kubernetes | Google, EE.UU. |
| 2014 | Craig McLuckie | Cofundador de Kubernetes | Google, EE.UU. |
| 2017 | Matthew Prince | CEO Cloudflare Workers | Cloudflare, EE.UU. |
| 2017 | Michelle Zatlyn | Cofundadora Cloudflare | Cloudflare, EE.UU. |
| 2017 | Guillermo Rauch | CEO Vercel, Edge Functions | Vercel, EE.UU. |

## Cross-column dependencies

Lo que esta columna **recibe** de otras columnas:

- ↗ De [[02_ELE#1959 · Circuito integrado]] → habilita ARPANET (el IC hace posibles los IMP routers)
- ↗ De [[04_SOFTWARE#1969 · Unix]] → paralelo con ARPANET (mismo ecosistema; Unix se convierte en el SO de los servidores de internet)
- ↗ De [[07_MICRO_PC#1984 · Macintosh]] → habilita Mosaic (la GUI visual que Mosaic toma como referencia)
- ↗ De [[04_SOFTWARE#2013 · Docker]] → habilita Kubernetes (Docker es el formato de paquete que Kubernetes orquesta)
- ↗ De [[06_PARADIGMAS#2014 · Microservicios]] → habilita Kubernetes (la demanda de orquestación nace del modelo de microservicios)
- ↗ De [[08_ALG#2004 · MapReduce]] → habilita AWS (el patrón de procesamiento distribuido masivo)
- ↗ De [[01_LOG#1948 · Teoría de la Información]] → habilita TCP/IP (los canales de Shannon como sustrato matemático de la comunicación)
- ↗ De [[08_ALG#2008 · Nakamoto consensus]] → Edge computing (blockchain como fenómeno paralelo en la capa de borde)

Lo que esta columna **aporta** a otras columnas:

- ↘ AWS → habilita [[10_DATA#2007 · NoSQL · BigTable · Dynamo]] (Amazon Dynamo es el origen del movimiento NoSQL)
- ↘ Kubernetes → habilita [[06_PARADIGMAS#2010 · Go + Rust]] (K8s en Go consagra el lenguaje)
- ↘ Google → habilita [[10_DATA#2007 · NoSQL]] y [[08_ALG#2004 · MapReduce]] (Google publica BigTable y MapReduce)

## Lectura siguiente

- Si te interesa cómo internet gestiona y almacena sus datos → [[10_DATA]]
- Si quieres ver los algoritmos que hacen funcionar la web (PageRank, MapReduce) → [[08_ALG]]
- Si te interesa la capa de software que hace posible el cloud (Docker, Linux) → [[04_SOFTWARE]]

## Fuente

Datos extraídos del grafo interactivo en https://zoopa.es/files/historia-computacion-hitos-20260423.html
