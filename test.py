import json
def read_json():
    with open("bank.json", "r") as myfile:
        return json.load(myfile)


def write_to_json(list):
    with open("bank.json", "w") as myfile:
        myfile.write(json.dumps(list))



write_to_json([{"justin": 1}, {"amber": 2}])