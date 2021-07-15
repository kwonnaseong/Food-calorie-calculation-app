
import json

def read_data():
    raw_datas = []
    filtered_data = {}
    with open('data.txt', encoding = 'utf-8') as json_file:
        raw_datas = json.load(json_file)

    # 데이터 정제
    for raw_data in raw_datas :
        if 'item_desc_kor' not in raw_data or 'year' not in raw_data or 'cnt1' not in raw_data:
            continue
        name = raw_data['item_desc_kor']
        year = raw_data['year']
        calorie = raw_data['cnt1']
        if name in filtered_data and year < filtered_data[name]['year'] :
            continue
        filtered_data[name] = { 'name' : name, 'year' : year, 'calorie' : calorie }

    return filtered_data.values()

def main():
    print("라면 칼로리 확인\n\n")
    ramyun_list = read_data()

    while True :
        find_name = input('라면 이름 입력 : ')
        for info in ramyun_list :
            if find_name in info['name'] :
                print('{} : {}'.format(info['name'], info['calorie']))
            print('')

if __name__ == '__main__' :
    main()