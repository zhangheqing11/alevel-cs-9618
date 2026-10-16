"""Self-contained HTML output for generated handbooks."""

from __future__ import annotations

import html
import re

import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer


CSS = r"""
:root{--paper:#fcfdfd;--ink:#19313a;--muted:#546972;--line:#d6e2e4;--accent:#17687a;--wash:#edf5f6;--code:#e8eff0;--note:#fbf7ec;--gold:#b8901c;font-synthesis:none}
*{box-sizing:border-box}html{scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font-family:"PingFang SC","Noto Sans CJK SC",-apple-system,"Helvetica Neue",sans-serif;font-size:16px;line-height:1.8}a{color:var(--accent);text-underline-offset:3px}.layout{max-width:1440px;margin:auto;display:grid;grid-template-columns:285px minmax(0,1fr)}aside{height:100vh;position:sticky;top:0;overflow:auto;padding:28px 18px 60px;border-right:1px solid var(--line);background:var(--wash)}.brand{font-size:11px;letter-spacing:2px;color:var(--accent);font-weight:700}.nav-title{font-size:19px;font-weight:700;margin:2px 0 14px;line-height:1.4}#search{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:6px;background:var(--paper);color:var(--ink);font:inherit;font-size:14px;margin-bottom:10px}nav a{display:block;text-decoration:none;color:var(--muted);font-size:13.5px;line-height:1.45;padding:5px 8px;border-left:2px solid transparent}nav a:hover,nav a.active{color:var(--accent);background:var(--paper);border-color:var(--accent)}nav a.level-1{font-size:11px;letter-spacing:1.5px;color:var(--accent);font-weight:700;margin-top:16px}nav a.level-2{font-weight:650;color:var(--ink);margin-top:6px}nav a.level-3{padding-left:22px;font-size:12.5px;display:none}nav a.level-3.open{display:block}.toggle{float:right;border:0;background:transparent;color:var(--muted);cursor:pointer}main{min-width:0;max-width:1020px;padding:36px 52px 120px}h1{font-size:30px;line-height:1.35;margin:56px 0 16px;color:var(--accent)}h1:first-child{margin-top:0}h2{font-size:25px;line-height:1.4;margin:60px 0 10px;padding-bottom:8px;border-bottom:2px solid var(--accent)}h3{font-size:18px;margin:40px 0 8px;padding-top:14px;border-top:1px solid var(--line)}h4{font-size:15.5px;color:var(--accent);margin:18px 0 6px}p{margin:8px 0}li{margin:3px 0}table{border-collapse:collapse;width:100%;margin:12px 0 18px;font-size:14px;border-top:2px solid var(--accent);border-bottom:2px solid var(--accent)}thead th{background:var(--wash);text-align:left;font-weight:650}th,td{padding:6px 9px;border-bottom:1px solid var(--line);vertical-align:top}td:first-child{white-space:nowrap}.score-sentence{display:inline-block;background:var(--code);border-left:3px solid var(--muted);padding:1px 8px;font-family:Georgia,"Times New Roman",serif}.citation{white-space:nowrap;font-size:.9em}.stat{font-size:13px;color:var(--muted);background:var(--wash);padding:6px 10px;border-radius:4px;margin:6px 0 10px}.ms-quote{}.codehilite{background:var(--code);padding:12px 14px;overflow:auto;border-radius:4px}.codehilite pre{margin:0}.pseudocode{background:#f5f2e9}.search-hidden{display:none}.skip{position:absolute;left:-9999px}.skip:focus{left:16px;top:8px;background:var(--paper);z-index:9}#menu{display:none}
@media (max-width:900px){.layout{grid-template-columns:1fr}aside{position:fixed;inset:0 25% 0 0;z-index:5;transform:translateX(-105%);transition:transform .2s}aside.open{transform:none;box-shadow:0 0 30px rgba(0,0,0,.25)}#menu{display:block;position:fixed;left:12px;bottom:14px;z-index:6;padding:7px 14px;border-radius:16px;border:1px solid var(--accent);background:var(--paper);color:var(--accent);font:inherit;font-size:13px}main{padding:22px 16px 90px;overflow-x:clip}table{display:block;overflow-x:auto}td:first-child{white-space:normal}h1{font-size:25px}h2{font-size:21px}}
@media print{aside,#menu,.skip{display:none}.layout{display:block}main{max-width:none;padding:0}}
"""


