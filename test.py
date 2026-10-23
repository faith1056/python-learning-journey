import json

FILE = "tickets.json"


def create_ticket():
    try:
        with open(FILE) as f:
            tickets = json.load(f)
        if not isinstance(tickets, list):
            print("Invalid ticket data.")
            return
    except FileNotFoundError:
        tickets = []
    except (json.JSONDecodeError, OSError) as e:
        print(f"Loading error: {e}")
        return

    title = input("Enter ticket title: ").strip()
    description = input("Enter problem description: ").strip()
    if not title or not description:
        print("Title and description cannot be empty.")
        return

    ticket = {"id": f"T{len(tickets)+1:03d}", "title": title, "description": description}
    tickets.append(ticket)

    try:
        with open(FILE, "w") as f:
            json.dump(tickets, f, indent=4)
        print(f"\nTicket {ticket['id']} saved successfully!\n" + "=" * 45)
        for label, key in [("Ticket ID:", "id"), ("Title:", "title"), ("Description:", "description")]:
            print(f"{label:18}{ticket[key]}")
        print("=" * 45)
    except OSError as e:
        print(f"Saving error: {e}")


if __name__ == "__main__":
    create_ticket()


