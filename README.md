# AI Skills Primer for CCNP Candidates

> **Note:** This documentation was generated with the assistance of Generative AI.

A collection of hands-on examples and demonstrations designed to help network engineers preparing for CCNP-level certifications explore AI capabilities for network automation. These examples align with CCNP Automation blueprint topics and provide practical learning experiences with modern AI tools and frameworks.

## 🎯 Project Overview

This repository contains practical examples that demonstrate key AI and automation concepts relevant to network engineering professionals. The examples are designed as educational material for a presentation called "AI Skills Primer for CCNP Candidates" and focus on two core areas from the CCNP Automation blueprints:

1. **Construct an MCP server to provide network information to an AI-agent using Python FastMCP**
2. **Construct a conversational agent that leverages LLMs for network automation**

Each example is self-contained with its own documentation, dependencies, and learning objectives, making it easy to explore individual concepts or work through the complete learning path.

## 📚 Examples

### 🤖 [Conversational Agent](./conversational_agent/)

**Learning Focus:** Building AI-powered conversational interfaces for network automation

A comprehensive example demonstrating how to create a conversational AI agent using LangChain and local language models. This example showcases fundamental patterns for building chatbot interfaces that can be extended for network automation tasks.

**Key Technologies:**
- LangChain for LLM orchestration
- LangGraph for stateful conversations
- Ollama for local model hosting
- Rich for enhanced CLI interfaces

**CCNP Relevance:** Understanding how to create user-friendly interfaces for automation tools and integrate conversational AI into network operations workflows.

[**📖 View Conversational Agent Documentation →**](./conversational_agent/README.md)

---

### 🔧 [MCP pyATS Network Automation Tool](./mcp-pyats/)

**Learning Focus:** Creating Model Context Protocol servers for AI-powered network device interaction

A practical implementation of an MCP (Model Context Protocol) server that integrates Cisco's pyATS framework to provide AI agents with network device automation capabilities. This example demonstrates how to expose network automation functions as AI-accessible tools.

**Key Technologies:**
- FastMCP for Model Context Protocol implementation
- pyATS/Genie for network device automation
- Structured command parsing and data extraction
- Multi-vendor device support

**CCNP Relevance:** Direct application of programmatic device interaction, API integration patterns, and modern automation frameworks aligned with CCNP Automation objectives.

[**📖 View MCP pyATS Documentation →**](./mcp-pyats/README.md)

## 🚀 Getting Started

### Prerequisites

Before working with these examples, ensure you have:

1. **Python 3.12+** installed on your system
2. **Git** for cloning the repository
3. **Network access** to devices (for MCP pyATS examples)
4. **Ollama** or similar LLM runtime (for conversational agent examples)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hpreston/brkcrt-aiskills-primer.git
   cd brkcrt-aiskills-primer
   ```

2. **Choose an example to explore:**
   - Start with [Conversational Agent](./conversational_agent/) for AI fundamentals
   - Try [MCP pyATS](./mcp-pyats/) for network automation integration

3. **Follow the individual README instructions** for each example, which include:
   - Specific dependency installation
   - Configuration requirements
   - Step-by-step usage guides
   - Troubleshooting tips

## 🎓 Learning Path

For maximum learning benefit, consider this suggested progression:

### 1. **Foundation** - Conversational Agent
- Understand basic LLM integration patterns
- Learn conversation state management
- Explore local AI model deployment
- Practice with Python AI frameworks

### 2. **Network Integration** - MCP pyATS Tool
- Apply AI concepts to network automation
- Understand structured data parsing
- Practice with device connectivity patterns
- Explore API integration for AI tools

## 🎯 CCNP Automation Alignment

These examples directly support several CCNP Automation exam topics from the [Designing, Deploying and Managing Network Automation Systems v2.0 (350-901) AUTOCOR exam](https://learningcontent.cisco.com/documents/marketing/exam-topics/350-901-AUTOCOR-v2.0-7-9-2025.pdf):

| Topic | Conversational Agent | MCP pyATS | Learning Outcome |
|-------|---------------------|-----------|------------------|
| **APIs and Protocols** | ✅ LLM APIs | ✅ SSH, NETCONF patterns | Understanding modern API integration |
| **Network Automation** | ✅ Conversation automation | ✅ Device automation | Programmatic network interaction |
| **Data Formats** | ✅ JSON message handling | ✅ Structured parsing | Working with automation data |
| **Python Programming** | ✅ Advanced frameworks | ✅ pyATS integration | Automation scripting skills |
| **Infrastructure Integration** | ✅ Local model deployment | ✅ Device connectivity | Production-ready patterns |

## 🤝 Contributing

This project is designed as educational material. If you have suggestions for improvements or additional examples that would benefit CCNP candidates, please feel free to open issues or submit pull requests.

## 📄 License

This project is provided under the Cisco Sample Code License. See [LICENSE](./LICENSE) for full details.

The code in this repository is intended for educational and demonstration purposes to help network engineers learn AI and automation concepts.

## 🎤 Presentation Context

These examples were created to support the "AI Skills Primer for CCNP Candidates" presentation, designed to help network engineers understand how AI technologies can enhance traditional network automation approaches and prepare for modern networking challenges.

---

**Ready to explore AI-powered network automation?** 🚀

Choose an example from above and start your journey into the intersection of artificial intelligence and network engineering!

🤖 Happy learning! 🌐✨
