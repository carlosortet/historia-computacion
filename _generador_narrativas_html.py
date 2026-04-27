#!/usr/bin/env python3
"""
Generador de HTMLs estilo IBM 5324 Service Manual a partir de los .md narrativos.

Lee todos los .md del directorio fuente y genera .html correspondientes,
aplicando el template visual con tipografía IBM Plex, márgenes generosos,
agujeros de archivador, tabs laterales, headers con regla gruesa y
footer con número de página estilo "1-1" "2-15".

Uso:
    python3 _generador_narrativas_html.py
"""
import os
import re
import sys
from pathlib import Path

SRC_DIR = Path("/Users/cop/Documents/OBSIDIAN_WORKSPACE/BIBLIOTECA_COP_2026/proyectos-claude/06_COP_PERSONAL/narrativas-historia-computacion")
DST_DIR = Path("/Users/cop/Documents/03_PERSONAL/historia-computacion/narrativas")

# Mapeo columna → color del tab + nombre
COLUMN_META = {
    "00": {"color": "#1A1A1A", "name": "INDICE",         "label": "ÍNDICE",         "chapter": "0"},
    "01": {"color": "#1F70C1", "name": "LOGICA",         "label": "LÓGICA",         "chapter": "1"},
    "02": {"color": "#002D9C", "name": "ALGORITMOS",     "label": "ALGORITMOS",     "chapter": "2"},
    "03": {"color": "#DA1E28", "name": "ARQUITECTURA",   "label": "ARQUITECTURA",   "chapter": "3"},
    "04": {"color": "#F1C21B", "name": "ELECTRONICA",    "label": "ELECTRÓNICA",    "chapter": "4"},
    "05": {"color": "#198038", "name": "SOFTWARE",       "label": "SOFTWARE",       "chapter": "5"},
    "06": {"color": "#8A3FFC", "name": "PARADIGMAS",     "label": "PARADIGMAS",     "chapter": "6"},
    "07": {"color": "#FF832B", "name": "MICRO_PC",       "label": "MICRO+PC",       "chapter": "7"},
    "08": {"color": "#BA4E00", "name": "ROBOTICA",       "label": "ROBÓTICA",       "chapter": "8"},
    "09": {"color": "#0E6027", "name": "INTERNET",       "label": "INTERNET",       "chapter": "9"},
    "10": {"color": "#A56EFF", "name": "DATA",           "label": "DATA",           "chapter": "10"},
    "11": {"color": "#EE5396", "name": "IA",             "label": "IA",             "chapter": "11"},
    "12": {"color": "#33B1FF", "name": "PARALELISMO",    "label": "PARALELISMO",    "chapter": "12"},
    "13": {"color": "#9F1853", "name": "CUANTICA",       "label": "CUÁNTICA",       "chapter": "13"},
    "14": {"color": "#005D5D", "name": "SUPERCOMPUTACION","label": "SUPERCOMP",     "chapter": "14"},
    "15": {"color": "#A66A0A", "name": "SIMULACION",     "label": "SIMULACIÓN",     "chapter": "15"},
}

