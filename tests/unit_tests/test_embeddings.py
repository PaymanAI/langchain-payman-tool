"""Test embedding model integration."""

from typing import Type

from langchain_payman_tool.embeddings import PaymanAIEmbeddings
from langchain_tests.unit_tests import EmbeddingsUnitTests


class TestParrotLinkEmbeddingsUnit(EmbeddingsUnitTests):
    @property
    def embeddings_class(self) -> Type[PaymanAIEmbeddings]:
        return PaymanAIEmbeddings

    @property
    def embedding_model_params(self) -> dict:
        return {"model": "nest-embed-001"}
