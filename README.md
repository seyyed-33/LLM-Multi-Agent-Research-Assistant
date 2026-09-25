
| Agent | Role |
|-------|------|
| **Researcher** | Gathers accurate and relevant information about the topic |
| **Analyst** | Extracts key insights from the research |
| **Writer** | Produces a clear and concise summary |

## Features

- Multi-agent pipeline using LangChain Expression Language (LCEL)
- Local LLM inference with Ollama (Llama 3.2)
- Sequential chaining: each agent uses the previous agent's output
- Clean and modular code structure

## Technologies Used

- Python
- LangChain
- LangChain Ollama
- LangChain Core
- Ollama
- Llama 3.2

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running
- Llama 3.2 model pulled

## Installation

```bash
pip install -r requirements.txt
ollama pull llama3.2