# CSS común (estilo IBM 5324 manual técnico)
CSS = """
:root {
  --paper: #F5F1E8;
  --ink: #1A1A1A;
  --tab-color: %TAB_COLOR%;
  --rule: #1A1A1A;
  --shade: #E8DCC4;
  --note: #FAFAFA;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:'IBM Plex Sans','Helvetica Neue',Arial,sans-serif;
  background:#D8C8A4;  /* color "library shelf" alrededor de la página */
  color:var(--ink);
  font-size:14px;
  line-height:1.55;
  -webkit-font-smoothing:antialiased;
  padding:32px 0;
}
.page{
  background:var(--paper);
  max-width:840px;
  margin:0 auto 32px;
  position:relative;
  padding:48px 64px 56px 96px;
  min-height:1100px;
  box-shadow:0 1px 3px rgba(0,0,0,.15), 0 8px 24px rgba(0,0,0,.18);
}
/* AGUJEROS DE ARCHIVADOR (decorativos, izquierda) */
.holes{
  position:absolute;
  left:24px;
  top:0;
  bottom:0;
  width:14px;
  display:flex;
  flex-direction:column;
  justify-content:space-around;
  padding:120px 0;
  pointer-events:none;
}
.hole{
  width:14px;
  height:14px;
  border-radius:50%;
  background:#D8C8A4;
  box-shadow:inset 1px 1px 2px rgba(0,0,0,.4);
}
/* TAB LATERAL (chapter index, derecha) */
.tab{
  position:absolute;
  right:-24px;
  top:140px;
  width:48px;
  height:120px;
  background:var(--tab-color);
  color:#fff;
  display:flex;
  align-items:center;
  justify-content:center;
  font-family:'IBM Plex Sans',sans-serif;
  font-weight:600;
  font-size:11px;
  letter-spacing:1.5px;
  writing-mode:vertical-rl;
  text-orientation:mixed;
  transform:rotate(180deg);
  box-shadow:2px 2px 0 rgba(0,0,0,.2);
  text-transform:uppercase;
}
/* CABECERA */
.page-header{
  display:flex;
  justify-content:space-between;
  align-items:flex-end;
  margin-bottom:6px;
  font-family:'IBM Plex Sans',sans-serif;
  gap:12px;
  flex-wrap:wrap;
}
.book-title{
  font-size:11px;
  letter-spacing:.5px;
  color:#666;
  text-transform:uppercase;
  font-weight:500;
}
.doc-num{
  font-family:'IBM Plex Mono',monospace;
  font-size:10px;
  color:#666;
  letter-spacing:.5px;
}
.header-nav{
  display:flex;
  gap:6px;
  font-family:'IBM Plex Mono',monospace;
  font-size:10px;
  letter-spacing:1px;
}
.header-nav a{
  background:#1A1A1A;
  color:#33ff66;
  text-decoration:none;
  padding:3px 8px;
  border:1px solid #1A1A1A;
  text-shadow:0 0 6px rgba(51,255,102,.45);
  text-transform:uppercase;
  font-weight:500;
}
.header-nav a:hover{
  background:#33ff66;
  color:#1A1A1A;
  text-shadow:none;
}
.header-nav a.secondary{
  background:transparent;
  color:#666;
  text-shadow:none;
  border:1px solid #999;
}
.header-nav a.secondary:hover{
  background:var(--tab-color);
  color:#fff;
  border-color:var(--tab-color);
}
.page-title{
  font-size:28px;
  font-weight:700;
  margin:8px 0 4px;
  letter-spacing:-.3px;
  line-height:1.15;
}
.page-subtitle{
  font-size:14px;
  color:#444;
  font-weight:400;
  margin-bottom:14px;
  font-style:italic;
}
.title-rule{
  border:none;
  border-bottom:3px solid var(--rule);
  margin:0 0 28px;
}
/* SECCIONES (procedimiento) */
.section{
  margin-bottom:32px;
  page-break-inside:avoid;
}
.section-head{
  display:flex;
  align-items:baseline;
  gap:14px;
  margin-bottom:6px;
  margin-top:4px;
}
.proc-num{
  font-family:'IBM Plex Mono',monospace;
  font-size:13px;
  font-weight:700;
  color:var(--ink);
  background:var(--shade);
  padding:2px 8px;
  border:1px solid var(--ink);
  letter-spacing:.5px;
  white-space:nowrap;
}
.section-title{
  font-size:18px;
  font-weight:700;
  flex:1;
}
.section-rule{
  border:none;
  border-bottom:1px solid var(--ink);
  margin:0 0 14px;
}
.section p{
  margin:0 0 12px;
  text-align:justify;
  hyphens:auto;
}
.section blockquote{
  border-left:3px solid var(--tab-color);
  padding:6px 14px 6px 18px;
  margin:14px 0;
  font-style:italic;
  color:#444;
  background:var(--note);
}
/* CADENA: items con badge tipo IBM */
.chain-item{
  margin:0 0 22px;
  padding:0 0 0 0;
}
.chain-head{
  display:flex;
  align-items:flex-start;
  gap:10px;
  margin:0 0 8px;
}
.badge{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  width:22px;
  height:22px;
  border-radius:50%;
  background:var(--ink);
  color:#fff;
  font-family:'IBM Plex Sans',sans-serif;
  font-size:11px;
  font-weight:700;
  flex-shrink:0;
  margin-top:2px;
}
.chain-year{
  font-family:'IBM Plex Mono',monospace;
  font-weight:700;
  color:var(--tab-color);
  font-size:14px;
  white-space:nowrap;
}
.chain-title{
  font-weight:700;
  font-size:15px;
  flex:1;
}
.chain-person{
  color:#444;
  font-style:italic;
  font-weight:400;
}
.chain-body{
  padding-left:32px;
  margin-bottom:6px;
}
.chain-rel{
  padding-left:32px;
  font-size:12px;
  color:#444;
  border-top:1px dotted #999;
  padding-top:6px;
  margin-top:8px;
}
.chain-rel strong{color:var(--ink)}
/* TABLA */
table{
  width:100%;
  border-collapse:collapse;
  margin:14px 0;
  font-size:12px;
}
th{
  background:var(--shade);
  color:var(--ink);
  text-align:left;
  padding:8px 10px;
  border:1px solid var(--ink);
  font-weight:700;
  letter-spacing:.3px;
}
td{
  padding:7px 10px;
  border:1px solid var(--ink);
  vertical-align:top;
}
/* CROSS-COLUMN dependencies */
.cross-list{
  list-style:none;
  margin:8px 0;
  padding:0;
}
.cross-list li{
  padding:6px 0 6px 28px;
  position:relative;
  border-bottom:1px dotted #999;
  font-size:13px;
}
.cross-list li:last-child{border-bottom:none}
.cross-list .arrow{
  position:absolute;
  left:0;
  top:6px;
  font-family:'IBM Plex Mono',monospace;
  font-weight:700;
  color:var(--tab-color);
  font-size:14px;
}
.cross-list a{
  color:var(--ink);
  text-decoration:underline;
  text-decoration-color:#999;
}
.cross-list a:hover{
  text-decoration-color:var(--tab-color);
  color:var(--tab-color);
}
/* LECTURA SIGUIENTE */
.next-list{
  list-style:none;
  margin:8px 0;
  padding:0;
}
.next-list li{
  padding:8px 0 8px 28px;
  position:relative;
  border-bottom:1px dotted #999;
}
.next-list li::before{
  content:"►";
  position:absolute;
  left:4px;
  top:8px;
  color:var(--tab-color);
  font-size:11px;
}
/* FOOTER */
.page-footer{
  position:absolute;
  bottom:24px;
  left:96px;
  right:64px;
  display:flex;
  justify-content:space-between;
  font-family:'IBM Plex Mono',monospace;
  font-size:10px;
  color:#666;
  letter-spacing:.5px;
  border-top:1px solid #999;
  padding-top:8px;
}
.page-footer .nav a{
  color:#666;
  text-decoration:none;
  border:1px solid #999;
  padding:1px 6px;
  margin:0 2px;
}
.page-footer .nav a:hover{
  background:var(--tab-color);
  color:#fff;
  border-color:var(--tab-color);
}
/* HOVER MARKS */
a{color:var(--ink);text-decoration:underline;text-decoration-color:#999}
a:hover{color:var(--tab-color);text-decoration-color:var(--tab-color)}
/* PRINT */
@media print{
  body{background:white;padding:0}
  .page{margin:0;box-shadow:none;page-break-after:always;max-width:none;min-height:auto}
  .page-footer{position:relative;bottom:auto;left:0;right:0;margin-top:32px}
  .holes{display:none}
}
/* RESPONSIVE */
@media (max-width:900px){
  body{padding:8px 0;background:var(--paper)}
  .page{padding:24px 18px 56px 18px;max-width:100%;margin:0 0 16px}
  .holes{display:none}
  .tab{right:-12px;width:32px;height:90px;font-size:10px;top:80px}
  .page-title{font-size:22px}
  .section-title{font-size:16px}
  .chain-body,.chain-rel{padding-left:0}
  .page-footer{left:18px;right:18px;bottom:14px;font-size:9px}
}
"""

