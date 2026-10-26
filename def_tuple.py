def show_categories(categories):
    for category in categories:
        print(category)


ticket_categories = (
    "Network",
    "Hardware",
    "Software",
    "Other",
)

show_categories(ticket_categories)



tickets = []

tickets.append(("T001", "WiFi problem"))
tickets.append(("T002", "WiFi problem"))

print(len(tickets))