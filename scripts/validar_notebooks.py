"""Valida e executa notebooks em kernels novos sem sobrescrever as fontes."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient


def main():
    raiz = Path(__file__).resolve().parents[1]
    arquivos = sorted((raiz / "notebooks").rglob("*.ipynb"))
    if not arquivos:
        raise RuntimeError("Nenhum notebook encontrado.")
    for caminho in arquivos:
        notebook = nbformat.read(caminho, as_version=4)
        nbformat.validate(notebook)
        cliente = NotebookClient(
            notebook, timeout=120, kernel_name="python3",
            resources={"metadata": {"path": str(caminho.parent)}},
        )
        cliente.execute()
        destino = raiz / "build" / "executed" / caminho.relative_to(raiz / "notebooks")
        destino.parent.mkdir(parents=True, exist_ok=True)
        nbformat.write(notebook, destino)
        print(f"OK: {caminho.relative_to(raiz)}")
    print(f"{len(arquivos)} notebook(s) executado(s) sem erros.")


if __name__ == "__main__":
    main()