# HTML envoltorio
HTML_WRAPPER = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%TITLE% · Narrativas Historia Computación · 498 Advance</title>
<meta name="description" content="%DESCRIPTION%">
<meta name="author" content="Carlos Ortet · 498 Advance">
<link rel="canonical" href="https://zoopa.es/files/narrativas/narrativa-%FILENAME_BASE%.html">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%231A1A1A'/%3E%3Ctext x='50' y='62' font-family='IBM Plex Sans,sans-serif' font-size='52' font-weight='900' fill='%2333B1FF' text-anchor='middle' letter-spacing='-3'%3E498%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>%CSS%</style>
</head>
<body>
<article class="page">
  <div class="holes" aria-hidden="true">
    <span class="hole"></span><span class="hole"></span><span class="hole"></span>
  </div>
  <div class="tab" aria-hidden="true">%TAB_LABEL%</div>
  <header class="page-header">
    <span class="book-title">Narrativas · Historia de la Computación · Vol. 2</span>
    <span class="header-nav">
      <a href="https://zoopa.es/files/historia-computacion-hitos-20260423.html" title="Volver al grafo interactivo">◄ GRAFO</a>
      <a href="00_INDICE.html" class="secondary" title="Índice de las 15 narrativas">◄ ÍNDICE</a>
    </span>
    <span class="doc-num">SX-498A-V02 · %DOC_NUM%</span>
  </header>
  <h1 class="page-title">%TITLE%</h1>
  <p class="page-subtitle">%SUBTITLE%</p>
  <hr class="title-rule">

