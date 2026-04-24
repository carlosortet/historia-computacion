---
titulo: Historia de la Computación — Hitos, Descubrimientos y Relaciones
fecha: 2026-04-23
autor: Carlos Ortet
tipo: knowledge / línea temporal
estado: verificado y enriquecido
---

# Historia de la Computación

> Línea temporal estructurada de los hitos que conectan la lógica formal del siglo XIX con la era actual de IA generativa, computación cuántica y exascala. Cada bloque incluye el aporte central, la fecha verificada y su **relación causal** con bloques previos o posteriores.

---

## 1. LÓGICA FORMAL — La base matemática

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1847–1854** | George Boole | *Mathematical Analysis of Logic* (1847) y *Laws of Thought* (1854): álgebra booleana | Habilita el siguiente salto → Shannon |
| **1879** | Gottlob Frege | *Begriffsschrift*: lógica de predicados y cuantificadores | Influye en Russell, Hilbert, Turing |
| **1928–1931** | Hilbert · Gödel | *Entscheidungsproblem* (Hilbert) y teoremas de incompletitud (Gödel) | Plantea el reto que Turing y Church responden en 1936 |
| **1937** | Claude Shannon | *A Symbolic Analysis of Relay and Switching Circuits*: aplica Boole a circuitos eléctricos | Fusiona lógica + electrónica → puente directo a la era electrónica |

> **Cadena causal:** Boole → Frege → crisis de fundamentos → Turing/Church (1936) → Shannon traduce todo a circuitos.

---

## 2. ARQUITECTURA — El concepto de "ordenador"

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1837** | Charles Babbage | Máquina Analítica: memoria, control, cálculo, programa | Primera arquitectura conceptual general |
| **1843** | Ada Lovelace | Notas sobre la Máquina Analítica: primer algoritmo destinado a una máquina | Inaugura la distinción **hardware/software** |
| **1936** | Alan Turing | *On Computable Numbers*: máquina universal | Base teórica de todo ordenador de propósito general |
| **1945** | John von Neumann | *First Draft of a Report on the EDVAC*: arquitectura de programa almacenado | Modelo dominante hasta hoy (CPU + memoria + bus) |
| **1949** | Maurice Wilkes | EDSAC en Cambridge: primer ordenador von Neumann plenamente operativo | Convierte la teoría de von Neumann en realidad práctica |

> **Cadena causal:** Babbage/Lovelace (concepto) → Turing (teoría) → von Neumann (modelo de implementación) → Wilkes (realización).

---

## 3. ELECTRÓNICA — De válvulas a chips

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1941** | Konrad Zuse | Z3: primer ordenador programable y automático funcional (relés electromecánicos) | Demuestra la viabilidad práctica antes que los aliados |
| **1943–1944** | Tommy Flowers | Colossus (Bletchley Park): computación electrónica con válvulas para criptoanálisis | Primer ordenador electrónico programable |
| **1945–1946** | Eckert y Mauchly | ENIAC: ordenador electrónico de propósito general | Consolida el paradigma electrónico |
| **1947** | Bardeen, Brattain, Shockley (Bell Labs) | Transistor de unión bipolar | Permite miniaturización: sustituye válvulas |
| **1958–1959** | Jack Kilby (TI) y Robert Noyce (Fairchild) | Circuito integrado | Hace posible concentrar miles → millones de transistores en un chip |

> **Cadena causal:** Shannon habilita la lógica electrónica → Zuse/Colossus/ENIAC la materializan → transistor + IC inician la ley de Moore (formulada por Gordon Moore en **1965**).

---

## 4. SOFTWARE E INGENIERÍA DEL SOFTWARE

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1952** | Grace Hopper | Compilador A-0: primer compilador funcional | Acerca la programación al lenguaje humano |
| **1957** | John Backus (IBM) | FORTRAN: primer lenguaje de alto nivel ampliamente adoptado | Despega el software científico |
| **1958–1960** | McCarthy · Naur et al. | LISP (1958) y ALGOL 60 (1960) | LISP → IA y lenguajes funcionales; ALGOL → toda la familia C/Pascal/Java |
| **1968** | Edsger Dijkstra | *Go To Statement Considered Harmful* + programación estructurada | Funda la ingeniería del software moderna |
| **1969–1973** | Ken Thompson y Dennis Ritchie (Bell Labs) | Unix (1969) y C (1972–73) | Base de macOS, Linux, Android, iOS, servidores… |

> **Cadena causal:** Hopper abre los compiladores → FORTRAN/ALGOL/LISP definen los grandes paradigmas → Dijkstra disciplina la práctica → Unix+C se convierten en sustrato universal.

---

