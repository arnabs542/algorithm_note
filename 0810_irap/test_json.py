import json
data_dict = {
    "method_dict":{
        "mapper": 'star',
        'quantification': 'featureconts',
        'DE_method': 'deseq2'
    },
    "meta_dict": {
        'GA': 'Comparison',
        'GB': 'Wildtype',
        'GC': "Shit"
    }
}

with open('test.json', "w") as f:
    json.dump(data_dict, f, indent=4)
    f.close()