%CONTENT%

  <footer class="page-footer">
    <span>SX-498A-V02 · Capítulo %CHAPTER%</span>
    <span class="nav">
      <a href="https://zoopa.es/files/historia-computacion-hitos-20260423.html" title="Volver al grafo interactivo">◄ GRAFO</a>
      <a href="00_INDICE.html" title="Volver al índice">◄ ÍNDICE</a>
      %PREV_LINK%
      %NEXT_LINK%
    </span>
    <span>%CHAPTER%-%PAGE%</span>
  </footer>
</article>
</body>
</html>
"""


def parse_frontmatter(text):
    """Extrae el frontmatter YAML simple (key: value)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end+3:].lstrip("\n")
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body


def md_inline(text):
    """Convierte negritas/links/itálicas markdown a HTML inline."""
    # escape HTML básico (sólo & < > para no romper nada de lo escrito)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # bold **x**
    text = re.sub(r"\*\*([^*]+?)\*\*", r"<strong>\1</strong>", text)
    # italics *x* (solo si no son **)
    text = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", text)
    # inline code `x`
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    # wikilinks [[file#section|alias]] o [[file#section]] o [[file]]
    def wiki_repl(m):
        full = m.group(1)
        alias = None
        if "|" in full:
            target, alias = full.split("|", 1)
        else:
            target = full
        # separa archivo y anchor
        if "#" in target:
            file_part, anchor = target.split("#", 1)
            anchor_slug = re.sub(r"[^a-z0-9]+", "-", anchor.lower()).strip("-")
        else:
            file_part = target
            anchor_slug = ""
        # si el archivo empieza por XX_ buscamos su HTML
        href = "#" + anchor_slug if not file_part.strip() else f"{file_part.strip()}.html" + (f"#{anchor_slug}" if anchor_slug else "")
        label = alias if alias else target
        return f'<a href="{href}">{label}</a>'
    text = re.sub(r"\[\[([^\]]+)\]\]", wiki_repl, text)
    # markdown links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def slug(text):
    """Genera anchor slug compatible con wikilinks."""
    s = re.sub(r"[^a-z0-9áéíóúñ]+", "-", text.lower()).strip("-")
    s = (s.replace("á","a").replace("é","e").replace("í","i")
         .replace("ó","o").replace("ú","u").replace("ñ","n"))
    return s


