# mcp_news

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como instalar no Claude Desktop](#como-instalar-no-claude-desktop)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

Este projeto `mcp_news` oferece uma ferramenta para buscar e resumir notícias da web. Utilizando o protocolo MCP (Model Context Protocol), ele permite que um modelo de linguagem interaja com uma ferramenta de busca de notícias de forma segura, por meio de uma senha, e apresente os resultados de forma estruturada. A ideia é fornecer um resumo conciso e direto ao ponto sobre um determinado tema, simulando o trabalho de apuração jornalística.

## Estrutura do projeto

Este projeto leva em consideração as explicações do professor Sandeco Macedo, da UFG (Universidade Federal de Goiás), sobre MCPs por meio do livro [MCP e A2A para Leigos
](https://physia.com.br/mcp/). É um MCP-Server simples que utiliza somente o pacote FastMCP, seguindo também as orientações do repositório oficial do [Model Context Protol](https://github.com/modelcontextprotocol/python-sdk), da Anthropic.

Este MCP-Server tem as seguintes classes: 

* tool `search_news`:
    * Esta ferramenta é responsável por realizar a busca de notícias na web.
    * Argumentos:
        * `pesquisa` (str): O termo ou tema a ser pesquisado.
        * `senha` (str): Uma senha para autorizar o uso da ferramenta.
    * Funcionamento: Se a senha fornecida estiver correta (conforme definido em um arquivo `.env`), a ferramenta utiliza `WebSearchTool` (de `smolagents`) para buscar a notícia. Caso contrário, retorna uma mensagem de erro.
    * Retorno: O resultado da busca ou uma mensagem de erro.
* prompt `acesso`:
    * Este prompt é projetado para ser usado por um modelo de linguagem. Ele instrui o modelo a atuar como um jornalista experiente.
    * Argumentos (para o modelo preencher e depois usar na tool):
        * `senha` (str): A senha para acessar a `tool search_news`.
        * `tema` (str): O tema da pesquisa de notícias.
    * Funcionamento: O prompt guia o modelo a:
        1.  Verificar a senha.
        2.  Formular uma consulta de pesquisa combinando o `tema` com a palavra "news".
        3.  Chamar a `tool search_news` com a consulta e a senha.
        4.  Com base nos resultados da tool, criar um resumo da notícia em um formato específico (Título, parágrafo 1: Resumo, parágrafo 2: Contexto adicional).
    * Retorno: Uma string formatada contendo o resumo da notícia ou uma indicação de falha se a senha estiver incorreta.
 
Se quiser conversar sobre esse projeto, basta acessar a versão [TalkToGitHub](https://talktogithub.com/marioluciofjr/mcp_news)

Want to better understand this repository, but you don't speak Portuguese? Check out this complete tutorial: [`Codebase - mcp_news`](https://code2tutorial.com/tutorial/a67c8977-c7d2-49de-8374-c601a2893a00/index.md)


## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/c0604008-f730-413f-9c4e-9b06c0912692" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/cf957637-962d-4548-87d4-bbde91fadc22" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/18c95cc3-d8bc-486c-b0cf-b5d128980176" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/abafaea5-eb57-4965-9130-7816280a8d84" />&nbsp;&nbsp;&nbsp
 </div><br>

* MCP (Model Context Protocol);
* Python;
* Claude Desktop;
* VSCode;
* Powershell.

## Requisitos

* Python instalado (versão 3.10 ou superior);
* Pacote `uv` instalado;
* Claude Desktop instalado.

## Como instalar no Claude Desktop

Agora vou detalhar um passo a passo no Windows 11, utilizando o terminal (atalho `CTRL` + `J`) no VSCode: 

1. Instalei a [versão mais atualizada do Python](https://www.python.org/downloads/)
2. Já no VSCode, utilize o terminal para verificiar a versão do python com o comando
   ```powershell
   python --version
   ```
3. Depois instale o `uv` com o comando
   ```powershell
   pip install uv
   ```
4. Para conferir se estava tudo certo, utilize o comando
   ```powershell
   uv
   ```
5. Faça o download do zip desse projeto para a sua máquina pelo caminho `Code` > `Download ZIP` aqui mesmo no GitHub. Descompacte a pasta no diretório que preferir.

6. No VSCode use o caminho `CTRL` + `O` e escolha a pasta que acabou de descompactar

7. Voltando ao terminal, utilize o comando abaixo para inicializar um novo projeto Python, criando arquivos de configuração e dependências automaticamente
   ```powershell
   uv init
   ```
8. Adicione as dependências necessárias deste projeto
    ```powershell
    uv add mcp[cli] dotenv smolagents[toolkit]
    ```
9. Verifique se está tudo ok, com o comando abaixo
    ```powershell
    mcp
    ```

> [!IMPORTANT]
> Se aparecer esta informação abaixo no seu terminal é porque está tudo certo
> 
> ![Image](https://github.com/user-attachments/assets/7c692a88-929e-4b8c-84df-b8ce0f004139)

10. Renomeie o arquivo `.env.example` clicando nele e usando o atalho F2 do teclado. Renomeie como `.env` somente.

11. Instale o json abaixo do MCP-Server diretamente no arquivo `claude_desktop_config.json`
    ```json
    "news": {
      "command": "uv",
      "args": [
        "--directory",
        "C://Users//meu_usuario//OneDrive//area_de_trabalho//MCPs//mcp_news",
        "run",
        "server.py"
      ]
    }
    ```
> [!IMPORTANT]
> O meu diretório foi algo parecido com isso "C://Users//meu_usuario//OneDrive//area_de_trabalho//MCPs//mcp_news", mas é óbvio que você deve colocar o seu caminho para a pasta `mcp_news`
> 

> [!IMPORTANT]
> Se você já instalou o Claude Desktop corretamente, siga o caminho para acessar o arquivo `claude_desktop_config.json` no seu computador\
> 11a. Com o Claude Desktop aberto, utilize o atalho `CTRL` + `,`\
> 11b. Clique na aba `Desenvolvedor` e depois em `Editar configuração`\
> 11c. Procure o arquivo `claude_desktop_config.json` e edite no VSCode corretamente\
> 11d. Salve o arquivo com `CTRL` + `S`\
> 11e. Feche o Claude Desktop e abra novamente depois de alguns segundos\
> 11f. Confira no ícone de configuração se a ferramenta do MCP `mcp_news` está instalada corretamente
>
> ![Image](https://github.com/user-attachments/assets/6553bcd2-1f3c-4963-9d6a-15b0dc614edd)
>
> A ferramenta foi nomeada como `search_news`.
>
> 11g. Para utilizar, você deve clicar no ícone de '+' e, na opção `Adicionar do news`, clicar no no prompt chamado `acesso`.
> Ao clicar no prompt `acesso`, aparecerá um formulário. Basta preencher e clicar no botão `Adicionar prompt` e executar no Claude Desktop.

## Links úteis

* [Documentação oficial do Model Context Protocol](https://modelcontextprotocol.io/introduction) - Você saberá todos os detalhes dessa inovação da Anthropic
* [Site oficial da Anthropic](https://www.anthropic.com/) - Para ficar por dentro das novidaddes e estudos dos modelos Claude
* [Como baixar o Claude Desktop](https://claude.ai/download) - Link direto para download
* [Como instalar o VSCode](https://code.visualstudio.com/download)- Link direto para download
* [Documentação oficial do pacote uv](https://docs.astral.sh/uv/) - Você saberá todos os detalhes sobre o `uv` e como ele é importante no python
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) - site muito bom para conseguir ícones do ecossistema de IA
* [Devicon](https://devicon.dev/) - site bem completo também com ícones gerais sobre tecnologia
* [Smolagents](https://github.com/huggingface/smolagents) - documenttação oficial da biblioteca smolagents


## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/mcp_news/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 
