import requests

def fetch_crypto_price(crypto_symbol="bitcoin"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto_symbol,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if crypto_symbol not in data:
            print(f"Error: Cryptocurrency '{crypto_symbol}' not found.")
            return
        
        price = data[crypto_symbol]["usd"]
        change_24h = data[crypto_symbol].get("usd_24h_change", 0)
        
        change_str = f"+{change_24h:.2f}%" if change_24h > 0 else f"{change_24h:.2f}%"
        
        print(f"{crypto_symbol.capitalize()} Price")
        print(f"Current Price: ${price:,.2f} USD")
        print(f"24h Change: {change_str}")
    
    except requests.exceptions.HTTPError as http_err:
        status_code = response.status_code
        if status_code == 404:
            print("Error: API endpoint not found.")
        elif status_code == 429:
            print("Error: Too many requests. Rate limit exceeded.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the API. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
    except ValueError:
        print("Error: Invalid response from the server (not valid JSON).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum) [default: bitcoin]: ").strip()
    if not crypto:
        crypto = "bitcoin"
    
    fetch_crypto_price(crypto.lower())