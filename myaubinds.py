import json

def move_binds():
    source_file = input("Enter the path to the config you want to take the binds from: ")
    destination_file = input("Enter the path to the config you want the binds moved to: ")

    with open(source_file, 'r') as f:
        source_data = json.load(f)

    binds = {}

    for key, value in source_data.items():
        if 'key' in value:
            binds[key] = value['key']

    with open(destination_file, 'r') as f:
        destination_data = json.load(f)

    for key, value in destination_data.items():
        if key in binds:
            destination_data[key]['key'] = binds[key]

    with open(destination_file, 'w') as f:
        json.dump(destination_data, f, indent=2)

move_binds()
