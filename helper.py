import os, sys, time, csv, json


class Helper:

    def __init__(self, debug=False):
        self.debug = debug

    def debug_msg(self, msg):
        if self.debug:
            print(msg)

    def create_dir(self, dir_name, parent_dir):
        new_dir = os.path.join(parent_dir, dir_name)
        if not self.check_dir(new_dir):
            os.mkdir(new_dir)
            self.debug_msg('Created directoy : {}'.format(new_dir))
        return new_dir

    def check_dir(self, full_dir):
        try:
            os.listdir(full_dir)
            self.debug_msg('Directory Exists : {}'.format(full_dir))
            return True
        except FileNotFoundError:
            self.debug_msg('Directory does not Exists : {}'.format(full_dir))
            return False

    def writing_csv(self, data, csv_filename):
        myFile = open(csv_filename, 'a', newline='', encoding='utf-8', errors='replace')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerow(data)

        return csv_filename

    def reading_csv(self, csv_filename):
        if os.path.exists(csv_filename):
            f = open(csv_filename, 'r', newline='', encoding='utf-8', errors='replace')
            csv_data = []
            reader = csv.reader(f)
            for row in reader:
                csv_data.append(row)
            f.close()
            return csv_data
        else:
            return []

    def write_to_json(self, filepath, data):
        with open(filepath, 'w') as js:
            json.dump(data, js, indent=3)

    def read_json(self, filepath):
        try:
            with open(filepath, 'r') as js:
                return json.load(js)
        except FileNotFoundError:
            return []

    def append_to_json(self, filepath, data):
        ext_data = self.read_json(filepath)
        if data not in ext_data:
            ext_data.append(data)
        self.write_to_json(filepath, ext_data)

    def append_to_csv(self, csv_filename, new_data):
        old_data = self.reading_csv(csv_filename)
        old_data.append(new_data)
        self.writing_csv(old_data,csv_filename)
