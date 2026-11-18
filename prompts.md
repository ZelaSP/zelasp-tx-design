# 🤖 Documentação do Uso de Inteligência Artificial — `prompts.md`

**Disciplina:** Software & Total Experience Design (`CitizenTech: Da Proposta ao Roadmap`)  
**Professor:** Henrique Cordeiro  
**Turma:** 1ESPW — Engenharia de Software (1º Ano · FIAP)  
**Projeto:** ZelaSP — Zeladoria Cidadã Inteligente  
**Integrantes:**
* Gustavo Rezende Louro — RM570708
* João Pedro Lagonegro Bosco e Silva — RM569444
* João Pedro Maschion da Cruz Sá — RM570509
* Lucas Henrique Alves da Silva — RM572216

---

## 1. Ferramentas de IA Utilizadas e Finalidades

* **ChatGPT / Codex (OpenAI):** Utilizado inicialmente como assistente na estruturação do código HTML e estilos CSS para a apresentação executiva em formato widescreen 16:9 (`ZelaSP_Apresentacao_GS_2026.html`), organizando visualmente os cards, a tipografia e o layout dos 12 slides a partir da pauta elaborada pelos alunos, além do apoio na síntese textual (`CX / EX / UX / MX`). Posteriormente, atuou também na auditoria cruzada de consistência entre os entregáveis, orientando a revisão dos relacionamentos UML (`UC02` ViaCEP como comportamento opcional `«extend»`), dos requisitos e do roadmap.
* **Google Antigravity (Claude / Gemini):** Apoio na auditoria de conformidade dos textos dos slides contra o edital oficial (`GS-CitizenTech.pdf`) e contra o código real (`zelasp-web`, `zelasp-python` e `zelasp-math`); implementação das revisões nos slides, em `gerar_diagramas.py` (incluindo o ajuste de `UC02` ViaCEP para `«extend»` opcional e rótulos de `UC01`/`UC10`) e na conversão de emojis em ícones vetoriais **SVG** inline; configuração da exportação do PDF (`Apresentacao_TX_Design_ZelaSP.pdf`) via Chrome Headless; e padronização da documentação (`README.md` e `prompts.md`).

