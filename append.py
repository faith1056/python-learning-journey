tickets = [
    {"title": "Wi-Fi problem", "urgency": "high"},
    {"title": "Broken mouse", "urgency": "low"},
    {"title": "Login problem", "urgency": "high"}
]

high_urgency_tickets = []
for ticket in tickets:
    if ticket["urgency"] == "high":
        high_urgency_tickets.append(ticket["title"])
print(high_urgency_tickets)



tickets = [
    {"title": "Printer broken", "urgency": "low"},
    {"title": "Internet down", "urgency": "high"},
    {"title": "Computer won't start", "urgency": "high"},
    {"title": "Mouse missing", "urgency": "low"}
]


low_urgency_tickets = []
for ticket in tickets:
    if ticket["urgency"] == "low":
        low_urgency_tickets.append(ticket["title"])
print(low_urgency_tickets)



tickets = [
    {"title": "Wi-Fi problem", "urgency": "high"},
    {"title": "Broken mouse", "urgency": "low"},
    {"title": "Login problem", "urgency": "high"}
]

high_count = 0
for ticket in tickets:
    if ticket["urgency"] == "high":
        high_count = high_count +1
print(high_count)



low_count = 0

for ticket in tickets:
    if ticket["urgency"] == "low":
        low_count = low_count +1

print(low_count)



count = 0

for number in [2, 4, 6, 8]:
    count = count + 1

print(count)



tickets = [
    {"title": "Wi-Fi problem", "urgency": "high"},
    {"title": "Broken mouse", "urgency": "low"},
    {"title": "Login problem", "urgency": "high"},
    {"title": "Printer broken", "urgency": "low"}
]

low_count = 0

for ticket in tickets:
    if ticket["urgency"] == "low":
        low_count = low_count + 1

print(low_count)




tickets = [
    {"title": "Wi-Fi", "urgency": "high"},
    {"title": "Mouse", "urgency": "low"},
    {"title": "Login", "urgency": "high"},
    {"title": "Printer", "urgency": "low"},
    {"title": "Keyboard", "urgency": "low"}
]


low_urgency = 0
for ticket in tickets:
    if ticket["urgency"] == "low":
        low_urgency = low_urgency +1
print(low_urgency)



count = 0

prices = [100, 200, 300]

total = 0

for price in prices:
    total = total + price

print(total)



prices = [200, 500, 100]
total = 0
for price in prices:
    total = total + price
print(total)
