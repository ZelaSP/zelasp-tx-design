# -*- coding: utf-8 -*-
"""
Gera a Apresentacao Executiva Widescreen (16:9 - 960x540 pt) em PDF
para a disciplina 05 - Software & Total Experience Design (ZelaSP - GS 2026.2).
Cobre 100% da rubrica oficial (100 pontos / 7 blocos obrigatorios).
"""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUT_PDF = os.path.join(BASE_DIR, 'Apresentacao_TX_Design_ZelaSP.pdf')

PAGE_W, PAGE_H = 960, 540  # 16:9 Widescreen

# Paleta Civica ZelaSP
C_NAVY = colors.HexColor('#0f172a')
C_BLUE_DARK = colors.HexColor('#1e3a8a')
C_BLUE = colors.HexColor('#1d4ed8')
C_BLUE_LIGHT = colors.HexColor('#eff6ff')
C_BLUE_BORDER = colors.HexColor('#bfdbfe')
C_EMERALD_DARK = colors.HexColor('#065f46')
C_EMERALD = colors.HexColor('#059669')
C_EMERALD_LIGHT = colors.HexColor('#ecfdf5')
C_EMERALD_BORDER = colors.HexColor('#a7f3d0')
C_AMBER_DARK = colors.HexColor('#92400e')
C_AMBER_LIGHT = colors.HexColor('#fffbeb')
C_AMBER_BORDER = colors.HexColor('#fde68a')
C_RED_DARK = colors.HexColor('#991b1b')
C_RED_LIGHT = colors.HexColor('#fef2f2')
C_RED_BORDER = colors.HexColor('#fecaca')
C_SLATE_BG = colors.HexColor('#f8fafc')
C_SLATE_CARD = colors.HexColor('#ffffff')
C_SLATE_BORDER = colors.HexColor('#cbd5e1')
C_TEXT_MAIN = colors.HexColor('#0f172a')
C_TEXT_MUTED = colors.HexColor('#475569')


def draw_slide_chrome(c, slide_num, total_slides, section_tag, title, subtitle):
    # Background
    c.setFillColor(C_SLATE_BG)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Top accent bar
    c.setFillColor(C_BLUE_DARK)
    c.rect(0, PAGE_H - 8, PAGE_W, 8, stroke=0, fill=1)

    # Section pill
    c.setFillColor(C_BLUE_LIGHT)
    c.setStrokeColor(C_BLUE_BORDER)
    c.setLineWidth(1)
    c.roundRect(36, PAGE_H - 42, 270, 20, 10, stroke=1, fill=1)
    c.setFillColor(C_BLUE)
    c.setFont('Helvetica-Bold', 8.5)
    c.drawString(48, PAGE_H - 35, section_tag.upper())

    # Top right badge
    c.setFillColor(C_TEXT_MUTED)
    c.setFont('Helvetica-Bold', 8.5)
    c.drawRightString(PAGE_W - 36, PAGE_H - 34, 'FIAP · GS 2026.2 · SOFTWARE & TOTAL EXPERIENCE DESIGN · 1ESPW')

    # Main Title & Subtitle
    c.setFillColor(C_TEXT_MAIN)
    c.setFont('Helvetica-Bold', 20)
    c.drawString(36, PAGE_H - 70, title)

    c.setFillColor(C_TEXT_MUTED)
    c.setFont('Helvetica', 10.5)
    c.drawString(36, PAGE_H - 88, subtitle)

    # Divider line
    c.setStrokeColor(C_SLATE_BORDER)
    c.setLineWidth(1)
    c.line(36, PAGE_H - 98, PAGE_W - 36, PAGE_H - 98)

    # Footer
    c.setStrokeColor(C_SLATE_BORDER)
    c.line(36, 30, PAGE_W - 36, 30)
    c.setFillColor(C_TEXT_MUTED)
    c.setFont('Helvetica', 8)
    c.drawString(36, 15, 'ZelaSP — Zeladoria Cidadã Inteligente | Professor Henrique Cordeiro | Turma 1ESPW')
    c.setFont('Helvetica-Bold', 8.5)
    c.drawRightString(PAGE_W - 36, 15, f'Slide {slide_num} de {total_slides}')


def draw_card(c, x, y, w, h, bg=C_SLATE_CARD, border=C_SLATE_BORDER, radius=10):
    c.setFillColor(bg)
    c.setStrokeColor(border)
    c.setLineWidth(1.2)
    c.roundRect(x, y, w, h, radius, stroke=1, fill=1)


def draw_paragraph(c, text, x, y_top, w, font='Helvetica', size=9.5, leading=13.5, color=C_TEXT_MAIN):
    style = ParagraphStyle(
        name='SlidePara',
        fontName=font,
        fontSize=size,
        leading=leading,
        textColor=color,
    )
    p = Paragraph(text, style)
    pw, ph = p.wrap(w, 500)
    p.drawOn(c, x, y_top - ph)
    return ph


