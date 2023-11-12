import requests
res_parse_list = []
response = requests.get("https://coinmarketcap.com")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

bitcoin_exchange_rate = res_parse_list[0]
print(f"Bitcoin - {bitcoin_exchange_rate}")
bitcoin_exchange_rate = res_parse_list[1]
print(f"Etherium - {bitcoin_exchange_rate}")
bitcoin_exchange_rate = res_parse_list[2]
print(f"Tether USDt - {bitcoin_exchange_rate}")
bitcoin_exchange_rate = res_parse_list[3]
print(f"BNB - {bitcoin_exchange_rate}")