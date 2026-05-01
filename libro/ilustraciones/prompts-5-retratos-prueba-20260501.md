# Prompts · 5 retratos prueba para validación de dirección de arte

**Proyecto:** *El Hilo Invisible de la IA*
**Fecha:** 1 mayo 2026
**Modelo recomendado:** `imagen-4.0-ultra-generate-001` (Imagen 4 Ultra)
**Aspect ratio:** `3:4` (formato A5 vertical)
**Cantidad por test:** 1 imagen por personaje (5 totales)

---

## Criterios de selección de los 5 personajes

Hemos elegido **5 personajes que cubren todo el espectro temporal y emocional del libro**. Si el sistema visual funciona con estos 5, funcionará con los 30.

| # | Personaje | Año significativo | Edad | Por qué este personaje |
|---|-----------|---------------------|------|------------------------|
| 1 | **Walter Pitts** | 1943 | 20 | El más difícil: chico raro, marginal, pose informal · si funciona, todo el libro funciona |
| 2 | **Ada Lovelace** | 1843 | 28 | Único retrato femenino del cuarteto fundacional · vestido victoriano · validar registro de época XIX |
| 3 | **Alan Turing** | 1950 | 38 | Icono ya muy retratado (high recognition) · prueba de "no caer en el cliché" |
| 4 | **Grace Hopper** | 1947 | 41 | Uniforme militar femenino · validar capacidad del estilo para uniformes sin volverse rígido |
| 5 | **Geoffrey Hinton** | 2024 | 76 | Personaje contemporáneo · validar que el estilo XIX-acuarela funciona con figuras modernas |

---

## Prompt 1 · Walter Pitts (1943)

### Contexto del personaje
Walter Pitts, 20 años, en la cocina de los McCulloch en Chicago, mientras escribe junto a Warren McCulloch el paper que daría origen a las redes neuronales. Chico de aspecto desgreñado, pelo oscuro despeinado, mirada intensa pero esquiva, ropa modesta de obrero (camisa abotonada arrugada, sin chaqueta), sentado a una mesa de cocina con papeles y un vaso de leche al lado. Sin pose. Sorprendido en mitad del pensamiento.

### Prompt EN (para Imagen 4)
```
Sepia watercolor portrait of Walter Pitts, 20 years old, 1943, sitting at a humble kitchen table in Chicago, dark messy hair, intense thoughtful eyes looking down at scattered papers, wearing a wrinkled workman's button-up shirt without jacket, holding a pen, a glass of milk beside him, deep concentration on his face, no pose just caught in the middle of a thought, soft sepia and warm cream colors, ink and watercolor on textured cream paper, in the style of Edward Gorey meets 19th century scientific notebook illustration, expressive but minimalist, NOT digital art, NOT vector graphics, NOT modern, museum quality book illustration, white textured paper background, intimate and human
```

### Variables del template
- `[PERSON_NAME]`: Walter Pitts
- `[AGE]`: 20
- `[HISTORICAL_CONTEXT_KEYWORD]`: Chicago kitchen 1943, scattered papers
- `[SIGNATURE_OBJECT]`: pen and scattered papers, glass of milk
- `[POSE]`: looking down at papers, deep concentration

---

## Prompt 2 · Ada Lovelace (1843)

### Contexto del personaje
Ada Lovelace, 28 años, en la biblioteca de su casa en Londres, mientras traduce el paper de Menabrea sobre la Máquina Analítica de Babbage y añade las notas que la convertirían en la primera programadora de la historia. Vestido victoriano oscuro de seda, pelo recogido, perlas discretas. Pluma en la mano. Mirada inteligente, ligeramente desafiante, dirigida al lector. Concentración serena.

### Prompt EN
```
Sepia watercolor portrait of Ada Lovelace, 28 years old, 1843, in her London library writing notes by candlelight, dark Victorian silk dress with high collar, hair pulled back elegantly with discreet pearls, holding a quill pen mid-thought, looking up directly at the viewer with calm intelligent slightly defiant gaze, manuscript pages and inkwell on the desk before her, soft sepia and warm cream tones, ink and watercolor on textured cream paper, in the style of Edward Gorey meets 19th century scientific notebook illustration, expressive but minimalist, NOT digital art, NOT vector graphics, NOT modern photography, museum quality book illustration, intimate composition, white textured paper background
```

