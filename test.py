# def ticket_total(price, quantity):
#     total = price * quantity
#     print(total)
# ticket_total(7, 3)

# def passing_scores(scores):
#     passed = []
#     for index in range(len(scores)):
#         if scores[index] >= 50:
#             passed.append(scores[index])
#     return passed
# print(passing_scores([50, 80, 65, 0]))

def add_tag(profile, tag, tage):
    updated = profile.copy()
    updated["tags"].append(tag)
    updated["tage"].append(tage)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(original)

# 5

def reserve_stock(stock, order):
    remaining = stock.copy()

    for item, quantity in order:
        if item not in stock:
            raise ValueError("Unknown item")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > remaining[item]:
            raise ValueError("Insufficient stock")

        remaining[item] -= quantity

    return remaining

# 4
def summarise_amounts(raw_values):
    total = 0
    rejected = 0

    for raw in raw_values:
        try:
            amount = int(raw)
        except ValueError:
            rejected += 1
        else:
            if amount < 0:
                rejected += 1
            else:
                total += amount

    return {"total": total, "rejected": rejected}
#3
def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
# 2
def ticket_total(price, quantity):
    total = price * quantity
    return total

amount = ticket_total(7, 3)
print(amount)
