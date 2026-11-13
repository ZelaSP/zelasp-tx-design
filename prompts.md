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

* **ChatGPT (OpenAI):** Utilizado como assistente na estruturação do código HTML e estilos CSS para a apresentação executiva em formato widescreen 16:9 (`ZelaSP_Apresentacao_GS_2026.html`), organizando visualmente os cards, a tipografia e o layout dos 12 slides a partir da pauta de conteúdos e especificações técnicas elaboradas pelos alunos; e apoio na redação, síntese e polimento textual de tópicos conceituais (como a síntese da arquitetura de Total Experience: `CX / EX / UX / MX`).
* **Google Antigravity (Claude / Gemini):** Apoio na auditoria de conformidade dos textos dos slides contra o edital oficial (`GS-CitizenTech.pdf`) e contra as métricas e o código real do projeto (`zelasp-web` e `zelasp-math`); conversão de emojis em ícones vetoriais **SVG** inline para acabamento profissional; apoio técnico na configuração do comando de exportação do PDF em alta fidelidade (`Apresentacao_TX_Design_ZelaSP.pdf`) via Chrome Headless; e suporte na redação, revisão ortográfica e padronização dos arquivos de documentação (`README.md` e `prompts.md`).

> **Nota de Autoria Própria (Entregáveis de Design e Engenharia de Software):**  
> * **Diagrama UML de Casos de Uso:** A modelagem dos casos de uso, o mapeamento dos 4 atores (`Cidadão`, `Agente Municipal`, `ViaCEP`, `Nó IoT ESP32`), a definição dos 10 casos de uso (`UC01–UC10`), os relacionamentos (`<<include>>` e `<<extend>>`) e a implementação do script em Python (`gerar_diagramas.py` com `matplotlib`) foram concebidos e desenvolvidos **exclusivamente pelos integrantes da equipe**. Nenhuma IA foi utilizada para gerar o diagrama ou sua lógica de casos de uso.  
> * **Wireframes e Protótipo de Média Fidelidade:** A arquitetura de informação, o layout das 3 telas principais (Novo Relato, Feed Comunitário e Painel Gestor), o fluxo de navegação, a identificação das Heurísticas de Nielsen (pins ① a ⑨) e as diretrizes de Tom de Voz foram criados e estruturados **diretamente pelos alunos**, derivados da aplicação real implementada em React ([`zelasp-web.vercel.app`](https://zelasp-web.vercel.app/)) e das necessidades da pessoa usuária na rua. Nenhuma IA foi utilizada para desenhar as telas ou definir o protótipo.

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
3. **Documentação Acadêmica (`README.md` e `prompts.md`):** Apoio na padronização textual e formatação das tabelas e seções descritivas.

*(Conforme destacado na seção 1, o Diagrama UML de Casos de Uso e os Wireframes/Protótipo de Média Fidelidade foram elaborados e desenhados exclusivamente pela equipe, sem geração por IA).*

---

## 4. Como o Grupo Verificou, Testou e Corrigiu os Resultados da IA

A revisão crítica e técnica realizada pelos alunos identificou e corrigiu desvios relevantes gerados pelas ferramentas:

1. **Correção da definição do índice GPCT (Alucinação detectada no Slide 10):** Na primeira redação sugerida pela IA para os textos dos slides, a sigla `GPCT` foi incorretamente expandida como *"Grau de Prioridade Crítica Territorial"*. A equipe identificou a inconsistência, consultou o código de [`riskCalculator.js`](../04%20-%20Front-end%20Design/src/utils/riskCalculator.js) e o relatório de Cálculo (`zelasp-math`), e corrigiu o texto para o nome oficial: **Gatilho Preditivo de Contingência Territorial**, mantendo os limiares operacionais reais (`≥2` Atenção / `≥4` Contingência) e a formulação diferencial ($q(t) \ge 30$ com $q'(t) > 0$).
2. **Alinhamento factual com dados oficiais e separação de métricas (Slide 02 e Slide 11):** A IA havia sugerido estimativas vagas e arredondadas (como *"500 mil chamados"*). A equipe substituiu essas menções pelos dados públicos oficiais da **Prefeitura de São Paulo / SMIT** (**~2 milhões de demandas solucionadas/ano na rede SP 156 nas 32 Subprefeituras**), separando com precisão o que é estimativa de tempo do formulário legado (**5–8 min**), o que é resultado de simulação matemática em 24h (**~1,4x** chamados repetidos, **2h** de antecipação e **−38,5%** de backlog em `zelasp-math`) e o que são metas futuras de roadmap (**META · SUS ≥ 85**, **META · −45%** chamados duplicados).
3. **Conferência literal com o código React publicado (`zelasp-web.vercel.app`):**
   * A IA havia criado frases fictícias no slide de **Tom de Voz** (Slide 08). O grupo substituiu todas elas por cópias literais das mensagens de interface reais presentes em `Header.jsx`, `App.jsx` e `viaCepService.js`.
   * Ajustamos o requisito `RF01` para especificar as **6 categorias** oficiais do formulário (`CATEGORIAS_ZELA`), alinhamos a regra `RN02` ao código do motor de risco (**≥ 10 apoios comunitários → +1 nível**, limite 5) e atualizamos os números do Painel Gestor (Slide 07) para a fila inicial real (`05 Pendentes`, `04 Prioridade máxima`).
4. **Adequação ao Edital e Refinamento de Apresentação:** A equipe inseriu cards explicativos no Slide 12 justificando a contribuição do ZelaSP às metas dos **ODS 11 e 9** (em coerência com Python, Matemática e Web), ampliou a Tela 01 para listar os 6 botões de categoria e comandou a substituição de emojis por ícones vetoriais SVG, eliminando ruídos visuais.
5. **Inspeção visual página a página:** As 12 páginas de `Apresentacao_TX_Design_ZelaSP.pdf` foram inspecionadas pela equipe para assegurar legibilidade em tela cheia, conformidade de contraste e proporção `16:9` sem qualquer quebra de layout.

---

## 5. Análise Crítica (Benefícios, Limitações e Dificuldades)

* **Benefícios:** A utilização de IA generativa acelerou a escrita do código HTML/CSS da apresentação de slides, garantiu agilidade na aplicação de estilos visuais e na conversão para ícones SVG, e serviu como excelente ferramenta de apoio para revisão textual, concisão e adequação da linguagem técnica.
* **Limitações e Dificuldades:** Ferramentas de IA frequentemente introduzem alucinações técnicas (como inventar significados para siglas internas do projeto), propõem números imprecisos sem citar fontes oficiais e sugerem textos genéricos que não condizem com a experiência real do produto. A modelagem da arquitetura de software (casos de uso UML), o design dos wireframes, a avaliação heurística e o cruzamento com o código-fonte implementado exigiram a atuação direta, o discernimento e a responsabilidade técnica exclusiva dos alunos da equipe.
