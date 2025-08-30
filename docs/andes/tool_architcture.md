---
sidebar_position: ?
title: Andes Architecture
---

## Visão Geral

O projeto está dividido em três grandes partes:

- **CLI (`src/cli/`)** → Interface de linha de comando, responsável por interagir com o usuário via terminal e executar comandos.
- **Extensão (`src/extension/`)** → Ponto de entrada para a extensão (ex.: VSCode).
- **Linguagem (`src/language/`)** → Definições da DSL (baseada em Langium), incluindo gramática, validação e escopo.

---

## Estrutura de Diretórios

### `src/cli/`
Contém a implementação da **CLI** e seus utilitários.

- **`artifacts/`**
  - **`bdd/`**
    - `BDDService.ts` → Serviço principal para execução de cenários BDD.
    - `application.ts` → Aplicação que integra BDD ao restante da CLI.
    - `generator.ts` → Geração de arquivos relacionados a BDD.
  - **`generative_ai/`**
    - `application.ts` → Integração com ferramentas de IA.
  - **`graph/`**
    - `graph.ts` → Manipulação e geração de grafos.
  - **`made/`**
    - `application.ts` → Serviço específico para geração/execução de artefatos *made*.
  - **`spark/`**
    - `application.ts` → Serviço específico para geração/execução de artefatos *spark*.
  - **`util/`**
    - `envLoader.ts` → Utilitário para carregar variáveis de ambiente.

- **`vscode_util/`**
  - `vscodeutil.ts` → Funções utilitárias para integração com VSCode.
  
- **Arquivos principais da CLI**
  - `cli-util.ts` → Funções comuns para execução da CLI.
  - `generator-utils.ts` → Funções auxiliares para os geradores.
  - `generator.ts` → Orquestrador da geração de artefatos.
  - `main.ts` → Ponto de entrada da CLI.
  - `translate-utils.ts` → Traduz objetos gerados pelo **Langium** para objetos que podem ser interpretados pela biblioteca principal.

---

### `src/extension/`
Contém a extensão (integração com VSCode).

- `main.ts` → Ponto de entrada da extensão, inicializa a comunicação entre editor e linguagem.

---

### `src/language/`
Aqui fica o **coração da DSL**, construída com **Langium**.

- Arquivos de definição da linguagem:
  - `andes.langium` → Gramática principal da linguagem Andes.
  - `entities.langium` → Definição de entidades.
  - `helpers.langium` → Regras auxiliares.
  - `requirement.langium` → Definição de requisitos.
  - `terminals.langium` → Definição de tokens/terminais.
  - `usecase.langium` → Definição de casos de uso.

- Arquivos TypeScript de suporte:
  - `andes-module.ts` → Módulo principal que conecta as partes da linguagem.
  - `andes-scope.ts` → Regras de escopo e resolução de referências.
  - `andes-validator.ts` → Validações semânticas da linguagem.
  - `main.ts` → Ponto de inicialização da linguagem.
  - `main-browser.ts` → Inicialização voltada para ambiente de navegador.

---

## Fluxo Arquitetural

1. **Usuário executa CLI**  
   - Entrada em `src/cli/main.ts`.
   - Invoca módulos como BDD, geração de grafos e arquivos made, spark etc.
   - Quando precisa interpretar modelos da linguagem, usa `translate-utils.ts`.

2. **Extensão (VSCode)**  
   - Carregada via `src/extension/main.ts`.
   - Usa a definição da DSL em `src/language/` para parsing, validação e escopo.
   - Exibe feedback no editor.

3. **Linguagem (Langium)**  
   - DSL definida em `.langium` files.
   - Parsing + validação → gera AST.
   - O **AST é traduzido por `translate-utils.ts`** para objetos de domínio que os módulos da CLI entendem.

---
