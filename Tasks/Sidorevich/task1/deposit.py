from decimal import Decimal


def proc(deposit, rate, years):
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    for _ in range(years):
        for m in months:
            per_month = deposit * rate / 365 * m
            deposit += per_month

    return deposit


# Begin

years = 5

# float proc
deposit = 20000.0
rate = 0.15

result = proc(deposit, rate, years)
print("Float deposit =", round(result, 2), "BYN (", result, ")")

# decimal proc
deposit = Decimal(str(deposit))
rate = Decimal(str(rate))

result = proc(deposit, rate, years)
print("Decml deposit =", round(result, 2), "BYN (", result, ")")