def md_to_sections(body):
    """Parsea el body markdown en secciones tipo IBM (procedure number + title)."""
    # números de procedimiento por sección (para el estilo "1212" del manual)
    section_proc_map = {
        "El arco":              "0001",
        "La cadena":            "0010",
        "Personas clave":       "0050",
        "Cross-column dependencies": "0080",
        "Lectura siguiente":    "0090",
        "Fuente":               "0099",
        "Las 15 columnas · resúmenes ejecutivos": "0010",
        "El proyecto":          "0001",
        "Cómo está organizado": "0005",
        "Mapa de cross-column dependencies (alto nivel)": "0050",
        "Rutas de lectura recomendadas": "0070",
        "Personas que aparecen en múltiples columnas": "0080",
        "Convenciones del directorio": "0090",
        "Versionado":           "0095",
        "Mantenimiento":        "0096",
        "Licencia":             "0097",
        "Autor":                "0099",
    }

    out_html = []
    lines = body.split("\n")
    i = 0
    n = len(lines)

    # extrae el quote inicial (TLDR) si está al principio
    while i < n and not lines[i].strip():
        i += 1

    # buscar primer h1 -> ya viene del page-title, se omite
    if i < n and lines[i].startswith("# "):
        i += 1
        while i < n and not lines[i].strip():
            i += 1

    # quote inicial -> page subtitle (lo extraemos antes en parse principal)

    while i < n:
        line = lines[i]
        # h2 = nueva sección (procedure)
        if line.startswith("## "):
            title = line[3:].strip()
            proc = section_proc_map.get(title, "0000")
            out_html.append(f'\n  <section class="section" id="{slug(title)}">')
            out_html.append(f'    <div class="section-head">')
            out_html.append(f'      <span class="proc-num">{proc}</span>')
            out_html.append(f'      <h2 class="section-title">{md_inline(title)}</h2>')
            out_html.append(f'    </div>')
            out_html.append(f'    <hr class="section-rule">')
            i += 1
            # consumir hasta próxima h2
            section_lines = []
            while i < n and not lines[i].startswith("## "):
                section_lines.append(lines[i])
                i += 1
            out_html.append(render_section_content(section_lines, title))
            out_html.append(f'  </section>')
        else:
            i += 1

    return "\n".join(out_html)


def render_section_content(lines, section_title):
    """Renderiza el contenido de una sección. Detecta: h3 (cadena items), tablas, listas, párrafos."""
    out = []
    i = 0
    n = len(lines)
    badge_idx = 0
    badges = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # H3 = chain item (### AÑO · Label — Persona)
        if line.startswith("### "):
            heading = line[4:].strip()
            badge = badges[badge_idx % len(badges)] if section_title == "La cadena" else None
            badge_idx += 1
            # parsear: "AÑO · Label — Persona"
            year_match = re.match(r"(\d{4}(?:\s*[·-]\s*\d{4})?)\s*·\s*(.+)", heading)
            if year_match:
                year = year_match.group(1)
                rest = year_match.group(2)
                # separar persona (después del — em-dash o --)
                person_match = re.search(r"\s+[—–-]\s+(.+)$", rest)
                if person_match:
                    label = rest[:person_match.start()].strip()
                    person = person_match.group(1).strip()
                else:
                    label = rest
                    person = ""
            else:
                year = ""
                label = heading
                person = ""

            anchor = slug(heading)
            out.append(f'    <div class="chain-item" id="{anchor}">')
            out.append(f'      <div class="chain-head">')
            if badge:
                out.append(f'        <span class="badge" aria-hidden="true">{badge}</span>')
            out.append(f'        <span class="chain-year">{year}</span>')
            person_html = ('&nbsp;<span class="chain-person">— ' + md_inline(person) + '</span>') if person else ''
            out.append(f'        <h3 class="chain-title">{md_inline(label)}{person_html}</h3>')
            out.append(f'      </div>')
            i += 1

            # consumir hasta próximo h3 o h2 o ---
            block = []
            while i < n and not lines[i].startswith("### ") and not lines[i].startswith("## "):
                if lines[i].strip() == "---":
                    i += 1
                    break
                block.append(lines[i])
                i += 1

            # separar narración de "Conduce a / Depende de" (línea con bold)
            narr_lines = []
            rel_lines = []
            for bl in block:
                if re.search(r"\*\*Conduce a:?\*\*", bl) or re.search(r"\*\*Depende de:?\*\*", bl):
                    rel_lines.append(bl)
                else:
                    narr_lines.append(bl)

            # narración
            narr_html = render_paragraphs(narr_lines)
            if narr_html:
                out.append(f'      <div class="chain-body">{narr_html}</div>')

            # relación
            if rel_lines:
                rel_text = " ".join(l.strip() for l in rel_lines if l.strip())
                out.append(f'      <div class="chain-rel">{md_inline(rel_text)}</div>')

            out.append(f'    </div>')

        # Tabla
        elif line.startswith("| "):
            tbl_lines = []
            while i < n and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            out.append(render_table(tbl_lines))

        # Lista
        elif stripped.startswith("- "):
            list_lines = []
            while i < n and (lines[i].strip().startswith("- ") or (lines[i].startswith("  ") and lines[i].strip())):
                list_lines.append(lines[i])
                i += 1
            css_class = "cross-list" if section_title == "Cross-column dependencies" else "next-list" if section_title == "Lectura siguiente" else ""
            out.append(render_list(list_lines, css_class))

        # Quote
        elif stripped.startswith("> "):
            quote_lines = []
            while i < n and lines[i].strip().startswith("> "):
                quote_lines.append(lines[i].strip()[2:])
                i += 1
            out.append(f'    <blockquote>{md_inline(" ".join(quote_lines))}</blockquote>')

        # Separator
        elif stripped == "---":
            i += 1

        # Code block
        elif stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_text = "\n".join(code_lines).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            out.append(f'<pre style="background:var(--shade);padding:12px 16px;font-family:IBM Plex Mono,monospace;font-size:11px;border:1px solid var(--ink);overflow-x:auto;line-height:1.4">{code_text}</pre>')

        # Párrafo normal
        else:
            para_lines = []
            while i < n and lines[i].strip() and not lines[i].startswith("#") and not lines[i].strip().startswith("|") and not lines[i].strip().startswith("- ") and not lines[i].strip().startswith("> ") and not lines[i].strip() == "---":
                para_lines.append(lines[i].strip())
                i += 1
            if para_lines:
                out.append(f'    <p>{md_inline(" ".join(para_lines))}</p>')

    return "\n".join(out)