---

## Prompt 3 · Alan Turing (1950)

### Contexto del personaje
Alan Turing, 38 años, en su despacho de la Universidad de Manchester, mientras escribe *Computing Machinery and Intelligence*. Cabello oscuro despeinado, jersey de punto sobre camisa abierta sin corbata (informal británico años 50), mirada melancólica y profunda dirigida ligeramente hacia un lado, sosteniendo un lápiz, papeles llenos de fórmulas en la mesa. Aspecto humano, no icónico. **Específicamente NO la imagen tópica del Imitation Game.**

### Prompt EN
```
Sepia watercolor portrait of Alan Turing, 38 years old, 1950, sitting at his cluttered office desk at Manchester University, dark unruly hair, wearing a knitted wool sweater over an open-collar shirt without tie, melancholic deep thoughtful eyes looking slightly off to the side, holding a pencil mid-thought, papers filled with mathematical formulas on the desk, NOT a polished cinematic portrait, NOT the famous photograph, just a quiet humble human moment, soft sepia and warm cream tones, ink and watercolor on textured cream paper, in the style of Edward Gorey meets 19th century scientific notebook illustration, expressive but minimalist, NOT digital art, NOT vector graphics, museum quality book illustration, intimate composition
```

---

## Prompt 4 · Grace Hopper (1947)

### Contexto del personaje
Grace Hopper, 41 años, capitana de la Marina estadounidense, en el laboratorio de Harvard junto al ordenador Mark II, sosteniendo el cuaderno de bitácora donde acaba de pegar la polilla del primer "bug". Uniforme militar formal pero ya algo arrugado por la jornada, gorra apoyada al lado, pelo recogido. Sonrisa contenida de quien sabe que acaba de ver algo absurdo y memorable. Postura erguida pero relajada.

### Prompt EN
```
Sepia watercolor portrait of Grace Hopper, 41 years old, 1947, in the Harvard Mark II computer laboratory, wearing a formal US Navy uniform slightly rumpled from the day, hair pulled back neatly, navy cap resting on the desk beside her, holding open a logbook with a moth taped inside, contained subtle smile of someone who just witnessed something absurd and memorable, upright but relaxed posture, large mechanical computer relays partially visible in the soft background, soft sepia and warm cream tones, ink and watercolor on textured cream paper, in the style of Edward Gorey meets 19th century scientific notebook illustration, expressive but minimalist, NOT digital art, NOT vector graphics, NOT military propaganda style, museum quality book illustration, intimate human moment
```

---

## Prompt 5 · Geoffrey Hinton (2024)

### Contexto del personaje
Geoffrey Hinton, 76 años, en su despacho universitario en Toronto, el día que se anunció su Premio Nobel de Física por backpropagation. Pelo cano abundante, gafas de pasta, camisa de cuadros abierta sobre camiseta interior (estilo profesor canadiense informal), expresión entre cansada y satisfecha, sosteniendo una taza de café. Detrás, una pizarra con ecuaciones medio borradas. **Reto de este test:** demostrar que el estilo acuarela XIX funciona con un personaje contemporáneo sin parecer fuera de lugar.

### Prompt EN
```
Sepia watercolor portrait of Geoffrey Hinton, 76 years old, 2024, in his university office in Toronto, abundant white hair slightly disheveled, thick black-rimmed eyeglasses, wearing an open plaid flannel shirt over a t-shirt in casual Canadian professor style, expression somewhere between tired and quietly satisfied, holding a coffee mug with both hands, a chalkboard with half-erased mathematical equations softly visible behind him, soft sepia and warm cream tones, ink and watercolor on textured cream paper, in the style of Edward Gorey meets 19th century scientific notebook illustration applied to a contemporary subject, expressive but minimalist, NOT digital art, NOT vector graphics, NOT modern photography, museum quality book illustration, intimate human moment, demonstrating that the historical aesthetic works with present-day figures
```

