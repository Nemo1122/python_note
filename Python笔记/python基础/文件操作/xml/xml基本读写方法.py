import xml.etree.ElementTree as ET

# 打开xml
tree = ET.parse("..\data\country.xml")
# 获取根节点
root = tree.getroot()

# 节点的标签名
root.tag    # data

# 节点的属性，以字典形式{属性名:属性值}
root[1].attrib  # {'name': 'Singapore', 'area': 'Asia'}

# 遍历root的子节点，打印子节点的标签名和属性值
for child in root:
    print(child.tag, child.attrib)

# country {'name': 'Liechtenstein'}
# country {'name': 'Singapore', 'area': 'Asia'}
# country {'name': 'Panama'}

# 获取子节点或内部其他节点的文本
root[0][1].text      # '2008'

# 获取节点的属性值
root[1].get("name", "未找到该属性")   # 'Singapore'

# 以元组的形式获取属性值
root[1].items()   # [('name', 'Singapore'), ('area', 'Asia')]

# 以list形式获取属性名
root[1].keys()   # ['name', 'area']

# 设置属性值
root[1].set('area', 'ASIA')
root[1].items()    # [('name', 'Singapore'), ('area', 'ASIA')]

# 查找第一个匹配的子元素，注意，只能查找子级
country = root.find("country")

# 查找所有匹配的子元素，注意，只能查找子级， 以list返回
country = root.findall("country")

# iter深度查找
for node in root[0].iter():
    print(node)
