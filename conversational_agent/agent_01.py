#! /usr/bin/env python3
"""
A simple conversational agent example using LangChain and a chat model."""

from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

# Read system prompt from file
with open("system_prompt.md", "r") as f:
    SYSTEM_PROMPT = f.read()

# Configure model details
MODEL_NAME = "gpt-oss:20b"
TEMPERATURE = 0.7
model = init_chat_model(
    model=MODEL_NAME, model_provider="ollama", temperature=TEMPERATURE
)

# Setup memory for conversation
checkpointer = InMemorySaver()

# Create agent
agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

# thread_id is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "conversation_1"}}

# Initialize Rich console for better formatting
console = Console()

# Display welcome message with Rich formatting
welcome_panel = Panel(
    "Welcome to the [bold blue]Conversational Agent[/bold blue]!\n\n"
    "🤖 I'm here to help answer your questions and have a conversation.\n"
    "💬 Just type your message and press Enter.\n"
    "🚪 Type [italic red]'exit'[/italic red], [italic red]'quit'[/italic red], or [italic red]'bye'[/italic red] to end the conversation.",
    title="🎉 AI Chat Assistant",
    title_align="center",
    border_style="blue",
    padding=(1, 2),
)
console.print(welcome_panel)
# Conversational loop
while True:
    # Get user input with Rich prompt
    console.print()  # Add some spacing
    user_input = Prompt.ask("[bold green]You[/bold green]")

    # Exit condition
    if user_input.lower() in {"exit", "quit", "bye"}:
        goodbye_panel = Panel(
            "[bold green]Thank you for chatting![/bold green]\n\n"
            "👋 It was great talking with you.\n"
            "🚀 Come back anytime for another conversation!",
            title="🎊 Goodbye!",
            title_align="center",
            border_style="green",
            padding=(1, 2),
        )
        console.print(goodbye_panel)
        break

    # Send message to the agent and get response
    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config,
    )

    # Display the agent's response with Rich markdown formatting and word wrapping
    agent_response = response["messages"][-1].content

    # Create a Markdown object to properly render markdown formatting
    markdown_response = Markdown(agent_response)

    # Create a panel for the agent's response with markdown rendering
    response_panel = Panel(
        markdown_response,
        title="🤖 Agent Response",
        title_align="left",
        border_style="cyan",
        padding=(0, 1),
        width=None,  # Auto-width for word wrapping
    )
    console.print(response_panel)
