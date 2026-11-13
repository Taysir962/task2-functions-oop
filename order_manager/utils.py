
def format_price(amount, currency="JOD", decimals=2):
    """Returns formatted price string like '12.50 JOD'."""
    return f"{amount:.{decimals}f} {currency}"