from __future__ import annotations


def baixar_texto(url: str, timeout: int = 15) -> str:
    """TODO: baixar o conteúdo textual de uma URL.

    O que implementar:
    1. Validar se a URL é http/https.
    2. Fazer request com `requests.get(url, timeout=timeout)`.
    3. Tratar erros de conexão e HTTP (requests.exceptions.RequestException).
    4. Opcionalmente validar `Content-Type` para evitar conteúdo não textual.
    5. Retornar `response.text`.
    """
    raise NotImplementedError("TODO: implementar download do texto com requests")
