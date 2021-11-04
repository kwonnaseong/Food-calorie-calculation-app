


def pretreatment_file(file_url):
    with open(file_url, 'r') as input_f:
        with open('p_result.txt', 'w') as output_f:
            for line in input_f.readlines():
                line.strip()# 양쪽 공백 지우기
                if line.find(':') != -1 and line.find('%') != -1:
                    res = line.split(':')#':'뒤의 문자 다 없애기
                    output_f.write(res[0] + "\n")


