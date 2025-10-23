#! /usr/bin/env python3
"""
A simple conversational agent example using LangChain and a chat model."""

from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from chat_resources import welcome_panel, goodbye_panel
from config_model import model

# Read system prompt from file
with open("system_prompt.md", "r") as f:
    SYSTEM_PROMPT = f.read()


# Setup memory for conversation
checkpointer = InMemorySaver()
config = {"configurable": {"thread_id": "conversation_1"}}

# Create agent
agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)


# Initialize Rich console for better formatting
console = Console()
console.print(welcome_panel)

# Conversational loop
while True:
    # Get user input with Rich prompt
    console.print()  # Add some spacing
    user_input = Prompt.ask("[bold green]You[/bold green]")

    # Exit condition
    if user_input.lower() in {"exit", "quit", "bye"}:
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
