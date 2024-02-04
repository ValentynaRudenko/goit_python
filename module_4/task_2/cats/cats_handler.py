def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = [cat.strip().split(",") for cat in file.readlines()]
            list_of_dicts = []
            for cat in cats:
                dict = {}
                dict["id"] = cat[0]
                dict["name"] = cat[1]
                dict["age"] = cat[2]
                list_of_dicts.append(dict)
            return list_of_dicts

    except FileNotFoundError:
        return f"File {path} not found"
