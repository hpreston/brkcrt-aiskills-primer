from rich.panel import Panel

# A standard welcome message panel at the start of a conversation
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

# A standard goodbye message panel at the end of a conversation
goodbye_panel = Panel(
    "[bold green]Thank you for chatting![/bold green]\n\n"
    "👋 It was great talking with you.\n"
    "🚀 Come back anytime for another conversation!",
    title="🎊 Goodbye!",
    title_align="center",
    border_style="green",
    padding=(1, 2),
)
