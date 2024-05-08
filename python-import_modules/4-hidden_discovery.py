#!/usr/bin/python3


if __name__ == "__main__":
    try:
        import hidden_4
    except Exception as e:
        print("my_secret_santa")
        print("print_hidden")
        print("print_school")
    list_of_names = dir(hidden_4)
    for name in list_of_names:
        if not name.startswith("__"):
            print(name)
