import sys
import os
from typing import List

# Adiciona o diretório wiseA ao sys.path para garantir que o módulo Wtool seja encontrado
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import cohere
import dotenv
from Wtool import Wtools

dotenv.load_dotenv()

# Obtém a chave da API do ambiente
key = os.getenv("cohere_api_key")

def gerar_txt(prompt: str) -> str:
    """
    Gera uma resposta de texto usando a API do Cohere.

    Args:
        prompt (str): O prompt fornecido pelo usuário.

    Returns:
        str: A resposta gerada ou uma mensagem de erro.
    """
    try:
        co = cohere.Client(key)
        response = co.chat(
            message=prompt,
            temperature=0.7,
            max_tokens=30
        )
        return response.text.strip()
    except Exception as e:
        return f"Erro ao gerar texto: {str(e)}"

class Wass:
    """
    Classe principal para seleção de ferramentas com base na entrada do usuário.

    Attributes:
        user_input (str): Entrada do usuário.
        tools (List[Wtools]): Lista de ferramentas disponíveis.
        prompt (str): Prompt gerado para a API.
        response (str): Resposta gerada pela API.
    """
    def __init__(self, user_input: str, tools: List[Wtools]):
        self.user_input = user_input
        self.tools = tools

        # Criar uma descrição detalhada de cada ferramenta
        tools_description = "\n".join([
            f"""
        - {tool.tool}:
          Descrição: {tool.description}
          Quando usar: {tool.usage}
          Palavra de execução: {tool.keypass}
        """ for tool in tools
        ])

        self.prompt = f"""Você é um assistente especializado em seleção de ferramentas. Sua única função é decidir qual ferramenta usar ou responder diretamente.

        FERRAMENTAS DISPONÍVEIS:
        {tools_description}

        PERGUNTA DO USUÁRIO: {self.user_input}

        INSTRUÇÕES:
        1. Analise as condições \"quando usar\" de cada ferramenta
        2. Se a pergunta corresponder às condições, retorne APENAS a palavra de execução EXATA (exemplo: >calendarshit< ou >weatherforecast<)
        3. Se não houver correspondência, responda diretamente à pergunta
        4. NÃO adicione explicações
        5. Seja preciso na correspondência das condições

        RESPOSTA:"""
        self.response = gerar_txt(self.prompt)

if __name__ == "__main__":
    user_input = "lembrar de ir trabalhar amanhã"
    tools = [
        Wtools(
            tool="mostrar calendario",
            usage="Quando o utilizador pede para ver o seu calendário ou algo relacionado ao dia ou mês",
            description="Mostra o calendário do utilizador",
            keypass=">calendarshit<"
        ),
        Wtools(
            tool="previsão do tempo",
            usage="Quando o utilizador pergunta sobre o clima ou condições meteorológicas apenas, nao sera relacionada a dia ou mes",
            description="Fornece a previsão do tempo atualizada",
            keypass=">ver o clima<"
        ),
        Wtools(
            tool="definir lembrete",
            usage="Quando o utilizador quer definir um lembrete para uma tarefa ou evento futuro",
            description="Define um lembrete para o utilizador",
            keypass=">setreminder<"
        )
    ]
    assistant = Wass(user_input, tools)
    print(assistant.response)


