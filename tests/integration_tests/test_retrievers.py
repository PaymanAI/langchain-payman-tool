from typing import Type

from langchain_payman_tool.retrievers import PaymanAIRetriever
from langchain_tests.integration_tests import (
    RetrieversIntegrationTests,
)


class TestPaymanAIRetriever(RetrieversIntegrationTests):
    @property
    def retriever_constructor(self) -> Type[PaymanAIRetriever]:
        """Get an empty vectorstore for unit tests."""
        return PaymanAIRetriever

    @property
    def retriever_constructor_params(self) -> dict:
        return {"k": 2}

    @property
    def retriever_query_example(self) -> str:
        """
        Returns a dictionary representing the "args" of an example retriever call.
        """
        return "example query"
