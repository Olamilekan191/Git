def budget_remaining(budget, food, transport):
    remaining = budget-food-transport
    return remaining

def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."

remaining = budget_remaining(2000, 500, 300)
print(remaining)
message = budget_message("Ada", remaining)
print(message)

remaining = budget_remaining(400, 500, 300)
print(remaining)
message = budget_message("Ada", remaining)
print(message)

remaining = budget_remaining(2000, 0, 0)
print(remaining)
message = budget_message("Ada", remaining)
print(message)
