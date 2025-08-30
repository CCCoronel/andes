---
sidebar_position: ?
title: Andes Lib Architecture
---

## Visão Geral dos Módulos

```
src/
├── application/ # Aplicações de alto nível (builders, creators, parsers)
├── documentation/ #Integração com Docusaurus
├── graph/ # Manipulação de grafos
├── model/ # Definições de modelos e tipos
├── renders/ # Renderização em diferentes formatos

```

---

## Módulos

### 1. `application/`
Contém a **lógica de aplicação** que orquestra os modelos e gera artefatos.

- **`domain/`** → Construção do domínio principal (ex.: `BuildDomain.ts`).
- **`proporse/`** → Propósito e escopo dos módulos.
- **`requisits/`** → Parsers de requisitos (`GraphParser`, `TableParser`, `RequirementsExtractor`).
- **`usercase/`** → Criação e parsing de casos de uso.
- **`made/`** → Criação de aplicações baseadas em **defaults** (backlog, épicos, stories).
- **Arquivos raiz** → `ApplicationCreator.ts`, `DocusaurusCreator.ts`, `IO.ts`.

> ⚡ Papel: transformar os modelos (em `model/`) em aplicações utilizáveis/documentáveis.

---

### 2. `documentation/`
Integração com **Docusaurus**, incluindo geração de diagramas e casos de uso.

- **`docusaurus/`**
  - `ClassDiagram.ts` → Criação de diagramas de classes.
  - `ModelUseCases.ts` → Documentação de casos de uso.
  - `DocksaurusService.ts` → Serviço central de integração.
  - `application.ts` → Orquestrador.

> ⚡ Papel: geração automática de documentação visual e técnica.

---

### 3. `graph/`
- Contém `graph.ts`, responsável por manipulação de grafos usados em parsing, análise de requisitos e geração de modelos.

> ⚡ Papel: suporte estrutural para relacionamentos entre entidades.

---

### 4. `model/`
Define a **estrutura central do domínio**.

- **`andes/`** → Classes e tipos de análise, projetos e requisitos.
- **`made/`** → Classes ligadas a backlog, roadmap, sprint, tasks e times.
- **`spark/`** → Estruturas de entidades, enums, pacotes e herança.

> ⚡ Papel: representar formalmente os elementos modelados pela linguagem Andes.

---

### 5. `renders/`
Camada responsável por **exportar e visualizar** os modelos em diferentes formatos.

- **`dsl/`**
  - `made/` e `spark/` → Renders de elementos das DSL.
- **`markdown/`**
  - `MermaidRender.ts` → Geração de diagramas em Mermaid (flowchart, statemachine).
  - `FileRender.ts`, `MarkdownRender.ts` → Renderização de arquivos Markdown.
- **`plantuml/`**
  - `PlantUmlRender.ts`, `classDiagram.ts` → Geração de diagramas UML.
- **Outros renders** → `TableRender.ts`, `SectionRender.ts`, `ParagraphRender.ts`, etc.

> ⚡ Papel: transformar modelos em representações visuais e documentais.

---

## Fluxo Arquitetural

1. **Modelagem** → O usuário define projetos, requisitos, casos de uso e backlog (em `model/`).
2. **Aplicação** → O módulo `application/` processa os modelos, gera representações e prepara para documentação.
3. **Graph** → Dá suporte estrutural na organização e relações entre entidades.
4. **Documentação** → `documentation/` gera documentos estruturados e integra com Docusaurus.
5. **Renderização** → `renders/` exporta em Markdown, UML, Mermaid e outros formatos visuais.