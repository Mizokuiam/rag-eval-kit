# rag-eval-kit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org)
[![CI Status](https://github.com/Mizokuiam/rag-eval-kit/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Mizokuiam/rag-eval-kit/actions/workflows/python-ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- [![PyPI version](https://badge.fury.io/py/rag-eval-kit.svg)](https://badge.fury.io/py/rag-eval-kit) --> <!-- Placeholder for when published -->

A lightweight, modular Python toolkit for evaluating Retrieval-Augmented Generation (RAG) pipelines end-to-end.

`rag-eval-kit` helps you measure the quality of both the **retrieval** component (finding the right context) and the **generation** component (synthesizing an answer based on context) using your ground truth data and LLM-as-a-judge techniques. Gain insights into your RAG system's performance and identify areas for improvement.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Prepare Your Dataset](#prepare-your-dataset)
  - [Integrate Your RAG Components](#integrate-your-rag-components)
  - [Run Evaluation](#run-evaluation)
  - [Interpret Results](#interpret-results)
- [Core Concepts Explained](#core-concepts-explained)
- [Customization](#customization)
- [Limitations & Considerations](#limitations--considerations)
- [Contributing](#contributing)
- [License](#license)

## Features

*   **Modular Design:** Easily plug in your own retriever, generator, and LLM client functions.
*   **Core RAG Metrics:** Calculates standard metrics out-of-the-box:
    *   **Retrieval:** Context Precision, Context Recall
    *   **Generation:** Faithfulness, Answer Relevancy (using LLM-as-a-judge)
*   **Customizable Prompts:** Modify the default prompts used for LLM-as-a-judge evaluations.
*   **Simple Data Format:** Uses easy-to-create JSON Lines (`.jsonl`) datasets.
*   **Clear Reporting:** Provides per-item progress and an aggregated summary of results.

## Getting Started

### Installation

Clone the repository and install the base dependency (`typer`):

```bash
git clone https://github.com/Mizokuiam/rag-eval-kit.git
cd rag-eval-kit
pip install -r requirements.txt
```

**Crucially, you must add the dependencies required for your specific retriever, generator, and LLM client** to requirements.txt and install them. For example:

```bash
# If using OpenAI for judging
# echo "openai>=1.0.0,<2.0.0" >> requirements.txt

# If using ChromaDB + SentenceTransformers for retrieval
# echo "chromadb>=0.4.0,<0.5.0" >> requirements.txt
# echo "sentence-transformers>=2.2.0,<3.0.0" >> requirements.txt

# If using Ollama via requests
# echo "requests>=2.20.0,<3.0.0" >> requirements.txt

# Then install your added dependencies
pip install -r requirements.txt
```

For development (e.g., running linters or tests), install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

### Prepare Your Dataset

Create a JSON Lines (.jsonl) file where each line is a JSON object containing:

- `question` (str): The input question for your RAG system.
- `ground_truth_context_ids` (List[str]): A list of document IDs that are considered relevant/necessary to answer the question. These IDs must match those used by your retrieval system.
- `ground_truth_answer` (str): The ideal or expected answer. (Currently used for reference; future metrics might leverage this).

See `sample_dataset.jsonl` for an example format.

### Integrate Your RAG Components

Open the `evaluate.py` script. This is where you connect rag-eval-kit to your system.

You MUST replace the placeholder functions (`my_dummy_retriever`, `my_dummy_generator`, `my_dummy_llm_client`) with functions that call your actual RAG components:

- `your_retriever_func(question: str) -> RetrievalResult`:
  - Input: question string.
  - Output: A dictionary `{ "retrieved_ids": List[str], "retrieved_content": List[str] }`.

- `your_generator_func(question: str, context: List[str]) -> str`:
  - Input: Original question string, context list of retrieved document strings.
  - Output: The final generated answer string.

- `your_llm_client_func(prompt: str) -> str`:
  - Input: A formatted prompt string (for Faithfulness or Relevancy checks).
  - Output: The LLM's response string (e.g., "SUPPORTED", "UNSUPPORTED", "RELEVANT", "IRRELEVANT").

Recommendation: Use a capable model (e.g., GPT-4, Claude 3, Llama 3 70B) for reliable evaluation judgments.

### Run Evaluation

Execute the evaluate.py script from your terminal, providing the path to your dataset:

```bash
python evaluate.py sample_dataset.jsonl
```

Or, if your dataset is located elsewhere:

```bash
python evaluate.py /path/to/your/evaluation_data.jsonl
```

### Interpret Results

The script will output:

- Progress for each item being processed.
- Metrics calculated for each item (Context Precision, Context Recall, Faithfulness, Answer Relevancy).
- A final summary showing the average scores across the entire dataset.

Example Summary Output:

```
--- Evaluation Summary ---
total_items_processed: 5
average_context_precision: 0.8500
average_context_recall: 0.9000
average_faithfulness: 0.7500
average_answer_relevancy: 0.9500
```

## Core Concepts Explained

- **Context Precision**: Of the documents your system retrieved, how many were actually relevant (present in `ground_truth_context_ids`)? High precision means less noise in the context.
  - Formula: |Retrieved ∩ GroundTruth| / |Retrieved|

- **Context Recall**: Of all the documents that should have been retrieved (`ground_truth_context_ids`), how many did your system actually find? High recall means fewer relevant documents were missed.
  - Formula: |Retrieved ∩ GroundTruth| / |GroundTruth|

- **Faithfulness**: Does the generated answer only contain information verifiable from the retrieved context? This measures hallucination or contradiction against the provided context. (Evaluated via LLM-as-a-judge).

- **Answer Relevancy**: Does the generated answer directly and completely address the original question? This measures if the answer is on-topic and useful, irrespective of the context. (Evaluated via LLM-as-a-judge).

## Customization

- **LLM-as-a-Judge Prompts**: The default prompts (`DEFAULT_FAITHFULNESS_PROMPT_TEMPLATE`, `DEFAULT_RELEVANCY_PROMPT_TEMPLATE` in `rag_eval_kit/core.py`) can be overridden by passing a custom `prompt_template` string when calling `evaluate_faithfulness` or `evaluate_relevancy` (requires modifying `run_evaluation` or calling metrics functions directly).

- **Adding Metrics**: Extend `rag_eval_kit/core.py` by adding new metric functions (e.g., semantic similarity to `ground_truth_answer`, latency measurement) and integrating them into the `run_evaluation` loop.

## Limitations & Considerations

- **LLM-as-a-Judge**: Evaluations depend on the capability of the judge LLM and prompt quality. They can incur cost and latency. Ambiguous LLM responses might result in None scores.

- **Ground Truth**: Retrieval metrics are only as good as the `ground_truth_context_ids` provided in your dataset.

- **Error Handling**: Basic error handling is included, but production use cases may require more robust handling of API errors, data validation, etc.

- **Synchronous Execution**: Evaluation is currently sequential. For large datasets, consider parallelization (e.g., asyncio, multiprocessing) for performance, especially for LLM calls.

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to report bugs, suggest features, and submit pull requests.

We adhere to a [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.