import time
import json

def main():
    filename = input('Enter a CSV filename: ')
    
    if not filename.lower().endswith('.csv'):
        raise ValueError('You must enter a .csv filename')
    
    output_filename = f'{filename[:-4]}.{time.time()}.json'

    with open(filename, encoding='utf-8') as file:
        header = file.readline().strip().split(',')
        data = []
        for each_line in file:
            values = each_line.strip().split(',')
            d = dict(zip(header, values))
            data.append(d)
        
    with open(output_filename, mode='wt', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)
        print(f'JSON data saved to {output_filename}')


if __name__ == '__main__':
    main()
