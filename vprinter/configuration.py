import json


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Configuration:
    def __init__(self, name, amount, total_expense, amount_in_words):
        self.name = name
        self.amount = amount
        self.total_expense = total_expense
        self.amount_in_words = amount_in_words

    def to_dictionary(self):
        return {
            "name": self.name,
            "amount": [self.amount.x, self.amount.y],
            "total_expense": [self.total_expense.x, self.total_expense.y],
            "amount_in_words": [self.amount_in_words.x, self.amount_in_words.y]
        }


class ConfigurationSettings:
    def __init__(self):
        self.data = {}
        with open('configurations.json') as json_data:
            self.data = json.load(json_data)

    def add_config(self, configuration):
        self.data[configuration.name] = configuration.to_dictionary()

    def save(self):
        with open('configurations.json', 'w') as outfile:
            json.dump(self.data, outfile)
