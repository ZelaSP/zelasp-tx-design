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

* **Google Antigravity (Claude & Gemini):** Utilizada como assistente na organização estrutural dos 7 blocos da apresentação executiva, revisão das justificativas individuais de Requisitos Funcionais (RF), Requisitos Não Funcionais (RNF) e Regras de Negócio (RN), geração dos scripts Python (`ReportLab` e `Matplotlib`) para diagramação visual do Diagrama UML de Casos de Uso, Fluxo do Protótipo de Média Fidelidade e Roadmap, além de apoio na formatação visual e redação dos textos.

---

## 2. Prompts Utilizados durante o Desenvolvimento

### Prompt 1 — Estruturação e Justificativa Individual de RF, RNF e RN
> *"Com base no escopo do ZelaSP (relato em menos de 15 segundos com ViaCEP e GPS, apoio comunitário +1 para evitar chamados duplicados e painel de triagem da Prefeitura com índice GPCT), estruture os Requisitos Funcionais (RF), Requisitos Não Funcionais (RNF) e Regras de Negócio (RN). Conforme exigido pelo edital, não faça apenas uma lista: para cada item, explicite a descrição, a classificação (por que pertence àquela categoria) e a justificativa ligada ao problema real das ruas de São Paulo."*

### Prompt 2 — Modelagem do Diagrama UML de Casos de Uso e Contextualização
> *"Gere um Diagrama UML de Casos de Uso legível para a plataforma ZelaSP contendo os atores Cidadão, Agente Municipal da Subprefeitura, API Externa ViaCEP e Nó IoT ESP32, destacando as relações <<include>> e <<extend>> entre os casos de uso e uma tabela contextualizando quem é cada ator, o que faz e qual objetivo pretende alcançar."*

### Prompt 3 — Mapeamento das Heurísticas de Nielsen, Tom de Voz e Roadmap
> *"Relacione as telas do nosso protótipo web ZelaSP (Abertura animada com os 4 problemas, Login por perfil, Área do Cidadão e Painel da Prefeitura) com as Heurísticas de Usabilidade de Jakob Nielsen, apontando onde cada heurística aparece nas telas. Em seguida, organize a tabela de Tom de Voz com os textos reais de botões e avisos da interface e estruture o Roadmap em 4 etapas lógicas."*

### Prompt 4 — Apoio na Formatação dos Slides em PDF e Escrita dos Textos
> *"Ajude na formatação visual da apresentação de slides em formato widescreen (16:9) em PDF e ajude a escrever e revisar os textos de cada bloco para que a história fique clara, direta e bem conectada entre problema, solução, experiência do usuário e próximos passos."*

---

## 3. Funcionalidades e Artefatos Desenvolvidos com Auxílio da IA

1. **Apresentação Executiva de 10 Slides em PDF (`Apresentacao_TX_Design_ZelaSP.pdf`):** Gerada em formato 16:9 (`960x540 pt`) cobrindo os 7 entregáveis obrigatórios (Capa, Problema, Escopo Dentro/Fora, RF/RNF/RN justificados, Diagrama UML e Contextualização, Protótipo/Heurísticas/Tom de Voz e Roadmap).
2. **Diagramas Visuais de Engenharia e UX (`assets/`):**
   * `diagrama_casos_de_uso.png`: Diagrama UML com fronteira do sistema, 4 atores e 10 casos de uso.
   * `prototipo_media_fidelidade.png`: Fluxo navegável das 4 telas com marcação das heurísticas H1 a H8.
   * `roadmap_evolucao.png`: Sequência de evolução do projeto em 4 fases.
3. **Documentação Completa e Ficha da CitizenTech (`README.md`):** Consolidação da proposta e rastreabilidade entre requisitos, casos de uso e telas do protótipo.

---

## 4. Como o Grupo Verificou, Testou e Ajustou os Resultados

1. **Verificação da Regra de Justificativa Obrigatória (Slide 46 do Edital):** Conferimos item por item nas tabelas de `RF01–RF06`, `RNF01–RNF04` e `RN01–RN04` para garantir que nenhum requisito ficasse apenas listado sem explicar *por que pertence àquela categoria* e *por que é necessário para o usuário*.
2. **Coerência Real entre Requisitos, UML e Protótipo na Vercel:** Validamos que todos os casos de uso do diagrama (`UC01` a `UC10`) e todos os textos citados na seção de **Tom de Voz** correspondem fielmente às funcionalidades e botões reais que implementamos em [https://zelasp-web.vercel.app/](https://zelasp-web.vercel.app/).
3. **Inspeção Visual Slide a Slide:** Inspecionamos todas as 10 páginas do arquivo `Apresentacao_TX_Design_ZelaSP.pdf` para confirmar ausência de sobreposição de texto, contraste adequado e legibilidade das tabelas e diagramas.

---

## 5. Análise Crítica (Benefícios, Limitações e Dificuldades)

* **Benefícios:** O uso da IA permitiu diagramar uma apresentação técnica limpa em 16:9 e gerar o Diagrama UML de Casos de Uso e o fluxo de wireframes de média fidelidade em alta resolução, mantendo total alinhamento com o que já havíamos construído em Python, Matemática e React.
* **Limitações e Dificuldades:** Inicialmente, descrições genéricas tendem a misturar Requisitos Funcionais com Regras de Negócio. Foi fundamental a revisão conceitual da equipe para separar claramente *ações do sistema* (`RF`), *atributos de qualidade/desempenho* (`RNF`) e *condições de domínio e alçada* (`RN`), amarrando cada item aos bairros reais de São Paulo.
