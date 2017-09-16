import json

from utilities import parse_money

def main():
    with open("products.json") as input_file:
        data = json.load(input_file)
        print(json.dumps(sorted(data, key=lambda p: parse_money(p["price"], p["currency"])), indent=4))

if __name__ == "__main__":
    main()
