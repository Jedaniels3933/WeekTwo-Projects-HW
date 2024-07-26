service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
}
def next_id():
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
        return last_id + 1
def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter customer name:")
        issue = input("Please enter the issue:")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this correct? (Y/N): ").lower()
        if correct == 'y':   #Create new ticket
            service_tickets[new_id] = {'Customer': customer, "Issue": issue, "Status": "open"}
            break
        else:
            print("Please try again.")
def main():
    while True:
        ans= input('''
"Service Ticket Manager
Enter an option , please: 
1. Create a new ticket
2. Update service ticket
3. View all tickets
4.Quit
''')                  
        if ans == '1':
            new_ticket()
        elif ans == '2':
            print("Updating a ticket")
            ticket_id = int(input("Enter the ID of the ticket you want to update: "))
            if ticket_id in service_tickets:
                customer = input("Please enter the new customer name:")
                issue = input("Please enter the new issue:")
                service_tickets[ticket_id] = {'Customer': customer, "Issue": issue, "Status": "open"}
                print("Ticket updated successfully.")
        elif ans == '3':
                print(service_tickets)
        elif ans == '4':
                print("Fine then, just quit on me ")
main()