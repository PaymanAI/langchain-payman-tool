from importlib import metadata

from langchain_payman_tool.chat_models import ChatPaymanAI
from langchain_payman_tool.document_loaders import PaymanAILoader
from langchain_payman_tool.embeddings import PaymanAIEmbeddings
from langchain_payman_tool.retrievers import PaymanAIRetriever
from langchain_payman_tool.toolkits import PaymanAIToolkit
from langchain_payman_tool.tools import PaymanAITool
from langchain_payman_tool.vectorstores import PaymanAIVectorStore

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "ChatPaymanAI",
    "PaymanAIVectorStore",
    "PaymanAIEmbeddings",
    "PaymanAILoader",
    "PaymanAIRetriever",
    "PaymanAIToolkit",
    "PaymanAITool",
    "__version__",
]
