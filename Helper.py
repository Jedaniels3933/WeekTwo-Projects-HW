def next_id():
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
        return last_id + 1