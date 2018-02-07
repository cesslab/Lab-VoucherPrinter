import csv


class Voucher:
    def __init__(self):
        self.error = None
        self.subjects = []
        self.payoffs = []

    def open_file(self, filename):
        try:
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter='\t')
                for row in csv_reader:
                    if row[1]:
                        self.subjects.append(row[1].strip())
                        self.payoffs.append(row[4].strip())
                return True
        except Exception as e:
            self.error = e
            return False