JS = r"""
(function(){
  var side=document.getElementById('side'),menu=document.getElementById('menu');
  if(menu)menu.onclick=function(){side.classList.toggle('open')};
  document.querySelectorAll('nav a.level-2').forEach(function(link){
    var next=link.nextElementSibling, button=document.createElement('button');
    button.className='toggle';button.type='button';button.textContent='▾';button.setAttribute('aria-label','展开或折叠题型');
    link.appendChild(button);button.onclick=function(e){e.preventDefault();var open=next&&next.classList.contains('open');
      var n=next;while(n&&n.tagName==='A'&&n.classList.contains('level-3')){n.classList.toggle('open',!open);n=n.nextElementSibling}button.textContent=open?'▸':'▾';};
  });
  var search=document.getElementById('search');
  if(search)search.oninput=function(){var q=search.value.trim().toLowerCase();document.querySelectorAll('main h1,main h2,main h3,main h4,main p,main li,main table').forEach(function(el){el.classList.toggle('search-hidden',!!q&&el.textContent.toLowerCase().indexOf(q)<0)});};
  var links=[].slice.call(document.querySelectorAll('nav a')),heads=links.map(function(a){return document.getElementById(a.getAttribute('href').slice(1))});
  function active(){var y=scrollY+90,at=-1;heads.forEach(function(h,i){if(h&&h.getBoundingClientRect().top+scrollY<=y)at=i});links.forEach(function(a,i){a.classList.toggle('active',i===at)});}
  addEventListener('scroll',active);active();
})();
"""


def _pseudo_highlight(code: str) -> str:
    escaped = html.escape(code)
    # Comments first, then keywords/operators in the remaining text.  The simple
    # lexer is intentionally conservative so identifiers and quoted strings keep
    # their original appearance.
    pieces = re.split(r"(//[^\n]*)", escaped)
    keywords = r"\b(DECLARE|CONSTANT|IF|THEN|ELSE|ENDIF|FOR|TO|NEXT|WHILE|DO|ENDWHILE|REPEAT|UNTIL|CASE|OF|OTHERWISE|ENDCASE|FUNCTION|RETURNS|ENDFUNCTION|PROCEDURE|ENDPROCEDURE|RETURN|INPUT|OUTPUT|OPENFILE|READFILE|WRITEFILE|CLOSEFILE|TRUE|FALSE|AND|OR|NOT)\b"
    out: list[str] = []
    for index, piece in enumerate(pieces):
        if index % 2:
            out.append(f'<span class="pseudocode-comment">{piece}</span>')
        else:
            piece = re.sub(keywords, r'<span class="pseudocode-keyword">\1</span>', piece)
            piece = piece.replace("←", '<span class="pseudocode-operator">←</span>')
            out.append(piece)
    return "".join(out)


def _highlight_code(fragment: str) -> str:
    pattern = re.compile(r'<pre><code(?: class="language-([\w-]+)")?>(.*?)</code></pre>', re.S)

    def replace(match: re.Match) -> str:
        language = match.group(1) or "text"
        code = html.unescape(match.group(2))
        if language.lower() in {"pseudocode", "pseudo"}:
            return f'<pre class="codehilite pseudocode"><code>{_pseudo_highlight(code)}</code></pre>'
        if language.lower() in {"python", "py"}:
            highlighted = highlight(code, PythonLexer(), HtmlFormatter(nowrap=True))
            return f'<pre class="codehilite python"><code>{highlighted}</code></pre>'
        return f'<pre class="codehilite"><code>{html.escape(code)}</code></pre>'

    return pattern.sub(replace, fragment)


def _nav(fragment: str) -> str:
    headings = []
    for match in re.finditer(r'<h([1-3])(?: id="([^"]+)")?>(.*?)</h\1>', fragment, re.S):
        level, hid, label = int(match.group(1)), match.group(2), re.sub(r"<[^>]+>", "", match.group(3)).strip()
        if not hid:
            continue
        headings.append((level, hid, html.unescape(label)))
    parts = []
    for level, hid, label in headings:
        parts.append(f'<a class="level-{level}" href="#{html.escape(hid, quote=True)}">{html.escape(label)}</a>')
    return "\n".join(parts)


def render_html(source: str, title: str, kind: str = "handbook") -> str:
    """Convert Markdown into a fully self-contained HTML document."""

    fragment = markdown.markdown(
        source,
        extensions=["extra", "attr_list", "sane_lists", "toc"],
        output_format="html5",
    )
    fragment = _highlight_code(fragment)
    nav = _nav(fragment)
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><title>{html.escape(title)}</title><style>{CSS}</style></head>
<body data-kind="{html.escape(kind, quote=True)}"><a class="skip" href="#main">跳到正文</a>
<div class="layout"><aside id="side"><div class="brand">CIE 9618 · COMPUTER SCIENCE</div><div class="nav-title">{html.escape(title)}</div>
<input id="search" type="search" placeholder="搜索题型、概念、关键词…" aria-label="搜索"><nav>{nav}</nav></aside>
<button id="menu" type="button" aria-label="目录">目录</button><main id="main">{fragment}</main></div><script>{JS}</script></body></html>'''
