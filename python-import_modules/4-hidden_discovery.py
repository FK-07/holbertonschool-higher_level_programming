#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    all_names = dir(hidden_4)
    sorted_names = sorted(all_names)
    for name in sorted_names:
        if not name.startswith("__"):
            print("{}".format(name))