## 5. PROGRAMACIÓN ORIENTADA A OBJETOS

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1967** | Ole-Johan Dahl y Kristen Nygaard (Oslo) | **Simula 67**: clases, objetos, herencia | Primer hito real de la POO |
| **1972–1980** | Alan Kay, Dan Ingalls, Adele Goldberg (Xerox PARC) | **Smalltalk** (Smalltalk-72 → Smalltalk-80): objetos, clases, paso de mensajes, GUI | Inspira Mac, Objective-C, Java… |
| **1985** | Bjarne Stroustrup (Bell Labs) | **C++**: POO sobre C | Lleva objetos al software de sistemas y alto rendimiento |
| **1991–1995** | Guido van Rossum · James Gosling | **Python** (1991) y **Java** (1995) | Java masifica POO en empresa; Python la combina con scripting y se convierte hoy en lengua franca de IA |

> **Cadena causal:** Simula (concepto puro) → Smalltalk (manifestación radical + GUI) → C++/Java (adopción industrial) → Python (puente a la era de la IA).

---

## 6. MICROPROCESADOR Y PC

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1971** | Federico Faggin, Ted Hoff, Stanley Mazor, Masatoshi Shima (Intel) | **Intel 4004**: primer microprocesador comercial (4 bits) | Inicia la era del "ordenador en un chip" |
| **1972** | Faggin et al. (Intel) | **Intel 8008** (8 bits) | Antecesor directo de la familia x86 |
| **1974** | Equipo Intel | **Intel 8080** | Hace viables Altair 8800 y los primeros microordenadores |
| **1975** | MITS Altair 8800 + Microsoft (Gates/Allen) | Primer microordenador de éxito + Altair BASIC | Nace la industria del software para PC |
| **1976–1977** | Steve Wozniak (con Steve Jobs) | **Apple I** (1976) y **Apple II** (1977) | Acerca el ordenador personal al gran público |
| **1981** | IBM (con MS-DOS de Microsoft) | **IBM PC** (modelo 5150) | Estandariza la arquitectura PC; modelo abierto = explosión de clones |
| **1984** | Apple Macintosh | Primer PC de éxito masivo con GUI (heredada de Xerox PARC) | Lleva Smalltalk/PARC al mercado |

> **Cadena causal:** Circuito integrado → 4004/8080 → Altair → Apple/IBM PC → Mac populariza la GUI nacida en PARC.

---

## 7. INTELIGENCIA ARTIFICIAL

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1943** | McCulloch y Pitts | Modelo matemático de neurona artificial | Semilla de las redes neuronales |
| **1950** | Alan Turing | *Computing Machinery and Intelligence*: test de Turing | Marco filosófico de referencia |
| **1956** | McCarthy, Minsky, Shannon, Rochester | **Conferencia de Dartmouth**: nace formalmente el campo de la IA | Acuña el término "Artificial Intelligence" |
| **1958** | Frank Rosenblatt | **Perceptrón** | Primera red neuronal entrenable; primera ola conexionista |
| **1969** | Minsky y Papert | *Perceptrons*: limita expectativas → primer **invierno de la IA** | Frena el conexionismo durante ~15 años |
| **1986** | Rumelhart, Hinton, Williams | Populariza **backpropagation** | Resucita las redes neuronales |
| **1997** | IBM **Deep Blue** vs. Kasparov | Primera derrota de un campeón mundial de ajedrez | Hito simbólico de IA simbólica/búsqueda |
| **2012** | Krizhevsky, Sutskever, Hinton | **AlexNet** gana ImageNet con CNNs en GPU | Detona la revolución del deep learning moderno |
| **2016** | DeepMind | **AlphaGo** vence a Lee Sedol | Demuestra el poder de RL + redes profundas |
| **2017** | Vaswani et al. (Google) | *Attention Is All You Need*: **Transformer** | Base de todos los LLM actuales (GPT, Claude, Gemini…) |
| **2018** | Hinton, LeCun, Bengio | **Premio Turing** por deep learning | Reconocimiento institucional |
| **2022–2026** | OpenAI · Anthropic · Google · Meta | ChatGPT (2022), GPT-4, Claude 3/4, Gemini, Llama | Era de los **LLM** y la IA generativa |

> **Cadena causal:** Dartmouth (campo) → perceptrón → invierno → backprop → **GPU + AlexNet** (2012, aquí se enchufan las GPUs) → Transformer (2017) → LLMs.

---

## 8. GPU Y COMPUTACIÓN ACELERADA

> **Por qué pertenecen al núcleo de la historia:** las GPU son el puente físico entre la informática clásica y la explosión de IA. Sin paralelismo masivo, ni AlexNet (2012) ni los LLM actuales serían viables económicamente.

