from datetime import datetime


def calculate_vinted_prices(purchase_price, purchase_date, quality):
    """
    Calculate the listing price and lowest acceptable price for a second-hand clothing item on Vinted.

    Parameters:
    purchase_price (float): The original purchase price of the item in GBP.
    purchase_date (str): The date of purchase in 'YYYY-MM-DD' format.
    quality (str): The quality of the item ('new', 'like new', 'good', 'fair', 'poor').

    Returns:
    dict: A dictionary containing the listing price and the lowest acceptable price in GBP.
    """

    # Define depreciation rates per year for different quality levels
    depreciation_rates = {
        'new': 0.2,
        'like new': 0.25,
        'good': 0.3,
        'fair': 0.4,
        'poor': 0.6
    }

    # Define lowest acceptable price factors for different quality levels
    lowest_price_factors = {
        'new': 0.8,
        'like new': 0.7,
        'good': 0.6,
        'fair': 0.5,
        'poor': 0.4
    }

    # Vinted fee percentage (hypothetical, adjust based on actual fees)
    vinted_fee_percentage = 0.0

    # Ensure the quality is valid
    if quality not in depreciation_rates:
        raise ValueError("Invalid quality. Valid options are: 'new', 'like new', 'good', 'fair', 'poor'.")

    # Calculate the age of the item
    purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
    current_date = datetime.now()
    age_in_years = (current_date - purchase_date).days / 365.25

    # Calculate the depreciated value
    depreciation_rate = depreciation_rates[quality]
    depreciated_value = purchase_price * ((1 - depreciation_rate) ** age_in_years)

    # Calculate the listing price (aiming for 90% of the depreciated value to stay competitive)
    listing_price = depreciated_value * 0.9

    # Calculate the lowest acceptable price
    lowest_price_factor = lowest_price_factors[quality]
    lowest_acceptable_price = listing_price * lowest_price_factor

    # Factor in Vinted fees
    listing_price_after_fee = listing_price * (1 - vinted_fee_percentage)
    lowest_acceptable_price_after_fee = lowest_acceptable_price * (1 - vinted_fee_percentage)

    return {
        'listing_price': round(listing_price_after_fee, 2),
        'lowest_acceptable_price': round(lowest_acceptable_price_after_fee, 2)
    }


# Get user input
purchase_price = float(input("Enter the purchase price in GBP: "))
purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")
quality = input("Enter the quality of the item ('new', 'like new', 'good', 'fair', 'poor'): ")

# Calculate prices
prices = calculate_vinted_prices(purchase_price, purchase_date, quality)

# Print results
print(f"Listing Price: £{prices['listing_price']}")
print(f"Lowest Acceptable Price: £{prices['lowest_acceptable_price']}")
