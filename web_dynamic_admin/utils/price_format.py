def price_format(price):
    """format the price with commas"""
    # Convert price to string and reverse it
    price_str = str(price)[::-1]

    # Insert commas every three characters
    formatted_price = ",".join(price_str[i:i+3] for i in range(0, len(price_str), 3))

    # Reverse the formatted price and return
    return formatted_price[::-1]
