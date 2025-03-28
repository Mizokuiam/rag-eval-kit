# rag_eval_kit/__init__.py
"""
rag-eval-kit: A toolkit for evaluating Retrieval-Augmented Generation pipelines.
Provides functions to assess retriever performance (precision, recall) and
generator performance (faithfulness, answer relevancy) using ground truth data
and LLM-as-a-judge techniques.
"""
from .core import (
    calculate_retrieval_metrics,
    evaluate_faithfulness,
    evaluate_relevancy,
    run_evaluation,
    DEFAULT_FAITHFULNESS_PROMPT_TEMPLATE,
    DEFAULT_RELEVANCY_PROMPT_TEMPLATE,
)

__version__ = "0.1.0"

__all__ = [
    "calculate_retrieval_metrics",
    "evaluate_faithfulness",
    "evaluate_relevancy",
    "run_evaluation",
    "DEFAULT_FAITHFULNESS_PROMPT_TEMPLATE",
    "DEFAULT_RELEVANCY_PROMPT_TEMPLATE",
    "__version__",
]
