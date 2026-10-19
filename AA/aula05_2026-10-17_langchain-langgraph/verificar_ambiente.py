import sys
from importlib import import_module
from importlib.metadata import version
print("Python:", sys.version.split()[0])
for pacote, modulo in [("requests", "requests"), ("pydantic", "pydantic"),
                        ("langchain-core", "langchain_core"),
                        ("langgraph", "langgraph"),
                        ("langchain-ollama", "langchain_ollama")]:
    import_module(modulo)
    print(pacote, version(pacote))
print("Imports prontos. Servidor Ollama e modelo não foram testados.")