| Año | Hito | Aportación | Relación clave |
|---|---|---|---|
| **1999** | NVIDIA **GeForce 256** | Primera GPU comercial con T&L acelerado | Despega el cómputo gráfico programable |
| **2001** | NVIDIA GeForce 3 / shaders programables | Empieza a verse la GPU como procesador genérico | Base para GPGPU |
| **2006** | NVIDIA **CUDA** | Convierte la GPU en plataforma de cómputo general (C/C++) | Habilita HPC + simulación + IA en GPU |
| **2012** | AlexNet entrenado en 2× GTX 580 | Primera "killer app" de IA sobre GPU | Confirma el matrimonio GPU↔Deep Learning |
| **2017–2026** | NVIDIA Volta → Hopper → Blackwell | Tensor Cores, NVLink, HBM3 | Hardware específico para entrenar e inferir LLMs |

### VRAM — subcomponente decisivo, no bloque fundacional

- **Función:** memoria de trabajo de alta velocidad (GDDR/HBM) cercana a la GPU; almacena texturas, datos y **tensores** sin depender continuamente de la RAM del sistema.
- **Por qué importa:** su **tamaño** decide qué modelos caben (cuello de botella en inferencia local de LLMs); su **ancho de banda** decide cuán rápido se alimentan los núcleos.
- **Por qué no está al nivel de Boole/Turing/von Neumann:** es una optimización de la arquitectura, no un cambio de paradigma.

---

## 9. COMPUTACIÓN CUÁNTICA

| Año | Protagonista | Aportación | Relación clave |
|---|---|---|---|
| **1980** | Paul Benioff | Modelo cuántico de máquina de Turing | Primer ordenador cuántico teórico |
| **1981–1982** | Richard Feynman | Propone simular física con ordenadores cuánticos | Motivación fundacional |
| **1985** | David Deutsch | **Computador cuántico universal** | Análogo cuántico de la máquina universal de Turing |
| **1994** | Peter Shor | **Algoritmo de Shor** (factorización) | Demuestra ventaja cuántica práctica → reto a RSA |
| **1996** | Lov Grover | Algoritmo de búsqueda en √N | Segundo algoritmo cuántico paradigmático |
| **1998** | Chuang, Gershenfeld, Kubinec | Primer ordenador cuántico de **2 qubits** (NMR) | Demostración experimental |
| **2019** | Google **Sycamore** (53 qubits) | Anuncia "supremacía cuántica" (disputada por IBM) | Primer hito mediático |
| **2024** | Google **Willow** (105 qubits) | Avance en **corrección de errores** | Primer signo serio hacia computación tolerante a fallos |
| **2025** | **IBM Quantum** | Roadmap detallado hacia escala tolerante a fallos | Industrialización del campo |

> **Cadena causal:** Feynman/Deutsch (idea) → Shor/Grover (algoritmos que justifican el esfuerzo) → primeras demos físicas → escalado actual de qubits + corrección de errores.

---

## 10. SUPERCOMPUTACIÓN

| Año | Sistema | Hito | Relación clave |
|---|---|---|---|
| **1976** | **Cray-1** | Referencia fundacional de la supercomputación vectorial | Define el género |
| **1997** | **ASCI Red** (Sandia / Intel) | Primer superordenador en superar **1 teraflop** | Prueba que clusters x86 pueden liderar |
| **2008** | **Roadrunner** (LANL / IBM) | Primer **petaflop** (Cell + Opteron) | Primera arquitectura híbrida ganadora |
| **2022** | **Frontier** (ORNL / HPE+AMD) | Primer **exascale** oficialmente confirmado | Inicia la era exascale (con GPUs) |
| **2024** | **Aurora** (Argonne / Intel) | Segundo exascale; arquitectura GPU Intel | Diversifica proveedores |
| **2024–2025** | **El Capitan** (LLNL / HPE+AMD) | **Nº 1 del TOP500**; >1.7 exaflops sostenidos | Consolida la era exascale |
| **2025** | **JUPITER Booster** (Jülich, EuroHPC) | Primer **exascale europeo**; 4º del TOP500 | Soberanía tecnológica europea |

> **Patrón:** desde Roadrunner (2008) la supercomputación es **híbrida CPU+acelerador**, y desde Frontier (2022) el acelerador dominante es la **GPU** → cierre del círculo con la sección 8.

---

## Mapa de relaciones transversales

