# -*- coding: utf-8 -*-
"""
Gera o Diagrama UML de Casos de Uso de alta resolucao para a entrega de
05 - Software & Total Experience Design (ZelaSP - GS 2026.2):
- assets/diagrama_casos_de_uso.png
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
os.makedirs(OUT_DIR, exist_ok=True)


def draw_stick_figure(ax, x, y, label, sublabel, color='#1e40af'):
    head = Circle((x, y + 0.42), 0.16, facecolor='#eff6ff', edgecolor=color, linewidth=2.2, zorder=5)
    ax.add_patch(head)
    ax.plot([x, x], [y + 0.26, y - 0.12], color=color, linewidth=2.2, zorder=5)
    ax.plot([x - 0.22, x + 0.22], [y + 0.14, y + 0.14], color=color, linewidth=2.2, zorder=5)
    ax.plot([x, x - 0.18], [y - 0.12, y - 0.42], color=color, linewidth=2.2, zorder=5)
    ax.plot([x, x + 0.18], [y - 0.12, y - 0.42], color=color, linewidth=2.2, zorder=5)
    ax.text(x, y - 0.62, label, ha='center', va='top', fontsize=10.5, fontweight='bold', color='#0f172a')
    if sublabel:
        ax.text(x, y - 0.88, sublabel, ha='center', va='top', fontsize=8.5, color='#475569')


def gerar_diagrama_casos_de_uso():
    fig, ax = plt.subplots(figsize=(14, 8.2), dpi=220)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.2)
    ax.axis('off')
    fig.patch.set_facecolor('#f8fafc')

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

    boundary = FancyBboxPatch(
        (2.85, 0.55), 8.3, 6.55,
        boxstyle='round,pad=0.12,rounding_size=0.22',
        facecolor='#ffffff', edgecolor='#1e40af', linewidth=2.2, zorder=1
    )
    ax.add_patch(boundary)
    ax.text(
        7.0, 6.82,
        '«system»  Plataforma ZelaSP (Módulos Atuais + Arquitetura Proposta)',
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1e40af',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#eff6ff', edgecolor='#bfdbfe', lw=1)
    )

    # Atores à esquerda (Humanos)
    draw_stick_figure(ax, 1.25, 5.2, 'Cidadão', '(Morador / Pedestre SP)', color='#1d4ed8')
    draw_stick_figure(ax, 1.25, 2.0, 'Agente Municipal', '(Operador Subprefeitura)', color='#047857')

    # Atores à direita (Sistemas Externos / Borda IoT)
    draw_stick_figure(ax, 12.75, 5.3, 'API ViaCEP', '«sistema externo»', color='#7c3aed')
    draw_stick_figure(ax, 12.75, 2.1, 'Nó IoT ESP32', '«borda proposta»', color='#d97706')

    ucs = {
        'UC01': (4.9, 5.85, 3.1, 0.72, 'UC01: Relatar Ocorrência\n(Meta de Tempo: ≤ 15s)', '#eff6ff', '#2563eb'),
        'UC02': (9.2, 6.00, 2.9, 0.68, 'UC02: Consultar CEP\nvia ViaCEP (Opcional)', '#f5f3ff', '#7c3aed'),
        'UC03': (9.2, 4.80, 2.9, 0.68, 'UC03: Capturar GPS do\nNavegador (Opcional)', '#eff6ff', '#3b82f6'),
        'UC04': (4.9, 4.65, 3.1, 0.72, 'UC04: Consultar e Filtrar\nChamados do Bairro', '#f8fafc', '#475569'),
        'UC05': (4.9, 3.55, 3.1, 0.72, 'UC05: Apoiar Chamado\nExistente (+1 Apoio)', '#ecfdf5', '#059669'),
        'UC06': (9.2, 3.55, 2.9, 0.72, 'UC06: Calcular Prioridade\nde Risco (Nível 1 a 5)', '#fef3c7', '#d97706'),
        'UC07': (4.9, 2.40, 3.1, 0.72, 'UC07: Monitorar Índice\nTerritorial GPCT', '#ecfdf5', '#047857'),
        'UC08': (4.9, 1.10, 3.1, 0.72, 'UC08: Atualizar Status e\nParecer de Vistoria', '#ecfdf5', '#047857'),
        'UC09': (9.2, 1.15, 2.9, 0.68, 'UC09: Excluir Registro\nInválido (2 Cliques)', '#fef2f2', '#dc2626'),
        'UC10': (9.2, 2.35, 2.9, 0.68, 'UC10: Emitir Alerta IoT\n(Integração Proposta)', '#fffbeb', '#d97706'),
    }

    for _, (cx, cy, w, h, text, fc, ec) in ucs.items():
        el = Ellipse((cx, cy), w, h, facecolor=fc, edgecolor=ec, linewidth=1.7, zorder=3)
        ax.add_patch(el)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=8.3, fontweight='bold', color='#0f172a', zorder=4)

    # Associações diretas (Ator -> Caso de Uso), com corredor limpo entre UC07 e UC08
    assoc = [
        ((1.65, 5.35), (3.35, 5.85), '#1d4ed8'),
        ((1.65, 5.15), (3.35, 4.65), '#1d4ed8'),
        ((1.65, 4.95), (3.35, 3.65), '#1d4ed8'),
        ((1.65, 2.32), (3.42, 4.48), '#047857'),
        ((1.65, 2.15), (3.35, 2.40), '#047857'),
        ((1.65, 1.98), (7.80, 1.30), '#047857'),
        ((1.65, 1.82), (3.35, 1.15), '#047857'),
        ((12.35, 5.45), (10.65, 6.00), '#7c3aed'),
        ((12.35, 2.25), (10.65, 2.35), '#d97706'),
    ]
    for (x1, y1), (x2, y2), col in assoc:
        ax.plot([x1, x2], [y1, y2], color=col, linewidth=1.4, alpha=0.85, zorder=2)

    def draw_rel(p1, p2, label, color='#475569', dx=0.0, dy=0.11):
        ax.annotate(
            '', xy=p2, xytext=p1,
            arrowprops=dict(arrowstyle='->', linestyle='--', color=color, lw=1.3),
            zorder=4
        )
        mx, my = (p1[0] + p2[0]) / 2 + dx, (p1[1] + p2[1]) / 2 + dy
        ax.text(
            mx, my, label, fontsize=7.5, ha='center', va='center',
            color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.12', facecolor='#ffffff', edgecolor='none', alpha=0.92),
            zorder=5
        )

    draw_rel((7.75, 6.00), (6.45, 5.95), '«extend»', '#7c3aed')
    draw_rel((7.75, 4.95), (6.40, 5.65), '«extend»', '#2563eb')
    draw_rel((6.35, 5.60), (7.85, 3.80), '«include»', '#d97706')
    draw_rel((6.45, 3.55), (7.75, 3.55), '«include»', '#059669')
    draw_rel((9.20, 2.69), (9.20, 3.19), '«include»', '#d97706', dx=0.48, dy=0.0)

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


if __name__ == '__main__':
    p1 = gerar_diagrama_casos_de_uso()
    print('Gerado com sucesso:', p1)
