
import json
import os
import re
import textwrap
import requests

from dotenv import load_dotenv
from colorama import init, Fore, Style

init(autoreset=True)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FILE = "tickets.json"

WIDTH = 50
CONTENT_WIDTH = WIDTH - 4


# ---------- TERMINAL DESIGN ----------

def print_header():
    title = "CAMPUSFLOW"
    subtitle = "AI-POWERED IT SUPPORT"

    print()
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * (WIDTH - 2) + "╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + title.center(WIDTH - 2) + "║")
    print(Fore.CYAN + "║" + subtitle.center(WIDTH - 2) + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * (WIDTH - 2) + "╝")


def print_section(title, color):
    print()
    print(color + Style.BRIGHT + "┌" + "─" * (WIDTH - 2) + "┐")
    print(color + Style.BRIGHT + "│" + title.center(WIDTH - 2) + "│")
    print(color + Style.BRIGHT + "├" + "─" * (WIDTH - 2) + "┤")


def print_box_line(text="", color=Fore.WHITE, indent=2):
    available_width = CONTENT_WIDTH - indent

    lines = textwrap.wrap(
        str(text),
        width=available_width,
        break_long_words=True,
        break_on_hyphens=False,
    ) or [""]

    for line in lines:
        content = (" " * indent + line).ljust(CONTENT_WIDTH)
        print(color + "│" + content + "│")


def print_box_bottom(color):
    print(color + "└" + "─" * (WIDTH - 2) + "┘")


def print_ticket_field(label, value):
    """Display ticket details with aligned labels."""
    label_width = 13
    value_width = CONTENT_WIDTH - label_width - 3

    lines = textwrap.wrap(
        str(value),
        width=value_width,
        break_long_words=True,
        break_on_hyphens=False,
    ) or [""]

    for index, line in enumerate(lines):
        if index == 0:
            content = f"  {label:<{label_width}}{line}"
        else:
            content = f"  {'':<{label_width}}{line}"

        print(Fore.WHITE + "│" + content.ljust(CONTENT_WIDTH) + "│")


# ---------- AI RESPONSE FORMATTING ----------

def clean_ai_text(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"^\s*[-*]\s+", "", text)

    return text.strip()


def print_ai_suggestions(text):
    for line in text.splitlines():
        line = clean_ai_text(line)

        if not line:
            print_box_line()
        elif re.match(r"^\d+[\.)]\s+", line):
            print_box_line(line, Fore.WHITE, indent=2)
        else:
            print_box_line(line, Fore.WHITE, indent=5)


# ---------- AI INTEGRATION ----------

def get_ai_suggestions(description):
    if not GEMINI_API_KEY:
        return "AI suggestions unavailable: API key is missing."

    prompt = (
        "You are an IT support assistant. "
        "Analyse the reported problem and suggest exactly 3 practical "
        "ways to investigate or fix it. "
        "Use simple English. Number each suggestion. "
        "Keep each suggestion short. "
        "Do not claim the problem has already been fixed.\n\n"
        f"Ticket description: {description}"
    )

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-3.5-flash-lite:generateContent"
    )

    try:
        response = requests.post(
            url,
            headers={
                "x-goog-api-key": GEMINI_API_KEY,
                "Content-Type": "application/json",
            },
            json={
                "contents": [
                    {"parts": [{"text": prompt}]}
                ]
            },
            timeout=30,
        )

        response.raise_for_status()
        data = response.json()

        suggestions = data["candidates"][0]["content"]["parts"][0]["text"]

        if not suggestions.strip():
            return "AI suggestions unavailable: The model returned an empty response."

        return suggestions

    except requests.exceptions.Timeout:
        return "AI suggestions unavailable: The request timed out."

    except requests.exceptions.ConnectionError:
        return "AI suggestions unavailable: Check your internet connection."

    except requests.exceptions.HTTPError as error:
        status = error.response.status_code if error.response is not None else None

        if status in (400, 403):
            return "AI suggestions unavailable: Check the API key or request settings."

        if status == 404:
            return "AI suggestions unavailable: The selected model may be unavailable."

        if status == 429:
            return "AI suggestions unavailable: The API usage limit may have been reached."

        return "AI suggestions unavailable: The AI service returned an error."

    except requests.exceptions.RequestException:
        return "AI suggestions unavailable: A network request failed."

    except (KeyError, IndexError, TypeError, ValueError):
        return "AI suggestions unavailable: The response was unexpected."


# ---------- TICKET STORAGE ----------

def load_tickets():
    try:
        with open(FILE, "r") as file:
            tickets = json.load(file)

        if not isinstance(tickets, list):
            print(Fore.RED + "\nError: Ticket data must be a JSON list.")
            return None

        return tickets

    except FileNotFoundError:
        return []

    except (json.JSONDecodeError, OSError) as error:
        print(Fore.RED + f"\nError loading tickets: {error}")
        return None


def save_tickets(tickets):
    try:
        with open(FILE, "w") as file:
            json.dump(tickets, file, indent=4)

        return True

    except OSError as error:
        print(Fore.RED + f"\nError saving tickets: {error}")
        return False


def get_next_id(tickets):
    numbers = [
        int(ticket["id"][1:])
        for ticket in tickets
        if isinstance(ticket, dict)
        and isinstance(ticket.get("id"), str)
        and ticket["id"].startswith("T")
        and ticket["id"][1:].isdigit()
    ]

    return f"T{max(numbers, default=0) + 1:03d}"


# ---------- CREATE TICKET ----------

def create_ticket():
    tickets = load_tickets()

    if tickets is None:
        return

    print_header()

    print(Fore.CYAN + Style.BRIGHT + "\n  CREATE NEW TICKET")
    print(Fore.CYAN + "  " + "─" * 30)

    title = input(Fore.WHITE + "\n  Ticket title: ").strip()
    description = input(
        Fore.WHITE + "  Describe the problem: "
    ).strip()

    if not title or not description:
        print(Fore.RED + "\n  Error: Title and description cannot be empty.")
        return

    ticket = {
        "id": get_next_id(tickets),
        "title": title,
        "description": description,
    }

    # Save the ticket before contacting the AI.
    tickets.append(ticket)

    if not save_tickets(tickets):
        return

    print(Fore.GREEN + "\n  ✓ Ticket created and saved successfully.")
    print(Fore.CYAN + "\n  Getting AI suggestions...")

    # Send the actual ticket description to the AI.
    suggestions = get_ai_suggestions(ticket["description"])

    # Store the AI response with the ticket.
    ticket["ai_suggestions"] = suggestions

    if not save_tickets(tickets):
        print(Fore.YELLOW + "  Warning: AI suggestions could not be saved.")

    # Display the result.
    print_header()

    print(Fore.GREEN + Style.BRIGHT + "\n  ✓ TICKET CREATED SUCCESSFULLY")

    print_section("TICKET DETAILS", Fore.CYAN)

    print_ticket_field("Ticket ID", ticket["id"])
    print_ticket_field("Title", ticket["title"])
    print_ticket_field("Description", ticket["description"])

    print_box_bottom(Fore.CYAN)

    print_section("AI TROUBLESHOOTING", Fore.MAGENTA)

    print_ai_suggestions(suggestions)

    print_box_bottom(Fore.MAGENTA)

    print(Fore.GREEN + Style.BRIGHT + "\n  ✓ Your ticket is ready!")
    print(Fore.WHITE + "  Stored in tickets.json\n")


if __name__ == "__main__":
    create_ticket()