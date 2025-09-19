class Wtools:
    """
    Classe que representa uma ferramenta com informações sobre seu uso, descrição e palavra-chave.

    Attributes:
        tool (str): Nome da ferramenta.
        usage (str): Quando a ferramenta deve ser usada.
        description (str): Descrição da ferramenta.
        keypass (str, optional): Palavra-chave para executar a ferramenta.
    """
    def __init__(self, tool: str, usage: str, description: str, keypass: str = None):
        self.tool = tool
        self.usage = usage
        self.description = description
        self.keypass = keypass

    def __str__(self) -> str:
        """
        Retorna uma representação em string da ferramenta.

        Returns:
            str: Representação em string da ferramenta.
        """
        return f"Tool: {self.tool} - {self.description}"

    def __repr__(self) -> str:
        """
        Retorna uma representação detalhada da ferramenta para desenvolvedores.

        Returns:
            str: Representação detalhada da ferramenta.
        """
        return f"Wtools('{self.tool}', '{self.usage}', '{self.description}', '{self.keypass}')"

    def to_json(self) -> dict:
        """
        Converte a ferramenta para um dicionário serializável em JSON.

        Returns:
            dict: Dicionário com os atributos da ferramenta.
        """
        return {
            "tool": self.tool,
            "usage": self.usage,
            "description": self.description,
            "keypass": self.keypass
        }

    @classmethod
    def from_json(cls, data: dict):
        """
        Cria uma instância de ferramenta a partir de dados JSON.

        Args:
            data (dict): Dados JSON contendo os atributos da ferramenta.

        Returns:
            Wtools: Instância da ferramenta criada.
        """
        return cls(
            tool=data.get("tool"),
            usage=data.get("usage"),
            description=data.get("description"),
            keypass=data.get("keypass")
        )

    @staticmethod
    def tools_to_json(tools: list) -> dict:
        """
        Converte uma lista de ferramentas para um dicionário serializável em JSON.

        Args:
            tools (list): Lista de instâncias de Wtools.

        Returns:
            dict: Dicionário contendo as ferramentas e seus atributos.
        """
        return {
            tool.tool: {
                "descrição": tool.description,
                "quando usar": tool.usage,
                "caso de uso": "no caso de uso retorne apenas palavra de execução da ferramenta",
                "palavra de execução da ferramenta": tool.keypass
            }
            for tool in tools
        }

if __name__ == "__main__":
    tool1 = Wtools(
        tool="mostrar calendario",
        usage="Quando o utilizador pede para ver o seu calendário ou algo relacionado ao dia ou mês",
        description="Mostra o calendário do utilizador",
        keypass=">calendarshit<"
    )

    tool2 = Wtools(
        tool="exemplo",
        usage="uso do exemplo",
        description="descrição do exemplo",
        keypass="chave do exemplo"
    )

    tools = [tool1, tool2]
    print(Wtools.tools_to_json(tools))
