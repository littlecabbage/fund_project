from urllib.parse import urlencode
from typing import LiteralString
import requests
import tomlkit

with open("configs/day_day_funds_url.toml") as f:
    prefix = tomlkit.load(f)['day_day_funds_prefix']


def search_funds(funds_name) -> LiteralString:
    action_name = "fundSearch"
    key = urlencode(funds_name)
    m = "1"
    # noinspection SpellCheckingInspection
    url = prefix + f"?action_ame={action_name}&key={key}&pageindex&pagesize&m={m}"
    print(url)
    # Get 请求 url
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        return content
    else:
        return f"请求失败{response.status_code}"


def get_fund_detail_information(funds_code: int):
    """
    获取基金详情信息
    :param funds_code: 基金代码
    :return:基金详情信息
    """
    action_name = "fundMNDetailInformation"
    f_code = funds_code
    url = prefix + f"?action_name={action_name}&FCODE={f_code}"

    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        return content
    else:
        return f"请求失败{response.status_code}"
