import json

def main():  
    with open('json/test.json')as f:
        jsn = json.load(f)
        print(jsn)
    for jsn_key in jsn:
        print(jsn_key)
    for jsn_value in jsn.values():
        print(jsn_value)

    json_open = open('json/test.json', 'r')
    load_json = json.load(json_open)

    for value in load_json.values():
        # print(value["key3"])
        print()#value

if __name__ == "__main__":
    main()