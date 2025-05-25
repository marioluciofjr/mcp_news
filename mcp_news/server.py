# server.py

from mcp.server.fastmcp import FastMCP 
from typing import Annotated
from pydantic import Field
import os
from dotenv import load_dotenv
from smolagents import WebSearchTool

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

senha_correta = os.getenv("SENHA")

# Inicializa o servidor FastMCP 
mcp = FastMCP("news")

@mcp.tool(name="search_news")
def search_news(pesquisa: str, senha: str):
	"""
	Ferramenta protegida por senha. Se a senha estiver correta, o resultado será mostrado.
	"""
	search_tool = WebSearchTool()
      
	if senha != senha_correta:
		resultado = "Erro: Senha incorreta ou não fornecida."
	else:
		# Ação protegida
		resultado = search_tool(f"{pesquisa}")
	return resultado

@mcp.prompt()
def acesso(
	senha: Annotated[str, Field(description="""Digite a senha correta para acessar a tool""")], 
	tema: Annotated[str, Field(description="""Digite o tema da pesquisa""")]) -> str:
	"""
	Prompt que libera o acesso para utilizar a tool 'search_news'. Tem como argumentos a senha, que é alfanumérica e deve 
	ser digitada corretamente e o tema de pesquisa.
	"""

	prompt = f"""
	<função>
	Você é uma jornalista experiente que sabe apurar bem uma notícia. Você não cai em fake news e sabe exatamente o valor de noticiar 
	algo com embasamento. Você entende a importância de manter sua credibilidade jornalística.
	</função>

	<contexto>
	Você só exercerá seu trabalho se a senha definida como {senha} estiver correta na tool 'search_news'.
	</contexto>

	<tarefa>
	Foque sua pesquisa mesclando a palavra-chave definida por {tema} + a palavra 'news'. Salve isso em um placeholder chamado 'pesquisa'.
	Esse placeholder será o argumento na tool 'search_tool'.
	</tarefa>
	"""

	return prompt

if __name__ == "__main__":
    mcp.run(transport='stdio')

