import yaml

with open('data/login.yaml',encoding='utf-8') as y:
    data = yaml.load(y)
print(data)