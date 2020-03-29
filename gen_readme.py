import json

files = ['ask_ubuntu.json', 'chatbot.json', 'web_applications.json']
readme = []
readme.append('# NLU Datasets')
readme.append('## Intent Classification')

with open('nlu_datasets/intent_classification/index.json', 'r') as f:
    index = json.load(f)
    for data in index:
        print(data)
        name = ' '.join(data['name'].split('_')).title()
        readme.append('### {}'.format(name))
        readme.append('')

with open('README.md', 'w') as f:
    f.writelines([line + '\n' for line in readme])
