"""Gera site/index.html a partir de index.template.html.

Insere os ícones Phosphor (licença MIT) em linha, a faixa de áreas,
os cartões dos sócios e a lista de conteúdos.
Uso: python3 site/src/build.py
"""
import re
from pathlib import Path

SRC = Path(__file__).parent
SITE = SRC.parent
ICONS = SITE / "assets" / "icons"


def icon(name):
    svg = (ICONS / f"{name}.svg").read_text()
    return svg.replace("<svg ", '<svg class="i" aria-hidden="true" focusable="false" ', 1)


AREAS = ["Administrativo", "Aeronáutico", "Arbitragem", "Autoral", "Cível", "Compliance",
         "Construção civil", "Consumidor", "Contratos", "Digital", "Imobiliário", "Infraestrutura",
         "Licitações", "Mídias e publicidade", "Patrimonial", "Petróleo e gás", "Planejamento",
         "Propriedade intelectual", "Regulatório", "Societário", "Startups", "Terceiro setor",
         "Trabalhista", "Tributário", "Urbanístico"]

PARTNERS = [
    dict(foto="elias", nome="Elias Succar Neto", cargo="Sócio", oab="405.854",
         foco="Head da Área de Resolução de Conflitos. Contratos públicos e privados, imobiliário, urbanístico e meio ambiente.",
         bio="Ingressou no escritório como estagiário, no primeiro ano da faculdade. Atua no contencioso cível e contratual, nos setores imobiliário, urbanístico e ambiental e em licitações e contratos públicos.",
         form=["Direito, Universidade de Taubaté (2017)", "Pós-graduação em Direito Imobiliário, Faculdade Damásio", "Associado ao IBRADIM"],
         mail="elias"),
    dict(foto="dalas", nome="Dálas Patrícia Viana de Oliveira", cargo="Sócia", oab="340.957",
         foco="Consultoria Empresarial. Governança e compliance, gestão de contratos, ESG e LGPD.",
         bio="Mais de 10 anos em governança, gestão de contratos e no contencioso trabalhista e sindical. Atua na implantação de programas de compliance, ESG, LGPD, ética e integridade, e na consultoria para o Terceiro Setor.",
         form=["Direito, Universidade do Vale do Paraíba (2005)", "Certificação em Compliance Público e Anticorrupção, CPC &amp; ICP (2019)", "Curso livre de Compliance de LGPD, LEC-FGV"],
         mail="dalas"),
    dict(foto="gabriela", nome="Gabriela Dellú", cargo="Sócia", oab="474.563",
         foco="Consultivo e Contencioso Trabalhista. Relações de trabalho na indústria e em serviços.",
         bio="Coordena a defesa de clientes em reclamações trabalhistas, com atuação em audiências, perícias técnicas e sustentações orais, em especial nos setores de engenharia, manutenção industrial e infraestrutura. Atua também no consultivo e preventivo trabalhista.",
         form=["Direito, Universidade do Vale do Paraíba (2021)", "Pós-graduação em Direito Processual Aplicado, Escola Paulista de Direito", "Pós-graduações em Direito do Trabalho e Processual do Trabalho e em Família e Sucessões, Legale", "Especialização em Cálculos Trabalhistas, Instituto de Direito Real"],
         mail="gabriela"),
    dict(foto="vitor", nome="Vitor Vidal", cargo="Sócio", oab="489.635",
         foco="Consultoria Societária e Tributária. Planejamento fiscal, private equity, venture capital e M&amp;A.",
         bio="Iniciou a carreira no escritório como estagiário. Atua em operações societárias, reestruturações e M&amp;A, em planejamento e contencioso tributário e em propriedade industrial: marcas, softwares e ativos intangíveis.",
         form=["Direito, Universidade Anhanguera (2022)", "Pós-graduação em Direito Empresarial, FACEO (2024)", "Pós-graduação em Direito Societário, FGV-LAW SP (2026)"],
         mail="vitor"),
]

POSTS = [
    ("Óleo e gás", "Licitação da Petrobras segue a Lei 14.133?", "As estatais seguem a Lei das Estatais e o seu próprio regulamento, com prazos e fases diferentes."),
    ("Compliance", "Due Diligence de Integridade", "Como a avaliação de integridade influencia o acesso de fornecedores às contratações de estatais."),
    ("Societário", "Consórcios: o que definir antes de assinar", "Responsabilidade, divisão de escopo e emissão de atestados no acordo entre consorciadas."),
    ("Societário", "Acordo de sócios: por que formalizar", "Regras de voto, entrada, saída e transferência de participação definidas antes do conflito."),
]


def partner_html(p, i):
    form = "".join(f"<li>{f}</li>" for f in p["form"])
    return f"""<article class="partner reveal" style="--d:{i}">
          <div class="ph"><img src="assets/img/{p['foto']}.jpg" alt="{p['nome']}, {p['cargo'].lower()}" width="700" height="1068" loading="lazy"></div>
          <div class="person">
            <h3>{p['nome']}</h3>
            <p class="role">{p['cargo']}</p>
            <p class="oab">OAB/SP {p['oab']}</p>
            <p class="focus">{p['foco']}</p>
          </div>
          <details>
            <summary>Atuação e formação</summary>
            <p>{p['bio']}</p>
            <ul>{form}</ul>
          </details>
          <a class="mail" href="mailto:{p['mail']}@gmpadua.com.br">{icon('envelope-simple')}{p['mail']}@gmpadua.com.br</a>
        </article>"""


def post_html(k, t, d, i):
    return f"""<a class="post reveal" style="--d:{i}" href="https://www.instagram.com/gmpadua.advogados/" target="_blank" rel="noopener">
          <span class="k">{k}</span>
          <div><h3>{t}</h3><p>{d}</p></div>
          <span class="go" aria-hidden="true">{icon('arrow-up-right')}</span>
        </a>"""


html = (SRC / "index.template.html").read_text()
html = html.replace("{{areas}}", "".join(f"<li>{a}</li>" for a in AREAS))
html = html.replace("{{partners}}", "\n        ".join(partner_html(p, i) for i, p in enumerate(PARTNERS)))
html = html.replace("{{posts}}", "\n        ".join(post_html(*p, i) for i, p in enumerate(POSTS)))
html = re.sub(r"\{\{icon:([a-z-]+)\}\}", lambda m: icon(m.group(1)), html)

assert "{{" not in html, "placeholder sem substituição"
for ch in ("—", "–"):
    assert ch not in html, f"caractere proibido encontrado: {ch!r}"
(SITE / "index.html").write_text(html)
print("ok", len(html), "bytes")
