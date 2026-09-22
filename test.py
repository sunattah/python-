# def ticket_total(price, quantity):
#     total = price * quantity
#     print(total)
# ticket_total(7, 3)

def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
print(passing_scores([50, 80, 65, 0]))