def render_paragraphs(lines):
    """Renderiza líneas como párrafos preservando bloques."""
    out = []
    para = []
    for line in lines:
        s = line.strip()
        if s:
            para.append(s)
        else:
            if para:
                out.append(f'<p>{md_inline(" ".join(para))}</p>')
                para = []
    if para:
        out.append(f'<p>{md_inline(" ".join(para))}</p>')
    return "".join(out)


def render_table(lines):
    """Convierte líneas de tabla markdown a HTML."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        # quitar pipes externos y dividir
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return ""
    # rows[0] = header, rows[1] = separator (|---|---|), rows[2:] = data
    header = rows[0]
    body = rows[2:] if len(rows) > 2 else []
    out = ['    <table>']
    out.append('      <thead><tr>')
    for h in header:
        out.append(f'        <th>{md_inline(h)}</th>')
    out.append('      </tr></thead>')
    out.append('      <tbody>')
    for row in body:
        out.append('        <tr>')
        for c in row:
            out.append(f'          <td>{md_inline(c)}</td>')
        out.append('        </tr>')
    out.append('      </tbody>')
    out.append('    </table>')
    return "\n".join(out)


def render_list(lines, css_class=""):
    """Renderiza lista markdown como ul HTML."""
    items = []
    current = []
    for line in lines:
        if line.strip().startswith("- "):
            if current:
                items.append(" ".join(current).strip())
            current = [line.strip()[2:]]
        else:
            current.append(line.strip())
    if current:
        items.append(" ".join(current).strip())

    cls = f' class="{css_class}"' if css_class else ""
    out = [f'    <ul{cls}>']
    for it in items:
        # detecta arrows ↗ ↘ y los marca
        if it.startswith("↗") or it.startswith("↘"):
            arrow = it[0]
            rest = it[1:].strip()
            if css_class == "cross-list":
                out.append(f'      <li><span class="arrow">{arrow}</span>{md_inline(rest)}</li>')
            else:
                out.append(f'      <li>{md_inline(it)}</li>')
        else:
            out.append(f'      <li>{md_inline(it)}</li>')
    out.append('    </ul>')
    return "\n".join(out)


def extract_subtitle(body):
    """Extrae el primer blockquote (TLDR) tras el h1 como subtítulo."""
    lines = body.split("\n")
    in_quote = False
    quote_lines = []
    for line in lines:
        if line.startswith("> "):
            quote_lines.append(line[2:].strip())
            in_quote = True
        elif in_quote:
            break
    return " ".join(quote_lines) if quote_lines else ""


def remove_first_quote(body):
    """Elimina el primer blockquote del body (ya está en el subtítulo)."""
    lines = body.split("\n")
    out = []
    skipping = False
    skipped = False
    for line in lines:
        if not skipped and line.startswith("> "):
            skipping = True
            continue
        if skipping and not line.startswith("> "):
            skipping = False
            skipped = True
        out.append(line)
    return "\n".join(out)


def extract_h1(body):
    """Extrae el h1 principal del documento."""
    for line in body.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def split_h1_subtitle(h1):
    """De '# LÓGICA · Del binario...' separa columna y subtítulo."""
    if "·" in h1:
        parts = h1.split("·", 1)
        return parts[0].strip(), parts[1].strip()
    return h1, ""


def get_chapter_meta(filename):
    """De '01_LOGICA.md' extrae metadata."""
    base = filename.replace(".md", "")
    chapter_num = base.split("_")[0]
    return COLUMN_META.get(chapter_num, COLUMN_META["00"])


def get_nav_links(current_idx, all_files):
    """Genera links prev/next."""
    prev_link = ""
    next_link = ""
    if current_idx > 0:
        prev_file = all_files[current_idx - 1].replace(".md", ".html")
        prev_link = f'<a href="{prev_file}" title="Capítulo anterior">◄</a>'
    if current_idx < len(all_files) - 1:
        next_file = all_files[current_idx + 1].replace(".md", ".html")
        next_link = f'<a href="{next_file}" title="Capítulo siguiente">►</a>'
    return prev_link, next_link


def main():
    if not SRC_DIR.exists():
        print(f"ERROR: source dir no existe: {SRC_DIR}", file=sys.stderr)
        sys.exit(1)
    DST_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted([f for f in os.listdir(SRC_DIR) if f.endswith(".md") and not f.startswith(".")])
    print(f"Encontrados {len(md_files)} archivos .md")

    for idx, filename in enumerate(md_files):
        src_path = SRC_DIR / filename
        dst_filename = filename.replace(".md", ".html")
        dst_path = DST_DIR / dst_filename

        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()

        fm, body = parse_frontmatter(text)
        meta = get_chapter_meta(filename)

        h1 = extract_h1(body)
        col_name, h1_subtitle = split_h1_subtitle(h1)

        subtitle = extract_subtitle(remove_first_h1(body))
        body_clean = remove_first_quote(remove_first_h1(body))

        content_html = md_to_sections(body_clean)

        prev_link, next_link = get_nav_links(idx, md_files)

        html = (HTML_WRAPPER
                .replace("%TITLE%", col_name + (f" · {h1_subtitle}" if h1_subtitle else ""))
                .replace("%SUBTITLE%", subtitle if subtitle else f"Volumen 2 de la serie · Capítulo {meta['chapter']}")
                .replace("%CHAPTER%", meta["chapter"])
                .replace("%PAGE%", "1")
                .replace("%TAB_LABEL%", meta["label"])
                .replace("%TAB_COLOR%", meta["color"])
                .replace("%FILENAME_BASE%", meta["name"].lower())
                .replace("%DOC_NUM%", f"CAP-{meta['chapter'].zfill(2)}")
                .replace("%PREV_LINK%", prev_link)
                .replace("%NEXT_LINK%", next_link)
                .replace("%DESCRIPTION%", subtitle[:180] if subtitle else f"Narrativa de la columna {meta['label']}")
                .replace("%CSS%", CSS.replace("%TAB_COLOR%", meta["color"]))
                .replace("%CONTENT%", content_html))

        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"  ✓ {filename} → {dst_path.name} ({len(html)//1024}KB)")

    print(f"\nGenerados {len(md_files)} archivos HTML en {DST_DIR}")


def remove_first_h1(body):
    """Elimina el primer h1 del body."""
    lines = body.split("\n")
    out = []
    skipped = False
    for line in lines:
        if not skipped and line.startswith("# "):
            skipped = True
            continue
        out.append(line)
    return "\n".join(out)


if __name__ == "__main__":
    main()