```
LÓGICA  ──►  ARQUITECTURA  ──►  ELECTRÓNICA  ──►  MICRO+PC
(Boole,        (Turing,            (Zuse,             (Intel 4004,
Shannon)       von Neumann)        ENIAC,             Apple, IBM PC)
                                   transistor, IC)
                                          │
                                          ▼
                                    SOFTWARE  ──►  POO  ──►  IA clásica
                                   (Hopper,        (Simula,    (Dartmouth,
                                   FORTRAN, C)     Smalltalk,  perceptrón,
                                                   C++, Java,  backprop)
                                                   Python)         │
                                                                   ▼
                                              GPU + CUDA (2006)  ──►  Deep Learning (AlexNet 2012)
                                                                              │
                                                                              ▼
                                                                  Transformer (2017) ──► LLMs (2022→)
                                                                              │
                                                                              ▼
                                                              Supercomputación exascale (2022→)

           [línea paralela]   CUÁNTICA  (Feynman/Deutsch → Shor → Willow/IBM)
```

---

## Verificaciones y matices aplicados a la lista original

1. **Boole 1847–1854** ✓ — *Mathematical Analysis of Logic* (1847) + *Laws of Thought* (1854).
2. **Shannon 1937** ✓ — tesis de máster en MIT.
3. **Babbage 1837** ✓ — diseño de la Máquina Analítica (nunca terminada en vida).
4. **Lovelace 1843** ✓ — notas a la traducción del artículo de Menabrea.
5. **von Neumann 1945** ✓ — *First Draft of a Report on the EDVAC* (la atribución exclusiva es discutida: el equipo Eckert/Mauchly también contribuyó).
6. **Z3 1941, Colossus 1943–44, ENIAC 1945–46** ✓.
7. **Transistor 1947** ✓ — patente y demo en Bell Labs (Nobel 1956).
8. **Kilby 1958 / Noyce 1959** ✓ — Kilby (TI) primero conceptual, Noyce (Fairchild) con la versión planar fabricable.
9. **Hopper 1952** ✓ — compilador A-0; COBOL llega en 1959.
10. **Unix 1969 / C 1972–73** ✓ — Thompson y Ritchie en Bell Labs.
11. **Simula 67** ✓ — el nombre "orientado a objetos" lo acuña **Alan Kay** después.
12. **C++ 1985** ✓ — el proyecto empieza en 1979 como "C with Classes"; nombre C++ desde 1983; primera edición comercial 1985.
13. **Java 1995** ✓ — anunciado por Sun en mayo de 1995.
14. **Intel 4004 noviembre 1971** ✓.
15. **Apple I 1976 / Apple II 1977** ✓.
16. **IBM PC 12 agosto 1981** ✓.
17. **CUDA 2006** ✓ — anuncio noviembre 2006, SDK público junio 2007.
18. **Deep Blue 1997** ✓ — match de mayo de 1997 en Nueva York.
19. **Backpropagation 1986** ✓ — el algoritmo existía antes (Werbos 1974), pero el paper de Rumelhart/Hinton/Williams es el que lo populariza.
20. **Transformer 2017** ✓ — *Attention Is All You Need*, NeurIPS 2017.
21. **Frontier mayo 2022** ✓ — primer exascale TOP500.
22. **El Capitan 2024–2025** ✓ — Nº 1 del TOP500 desde noviembre 2024.
23. **JUPITER Booster 2025** ✓ — primer exascale europeo.

### Hitos añadidos para cerrar huecos

- **McCulloch-Pitts (1943)** — neurona artificial, anterior al perceptrón.
- **Frege (1879), Hilbert/Gödel (1928–1931)** — puente entre Boole y Turing.
- **LISP (1958) y ALGOL 60** — lenguajes que definen los grandes paradigmas.
- **Altair 8800 (1975) + Microsoft BASIC** — eslabón entre el 8080 y el Apple II.
- **Macintosh (1984)** — lleva Smalltalk/PARC al mercado.
- **AlexNet (2012) y AlphaGo (2016)** — transición de IA simbólica a deep learning aplicado.
- **Sycamore (2019)** — primer hito mediático cuántico previo a Willow.
- **Ley de Moore (Moore, 1965)** — encaja la electrónica con la economía del PC.

---

## Conclusión

La historia es **una sola línea** con **dos ramas finales paralelas** (cuántica y exascale clásica), y una **ola transversal** (la IA) que cruza casi todos los bloques.

- **GPUs** sí merecen estar en el bloque principal: son el puente físico que hace viable la IA moderna y la supercomputación actual.
- **VRAM** es subcomponente práctico: limita qué se puede ejecutar localmente, pero no es un cambio de paradigma equivalente a Boole, Turing o von Neumann.
- **CUDA (2006)** y **AlexNet (2012)** son los dos puntos de inflexión que conectan el mundo del hardware paralelo con el de la IA actual.
