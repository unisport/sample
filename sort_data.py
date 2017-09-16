import json

from utilities import parse_money

def main():
    with open("products.json", "r", encoding="utf8") as input_file, open("products.sorted.json", "w", encoding="utf8") as output_file:
        data = json.load(input_file)
        output_file.write(
            json.dumps(
                sorted(data, key=lambda p: parse_money(p["price"], p["currency"])),
                indent=4,
                ensure_ascii=False
            )
        )

if __name__ == "__main__":
    main()
