# Conversational Agent Example

> **Note:** This documentation was generated with the assistance of Generative AI.

A simple conversational agent built with Python and LangChain, designed as a learning primer for network, network automation, and infrastructure engineers exploring AI capabilities.

## 🎯 Overview

This project demonstrates how to build a basic conversational AI agent using modern Python libraries. The agent maintains conversation context, provides friendly responses with humor and emojis, and showcases fundamental AI agent patterns that can be applied to network automation and infrastructure management tasks.

## 🏗️ Architecture

The project consists of several key components:

- **`agent_01.py`** - Main application with conversation loop and agent initialization
- **`config_model.py`** - Model configuration and initialization 
- **`chat_resources.py`** - UI components for welcome/goodbye messages
- **`system_prompt.md`** - System prompt that defines the agent's personality and behavior

## 🚀 Quick Start

### Prerequisites

1. **Python 3.12++** installed on your system
2. **Ollama** installed and running locally ([Ollama on GitHub](https://github.com/ollama/ollama) for setup info)
3. A compatible language model (configured to use `gpt-oss:20b`)

### Installation

1. Clone or download this project to your local machine

2. Install the required Python dependencies:
   ```bash
   pip install langchain langgraph rich
   ```

3. Ensure Ollama is running with the required model:
   ```bash
   # Start Ollama (if not already running)
   ollama serve
   
   # Pull the model (in another terminal)
   ollama pull gpt-oss:20b
   ```

### Running the Agent

1. Navigate to the conversational agent directory:
   ```bash
   cd conversational_agent
   ```

2. Run the agent:
   ```bash
   python agent_01.py
   ```

3. Start chatting! The agent will:
   - Welcome you with a friendly message
   - Maintain conversation context throughout your session
   - Respond with humor, puns, and emojis
   - Remember previous parts of your conversation

4. Exit the conversation by typing `exit`, `quit`, or `bye`

## 💬 Example Interaction

```
🎉 AI Chat Assistant
┌─────────────────────────────────────────────────────────────┐
│  Welcome to the Conversational Agent!                      │
│                                                             │
│  🤖 I'm here to help answer your questions and have a      │
│  conversation.                                              │
│  💬 Just type your message and press Enter.                │
│  🚪 Type 'exit', 'quit', or 'bye' to end the conversation. │
└─────────────────────────────────────────────────────────────┘

You: Hello! I'm learning about network automation with AI.

🤖 Agent Response
┌─────────────────────────────────────────────────────────────┐
│ Hey there, future network automation wizard! 🧙‍♂️✨          │
│                                                             │
│ That's fantastic that you're diving into AI for network    │
│ automation! You're really going to *switch* up your game   │
│ (see what I did there? 😄). Network automation with AI is  │
│ like having a super-smart assistant that never sleeps and  │
│ doesn't need coffee! ☕                                     │
│                                                             │
│ What specific aspects are you curious about? Are you       │
│ thinking about automated configuration management,         │
│ intelligent monitoring, or maybe predictive network        │
│ analysis? I'm here to help you *route* through all the     │
│ possibilities! 🌐🚀                                         │
└─────────────────────────────────────────────────────────────┘
```

## 📚 External Libraries

This project uses the following external Python libraries:

### Core AI/ML Libraries
- **[LangChain](https://python.langchain.com/)** - Framework for developing applications with language models
  - Provides abstractions for working with LLMs
  - Handles conversation memory and context
  - Offers agent creation and management capabilities

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Extension of LangChain for building stateful, multi-actor applications
  - Provides checkpoint/memory management (`InMemorySaver`)
  - Enables complex agent workflows and state management

### User Interface Libraries  
- **[Rich](https://rich.readthedocs.io/)** - Advanced terminal formatting and display library
  - Creates beautiful console output with colors and formatting
  - Provides panels, prompts, and markdown rendering
  - Enhances user experience with professional-looking CLI interface

### Model Provider
- **[Ollama](https://ollama.ai/)** - Local LLM runtime (external dependency)
  - Runs language models locally on your machine
  - Provides privacy and control over your AI interactions
  - Supports various open-source models

## 🔧 Configuration

### Model Configuration

The agent is configured in `config_model.py` with the following settings:

- **Model**: `gpt-oss:20b` (via Ollama)
- **Temperature**: `0.7` (controls response creativity/randomness)
- **Provider**: `ollama` (local model serving)

### System Prompt

The agent's personality and behavior are defined in `system_prompt.md`. You can customize this file to change how the agent responds and behaves.

## 🛠️ Customization

### Changing the Model

To use a different model, modify `config_model.py`:

```python
MODEL_NAME = "your-preferred-model"  # e.g., "llama2", "mistral"
```

### Adjusting Response Style

Edit `system_prompt.md` to change the agent's personality:

```markdown
You are a helpful network automation expert. Provide technical, 
precise answers focused on infrastructure and networking topics.
```

### Modifying the UI

Customize the welcome and goodbye messages in `chat_resources.py` to match your preferences or branding.

## 🎓 Learning Opportunities

This project demonstrates several key concepts for network engineers learning AI:

1. **Conversation Memory** - How AI agents maintain context across interactions
2. **System Prompts** - How to guide AI behavior and responses
3. **Model Configuration** - Understanding temperature and other parameters
4. **Local AI Deployment** - Running models on your own infrastructure
5. **Python Integration** - Incorporating AI into existing automation workflows

## 🚧 Next Steps

Consider extending this project with:

- Integration with network APIs (NETCONF, RESTCONF, REST APIs)
- Network device configuration generation
- Log analysis and troubleshooting assistance  
- Integration with network monitoring tools
- Custom tools and functions for specific network tasks

## 📝 License

This project is provided as educational material for learning AI concepts in network automation contexts.

---

Happy learning! 🤖🌐✨