---

## Comando ejecutivo (workflow para generación)

```bash
# Variables
MODEL="imagen-4.0-ultra-generate-001"
ASPECT="3:4"
OUTPUT_DIR="/Users/cop/Documents/OBSIDIAN_WORKSPACE/BIBLIOTECA_COP_2026/proyectos-claude/05_PROPOSALS/active/libro-hilo-invisible-ia/ilustraciones/retratos-prueba"

mkdir -p "$OUTPUT_DIR"

# 5 generaciones (uno por uno · revisar cada uno antes del siguiente)
# 1. Pitts
/imagen --modelo $MODEL --ratio $ASPECT --nombre "test-01-pitts-1943" \
  "[PROMPT 1 ENTERO PEGADO AQUÍ]"

# 2. Lovelace
/imagen --modelo $MODEL --ratio $ASPECT --nombre "test-02-lovelace-1843" \
  "[PROMPT 2 ENTERO PEGADO AQUÍ]"

# 3. Turing
/imagen --modelo $MODEL --ratio $ASPECT --nombre "test-03-turing-1950" \
  "[PROMPT 3 ENTERO PEGADO AQUÍ]"

# 4. Hopper
/imagen --modelo $MODEL --ratio $ASPECT --nombre "test-04-hopper-1947" \
  "[PROMPT 4 ENTERO PEGADO AQUÍ]"

# 5. Hinton
/imagen --modelo $MODEL --ratio $ASPECT --nombre "test-05-hinton-2024" \
  "[PROMPT 5 ENTERO PEGADO AQUÍ]"
```

> **Nota:** Lanzar uno cada vez · revisar resultado antes de siguiente · iterar prompt si el primero no convence (no malgastar 5 generaciones con un prompt mal calibrado).

---

## Checklist de evaluación

Cuando los 5 estén generados, evaluar SI/NO en cada criterio:

### Coherencia del sistema
- [ ] Los 5 retratos parecen pertenecer al **mismo libro** (paleta · trazo · papel)
- [ ] El estilo XIX-acuarela funciona tanto en 1843 como en 2024
- [ ] Ninguno parece "AI generated" (sin caras simétricas perfectas, sin manos raras)
- [ ] Los 5 funcionan en **escala de grises** (test imprimibilidad B&N)

### Carácter de cada personaje
- [ ] Pitts transmite **vulnerabilidad + intelecto** (no glamour, no caricatura)
- [ ] Lovelace transmite **inteligencia desafiante** (no rigidez victoriana, no romanticismo)
- [ ] Turing **NO es la imagen tópica del Imitation Game**
- [ ] Hopper **NO parece propaganda militar** (es humana, contenida)
- [ ] Hinton no parece **fuera de lugar** en el estilo del libro

### Decisión final
- [ ] **GO** → continuar con los 25 retratos restantes con este template
- [ ] **NO-GO + iterar** → identificar qué cambiar en prompt template antes de re-probar
- [ ] **NO-GO + cambiar modelo** → probar Nano Banana 2 con los mismos prompts

---

## Próximas acciones inmediatas

- [ ] **Hoy 1 may:** ejecutar generación de los 5 retratos prueba (~30 min)
- [ ] **Hoy 1 may:** review interno + decisión GO/NO-GO
- [ ] **Si GO:** mañana 2 may, generar los 25 retratos restantes (orden de prioridad: Boole, Babbage, Shannon, McCulloch, Pascal, Leibniz, Turing-otro-momento, Russell, Frege, Hilbert, Wiener, Mead, McCarthy, Minsky, Newell, Simon, Engelbart, Kay, LeCun, Bengio, Schmidhuber, Goodfellow, Vaswani, Karpathy, Sutskever)
- [ ] **Mayo S2:** contactar 2-3 ilustradores profesionales para lámina A2 con brief adjunto

---

*Documento de prueba. Si los retratos validan dirección de arte, este documento se archiva y se procede con la lista completa de 30 retratos.*
