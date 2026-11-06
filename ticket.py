tickets = [
    {
       "title": "wifi",
       "urgency": "medium",
       "status": "open" 
    },
    {
      "title": "broken mouse",
      "urgency": "low",
      "status": "open" 
    },
    {
        "title" : "login problem",
        "urgency" : "high",
         "status": "open"
    }
]

for ticket in tickets:
    if ticket["urgency"] == "high":
        print(ticket["title"])

         
for ticket in tickets:
    if ticket["urgency"] == "high" and ticket["status"] == "open":

            print(tickets["title"])