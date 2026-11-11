# -*- coding: utf-8 -*-
"""
Gera os diagramas visuais de alta resolucao para a entrega de
05 - Software & Total Experience Design (ZelaSP - GS 2026.2):
1. diagrama_casos_de_uso.png (Diagrama UML de Casos de Uso)
2. prototipo_media_fidelidade.png (Fluxo de Telas + Heuristicas de Nielsen)
3. roadmap_evolucao.png (Roadmap visual em 4 etapas)
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse

OUT_DIR = os.path.join(os.path.dirname(__file__), 'assets')
os.makedirs(OUT_DIR, exist_ok=True)


def draw_stick_figure(ax, x, y, label, sublabel, color='#1e40af'):
    # Head
    head = Circle((x, y + 0.42), 0.16, facecolor='#eff6ff', edgecolor=color, linewidth=2.2, zorder=5)
    ax.add_patch(head)
    # Body
    ax.plot([x, x], [y + 0.26, y - 0.12], color=color, linewidth=2.2, zorder=5)
    # Arms
    ax.plot([x - 0.22, x + 0.22], [y + 0.14, y + 0.14], color=color, linewidth=2.2, zorder=5)
    # Legs
    ax.plot([x, x - 0.18], [y - 0.12, y - 0.42], color=color, linewidth=2.2, zorder=5)
    ax.plot([x, x + 0.18], [y - 0.12, y - 0.42], color=color, linewidth=2.2, zorder=5)
    # Labels
    ax.text(x, y - 0.62, label, ha='center', va='top', fontsize=10.5, fontweight='bold', color='#0f172a')
    if sublabel:
        ax.text(x, y - 0.88, sublabel, ha='center', va='top', fontsize=8.5, color='#475569')


def gerar_diagrama_casos_de_uso():
    fig, ax = plt.subplots(figsize=(14, 8.2), dpi=220)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.2)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

    # Title banner
    ax.text(
        7.0, 7.82,
        'DIAGRAMA UML DE CASOS DE USO — PLATAFORMA ZELASP',
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a'
    )
    ax.text(
        7.0, 7.48,
        'Interações entre Atores Humanos, Serviços Externos e Módulos do Sistema CitizenTech',
        ha='center', va='center', fontsize=9.5, color='#475569'
    )

    # System Boundary Box
    boundary = FancyBboxPatch(
        (2.85, 0.55), 8.3, 6.55,
        boxstyle='round,pad=0.12,rounding_size=0.22',
        facecolor='#ffffff', edgecolor='#1e40af', linewidth=2.2, zorder=1
    )
    ax.add_patch(boundary)
    ax.text(
        7.0, 6.82,
        '«system»  Plataforma ZelaSP (Web App + Motor de Triagem Territorial)',
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1e40af',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#eff6ff', edgecolor='#bfdbfe', lw=1)
    )

    # Actors Left
    draw_stick_figure(ax, 1.25, 5.2, 'Cidadão', '(Morador / Pedestre SP)', color='#1d4ed8')
    draw_stick_figure(ax, 1.25, 2.0, 'Agente Municipal', '(Operador Subprefeitura)', color='#047857')

    # Actors Right (External Systems)
    draw_stick_figure(ax, 12.75, 5.3, 'API ViaCEP', '«sistema externo»', color='#7c3aed')
    draw_stick_figure(ax, 12.75, 2.1, 'Nó IoT ESP32', '«sensor de borda»', color='#d97706')

    # Use Cases inside boundary: (id, x, y, w, h, title, fill, edge)
    ucs = {
        'UC01': (4.9, 5.85, 3.1, 0.72, 'UC01: Relatar Ocorrência\nem <15 Segundos', '#eff6ff', '#2563eb'),
        'UC02': (9.2, 6.00, 2.9, 0.68, 'UC02: Autopreencher Rua\ne Bairro por CEP', '#f5f3ff', '#7c3aed'),
        'UC03': (9.2, 4.80, 2.9, 0.68, 'UC03: Capturar Coordenadas\nvia GPS do Navegador', '#eff6ff', '#3b82f6'),
        'UC04': (4.9, 4.65, 3.1, 0.72, 'UC04: Consultar e Filtrar\nChamados do Bairro', '#f8fafc', '#475569'),
        'UC05': (4.9, 3.55, 3.1, 0.72, 'UC05: Apoiar Chamado\nExistente (+1 Apoio)', '#ecfdf5', '#059669'),
        'UC06': (9.2, 3.55, 2.9, 0.72, 'UC06: Calcular Prioridade\nde Risco (Nível 1 a 5)', '#fef3c7', '#d97706'),
        'UC07': (4.9, 2.35, 3.1, 0.72, 'UC07: Monitorar Índice\nTerritorial GPCT', '#ecfdf5', '#047857'),
        'UC08': (4.9, 1.20, 3.1, 0.72, 'UC08: Atualizar Status e\nParecer de Vistoria', '#ecfdf5', '#047857'),
        'UC09': (9.2, 1.20, 2.9, 0.68, 'UC09: Excluir Registro\nInválido (2 Cliques)', '#fef2f2', '#dc2626'),
        'UC10': (9.2, 2.35, 2.9, 0.68, 'UC10: Emitir Alerta Crítico\nde Queda/Fiação (Borda)', '#fffbeb', '#d97706'),
    }

    for code, (cx, cy, w, h, text, fc, ec) in ucs.items():
        el = Ellipse((cx, cy), w, h, facecolor=fc, edgecolor=ec, linewidth=1.7, zorder=3)
        ax.add_patch(el)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=8.3, fontweight='bold', color='#0f172a', zorder=4)

    # Solid association lines (Actor -> Use Case)
    assoc = [
        # Cidadao
        ((1.65, 5.35), (3.35, 5.85), '#1d4ed8'),
        ((1.65, 5.15), (3.35, 4.65), '#1d4ed8'),
        ((1.65, 4.95), (3.35, 3.65), '#1d4ed8'),
        # Agente Municipal
        ((1.65, 2.30), (3.35, 4.45), '#047857'),
        ((1.65, 2.15), (3.35, 2.35), '#047857'),
        ((1.65, 1.95), (3.35, 1.25), '#047857'),
        ((1.65, 1.75), (7.75, 1.15), '#047857'),
        # API ViaCEP
        ((12.35, 5.45), (10.65, 6.00), '#7c3aed'),
        # No IoT ESP32
        ((12.35, 2.25), (10.65, 2.35), '#d97706'),
    ]
    for (x1, y1), (x2, y2), col in assoc:
        ax.plot([x1, x2], [y1, y2], color=col, linewidth=1.4, alpha=0.85, zorder=2)

    # Dashed <<include>> and <<extend>> relationships
    def draw_rel(p1, p2, label, color='#475569'):
        ax.annotate(
            '', xy=p2, xytext=p1,
            arrowprops=dict(arrowstyle='->', linestyle='--', color=color, lw=1.3),
            zorder=4
        )
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        ax.text(
            mx, my + 0.11, label, fontsize=7.5, ha='center', va='center',
            color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.12', facecolor='#ffffff', edgecolor='none', alpha=0.9),
            zorder=5
        )

    draw_rel((6.45, 5.95), (7.75, 6.00), '«include»', '#7c3aed')
    draw_rel((7.75, 4.95), (6.40, 5.65), '«extend»', '#2563eb')
    draw_rel((6.35, 5.60), (7.85, 3.80), '«include»', '#d97706')
    draw_rel((6.45, 3.55), (7.75, 3.55), '«include»', '#059669')
    draw_rel((9.20, 2.69), (9.20, 3.20), '«include»', '#d97706')

    # Legend at bottom
    ax.text(
        7.0, 0.22,
        'Legenda UML:   ─── Associação Direta Ator/Caso de Uso     - - -> «include» Execução Obrigatória     - - -> «extend» Comportamento Opcional/Condicional',
        ha='center', va='center', fontsize=8.5, color='#334155',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='#e2e8f0', edgecolor='#cbd5e1', lw=1)
    )

    plt.tight_layout()
    out_path = os.path.join(OUT_DIR, 'diagrama_casos_de_uso.png')
    plt.savefig(out_path, dpi=220)
    plt.close(fig)
    return out_path


def gerar_prototipo_media_fidelidade():
    fig, ax = plt.subplots(figsize=(14, 7.8), dpi=220)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.8)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

    ax.text(
        7.0, 7.42,
        'PROTÓTIPO DE MÉDIA FIDELIDADE E FLUXO DE NAVEGAÇÃO — ZELASP WEB',
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        7.0, 7.10,
        'Jornada em 4 Telas Conectadas com Identificação das Heurísticas de Usabilidade de Nielsen (H1 a H8)',
        ha='center', va='center', fontsize=9.2, color='#475569'
    )

    screens = [
        {
            'x': 0.45, 'w': 2.95,
            'step': 'TELA 1 • ABERTURA',
            'title': 'SplashScreen Animada',
            'route': 'Entrada do App',
            'accent': '#1e40af',
            'blocks': [
                ('[Animação SVG Sequencial]', '#eff6ff', '#1e40af', '1. Fio Partido -> Religado\n2. Bueiro Aberto -> Tampado\n3. Entulho -> Calçada Limpa\n4. Carro -> Via Liberada\n-> Capa: Rua SP Revitalizada'),
                ('Resumo em 3 Passos', '#f8fafc', '#475569', '• Relate em 15 segundos\n• Apoie, não duplique\n• Acompanhe o reparo'),
                ('[Botão: Começar ->]', '#1e40af', '#ffffff', 'Ação principal + opção "Pular"'),
            ],
            'heuristic': 'H2: Linguagem visual do mundo real\nH3: Controle e liberdade ("Pular")'
        },
        {
            'x': 3.85, 'w': 2.95,
            'step': 'TELA 2 • ACESSO',
            'title': 'Login por Perfil',
            'route': 'Escolha de Visão',
            'accent': '#0f172a',
            'blocks': [
                ('Seletor de Perfil (Radio)', '#eff6ff', '#1d4ed8', '[●] Cidadão (Relatar / Apoiar)\n[○] Prefeitura (Gerenciar fila)'),
                ('Identificação Rápida', '#f8fafc', '#475569', 'Nome / E-mail demonstrativo\nSem exigência de CPF/ burocracia'),
                ('[Entrar como Cidadão ->]', '#1e40af', '#ffffff', 'Redireciona ao painel escolhido'),
            ],
            'heuristic': 'H8: Design minimalista (separa\nfunções de Cidadão e Prefeitura)'
        },
        {
            'x': 7.25, 'w': 2.95,
            'step': 'TELA 3 • VISÃO CIDADÃO',
            'title': 'Relato 15s + Apoio +1',
            'route': 'Modo Morador',
            'accent': '#2563eb',
            'blocks': [
                ('Formulário Enxuto (<15s)', '#eff6ff', '#1d4ed8', '• CEP -> ViaCEP preenche Rua/Bairro\n• Categoria + [Usar meu GPS]\n• [!] Checkbox Fio Energizado'),
                ('Alerta Preventivo 193', '#fef2f2', '#dc2626', 'Se risco elétrico: aviso vermelho\npara manter distância segura'),
                ('Chamados da Vizinhança', '#ecfdf5', '#059669', 'Card SP-2026-101 • Jabaquara\nBotão: [+1 Apoiar (14)] (PUT)'),
            ],
            'heuristic': 'H5: Prevenção de erro/acidente\nH6: Reconhecimento (ViaCEP/GPS)'
        },
        {
            'x': 10.65, 'w': 2.90,
            'step': 'TELA 4 • VISÃO PREFEITURA',
            'title': 'Triagem GPCT + Despacho',
            'route': 'Modo Subprefeitura',
            'accent': '#047857',
            'blocks': [
                ('Painel Territorial GPCT', '#ecfdf5', '#047857', 'Status: CONTINGÊNCIA ATIVADA\nScore por Bairro (Jabaquara, etc.)'),
                ('Fila Ordenada por Risco', '#fffbeb', '#b45309', '1º Nível 5 (Emergência) no topo\nFiltros: Bairro + Status + Busca'),
                ('Ações de Gestão (CRUD)', '#f8fafc', '#334155', '• [Despachar / Status] (Modal PUT)\n• [Excluir -> Confirmar?] (DELETE)'),
            ],
            'heuristic': 'H1: Visibilidade do status e GPCT\nH5: Exclusão em 2 cliques seguros'
        },
    ]

    for idx, sc in enumerate(screens):
        x, w = sc['x'], sc['w']
        # Card frame
        frame = FancyBboxPatch(
            (x, 1.15), w, 5.55,
            boxstyle='round,pad=0.06,rounding_size=0.16',
            facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.8, zorder=2
        )
        ax.add_patch(frame)

        # Browser top bar
        top_bar = FancyBboxPatch(
            (x, 6.12), w, 0.58,
            boxstyle='round,pad=0.02,rounding_size=0.12',
            facecolor=sc['accent'], edgecolor=sc['accent'], linewidth=1, zorder=3
        )
        ax.add_patch(top_bar)
        ax.text(x + 0.14, 6.48, sc['step'], fontsize=7.5, fontweight='bold', color='#bfdbfe', zorder=4)
        ax.text(x + 0.14, 6.24, sc['title'], fontsize=9.5, fontweight='bold', color='#ffffff', zorder=4)

        # Inner wireframe blocks
        cur_y = 5.88
        for b_title, b_bg, b_fg, b_desc in sc['blocks']:
            bh = 1.32 if 'Animação' in b_title or 'Formulário' in b_title else 1.12
            box = FancyBboxPatch(
                (x + 0.14, cur_y - bh), w - 0.28, bh,
                boxstyle='round,pad=0.04,rounding_size=0.08',
                facecolor=b_bg, edgecolor='#cbd5e1', linewidth=1.1, zorder=3
            )
            ax.add_patch(box)
            ax.text(
                x + 0.24, cur_y - 0.22, b_title,
                fontsize=8.2, fontweight='bold',
                color='#ffffff' if b_bg == '#1e40af' else b_fg, zorder=4
            )
            ax.text(
                x + 0.24, cur_y - 0.44, b_desc,
                fontsize=7.3, va='top',
                color='#e2e8f0' if b_bg == '#1e40af' else '#334155', zorder=4
            )
            cur_y -= (bh + 0.16)

        # Heuristic badge below screen
        hbox = FancyBboxPatch(
            (x, 0.25), w, 0.72,
            boxstyle='round,pad=0.04,rounding_size=0.10',
            facecolor='#fef3c7', edgecolor='#f59e0b', linewidth=1.3, zorder=3
        )
        ax.add_patch(hbox)
        ax.text(
            x + w / 2, 0.61, sc['heuristic'],
            ha='center', va='center', fontsize=7.6, fontweight='bold', color='#92400e', zorder=4
        )

        # Flow arrow to next screen
        if idx < len(screens) - 1:
            nx = screens[idx + 1]['x']
            ax.annotate(
                '', xy=(nx - 0.04, 3.95), xytext=(x + w + 0.04, 3.95),
                arrowprops=dict(arrowstyle='->', color='#1e40af', lw=2.4),
                zorder=5
            )

    plt.tight_layout()
    out_path = os.path.join(OUT_DIR, 'prototipo_media_fidelidade.png')
    plt.savefig(out_path, dpi=220)
    plt.close(fig)
    return out_path


def gerar_roadmap_visual():
    fig, ax = plt.subplots(figsize=(14, 5.6), dpi=220)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5.6)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

    ax.text(
        7.0, 5.20,
        'ROADMAP DE EVOLUÇÃO E PRÓXIMOS PASSOS — ZELASP',
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        7.0, 4.86,
        'Sequência Lógica de Validação Social, Evolução Técnica, Piloto Territorial e Escala Pública',
        ha='center', va='center', fontsize=9.2, color='#475569'
    )

    etapas = [
        (
            'ETAPA 1', 'Escuta e Testes com Moradores', '#1d4ed8', '#eff6ff',
            '• O que será feito:\n  Testes práticos na calçada com\n  moradores, idosos e comerciantes\n  no Jabaquara e Vila Mariana.\n\n'
            '• Objetivo / Resultado Esperado:\n  Validar leitura sob sol forte e\n  confirmar tempo de relato <15s\n  sem ajuda técnica.'
        ),
        (
            'ETAPA 2', 'Melhorias e Modo Offline (PWA)', '#0284c7', '#f0f9ff',
            '• O que será feito:\n  Ajustes de acessibilidade pós-teste,\n  fila offline (Service Worker) para\n  tempestades e raio GPS de 100m.\n\n'
            '• Objetivo / Resultado Esperado:\n  Garantir zero perda de relato sem\n  sinal 4G e sugerir apoio (+1)\n  automaticamente por proximidade.'
        ),
        (
            'ETAPA 3', 'Piloto em Subprefeitura + IoT', '#059669', '#ecfdf5',
            '• O que será feito:\n  Operação piloto com equipe da\n  Subprefeitura Vila Mariana/Jabaquara\n  e instalação de nós sensores ESP32.\n\n'
            '• Objetivo / Resultado Esperado:\n  Validar triagem real pelo índice\n  GPCT e abertura autônoma de\n  chamado em queda de árvore/fio.'
        ),
        (
            'ETAPA 4', 'Integração SP156 e Escala', '#047857', '#d1fae5',
            '• O que será feito:\n  API aberta para sincronizar com o\n  portal SP 156 e concessionárias\n  (Enel/Sabesp) + painel público.\n\n'
            '• Objetivo / Resultado Esperado:\n  Reduzir em >60% os chamados\n  duplicados e diminuir o tempo\n  médio de resposta em nível 5.'
        ),
    ]

    for i, (tag, title, col, bg, body) in enumerate(etapas):
        x = 0.5 + i * 3.35
        w = 3.05
        card = FancyBboxPatch(
            (x, 0.45), w, 4.05,
            boxstyle='round,pad=0.06,rounding_size=0.16',
            facecolor='#ffffff', edgecolor=col, linewidth=2.0, zorder=2
        )
        ax.add_patch(card)

        header = FancyBboxPatch(
            (x, 3.72), w, 0.78,
            boxstyle='round,pad=0.02,rounding_size=0.12',
            facecolor=col, edgecolor=col, linewidth=1, zorder=3
        )
        ax.add_patch(header)
        ax.text(x + 0.16, 4.22, tag, fontsize=8.0, fontweight='bold', color='#dbeafe', zorder=4)
        ax.text(x + 0.16, 3.92, title, fontsize=9.2, fontweight='bold', color='#ffffff', zorder=4)

        inner = FancyBboxPatch(
            (x + 0.12, 0.60), w - 0.24, 2.96,
            boxstyle='round,pad=0.04,rounding_size=0.10',
            facecolor=bg, edgecolor='#cbd5e1', linewidth=1, zorder=3
        )
        ax.add_patch(inner)
        ax.text(x + 0.22, 3.38, body, fontsize=8.0, va='top', color='#0f172a', linespacing=1.35, zorder=4)

        if i < len(etapas) - 1:
            ax.annotate(
                '', xy=(x + w + 0.28, 2.45), xytext=(x + w + 0.02, 2.45),
                arrowprops=dict(arrowstyle='->', color='#0f172a', lw=2.2),
                zorder=5
            )

    plt.tight_layout()
    out_path = os.path.join(OUT_DIR, 'roadmap_evolucao.png')
    plt.savefig(out_path, dpi=220)
    plt.close(fig)
    return out_path


if __name__ == '__main__':
    p1 = gerar_diagrama_casos_de_uso()
    p2 = gerar_prototipo_media_fidelidade()
    p3 = gerar_roadmap_visual()
    print('Gerados com sucesso:', p1, p2, p3)
