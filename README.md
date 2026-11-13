# ZelaSP — Software & Total Experience Design (Da Proposta ao Roadmap)

> **Global Solution 2026.2 · FIAP · Desafio CitizenTech**  
> **Disciplina:** Software & Total Experience Design  
> **Professor:** Henrique Cordeiro  
> **Turma:** 1ESPW — Engenharia de Software (1º Ano)  
> **Apresentação Executiva (Slides 16:9 em PDF):** [`Apresentacao_TX_Design_ZelaSP.pdf`](./Apresentacao_TX_Design_ZelaSP.pdf)  
> **Fonte Interativa dos Slides (HTML 16:9):** [`ZelaSP_Apresentacao_GS_2026.html`](./ZelaSP_Apresentacao_GS_2026.html)  
> **Protótipo Funcional no Ar (Vercel):** [https://zelasp-web.vercel.app/](https://zelasp-web.vercel.app/)  
> **Integrantes do Grupo:**
> * Gustavo Rezende Louro — RM570708
> * João Pedro Lagonegro Bosco e Silva — RM569444
> * João Pedro Maschion da Cruz Sá — RM570509
> * Lucas Henrique Alves da Silva — RM572216

---

## 📋 A Ficha da CitizenTech (Base Comum da Equipe)

| Campo da Ficha | Definição Oficial do Grupo (ZelaSP) |
| :--- | :--- |
| **Nome da CitizenTech** | **ZelaSP** — Zeladoria Cidadã Inteligente e Monitoramento Urbano |
| **Cidade e Bairros de Atuação** | **São Paulo — SP**, com foco inicial em **Jabaquara, Vila Mariana, Saúde, Bela Vista, Mooca e Vila Mascote** (e seleção dinâmica de outros bairros da capital via consulta ViaCEP). |
| **Cidadão Beneficiado** | Pedestres, idosos, pessoas com deficiência (PcD), moradores e comerciantes locais que enfrentam riscos diários nas calçadas e vias, além dos agentes de triagem das Subprefeituras. |
| **Problema em uma Frase** | O canal tradicional de zeladoria (rede SP 156 / SGZ, com ~2 milhões de demandas solucionadas/ano nas 32 Subprefeituras) é longo no formulário urbano tradicional (estimado em 5 a 8 min sem CEP/GPS automático), multiplica chamados repetidos em dias de temporal (~1,4x por ocorrência na simulação do módulo matemático) e oferece baixa visibilidade sobre a prioridade de atendimento. |
| **Como Funciona** | Em menos de 15 segundos (meta de 4 passos essenciais), o morador informa o CEP (**ViaCEP**) ou **GPS**, escolhe uma das 6 categorias urbanas, anexa foto e sinaliza risco elétrico ativo; vizinhos confirmam a ocorrência com **Também vi na rua · Apoiar** (`PUT`) sem duplicar protocolos, e a Prefeitura despacha equipes priorizadas por risco à vida (Níveis 1 a 5 e índice **GPCT — Gatilho Preditivo de Contingência Territorial**). |
| **O que cada parte faz** | • **Python (`zelasp-python`):** Motor lógico CLI de classificação de risco e triagem com JSON.<br>• **Matemática / DPS (`zelasp-math`):** Modelagem cúbica com limites, derivadas ($q'(t)$) e integrais ($\int q(t)\,dt$) do índice GPCT.<br>• **Edge/IoT (Wokwi):** Simulação de nó sensor ESP32 autônomo monitorando queda/anomalia em poste crítico.<br>• **Front-end & WebDev (`zelasp-web`):** Aplicação React + Vite + Tailwind integrada às APIs ViaCEP e MockAPI com CRUD completo e fallback `localStorage`.<br>• **Software & TX Design (esta entrega):** Escopo, engenharia de requisitos (RF/RNF/RN justificados), Diagrama UML de Casos de Uso, protótipo de média fidelidade, Heurísticas de Nielsen, Tom de Voz, Arquitetura TX (CX/EX/UX/MX) e Roadmap.<br>• **Storytelling:** Videopitch de 3 minutos em 9 etapas e e-mail estratégico com Arquétipo de Marca. |
| **Links Oficiais em Produção** | • **Deploy Web:** [https://zelasp-web.vercel.app/](https://zelasp-web.vercel.app/)<br>• **GitHub Web:** [https://github.com/ZelaSP/zelasp-web](https://github.com/ZelaSP/zelasp-web)<br>• **GitHub Python:** [https://github.com/ZelaSP/zelasp-python](https://github.com/ZelaSP/zelasp-python)<br>• **GitHub Math:** [https://github.com/ZelaSP/zelasp-math](https://github.com/ZelaSP/zelasp-math)<br>• **GitHub TX Design:** [https://github.com/ZelaSP/zelasp-tx-design](https://github.com/ZelaSP/zelasp-tx-design) |
| **Indicador de Impacto** | • **Agilidade ao cidadão:** meta de registro em **<15s**.<br>• **Redução de sobrecarga (simulação DPS 24h):** agrupamento sem duplicidade (`~1,4x` → `1x`) + alerta preditivo antecipam o pico em **2h** e reduzem o backlog acumulado em **38,5%**.<br>• **Escala municipal (meta do roadmap 12 meses):** **−45%** de chamados duplicados na cidade e priorização imediata de emergências Nível 5. |
| **ODS Conectados** | • **ODS 11** (Cidades Sustentáveis — Metas 11.2 e 11.7): segurança e acessibilidade nas calçadas (fios, bueiros, entulho) para idosos, pedestres e PcDs.<br>• **ODS 9** (Inovação e Infraestrutura): integração de ViaCEP, API REST, modelagem matemática (GPCT) e IoT ESP32 na modernização da zeladoria urbana. |

---

## 📑 Estrutura da Apresentação Executiva (12 Slides · 100 Pontos)

O arquivo oficial para avaliação em PDF é [`Apresentacao_TX_Design_ZelaSP.pdf`](./Apresentacao_TX_Design_ZelaSP.pdf) (formato widescreen `16:9`, gerado a partir de [`ZelaSP_Apresentacao_GS_2026.html`](./ZelaSP_Apresentacao_GS_2026.html)). A estrutura cobre integralmente os 7 entregáveis obrigatórios da disciplina:

### 1. Capa e Identificação (Slide 01 · 5 pontos)
Apresenta o projeto **ZelaSP**, a turma **1ESPW**, o **Professor Henrique Cordeiro**, o nome completo e RM dos 4 integrantes, os **ODS 11 e 9** com legenda resumida e o link do protótipo ao vivo (`zelasp-web.vercel.app`).

---

### 2. Descrição do Problema (Slide 02 · 10 pontos)
* **O que acontece nas ruas:** Quatro cenários críticos que degradam a segurança e a mobilidade nos bairros prioritários (Jabaquara, Vila Mariana, Saúde, Bela Vista, Mooca e Vila Mascote), acompanhados das 6 categorias implementadas no formulário (`Fios e Cabos Rompidos/Soltos`, `Poda de Árvore com Risco Elétrico`, `Tampa de Bueiro Furtada/Quebrada`, `Buraco em Via ou Calçada`, `Descarte Irregular de Entulho` e `Carro Abandonado`):
  1. **Fiação elétrica rompida:** cabos possivelmente energizados expõem pedestres ao risco de choque;
  2. **Bueiro sem tampa:** risco de queda grave, especialmente para idosos e pessoas com deficiência;
  3. **Entulho na calçada:** obstrução força o pedestre a desviar para o asfalto entre veículos;
  4. **Carro abandonado:** pode acumular água parada e favorecer focos de dengue.
* **Quem é afetado:** Pedestres, idosos, pessoas com deficiência (PcD), moradores, comerciantes e equipes de triagem das Subprefeituras.
* **Dados e transparência de fontes:**
  * **Dado público (SMIT / Prefeitura de SP):** A rede **SP 156** (integrada ao **SGZ** nas **32 Subprefeituras**) registra cerca de **~2 milhões de demandas solucionadas por ano**.
  * **Estimativa UX:** Fluxo de abertura tradicional sem autopreenchimento automático estimado em **5–8 min** (vs. **<15s** no fluxo ZelaSP).
  * **Simulação matemática (`zelasp-math`):** Picos em temporais multiplicam chamados repetidos (**~1,4x por ocorrência** na simulação de 24h) e reduzem a visibilidade do que exige resposta imediata.

---

### 3. Escopo da Solução (Slide 03 · 10 pontos)

| ✓ DENTRO DO ESCOPO (O que o ZelaSP faz) | × FORA DO ESCOPO (O que o ZelaSP não faz) |
| :--- | :--- |
| **01. Acesso por perfil + abertura educativa:** Entrada segmentada entre Cidadão e Prefeitura, com animação sequencial dos 4 problemas urbanos. | **01. Não executa obras físicas:** Não possui frota de caminhões ou asfalto; organiza triagem e despacho. |
| **02. Relato georreferenciado em menos de 15s:** API **ViaCEP**, coordenadas por **GPS** do navegador e foto de evidência. | **02. Não substitui atendimento emergencial:** Em acidente com vítima ou risco ativo, orienta acionar Bombeiros **193**, SAMU **192**, Defesa Civil **199** ou concessionária **Enel**. |
| **03. Apoio comunitário +1:** Deduplicação colaborativa por ocorrência existente (`PUT`), somando apoios sem gerar novo protocolo. | **03. Não aplica multas nem autuações:** Não substitui autuações da CET nem atendimento policial (**190**). |
| **04. Classificação automática de risco:** Motor determinístico de prioridade dos **níveis 1 a 5**. | **04. Não coleta dados sensíveis ou bancários:** Sem CPF, RG ou biometria — *Privacy by Design* e respeito à LGPD. |
| **05. Painel gestor + GPCT + IoT:** Filtros, atualização de status e parecer técnico, exclusão segura em 2 etapas e alertas simulados com ESP32. | — |

---

### 4. Requisitos Funcionais, Não Funcionais e Regras de Negócio (Slides 04 e 05 · 20 pontos)

Cada item explicita **Descrição**, **Classificação** (por que pertence àquela categoria) e **Justificativa** (conexão direta com o problema, escopo e pessoa usuária):

#### 4.1 Requisitos Funcionais (`RF01–RF06` — Slide 04)
| Código | Nome / Descrição | Classificação (Por que é RF?) | Justificativa (Por que é necessário?) |
| :--- | :--- | :--- | :--- |
| **RF01** | **Registrar ocorrência:** Categoria (6 tipos), CEP, GPS, risco elétrico, descrição e foto (`POST`). | Ação direta de entrada e persistência acionada pelo cidadão. | Substitui o formulário longo por fluxo guiado focado nos riscos reais. |
| **RF02** | **Autopreencher endereço:** ViaCEP valida CEP de 8 dígitos e completa logradouro e bairro. | Comportamento de integração externa e transformação automática de entrada. | Reduz erros: o pedestre na rua nem sempre conhece a grafia oficial da via. |
| **RF03** | **Apoiar ocorrência +1:** Somar apoio comunitário em chamado aberto na rua (`PUT`). | Interação do cidadão que altera o estado quantitativo do registro. | Evita chamados duplicados no mesmo ponto e quantifica o impacto coletivo. |
| **RF04** | **Consultar e filtrar:** Busca textual, filtros por bairro/status e ordenação Nível `5 → 1` (`GET`). | Define consulta, filtragem e ordenação de dados na fila pública e gestora. | O cidadão encontra relatos da rua; a Prefeitura vê primeiro as emergências. |
| **RF05** | **Monitorar índice GPCT:** Calcular e exibir o *Gatilho Preditivo de Contingência Territorial* no painel. | Processa chamados abertos e gera alerta analítico de suporte à decisão. | Aponta visualmente quando um território atinge saturação operacional. |
| **RF06** | **Gerir status e registros:** Atualizar status/parecer (`PUT`) e excluir inválidos em 2 cliques (`DELETE`). | Modela operações administrativas exclusivas do agente municipal. | Dá transparência ao andamento do reparo e mantém a fila pública íntegra. |

#### 4.2 Requisitos Não Funcionais (`RNF01–RNF04` — Slide 05)
| Código | Descrição | Classificação (Por que é RNF?) | Justificativa (Por que é necessário?) |
| :--- | :--- | :--- | :--- |
| **RNF01** | **Meta de relato rápido (≤ 15s / 4 passos essenciais).** | Usabilidade e eficiência — meta de tempo e esforço operacional. | Permite concluir o relato caminhando na calçada sem desistência. |
| **RNF02** | **Mobile-first responsivo (360–1920px), WCAG AA e alvos de toque ≥44px.** | Acessibilidade e ergonomia — padrão de qualidade da interface. | Garante leitura sob luz solar direta e uso acessível por todas as idades. |
| **RNF03** | **Sincronização em nuvem (MockAPI) com fallback em `localStorage`.** | Confiabilidade e tolerância a falhas — resiliência da persistência. | O sinal 4G oscila em tempestades; o cidadão não perde o registro. |
| **RNF04** | **ViaCEP e carregamento da fila com retorno < 2s (meta HTTP).** | Desempenho — restrição de latência de rede. | Reduz atrito e evita abandono ao informar o endereço manualmente. |

#### 4.3 Regras de Negócio (`RN01–RN04` — Slide 05)
| Código | Descrição | Classificação (Por que é RN?) | Justificativa (Por que é necessário?) |
| :--- | :--- | :--- | :--- |
| **RN01** | **Risco elétrico ou bueiro sem tampa → Prioridade 5.** | Política de domínio para proteção à vida no cálculo de severidade. | Risco de choque ou queda grave não pode esperar demandas estéticas. |
| **RN02** | **≥ 10 apoios comunitários → sobe +1 nível (teto 5).** | Regra matemática determinística de ponderação social (`riskCalculator.js`). | Valoriza validação coletiva e escalona problemas com amplo impacto. |
| **RN03** | **GPCT: ≥2 críticos abertos = Atenção Operacional; ≥4 = Contingência Ativada.** | Gatilho de governança territorial alinhado à modelagem DPS. | Antecipa reforço de equipes antes que a fila de um bairro sature. |
| **RN04** | **Só Prefeitura altera status ou exclui; chamados `RESOLVIDO` bloqueiam apoio.** | Segregação de alçada entre perfis e integridade de auditoria. | Evita encerramentos indevidos e preserva o histórico público de atendimento. |

---

### 5. Diagrama UML de Casos de Uso e Contextualização (Slide 06 · 15 pontos)

![Diagrama UML de Casos de Uso — ZelaSP](./assets/diagrama_casos_de_uso.png)

* **Contextualização dos 4 Atores (Slide 06):**
  1. **Cidadão (`HUMANO`):** Executa `UC01` (relatar em <15s), `UC03` (capturar GPS via `«extend»`), `UC04` (consultar/filtrar chamados) e `UC05` (apoiar +1). **Objetivo:** resolver riscos da sua rua rapidamente e acompanhar com transparência.
  2. **Agente Municipal (`HUMANO`):** Executa `UC04` (consultar fila), `UC07` (monitorar GPCT), `UC08` (atualizar status/parecer) e `UC09` (excluir inválido em 2 cliques). **Objetivo:** despachar equipes priorizando riscos Nível 5.
  3. **API ViaCEP (`EXTERNO`):** Serviço REST acionado em `UC02` (incluído obrigatoriamente por `UC01`). **Objetivo:** padronizar logradouro e bairro a partir do CEP sem digitação manual.
  4. **Nó IoT ESP32 (`BORDA`):** Sensor simulado no Wokwi que aciona `UC10` (emitir alerta crítico automático) e inclui `UC06` (cálculo de prioridade 1–5). **Objetivo:** detectar anomalias elétricas/estruturais antes mesmo do primeiro relato humano.

---

### 6. Protótipo de Média Fidelidade, Heurísticas, Tom de Voz e Arquitetura TX (Slides 07, 08 e 09 · 25 pontos)

* **Slide 07 — Fluxo Ponta a Ponta em Média Fidelidade (Pins ①–⑨):**
  1. **Tela 01 · Novo Relato (`Cidadão`):** Seleção entre os **6 botões de categorias urbanas** (`Fios e Cabos Rompidos/Soltos` destacado, `Poda com Risco Elétrico`, `Tampa de Bueiro Furtada`, `Buraco em Via ou Calçada`, `Descarte de Entulho` e `Carro Abandonado`), campo CEP (`04309-011 · Jabaquara` + `Buscar CEP`), `Usar meu GPS`, `Anexar foto`, caixa preventiva (`Risco de choque ou faíscas? → Nível 5. Não se aproxime (193 / 199).`) e ação `Publicar Relato`.
  2. **Tela 02 · Feed Comunitário (`Cidadão`):** Filtro `Todos os bairros` e busca com ação `Limpar`, cards reais (`SP-2026-101 · Av. Armando de A. Pereira · 14 apoios · Em execução` com botão `Também vi na rua · Apoiar (14)`, e `SP-2026-105 · Rua da Mooca · 5 apoios · Aberto`) mais confirmação toast em tempo real.
  3. **Tela 03 · Painel Gestor (`Prefeitura`):** Contadores (`05 Pendentes na fila`, `04 Prioridade máxima` sobre os dados iniciais), faixa `GPCT · CONTINGÊNCIA ATIVADA`, filtros e ações `Despachar / Status`, `Nota da Vistoria` e exclusão em 2 etapas (`Confirmar / Não`).
* **Slide 08 — Heurísticas de Nielsen e Tom de Voz (com strings literais do código):**
  * **H1 (Visibilidade):** selo `Nuvem`/`Local`, retorno ViaCEP, badges `ABERTO → RESOLVIDO`, faixa GPCT e toasts.
  * **H2 (Mundo Real):** abertura animada dos 4 cenários urbanos e categorias em linguagem cotidiana.
  * **H3 (Controle e Liberdade):** botão `Pular` na abertura, `Limpar` nos filtros e alternância rápida `Cidadão ↔ Prefeitura`.
  * **H5 (Prevenção de Erros):** validação de 8 dígitos no CEP, `Apoiar (+1)` contra duplicidade, alerta 193/199 e confirmação dupla `Confirmar / Não`.
  * **H6 (Reconhecimento) & H8 (Design Minimalista):** botões rápidos de bairro prioritário, hierarquia limpa e cor vermelha reservada a risco extremo/exclusão.
  * **Tom de Voz:** Cívico, empático, direto, transparente e preventivo — demonstrado por trechos literais de [`Header.jsx`](../04%20-%20Front-end%20Design/src/components/Header.jsx), [`App.jsx`](../04%20-%20Front-end%20Design/src/App.jsx) e [`viaCepService.js`](../04%20-%20Front-end%20Design/src/services/viaCepService.js).
* **Slide 09 — Arquitetura Total Experience (`CX / EX / UX / MX`):** Conecta a jornada do cidadão (`CX`), a operação pública (`EX`), a usabilidade na calçada (`UX`) e a camada multi-ambiente Web + ViaCEP + GPS + MockAPI + simulação ESP32 no Wokwi (`MX`), convergindo no motor determinístico de prioridade.

---

### 7. Modelagem GPCT, Roadmap de Evolução e Fechamento ODS (Slides 10, 11 e 12 · 15 pontos)

* **Slide 10 — GPCT (`Gatilho Preditivo de Contingência Territorial`):** Integra os limiares do painel web ([`riskCalculator.js`](../04%20-%20Front-end%20Design/src/utils/riskCalculator.js): `<2` = *Estável*, `≥2` = *Atenção Operacional*, `≥4` = *Contingência Ativada*) à modelagem diferencial/integral de DPS (`zelasp-math`: disparo com $q(t) \ge 30\text{ relatos/h}$ e $q'(t) > 0$, antecipando o pico em **2h** e reduzindo o backlog acumulado em **38,5%** na simulação de 24h).
* **Slide 11 — Roadmap de Evolução em 4 Fases (12 Meses):**
  1. **Meses 1–2 · Fase 01:** Testes de usabilidade em campo com moradores, idosos e PcDs sob luz solar (`META · SUS ≥ 85`, `Conclusão > 95%`).
  2. **Meses 3–4 · Fase 02:** Refino UX pós-teste, Service Workers (PWA offline evoluindo o fallback `localStorage`) e validação de foto (`META · −90% relatos incompletos ou trotes`).
  3. **Meses 5–6 · Fase 03:** Operação assistida com Subprefeituras Jabaquara/Vila Mariana + telemetria IoT ESP32 integrada ao painel GPCT (`META · −60% tempo de triagem Nível 5`).
  4. **Meses 7–12 · Fase 04:** Integração via API com SGZ/SP 156 e portal público de transparência para 32 Subprefeituras (`META · −45% chamados duplicados na cidade`).
* **Slide 12 — Links de Produção e ODS 11 & 9:** Consolida os links do deploy e repositórios ao lado da explicação explícita de contribuição do ZelaSP às metas dos **ODS 11 e 9**.

---

## 🛠️ Como Regenerar o Diagrama UML e o PDF

1. **Regenerar o Diagrama UML (`assets/diagrama_casos_de_uso.png`):**
   ```bash
   python gerar_diagramas.py
   ```
2. **Exportar o PDF 16:9 a partir de `ZelaSP_Apresentacao_GS_2026.html`:**
   Abra [`ZelaSP_Apresentacao_GS_2026.html`](./ZelaSP_Apresentacao_GS_2026.html) no navegador e utilize `↗ Imprimir / PDF` (ou Google Chrome Headless com suporte à regra `@page { size: 13.333in 7.5in; margin: 0; }`).
