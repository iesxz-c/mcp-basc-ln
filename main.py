from mcp.server.fastmcp import FastMCP
import os
# Create an MCP server
mcp = FastMCP("Demo")


FILE =  os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file_exists():
    if not os.path.exists(FILE):
        with open(FILE, 'w') as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    #important to add a docstring to the function
    """
    Append a new note to the text file.

    Args:
        message (str): The note content to be added.

    Returns:
        str: A success message indicating the note was added.
    """
    
    
    ensure_file_exists()
    with open(FILE, 'a') as f:
        f.write(message + "\n")
    return "Txt added successfully."


@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the notes file.

    Returns:
        str: The content of the notes file.
        If the file is empty, returns a message indicating no notes are available.
    """
    
    ensure_file_exists()
    with open(FILE, 'r') as f:
        content = f.read().strip()
    return content if content else "No notes available."

@mcp.resource("notes://latest")
def get_latest_notes() -> str:
    """Get the most recently added note from the notes file.

    Returns:
        str: The last note entry.
        If the file is empty, returns a message indicating no notes are available.
    """
    ensure_file_exists()
    with open(FILE, 'r') as f:
        content = f.readlines()
    return content[-1].strip() if content else "No notes available."

@mcp.prompt()
def notes_summary_prompt() -> str:
    """
    Generate a prompt asking  AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
        If the notes file is empty, returns a message indicating no notes are available.
    """
    ensure_file_exists()
    with open(FILE, 'r') as f:
        content = f.read().strip()
    return content if content else "No notes available."
##uv run mcp install main.py

