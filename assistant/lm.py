import cohere
import os
import json
import dotenv

dotenv.load_dotenv()

key = os.getenv("cohere_api_key")

def gerar_txt(prompt):
    try:
        co = cohere.Client(key)
        response = co.chat(
            message=prompt,  # Corrigido para usar o argumento correto
            temperature=0.7,
            max_tokens=30
        )
        return response.text.strip()  # Corrigido para acessar o atributo correto
    except Exception as e:
        return f"Erro: {str(e)}"

def agentwise(prompt, json_tools):
    try:
        with open(json_tools, 'r', encoding='utf-8') as f:
            tools = json.load(f)

        ferramentas = []
        for nome, info in tools.items():
            ferramentas.append(f"- {nome}: {info.get('descriçao', '')} | quando usar: {info.get('quando usar', '')} | palavra de execução: {info.get('palavra de execuçao da ferramenta', '')}")
        ferramentas_str = '\n'.join(ferramentas)

        base_prompt = f"""Você é um assistente especializado em seleção de ferramentas. Sua única função é decidir qual ferramenta usar ou responder diretamente.

FERRAMENTAS DISPONÍVEIS:
{ferramentas_str}

PERGUNTA DO USUÁRIO: {prompt}

INSTRUÇÕES:
1. Analise as condições "quando usar" de cada ferramenta
2. Se a pergunta corresponder às condições, retorne APENAS a palavra de execução EXATA
3. Se não houver correspondência, responda diretamente à pergunta
4. NÃO adicione explicações
5. Seja preciso na correspondência das condições

RESPOSTA:"""

        resposta = gerar_txt(base_prompt)
        return resposta.strip()
        
    except Exception as e:
        return f"Erro: {str(e)}"
    
if __name__ == "__main__":
    pergunta = "que dia e hoje?"
    json_tools = "C:\\Users\\marco\\Documents\\wiserAI\\libs-by\\decision\\tools.json"
    resposta = agentwise(pergunta, json_tools)
    print(resposta)