for i in range(4):
    current_file_url = f"cmq{i}.json"

    with open(debates_file_path) as file:
        current_file_data = file.read().split("\n")

    for line in current_file_data:
        print(line)