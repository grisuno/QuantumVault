import base64

client_id = "ARiFGf3NhZsNZnlToWteCHpZkCKE31chajDadW-BZ9g8PusPRoABHTH0djs1j2tGhF0ZrCnemB1dDxeS"
client_secret = "EP1WS2tCFcRU9e2Lqw9p-Ow5vwsr7sVT3FWcMH3LTVwKqbt_4BSZJhTx_rTEKKXVAGKomozTIQz-l2DT"
credentials = f"{client_id}:{client_secret}"
encoded = base64.b64encode(credentials.encode()).decode()
print(encoded)


encoded = "QVJpRkdmM05oWnNOWm5sVG9XdGVDSHBaa0NLRTMxY2hhakRhZFctQlo5ZzhQdXNQUm9BQkhUSDBkanMxajJ0R2hGMFpyQ25lbUIxZER4ZVM6RVAxV1MydENGY1JVOWUyTHF3OXAtT3c1dndzcjdzVlQzRldjTUgzTFRWd0txYnRfNEJTWkpoVHhfclRFS0tYVkFHS29tb3pUSVF6LWwyRFQ="
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)
