from dataclasses import dataclass
from qdrant_client import QdrantClient
from flare_ai_rag.ai import GeminiEmbedding
from flare_ai_rag.retriever.config import RetrieverConfig

@dataclass
class AppState:
    """Global application state container"""
    qdrant_client: QdrantClient | None = None
    retriever_config: RetrieverConfig | None = None
    embedding_client: GeminiEmbedding | None = None

# Global state instance
app_state = AppState() 