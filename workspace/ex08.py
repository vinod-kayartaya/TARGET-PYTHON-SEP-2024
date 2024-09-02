from pprint import pprint
import json


def main():
    p1 = {'firstname': 'Vinod', 'age' : 50, 'married': True}
    p1['email'] = 'vinod@vinod.co'
    p1['address'] = {
        'area': 'ISRO layout',
        'city': 'Bangalore',
        'state': 'Karnataka',
        'country': 'India'
    }
    pprint(p1)
    print(json.dumps(p1, indent='  '))


if __name__ == '__main__':
    main()
