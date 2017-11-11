import re

s = 'qitadss￥269.00dads￥13.123aasd￥323123x32a'

print(re.search(r'￥\d+\.\d{2}', s).group())