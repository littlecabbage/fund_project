import json
import tomlkit
from utils.dayday_funds_methods import get_fund_detail_information
with open("configs/funds.toml", 'r') as f:
    # print(tomlkit.load(f)['my_funds'])
    funds_info = tomlkit.load(f)
    funds_names = funds_info['my_funds']['funds_names']
    funds_code = funds_info['my_funds']['funds_code']


print(funds_code[1])
print(json.loads(
        get_fund_detail_information(funds_code[1])
    )
)