def build_pdf():
    c = canvas.Canvas(OUT_PDF, pagesize=(PAGE_W, PAGE_H))
    total_slides = 10

    # =========================================================================
    # SLIDE 1: CAPA (5 PONTOS)
    # =========================================================================
    c.setFillColor(C_NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Top bar
    c.setFillColor(C_EMERALD)
    c.rect(0, PAGE_H - 10, PAGE_W, 10, stroke=0, fill=1)

    # Left Hero Column
    c.setFillColor(colors.HexColor('#1e293b'))
    c.setStrokeColor(colors.HexColor('#334155'))
    c.roundRect(42, 54, 520, 430, 14, stroke=1, fill=1)

    # Logo if exists
    logo_path = os.path.join(ROOT_DIR, 'avatar_zelasp_icone_v2.jpg')
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 66, 396, width=62, height=62, preserveAspectRatio=True, mask='auto')

    c.setFillColor(colors.HexColor('#38bdf8'))
    c.setFont('Helvetica-Bold', 10)
    c.drawString(142, 440, 'GLOBAL SOLUTION 2026.2 · DESAFIO CITIZENTECH · FIAP')
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 31)
    c.drawString(142, 406, 'ZelaSP')

    c.setFillColor(colors.HexColor('#cbd5e1'))
    c.setFont('Helvetica', 13)
    c.drawString(66, 366, 'Zeladoria Cidadã Inteligente e Monitoramento Urbano em São Paulo')

    draw_paragraph(
        c,
        '<b>Proposta em uma frase:</b> Plataforma cívica que permite ao morador de São Paulo relatar riscos '
        'urbanos (fiação caída, bueiro aberto, entulho na calçada e carro abandonado) em menos de 15 segundos, '
        'unificando apoios da vizinhança sem duplicar chamados e priorizando o despacho das Subprefeituras.',
        66, 342, 470, size=10.2, leading=15, color=colors.HexColor('#e2e8f0')
    )

    # Metadata badges inside left box
    c.setFillColor(colors.HexColor('#0f172a'))
    c.setStrokeColor(colors.HexColor('#3b82f6'))
    c.roundRect(66, 178, 470, 96, 10, stroke=1, fill=1)
    c.setFillColor(colors.HexColor('#93c5fd'))
    c.setFont('Helvetica-Bold', 9.5)
    c.drawString(82, 254, 'IDENTIFICAÇÃO ACADÊMICA E ECOSSISTEMA')
    c.setFillColor(colors.white)
    c.setFont('Helvetica', 9.5)
    c.drawString(82, 234, '• Disciplina: Software & Total Experience Design (Da Proposta ao Roadmap)')
    c.drawString(82, 216, '• Professor: Henrique Cordeiro   |   Turma: 1ESPW (Engenharia de Software · 1º Ano)')
    c.drawString(82, 198, '• Bairros Foco SP: Jabaquara, Vila Mariana, Saúde, Bela Vista, Mooca e Vila Mascote')

    # Links & ODS box
    c.setFillColor(colors.HexColor('#064e3b'))
    c.setStrokeColor(colors.HexColor('#10b981'))
    c.roundRect(66, 76, 470, 84, 10, stroke=1, fill=1)
    c.setFillColor(colors.HexColor('#6ee7b7'))
    c.setFont('Helvetica-Bold', 9.5)
    c.drawString(82, 140, 'ODS ONU CONECTADOS & PROTÓTIPO FUNCIONAL NO AR')
    c.setFillColor(colors.white)
    c.setFont('Helvetica', 9.2)
    c.drawString(82, 121, '• ODS 11 (Cidades e Comunidades Sustentáveis) & ODS 9 (Inovação e Infraestrutura)')
    c.drawString(82, 103, '• Deploy Oficial (Vercel): https://zelasp-web.vercel.app/')
    c.drawString(82, 86, '• Repositório Web/UX: https://github.com/ZelaSP/zelasp-web')

    # Right Column: Team Members Card (5 pts rubric requirement)
    c.setFillColor(colors.HexColor('#1e293b'))
    c.setStrokeColor(colors.HexColor('#3b82f6'))
    c.roundRect(584, 54, 334, 430, 14, stroke=1, fill=1)

    c.setFillColor(colors.HexColor('#60a5fa'))
    c.setFont('Helvetica-Bold', 11)
    c.drawString(608, 452, 'INTEGRANTES DO GRUPO (1ESPW)')
    c.setStrokeColor(colors.HexColor('#334155'))
    c.line(608, 440, 894, 440)

    members = [
        ('Gustavo Rezende Louro', 'RM 570708', 'Arquitetura de Software & Requisitos'),
        ('João Pedro Lagonegro Bosco e Silva', 'RM 569444', 'Modelagem UML & Regras de Negócio'),
        ('João Pedro Maschion da Cruz Sá', 'RM 570509', 'Total Experience (TX), UI & Protótipo'),
        ('Lucas Henrique Alves da Silva', 'RM 572216', 'Heurísticas de Usabilidade & Roadmap'),
    ]
    my = 382
    for nome, rm, papel in members:
        c.setFillColor(colors.HexColor('#0f172a'))
        c.setStrokeColor(colors.HexColor('#475569'))
        c.roundRect(604, my, 294, 48, 8, stroke=1, fill=1)
        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 10)
        c.drawString(618, my + 30, nome)
        c.setFillColor(colors.HexColor('#38bdf8'))
        c.setFont('Helvetica-Bold', 9.5)
        c.drawRightString(886, my + 30, rm)
        c.setFillColor(colors.HexColor('#94a3b8'))
        c.setFont('Helvetica', 8.5)
        c.drawString(618, my + 12, papel)
        my -= 60

    # Summary of 7 deliverables inside right column bottom
    c.setFillColor(colors.HexColor('#0f172a'))
    c.setStrokeColor(colors.HexColor('#334155'))
    c.roundRect(604, 76, 294, 110, 8, stroke=1, fill=1)
    c.setFillColor(colors.HexColor('#fbbf24'))
    c.setFont('Helvetica-Bold', 9)
    c.drawString(618, 168, 'ESTRUTURA DESTA APRESENTAÇÃO (100 PTS)')
    c.setFillColor(colors.HexColor('#cbd5e1'))
    c.setFont('Helvetica', 8.2)
    c.drawString(618, 151, '1. Capa e Ficha da CitizenTech (5 pts)')
    c.drawString(618, 137, '2. Problema Real, Afetados e Dados SP156 (10 pts)')
    c.drawString(618, 123, '3. Escopo da Solução: Dentro vs. Fora (10 pts)')
    c.drawString(618, 109, '4. Requisitos (RF, RNF) e Regras (RN) Justificados (20 pts)')
    c.drawString(618, 95, '5. Diagrama UML de Casos de Uso e Atores (15 pts)')
    c.drawString(618, 81, '6. Protótipo, Heurísticas e Tom (25 pts) + 7. Roadmap (15 pts)')

    c.showPage()

    # =========================================================================
    # SLIDE 2: DESCRIÇÃO DO PROBLEMA (10 PONTOS)
    # =========================================================================
    draw_slide_chrome(
        c, 2, total_slides,
        'Entregável 2 · Descrição do Problema (10 pts)',
        'O Problema Real nas Ruas de São Paulo e a Falha dos Canais Atuais',
        'O que acontece no território, quem são os cidadãos afetados e por que o modelo atual gera lentidão e retrabalho'
    )

    # Card 1: O Que Acontece nas Ruas (Esquerda)
    draw_card(c, 36, 170, 282, 258, bg=C_SLATE_CARD, border=C_BLUE_BORDER)
    c.setFillColor(C_BLUE_DARK)
    c.roundRect(36, 396, 282, 32, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 10.5)
    c.drawString(50, 408, '1. O QUE ACONTECE NO TERRITÓRIO')
    draw_paragraph(
        c,
        'No trajeto diário pelos bairros de <b>Jabaquara, Vila Mariana, Saúde, Bela Vista, Mooca e Vila Mascote</b>, '
        'quatro problemas graves de zeladoria ameaçam a segurança nas calçadas e vias:<br/><br/>'
        '• <b>Fiação elétrica e cabos rompidos:</b> galhos e caminhões rompem fios que ficam energizados no passeio;<br/>'
        '• <b>Bueiros abertos sem tampa:</b> furto ou quebra de grelhas criando armadilhas na rua e calçada;<br/>'
        '• <b>Descarte irregular de entulho:</b> restos de obra obstruindo a passagem de pedestres;<br/>'
        '• <b>Carros abandonados:</b> carcaças enferrujadas acumulando água parada (dengue) e bloqueando a via.',
        48, 384, 258, size=8.8, leading=12.6
    )

    # Card 2: Quem é Afetado (Centro)
    draw_card(c, 338, 170, 284, 258, bg=C_SLATE_CARD, border=C_EMERALD_BORDER)
    c.setFillColor(C_EMERALD_DARK)
    c.roundRect(338, 396, 284, 32, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 10.5)
    c.drawString(352, 408, '2. QUEM É AFETADO DIRETAMENTE')
    draw_paragraph(
        c,
        '• <b>Pedestres, Idosos e Pessoas com Deficiência (PcD):</b> cadeirantes, deficientes visuais e idosos são '
        'forçados a caminhar no meio do asfalto quando a calçada está bloqueada por entulho, fios caídos ou bueiro sem tampa.<br/><br/>'
        '• <b>Moradores e Comerciantes Locais:</b> sofrem com quedas de energia, risco de choque elétrico na porta de casa '
        'e degradação da rua por veículos abandonados há meses.<br/><br/>'
        '• <b>Equipes das Subprefeituras:</b> operadores de triagem sobrecarregados que não conseguem distinguir um '
        'chamado simples de estética urbana de uma emergência real com risco de morte.',
        350, 384, 260, size=8.8, leading=12.6
    )

    # Card 3: Por que o SP 156 falha hoje (Direita)
    draw_card(c, 642, 170, 282, 258, bg=C_RED_LIGHT, border=C_RED_BORDER)
    c.setFillColor(C_RED_DARK)
    c.roundRect(642, 396, 282, 32, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 10.5)
    c.drawString(656, 408, '3. GARGALOS DO CANAL ATUAL (SP 156)')
    draw_paragraph(
        c,
        '• <b>Alta Fricção no Relato (5 a 8 min):</b> o portal/app SP 156 exige login gov.br/CPF, navegação em dezenas '
        'de subcategorias técnicas e preenchimento manual completo enquanto o cidadão está na rua.<br/><br/>'
        '• <b>Explosão de Chamados Duplicados:</b> quando um fio cai no Jabaquara, 20 vizinhos abrem 20 protocolos '
        'diferentes. O sistema não agrupa demandas vizinhas, gerando fila fantasma.<br/><br/>'
        '• <b>Opacidade ("Caixa-Preta"):</b> quem relata recebe apenas um número frio de protocolo e não sabe se a '
        'subprefeitura já vistoriou ou despachou equipe.',
        654, 384, 258, size=8.8, leading=12.6
    )

    # Bottom Evidence Banner
    draw_card(c, 36, 48, 888, 106, bg=C_BLUE_LIGHT, border=C_BLUE_BORDER)
    c.setFillColor(C_BLUE_DARK)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(52, 134, 'DADOS E EVIDÊNCIAS QUE FUNDAMENTAM A RELEVÂNCIA DO PROBLEMA EM SÃO PAULO')
    draw_paragraph(
        c,
        '<b>1) Volume Crítico de Zeladoria:</b> Os canais municipais de São Paulo recebem mais de <b>450 mil solicitações anuais</b> ligadas a '
        'poda/queda de árvores, buracos, bueiros e limpeza urbana (Dados Abertos SP156), com picos de crescimento superior a <b>300% em dias de temporal</b>.<br/>'
        '<b>2) Modelagem Matemática da Equipe (DPS):</b> Nossa simulação comprovou que sem deduplicação colaborativa, o acúmulo líquido de chamados '
        'ultrapassa a capacidade de despacho das subprefeituras em menos de 6 horas de chuva, tornando indispensável a triagem por severidade (GPCT).',
        52, 122, 856, size=8.8, leading=13.0
    )

    c.showPage()

    # =========================================================================
    # SLIDE 3: ESCOPO DA SOLUÇÃO (10 PONTOS)
    # =========================================================================
    draw_slide_chrome(
        c, 3, total_slides,
        'Entregável 3 · Escopo da Solução (10 pts)',
        'Escopo da CitizenTech ZelaSP: O Que Fazemos vs. Limites do Projeto',
        'Definição clara das funcionalidades contempladas no MVP e do que fica explicitamente fora do escopo'
    )

    # Top Value Proposition Banner
    draw_card(c, 36, 366, 888, 64, bg=C_BLUE_LIGHT, border=C_BLUE_BORDER)
    draw_paragraph(
        c,
        '<b>Objetivo Central e Necessidades Atendidas:</b> Conectar moradores e Subprefeituras de São Paulo por meio de uma '
        'interface web leve que reduz o tempo de relato na rua para <b>menos de 15 segundos</b>, transforma relatos repetidos '
        'em <b>apoio comunitário (+1)</b> no mesmo chamado e fornece à Prefeitura um painel de priorização baseado em risco à vida.',
        52, 418, 856, size=9.4, leading=13.8
    )

    # Left Column: DENTRO DO ESCOPO
    draw_card(c, 36, 48, 434, 304, bg=C_EMERALD_LIGHT, border=C_EMERALD_BORDER)
    c.setFillColor(C_EMERALD_DARK)
    c.roundRect(36, 318, 434, 34, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(52, 330, '✓ O QUE ESTÁ DENTRO DO ESCOPO (CONTEMPLADO)')

    in_scope_text = (
        '<b>1. Abertura Educativa e Acesso por Perfil:</b><br/>'
        'Animação sequencial explicando os 4 problemas urbanos e seleção de visão entre <b>Cidadão</b> e <b>Prefeitura</b>.<br/><br/>'
        '<b>2. Relato Cidadão em &lt;15s (ViaCEP + GPS):</b><br/>'
        'Preenchimento automático de rua e bairro ao digitar os 8 dígitos do CEP (API ViaCEP), captura de coordenadas GPS e anexo de foto.<br/><br/>'
        '<b>3. Deduplicação por Apoio Comunitário (+1):</b><br/>'
        'Botão <i>"Apoiar"</i> nos chamados abertos da vizinhança, somando peso comunitário via requisição <code>PUT</code> sem duplicar protocolo.<br/><br/>'
        '<b>4. Motor Automático de Prioridade (Nível 1 a 5):</b><br/>'
        'Cálculo instantâneo de urgência cruzando categoria, flag de risco elétrico (fiação soltando faísca) e número de apoios.<br/><br/>'
        '<b>5. Painel da Prefeitura com Índice GPCT e CRUD:</b><br/>'
        'Monitoramento territorial por bairro, atualização de status/parecer técnico (<code>EM_VISTORIA</code>, <code>EM_EXECUCAO</code>, <code>RESOLVIDO</code>) e exclusão segura.'
    )
    draw_paragraph(c, in_scope_text, 50, 306, 406, size=8.6, leading=12.0)

    # Right Column: FORA DO ESCOPO
    draw_card(c, 490, 48, 434, 304, bg=C_RED_LIGHT, border=C_RED_BORDER)
    c.setFillColor(C_RED_DARK)
    c.roundRect(490, 318, 434, 34, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(506, 330, '✕ O QUE FICA FORA DO ESCOPO (NÃO CONTEMPLADO)')

    out_scope_text = (
        '<b>1. Execução Física de Obras ou Manutenção de Campo:</b><br/>'
        'O ZelaSP é uma plataforma de triagem e inteligência cívica; <b>não</b> possui caminhões próprios, não realiza poda física nem tapa buracos.<br/><br/>'
        '<b>2. Substituição da Concessionária Elétrica ou Bombeiros (193):</b><br/>'
        'Não opera a rede elétrica da Enel nem substitui o resgate de emergência do Corpo de Bombeiros/SAMU (inclusive orienta ligar 193 em risco ativo).<br/><br/>'
        '<b>3. Aplicação de Multas de Trânsito ou Guincho Policial:</b><br/>'
        'No caso de carros abandonados ou descarte irregular, o sistema notifica a zeladoria municipal, mas não emite autuações da CET/GCM.<br/><br/>'
        '<b>4. Coleta de Dados Sensíveis ou Financeiros (LGPD):</b><br/>'
        'Não exige CPF, RG, biometria ou pagamento de taxas pelo morador, eliminando barreiras burocráticas de entrada.<br/><br/>'
        '<b>5. Atendimento Fora do Escopo de Zeladoria Urbana:</b><br/>'
        'Não processa ocorrências policiais (190), consultas médicas ou solicitações de impostos municipais (IPTU).'
    )
    draw_paragraph(c, out_scope_text, 504, 306, 406, size=8.6, leading=12.0)

    c.showPage()

    # =========================================================================
    # SLIDE 4: REQUISITOS FUNCIONAIS (RF01 A RF06) — JUSTIFICADOS (20 PTS - PARTE A)
    # =========================================================================
    draw_slide_chrome(
        c, 4, total_slides,
        'Entregável 4 · Requisitos e Regras de Negócio (20 pts · Parte 1/2)',
        'Requisitos Funcionais (RF): Descrição, Classificação e Justificativa',
        'Cada RF define uma ação concreta que o sistema deve executar, justificada pela dor real do usuário e pelo escopo'
    )

    style_th = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=8.5, leading=10.5, textColor=colors.white)
    style_td_code = ParagraphStyle('tdc', fontName='Helvetica-Bold', fontSize=8.2, leading=10.5, textColor=C_BLUE_DARK)
    style_td = ParagraphStyle('td', fontName='Helvetica', fontSize=8.0, leading=10.6, textColor=C_TEXT_MAIN)

    rf_data = [
        [
            Paragraph('Código / Classificação', style_th),
            Paragraph('Descrição do Requisito Funcional (O que o sistema faz)', style_th),
            Paragraph('Por que pertence a RF e Justificativa de Negócio / Usuário', style_th),
        ],
        [
            Paragraph('<b>RF01</b><br/>Requisito Funcional', style_td_code),
            Paragraph('Permitir ao cidadão registrar uma ocorrência informando CEP, categoria (fio, bueiro, entulho, carro ou buraco), descrição, flag de risco elétrico e foto.', style_td),
            Paragraph('<b>Classificação:</b> Define uma funcionalidade direta de entrada de dados pelo usuário.<br/><b>Justificativa:</b> Substitui o formulário burocrático do SP 156 por um fluxo enxuto focado nos 4 problemas reais observados nos bairros.', style_td),
        ],
        [
            Paragraph('<b>RF02</b><br/>Requisito Funcional', style_td_code),
            Paragraph('Consultar automaticamente a API pública ViaCEP ao digitar 8 dígitos de CEP e preencher logradouro e bairro no formulário (com opção de coordenadas via GPS).', style_td),
            Paragraph('<b>Classificação:</b> Comportamento funcional de integração e autopreenchimento.<br/><b>Justificativa:</b> Na rua e sob estresse, o cidadão muitas vezes não sabe o nome exato da via ou CEP completo; evita erros de digitação.', style_td),
        ],
        [
            Paragraph('<b>RF03</b><br/>Requisito Funcional', style_td_code),
            Paragraph('Permitir que moradores sumam apoio comunitário (<b>Apoiar +1</b> via <code>PUT</code>) a um chamado já existente no bairro em vez de abrir um protocolo repetido.', style_td),
            Paragraph('<b>Classificação:</b> Ação interativa do sistema acionada pelo ator Cidadão.<br/><b>Justificativa:</b> Ataca diretamente a raiz da duplicidade de chamados em dias de chuva, transformando ruído em termômetro de impacto social.', style_td),
        ],
        [
            Paragraph('<b>RF04</b><br/>Requisito Funcional', style_td_code),
            Paragraph('Filtrar, buscar textualmente e ordenar a fila de ocorrências por bairro, status operacional e nível de severidade (priorizando Nível 5 no topo).', style_td),
            Paragraph('<b>Classificação:</b> Função de consulta, processamento e exibição de dados.<br/><b>Justificativa:</b> Permite que o morador encontre rapidamente chamados da sua rua e que a Subprefeitura enxergue primeiro as emergências.', style_td),
        ],
        [
            Paragraph('<b>RF05</b><br/>Requisito Funcional', style_td_code),
            Paragraph('Disponibilizar no Painel da Prefeitura o cálculo em tempo real do índice territorial <b>GPCT</b> (Estável, Atenção Operacional ou Contingência Ativada).', style_td),
            Paragraph('<b>Classificação:</b> Funcionalidade analítica de apoio à decisão para o gestor público.<br/><b>Justificativa:</b> Traduz o modelo matemático de saturação em um alerta visual imediato quando um bairro acumula ocorrências críticas.', style_td),
        ],
        [
            Paragraph('<b>RF06</b><br/>Requisito Funcional', style_td_code),
            Paragraph('Permitir ao operador da Prefeitura atualizar o status do chamado (<code>EM_VISTORIA</code>, <code>EM_EXECUCAO</code>, <code>RESOLVIDO</code>) com nota técnica e excluir registros inválidos.', style_td),
            Paragraph('<b>Classificação:</b> Operações administrativas de atualização (<code>PUT</code>) e remoção (<code>DELETE</code>).<br/><b>Justificativa:</b> Fecha o ciclo de transparência para o cidadão acompanhar o reparo e mantém a fila pública limpa de trotes.', style_td),
        ],
    ]

    t_rf = Table(rf_data, colWidths=[105, 365, 418])
    t_rf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_BLUE_DARK),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, C_BLUE_LIGHT]),
        ('GRID', (0, 0), (-1, -1), 0.6, C_SLATE_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    tw, th = t_rf.wrap(888, 400)
    t_rf.drawOn(c, 36, PAGE_H - 108 - th)

    c.showPage()

    # =========================================================================
    # SLIDE 5: RNF E REGRAS DE NEGÓCIO (RN) — JUSTIFICADOS (20 PTS - PARTE B)
    # =========================================================================
    draw_slide_chrome(
        c, 5, total_slides,
        'Entregável 4 · Requisitos e Regras de Negócio (20 pts · Parte 2/2)',
        'Requisitos Não Funcionais (RNF) e Regras de Negócio (RN) Justificados',
        'Condições de qualidade/desempenho da interface (RNF) e restrições obrigatórias do processo de zeladoria (RN)'
    )

    style_td_rnf = ParagraphStyle('tdrnf', fontName='Helvetica-Bold', fontSize=7.8, leading=10.0, textColor=C_EMERALD_DARK)
    style_td_rn = ParagraphStyle('tdrn', fontName='Helvetica-Bold', fontSize=7.8, leading=10.0, textColor=C_AMBER_DARK)
    style_td_sm = ParagraphStyle('tdsm', fontName='Helvetica', fontSize=7.6, leading=9.8, textColor=C_TEXT_MAIN)

    rnf_rn_data = [
        [
            Paragraph('Código / Tipo', style_th),
            Paragraph('Descrição do Item', style_th),
            Paragraph('Por que pertence à categoria e Justificativa no Projeto', style_th),
        ],
        [
            Paragraph('<b>RNF01</b><br/>Não Funcional<br/>(Usabilidade)', style_td_rnf),
            Paragraph('O cadastro completo de uma ocorrência pelo cidadão deve exigir no máximo 4 interações e ser concluído em até 15 segundos.', style_td_sm),
            Paragraph('<b>Por que é RNF:</b> Define meta de tempo e qualidade de uso, não uma função isolada.<br/><b>Justificativa:</b> Garante que o morador consiga relatar caminhando na rua sem desistir no meio.', style_td_sm),
        ],
        [
            Paragraph('<b>RNF02</b><br/>Não Funcional<br/>(Acessibilidade)', style_td_rnf),
            Paragraph('Adotar paleta clara de alto contraste (WCAG AA), suporte a <code>prefers-reduced-motion</code> e layout responsivo <i>Mobile-First</i>.', style_td_sm),
            Paragraph('<b>Por que é RNF:</b> Restrição visual e ergonômica da interface.<br/><b>Justificativa:</b> O app é usado no celular sob luz solar forte nas calçadas de SP por cidadãos de todas as idades.', style_td_sm),
        ],
        [
            Paragraph('<b>RNF03</b><br/>Não Funcional<br/>(Resiliência)', style_td_rnf),
            Paragraph('Sincronizar dados com API REST em nuvem (MockAPI) mantendo fallback automático em <code>localStorage</code> em caso de oscilação de rede.', style_td_sm),
            Paragraph('<b>Por que é RNF:</b> Critério de disponibilidade e tolerância a falhas.<br/><b>Justificativa:</b> Durante tempestades em SP, o sinal móvel oscila; o cidadão não pode perder o relato.', style_td_sm),
        ],
        [
            Paragraph('<b>RNF04</b><br/>Não Funcional<br/>(Desempenho)', style_td_rnf),
            Paragraph('O carregamento inicial da lista e o retorno da consulta de CEP (ViaCEP) devem responder em menos de 2 segundos.', style_td_sm),
            Paragraph('<b>Por que é RNF:</b> Métrica de tempo de resposta do sistema.<br/><b>Justificativa:</b> Evita que o usuário digite o endereço manualmente por lentidão no autopreenchimento.', style_td_sm),
        ],
        [
            Paragraph('<b>RN01</b><br/>Regra de Negócio<br/>(Segurança)', style_td_rn),
            Paragraph('Chamados de <i>Fios Rompidos</i> com risco elétrico ativo ou <i>Tampa de Bueiro Furtada</i> recebem obrigatoriamente <b>Prioridade Máxima (Nível 5)</b>.', style_td_sm),
            Paragraph('<b>Por que é RN:</b> Regra de domínio que governa a pontuação de risco.<br/><b>Justificativa:</b> Risco iminente de eletrocussão ou queda grave exige atendimento antes de demandas estéticas.', style_td_sm),
        ],
        [
            Paragraph('<b>RN02</b><br/>Regra de Negócio<br/>(Escalonamento)', style_td_rn),
            Paragraph('Quando um chamado atinge <b>10 ou mais apoios comunitários</b>, seu nível de prioridade sobe automaticamente em +1 ponto (até o teto 5).', style_td_sm),
            Paragraph('<b>Por que é RN:</b> Condição matemática de reclassificação do processo.<br/><b>Justificativa:</b> Recompensa o uso do botão <i>Apoiar (+1)</i> e dá voz coletiva a problemas que afetam muita gente.', style_td_sm),
        ],
        [
            Paragraph('<b>RN03</b><br/>Regra de Negócio<br/>(Contingência)', style_td_rn),
            Paragraph('O índice <b>GPCT</b> muda para <i>Atenção Operacional</i> com ≥2 chamados críticos abertos (Nível ≥4) e para <i>Contingência Ativada</i> com ≥4.', style_td_sm),
            Paragraph('<b>Por que é RN:</b> Gatilho operacional fundamentado no cálculo de DPS.<br/><b>Justificativa:</b> Alerta a Subprefeitura antes que a fila do bairro entre em colapso durante chuvas intensas.', style_td_sm),
        ],
        [
            Paragraph('<b>RN04</b><br/>Regra de Negócio<br/>(Governança)', style_td_rn),
            Paragraph('Apenas o perfil <b>Prefeitura</b> pode alterar status de vistoria ou excluir registros (exigindo confirmação dupla), sendo vedado ao perfil Cidadão.', style_td_sm),
            Paragraph('<b>Por que é RN:</b> Política de alçada e permissão entre atores.<br/><b>Justificativa:</b> Impede que terceiros encerrem ou apaguem chamados reais abertos pela vizinhança.', style_td_sm),
        ],
    ]

    t_rn = Table(rnf_rn_data, colWidths=[105, 360, 423])
    t_rn.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, 4), [colors.white, C_EMERALD_LIGHT]),
        ('ROWBACKGROUNDS', (0, 5), (-1, -1), [colors.white, C_AMBER_LIGHT]),
        ('GRID', (0, 0), (-1, -1), 0.6, C_SLATE_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    tw, th = t_rn.wrap(888, 420)
    t_rn.drawOn(c, 36, PAGE_H - 104 - th)

    c.showPage()

    # =========================================================================
    # SLIDE 6: DIAGRAMA DE CASO DE USO (15 PTS - PARTE A: DIAGRAMA VISUAL)
    # =========================================================================
    draw_slide_chrome(
        c, 6, total_slides,
        'Entregável 5 · Diagrama de Caso de Uso (15 pts · Parte 1/2)',
        'Diagrama UML de Casos de Uso — Interações e Fronteira do Sistema',
        'Representação dos 4 atores (humanos e sistemas externos), 10 casos de uso e relações «include» e «extend»'
    )

    uml_img = os.path.join(ASSETS_DIR, 'diagrama_casos_de_uso.png')
    draw_card(c, 36, 42, 888, 392, bg=colors.white, border=C_BLUE_BORDER)
    if os.path.exists(uml_img):
        c.drawImage(uml_img, 44, 46, width=872, height=384, preserveAspectRatio=True, mask='auto')

    c.showPage()

    # =========================================================================
    # SLIDE 7: CONTEXTUALIZAÇÃO DOS ATORES E CASOS DE USO (15 PTS - PARTE B)
    # =========================================================================
    draw_slide_chrome(
        c, 7, total_slides,
        'Entregável 5 · Diagrama de Caso de Uso (15 pts · Parte 2/2)',
        'Contextualização dos Atores, Objetivos e Rastreabilidade com os RFs',
        'Explicação detalhada de quem interage com a solução, o que cada ator faz e qual objetivo pretende alcançar'
    )

    atores_data = [
        [
            Paragraph('Ator UML', style_th),
            Paragraph('Quem é e Papel no Ecossistema', style_th),
            Paragraph('O que faz no ZelaSP (Casos de Uso)', style_th),
            Paragraph('Objetivo que Pretende Alcançar + RFs', style_th),
        ],
        [
            Paragraph('<b>1. Cidadão</b><br/>(Ator Primário Humano)', style_td_code),
            Paragraph('Morador, pedestre, idoso ou comerciante que circula pelos bairros de São Paulo e identifica o problema na rua.', style_td),
            Paragraph('Executa <b>UC01</b> (Relatar Ocorrência), aciona <b>UC03</b> (GPS opcional), consulta a lista do bairro (<b>UC04</b>) e soma apoio em chamados abertos por vizinhos (<b>UC05</b>).', style_td),
            Paragraph('<b>Objetivo:</b> Resolver o risco na sua calçada em &lt;15s sem burocracia e acompanhar o reparo.<br/><b>RFs atendidos:</b> RF01, RF02, RF03, RF04.', style_td),
        ],
        [
            Paragraph('<b>2. Agente Municipal</b><br/>(Ator Primário Humano)', style_td_rnf),
            Paragraph('Operador técnico ou coordenador de zeladoria da Subprefeitura responsável por triar e despachar equipes.', style_td),
            Paragraph('Consulta e filtra a fila (<b>UC04</b>), monitora o índice <b>GPCT</b> (<b>UC07</b>), atualiza status/nota de vistoria (<b>UC08</b>) e exclui registros inválidos (<b>UC09</b>).', style_td),
            Paragraph('<b>Objetivo:</b> Priorizar chamados Nível 5 (risco à vida), eliminar duplicidades e agir antes do colapso.<br/><b>RFs atendidos:</b> RF04, RF05, RF06.', style_td),
        ],
        [
            Paragraph('<b>3. API ViaCEP</b><br/>(Ator Secundário Externo)', style_td_code),
            Paragraph('Serviço web público gratuito de consulta de endereçamento postal brasileiro.', style_td),
            Paragraph('É acionado obrigatoriamente via <code>«include»</code> no <b>UC02</b> sempre que o cidadão digita 8 números no campo CEP durante o relato (<b>UC01</b>).', style_td),
            Paragraph('<b>Objetivo:</b> Preencher logradouro e bairro sem erro de digitação humana.<br/><b>RFs atendidos:</b> RF02 (e RNF01/RNF04).', style_td),
        ],
        [
            Paragraph('<b>4. Nó IoT ESP32</b><br/>(Ator Secundário de Borda)', style_td_rn),
            Paragraph('Módulo embarcado instalado em postes críticos com sensores de inclinação, corrente e alagamento.', style_td),
            Paragraph('Executa autonomamente o <b>UC10</b> (Emitir Alerta Crítico de Borda), que inclui o cálculo de prioridade máxima (<b>UC06</b>) na fila da Subprefeitura.', style_td),
            Paragraph('<b>Objetivo:</b> Detectar queda de árvore/fio em tempo zero mesmo sem ação humana.<br/><b>RFs atendidos:</b> RF01, RF05 (e RN01).', style_td),
        ],
    ]

    t_at = Table(atores_data, colWidths=[125, 225, 275, 263])
    t_at.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_BLUE_DARK),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, C_BLUE_LIGHT]),
        ('GRID', (0, 0), (-1, -1), 0.6, C_SLATE_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    tw, th = t_at.wrap(888, 300)
    t_at.drawOn(c, 36, PAGE_H - 108 - th)

    # Bottom synthesis box explaining <<include>> and <<extend>>
    draw_card(c, 36, 44, 888, 92, bg=C_EMERALD_LIGHT, border=C_EMERALD_BORDER)
    c.setFillColor(C_EMERALD_DARK)
    c.setFont('Helvetica-Bold', 9.5)
    c.drawString(52, 118, 'COERÊNCIA DAS RELAÇÕES UML («INCLUDE» E «EXTEND») COM OS REQUISITOS DO PROJETO')
    draw_paragraph(
        c,
        '• <b>Relações «include» (Obrigatórias):</b> Sempre que o Cidadão relata uma ocorrência (<b>UC01</b>) ou apoia um chamado existente (<b>UC05</b>), '
        'o sistema executa obrigatoriamente o <b>UC06 (Calcular Prioridade de Risco 1 a 5)</b> para manter a fila ordenada em tempo real. '
        'Da mesma forma, informar um CEP válido inclui a busca automática no ViaCEP (<b>UC02</b>).<br/>'
        '• <b>Relação «extend» (Opcional/Condicional):</b> O <b>UC03 (Capturar Coordenadas GPS)</b> estende o relato (<b>UC01</b>) caso o cidadão clique em <i>"Usar meu GPS"</i>.',
        52, 106, 856, size=8.5, leading=12.4
    )

    c.showPage()

    # =========================================================================
    # SLIDE 8: PROTÓTIPO DE MÉDIA FIDELIDADE E FLUXO (25 PTS - PARTE A)
    # =========================================================================
    draw_slide_chrome(
        c, 8, total_slides,
        'Entregável 6 · Protótipo e Heurísticas (25 pts · Parte 1/2)',
        'Protótipo de Média Fidelidade e Fluxo de Navegação da Pessoa Usuária',
        'Representação das 4 telas principais, funcionalidades prioritárias e conexão entre a visão Cidadão e Prefeitura'
    )

    proto_img = os.path.join(ASSETS_DIR, 'prototipo_media_fidelidade.png')
    draw_card(c, 36, 84, 888, 350, bg=colors.white, border=C_BLUE_BORDER)
    if os.path.exists(proto_img):
        c.drawImage(proto_img, 44, 88, width=872, height=342, preserveAspectRatio=True, mask='auto')

    # Bottom Live Link Bar
    draw_card(c, 36, 38, 888, 38, bg=C_BLUE_LIGHT, border=C_BLUE_BORDER)
    c.setFillColor(C_BLUE_DARK)
    c.setFont('Helvetica-Bold', 9.2)
    c.drawString(52, 53, 'PROTÓTIPO NAVEGÁVEL NO AR (VERCEL): https://zelasp-web.vercel.app/   |   Fluxo completo Cidadão <-> Prefeitura compartilhando a mesma base MockAPI')

    c.showPage()

    # =========================================================================
    # SLIDE 9: HEURÍSTICAS DE NIELSEN E TOM DE VOZ (25 PTS - PARTE B)
    # =========================================================================
    draw_slide_chrome(
        c, 9, total_slides,
        'Entregável 6 · Protótipo e Heurísticas (25 pts · Parte 2/2)',
        'Heurísticas de Usabilidade Aplicadas nas Telas e Tom de Voz da Interface',
        'Onde cada heurística facilita o uso na prática e exemplos reais de microcopy (botões, instruções e avisos)'
    )

    # Left Column: Heuristicas de Nielsen
    draw_card(c, 36, 44, 436, 388, bg=C_SLATE_CARD, border=C_BLUE_BORDER)
    c.setFillColor(C_BLUE_DARK)
    c.roundRect(36, 400, 436, 32, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 10.5)
    c.drawString(50, 412, 'HEURÍSTICAS DE NIELSEN (ONDE APARECEM NAS TELAS)')

    heur_text = (
        '<b>1. Visibilidade do Status do Sistema (H1):</b><br/>'
        '• <i>Onde aparece:</i> Selo verde <code>MockAPI Conectada</code> no topo, indicador <code>Buscando endereço...</code> no CEP, '
        'etiquetas coloridas (<code>ABERTO</code>, <code>EM_VISTORIA</code>, <code>EM_EXECUCAO</code>, <code>RESOLVIDO</code>) e avisos <i>Toast</i>.<br/><br/>'
        '<b>2. Correspondência com o Mundo Real (H2):</b><br/>'
        '• <i>Onde aparece:</i> Na abertura ilustrada (fio, bueiro, entulho e carro) e nos nomes populares das categorias em vez de códigos técnicos de engenharia.<br/><br/>'
        '<b>3. Controle e Liberdade do Usuário (H3):</b><br/>'
        '• <i>Onde aparece:</i> Botão <code>Pular</code> na animação de abertura, botão <code>Limpar filtros</code> na busca e troca rápida entre visão Cidadão e Prefeitura.<br/><br/>'
        '<b>4. Prevenção de Erros e Acidentes (H5):</b><br/>'
        '• <i>Onde aparece:</i> Alerta vermelho imediato ao marcar <i>"Fio energizado"</i> e confirmação em <b>2 cliques</b> (<code>Excluir → Confirmar?</code>) antes de apagar um chamado.<br/><br/>'
        '<b>5. Reconhecimento em vez de Memorização (H6) & Minimalismo (H8):</b><br/>'
        '• <i>Onde aparece:</i> Autopreenchimento de rua/bairro por CEP e ocultação de botões administrativos da Prefeitura na tela do Cidadão.'
    )
    draw_paragraph(c, heur_text, 48, 390, 412, size=8.3, leading=11.6)

    # Right Column: Tom de Voz + Exemplos Reais da Interface
    draw_card(c, 488, 44, 436, 388, bg=C_SLATE_CARD, border=C_EMERALD_BORDER)
    c.setFillColor(C_EMERALD_DARK)
    c.roundRect(488, 400, 436, 32, 8, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 10.5)
    c.drawString(502, 412, 'TOM DE VOZ E EXEMPLOS REAIS DOS TEXTOS DA UI')

    tom_intro = (
        '<b>Escolha do Tom de Voz:</b> <i>Cívico, humano, direto e preventivo</i>. O cidadão que vê um fio faiscando ou '
        'um bueiro aberto está na calçada e com pressa: evitamos jargões burocráticos ("deferido", "autuação") e usamos verbos de ação claros.'
    )
    draw_paragraph(c, tom_intro, 500, 390, 412, size=8.3, leading=11.5)

    tom_table_data = [
        [
            Paragraph('Elemento da Tela', style_th),
            Paragraph('Texto Real na Interface ZelaSP (Microcopy)', style_th),
        ],
        [
            Paragraph('<b>Subtítulo de Abertura</b>', style_td_rnf),
            Paragraph('<i>"Fio caído, bueiro aberto, entulho na calçada ou carro abandonado: a vizinhança avisa, a prefeitura resolve e todo mundo acompanha."</i>', style_td_sm),
        ],
        [
            Paragraph('<b>Botão de Deduplicação</b>', style_td_rnf),
            Paragraph('<code>Apoiar (14)</code> + Dica: <i>"Viu o mesmo problema na sua rua? Clique em Apoiar para subir a prioridade sem duplicar chamado."</i>', style_td_sm),
        ],
        [
            Paragraph('<b>Alerta de Segurança Elétrica</b>', style_td_rn),
            Paragraph('<i>"Atenção: não se aproxime de cabos caídos. Em risco imediato à vida, acione os Bombeiros (193) ou a Defesa Civil (199)."</i>', style_td_sm),
        ],
        [
            Paragraph('<b>Botões de Ação (CTAs)</b>', style_td_rnf),
            Paragraph('Cidadão: <code>Registrar Ocorrência</code> · <code>Usar meu GPS</code><br/>Prefeitura: <code>Despachar / Status</code> · <code>Confirmar?</code>', style_td_sm),
        ],
        [
            Paragraph('<b>Feedback (Toast)</b>', style_td_rnf),
            Paragraph('<i>"Chamado SP-2026-107 registrado com prioridade Nível 5!"</i><br/><i>"Apoio registrado no protocolo SP-2026-101!"</i>', style_td_sm),
        ],
    ]
    t_tom = Table(tom_table_data, colWidths=[118, 294])
    t_tom.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_EMERALD_DARK),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, C_EMERALD_LIGHT]),
        ('GRID', (0, 0), (-1, -1), 0.5, C_SLATE_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    tw, th = t_tom.wrap(412, 290)
    t_tom.drawOn(c, 500, 336 - th)

    c.showPage()

    # =========================================================================
    # SLIDE 10: ROADMAP — PRÓXIMOS PASSOS DA SOLUÇÃO (15 PONTOS)
    # =========================================================================
    draw_slide_chrome(
        c, 10, total_slides,
        'Entregável 7 · Roadmap: Próximos Passos (15 pts)',
        'Roadmap de Continuidade: Como Desenvolveríamos, Testaríamos e Ampliaríamos',
        'Plano sequencial focado em escuta de moradores afetados, evolução técnica do protótipo, piloto em subprefeitura e métricas'
    )

    road_img = os.path.join(ASSETS_DIR, 'roadmap_evolucao.png')
    draw_card(c, 36, 152, 888, 280, bg=colors.white, border=C_BLUE_BORDER)
    if os.path.exists(road_img):
        c.drawImage(road_img, 44, 156, width=872, height=272, preserveAspectRatio=True, mask='auto')

    # Bottom Impact Metrics Card
    draw_card(c, 36, 42, 888, 98, bg=C_EMERALD_LIGHT, border=C_EMERALD_BORDER)
    c.setFillColor(C_EMERALD_DARK)
    c.setFont('Helvetica-Bold', 9.8)
    c.drawString(52, 122, 'COMO OS RESULTADOS SERÃO AVALIADOS EM CADA CICLO DO ROADMAP (INDICADORES DE IMPACTO)')
    draw_paragraph(
        c,
        '• <b>1. Taxa de Sucesso no Relato de Rua (Etapa 1):</b> Percentual de moradores (incluindo idosos) que concluem o envio em menos de 15 segundos nos testes presenciais.<br/>'
        '• <b>2. Taxa de Deduplicação Comunitária (Etapas 2 e 3):</b> Proporção de apoios somados (<code>+1</code>) em relação a novos chamados abertos no mesmo quarteirão (meta: reduzir em &gt;60% os protocolos repetidos).<br/>'
        '• <b>3. Tempo Médio de Despacho Crítico — Nível 5 (Etapas 3 e 4):</b> Redução do tempo entre o relato de fiação energizada/bueiro aberto e a mudança para <code>EM_VISTORIA</code> / <code>EM_EXECUCAO</code>.',
        52, 110, 856, size=8.4, leading=12.2
    )

    c.showPage()
    c.save()
    return OUT_PDF


if __name__ == '__main__':
    pdf_file = build_pdf()
    print('PDF gerado com sucesso em:', pdf_file)