> **Nota de Autoria Própria e Revisão Assistida (Entregáveis de Design e Engenharia de Software):**  
> * **Diagrama UML de Casos de Uso:** A **concepção original** do modelo de casos de uso — incluindo o mapeamento inicial dos 4 atores (`Cidadão`, `Agente Municipal`, `ViaCEP`, `Nó IoT ESP32`), a definição dos 10 casos de uso (`UC01–UC10`) e a estrutura inicial em Python (`gerar_diagramas.py`) — foi criada pelos integrantes da equipe. Posteriormente, a **revisão dos relacionamentos UML e rótulos** contou com apoio assistido por IA (auditoria com ChatGPT/Codex e atualização em `gerar_diagramas.py` com Google Antigravity): alteração do caso de uso `UC02` (consulta ViaCEP) para comportamento **opcional (`«extend»`)** em `UC01`, alinhamento de `UC03` (GPS) também como `«extend»` opcional, caracterização de `Nó IoT ESP32` como `«borda proposta»` ligado a `UC10 (Integração Proposta)` e ajuste de `UC01` para explicitar `Meta de Tempo: ≤ 15s`.  
> * **Wireframes e Protótipo de Média Fidelidade:** A arquitetura de informação, o layout das 3 telas principais (Novo Relato, Feed Comunitário e Painel Gestor), o fluxo de navegação, a identificação das Heurísticas de Nielsen (pins ① a ⑨) e as diretrizes de Tom de Voz foram concebidos originalmente pelos alunos a partir da aplicação em React ([`zelasp-web.vercel.app`](https://zelasp-web.vercel.app/)), recebendo depois revisão assistida apenas para alinhamento textual (como rótulos de foto demonstrativa, cache de consulta e metas).

---

## 2. Prompts Representativos Utilizados durante o Desenvolvimento

### Prompt 1 — Estruturação do Código HTML/CSS dos 12 Slides 16:9 (ChatGPT)
> *"Estruture um documento HTML/CSS em formato widescreen 16:9 (proporção 960x540 / 1920x1080) para apresentação executiva de slides do projeto acadêmico ZelaSP. Organize o layout em 12 slides com design system limpo, modo escuro profissional, tipografia moderna (Google Fonts) e cards responsivos, contemplando os conteúdos e seções fornecidos pela equipe: Capa com identificação acadêmica, Descrição do Problema, Escopo Dentro/Fora, Requisitos RF/RNF/RN, visualização do Diagrama UML e dos Wireframes elaborados pelo grupo, Heurísticas de Nielsen, Tom de Voz, Arquitetura TX (CX/EX/UX/MX), Modelagem GPCT, Roadmap de Evolução e Fechamento com ODS."*

### Prompt 2 — Apoio na Redação, Síntese e Tom Executivo dos Slides (ChatGPT)
> *"Ajude a sintetizar os textos técnicos elaborados pela equipe para que caibam com clareza nos slides da apresentação, mantendo a estrutura exigida de Descrição, Classificação e Justificativa para os Requisitos Funcionais, Não Funcionais e Regras de Negócio. O tom de voz deve ser executivo, direto e focado no valor público gerado para o cidadão e para a gestão municipal de São Paulo."*

### Prompt 3 — Substituição de Emojis por Ícones SVG e Automação de Exportação em PDF (Google Antigravity)
> *"Substitua todos os emojis presentes no código HTML da apresentação por ícones vetoriais SVG inline correspondentes (estilo Lucide/Feather), garantindo renderização consistente entre navegadores. Além disso, forneça o comando de linha para exportação do arquivo HTML para PDF de alta resolução (16:9 exato sem cortes ou quebras indevidas) utilizando o Google Chrome em modo headless."*

### Prompt 4 — Auditoria Factual e Cruzamento com Dados Oficiais do Projeto (Google Antigravity)
> *"Revise os textos dos slides comparando-os com o documento oficial da Global Solution, com as fontes públicas da Prefeitura de São Paulo / SMIT e com o repositório em produção do ZelaSP. Aponte e corrija discrepâncias de números (como dados de chamados anuais da rede SP 156), verifique se as regras de negócio refletem fielmente o código React, garanta que os ODS 11 e 9 estejam explicitamente justificados em alinhamento com os demais entregáveis e certifique-se de que estimativas de UX, simulações matemáticas e metas de roadmap estejam devidamente diferenciadas."*

---

## 3. Artefatos Desenvolvidos e Ajustados com Auxílio da IA

1. **Apresentação Executiva em HTML/CSS (`ZelaSP_Apresentacao_GS_2026.html`) e PDF (`Apresentacao_TX_Design_ZelaSP.pdf`):** Estruturação do código de layout 16:9, estilização CSS e automação do processo de compilação em PDF.
2. **Textos e Síntese Executiva dos Slides:** Apoio na redação e revisão gramatical dos textos explicativos dos slides (problema, escopo, detalhamento de requisitos, arquitetura TX e roadmap).
3. **Revisão Assistida do Diagrama UML (`gerar_diagramas.py` e `assets/diagrama_casos_de_uso.png`):** Ajustes pontuais nos relacionamentos e rótulos após auditoria cruzada (alteração de `UC02` ViaCEP para `«extend»` opcional em `UC01`, manutenção de `UC03` GPS como `«extend»`, meta `≤ 15s` em `UC01` e `UC10` como integração IoT proposta).
4. **Documentação Acadêmica (`README.md` e `prompts.md`):** Apoio na padronização textual e formatação das tabelas e seções descritivas.

*(A concepção original do modelo de casos de uso e a arquitetura visual dos wireframes de média fidelidade partiram da equipe; os ajustes posteriores assistidos por IA concentraram-se na revisão de relacionamentos UML e no alinhamento textual com o código e o roadmap.)*

---

## 4. Como o Grupo Verificou, Testou e Corrigiu os Resultados da IA

A revisão crítica e técnica realizada pelos alunos identificou e corrigiu desvios relevantes gerados pelas ferramentas:

1. **Correção da definição e separação do índice GPCT (Slide 10):** Na primeira redação sugerida pela IA para os textos dos slides, a sigla `GPCT` foi expandida incorretamente como *"Grau de Prioridade Crítica Territorial"*. A equipe consultou o código de [`riskCalculator.js`](https://github.com/ZelaSP/zelasp-web/blob/main/src/utils/riskCalculator.js) e o estudo de Matemática (`zelasp-math`), corrigiu para **Gatilho Preditivo de Contingência Territorial** e separou os dois mecanismos: contagem operacional do painel Web (`<2` estável, `2–3` atenção, `≥4` contingência) vs. simulação acadêmica temporal em Matemática (**−38,5%** do volume excedente sobre base já deduplicada).
2. **Alinhamento factual com dados oficiais, relatos informais e metas realistas (Slides 02, 03, 05 e 11):** A equipe preservou o dado público oficial da **Prefeitura de São Paulo / SMIT** (**~2 milhões de demandas solucionadas/ano na rede SP 156 nas 32 Subprefeituras**) e reconheceu que o SP156 já fornece protocolo e formas de acompanhamento ([perguntas frequentes oficiais do SP156](https://prefeitura.sp.gov.br/web/inovacao/w/acesso_a_informacao/350229)), posicionando o diferencial proposto na combinação de **registro simples, apoio comunitário e organização por risco** como hipótese a validar. Foram registrados apenas dois relatos informais de contexto (~30–40 min para remoção de árvore e ~10 min para lixeira de poste, sem medição pelo grupo, sem entrevistas formais, testes cronometrados ou parcerias externas), além de demarcar metas a validar (**registro em até 15s**, **WCAG AA**, **−45%** na parcela de chamados duplicados), seleção demonstrativa de foto e cache local apenas para consulta.
3. **Conferência literal e coerência cross-módulo (`zelasp-web` e `zelasp-python`):**
   * Substituição de textos fictícios no **Tom de Voz** (Slide 08) por mensagens literais do código atual (`Header.jsx`, `App.jsx` e `viaCepService.js`).
   * Uniformização da regra **RN01/RN02** com Python e JavaScript: **risco elétrico em qualquer categoria = nível 5**; bueiro sem tampa = nível 5; `≥ 10` apoios acrescentam um único nível (teto 5); `RESOLVIDO` bloqueia novos apoios; rótulo **“Chamados de risco alto/crítico”** nos contadores nível ≥4 e links diretos para `zelasp-web` (sem caminhos relativos locais).
4. **Revisão dos Relacionamentos UML (Slide 06 e `gerar_diagramas.py`):** Com apoio assistido do plano de auditoria (ChatGPT/Codex) e atualização via Google Antigravity, a equipe revisou o diagrama original para transformar `UC02` (consulta ViaCEP) de inclusão obrigatória em comportamento **opcional (`«extend»`)** de `UC01` — pois o código permite digitar o endereço manualmente sem informar CEP —, além de explicitar `UC10` e `Nó IoT ESP32` como integração proposta (`«borda proposta»`) e `UC01` com meta `≤ 15s`.
5. **Adequação ao Edital e Refinamento de Apresentação:** A equipe inseriu cards explicativos no Slide 12 justificando a contribuição do ZelaSP às metas dos **ODS 11 e 9** (em coerência com Python, Matemática e Web), ampliou a Tela 01 para listar os 6 botões de categoria e comandou a substituição de emojis por ícones vetoriais SVG, eliminando ruídos visuais.
6. **Inspeção visual página a página:** As 12 páginas de `Apresentacao_TX_Design_ZelaSP.pdf` e a imagem `assets/diagrama_casos_de_uso.png` foram inspecionadas após a regeneração para assegurar legibilidade em tela cheia, conformidade de contraste e proporção `16:9` sem quebras de layout.

---

## 5. Análise Crítica (Benefícios, Limitações e Dificuldades)

* **Benefícios:** A utilização de IA generativa acelerou a escrita do código HTML/CSS da apresentação de slides, garantiu agilidade na aplicação de estilos visuais e na conversão para ícones SVG, apoiou a revisão rigorosa dos relacionamentos UML (como identificar que ViaCEP em `UC02` é `«extend»` opcional) e ajudou na concisão e consistência técnica entre entregas.
* **Limitações e Dificuldades:** Ferramentas de IA frequentemente introduzem alucinações técnicas (como inventar significados para siglas internas do projeto), propõem números imprecisos sem citar fontes oficiais e sugerem textos genéricos que não condizem com a experiência real do produto. A concepção original dos wireframes e dos casos de uso, a avaliação heurística e a validação final de cada alteração técnica frente ao código-fonte implementado exigiram o discernimento e a responsabilidade técnica dos alunos da equipe.
