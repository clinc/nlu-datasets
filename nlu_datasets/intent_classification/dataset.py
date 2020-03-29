import json


def _get_intents(pairs):
    intents = sorted(list(set([intent for (_, intent) in pairs])))
    return intents

def simple_tokenize(query):
    return query.split()

def _load_data(data, datafile):
    if data is not None:
        return data
    elif datafile is not None:
        with open(datafile, 'r') as f:
            file_data = json.load(f)
        return file_data
    


class Dataset:

    def __init__(self, name=""):
        self.name = name
        self.intents = []
        self.all = []
        self.train = []
        self.val = []
        self.test = []

    def _load_all(self, datafile=None, data=None):
        self.all = _load_data(data, datafile)

    def _load_train(self, datafile=None, data=None):
        self.train = _load_data(data, datafile)

    def _load_val(self, datafile=None, data=None):
        self.val = _load_data(data, datafile)

    def _load_test(self, datafile=None, data=None):
        self.test = _load_data(data, datafile)

    def _form_all(self):
        self.all = self.train + self.val + self.test
        self._form_intents()

    def _form_intents(self):
        self.intents = _get_intents(self.all)
