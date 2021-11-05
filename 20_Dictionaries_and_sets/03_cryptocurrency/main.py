data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "totalOut": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


print('1.')
for key in sorted(data.keys()):
    print(key,':', data[key])
print('\n2.')
up = {'total_diff' : 100}
data['ETH'].update(up)
print('ETH:',data["ETH"])

print('\n3.')
upd = {'name' : "doge"}
data["tokens"][0]['fst_token_info'].update(upd)
print(data["tokens"][0])

print('\n4.')
data["ETH"]["totalOut"] = data["tokens"][0].pop('totalOut')
print('Значение в внутри “ETH”',data["ETH"])
print('tokens:',data["tokens"])


print('\n5.')
data["tokens"][1]['sec_token_info']['tota_price'] = data["tokens"][1]['sec_token_info'].pop('price')
print('название ключа',data["tokens"][1]['sec_token_info'])