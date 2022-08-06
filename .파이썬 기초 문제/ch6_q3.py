str = input().split('  ') #공백 2개를 기준으로 인덱스 나누기
for i in range(len(str)):
    str[i]=list(str[i].split(' ')) #공백 1개를 기준으로 중첩 문자열 내부의 인덱스 구분으로 문자를 1개씩 분리
for i in range(len(str)):
    for j in range(len(str[i])):  #이중 중첩문과 조건문으로 리스트 내부를 알파벳으로 바꾸기
        if str[i][j] == '.-':
            str[i][j] = 'A'
        elif str[i][j] == '-...':
            str[i][j] = 'B'
        elif str[i][j] == '-.-.':
            str[i][j] = 'C'
        elif str[i][j] == '-..':
            str[i][j] = 'D'
        elif str[i][j] == '.':
            str[i][j] = 'E'
        elif str[i][j] == '..-.':
            str[i][j] = 'F'
        elif str[i][j] == '--.':
            str[i][j] = 'G'
        elif str[i][j] == '....':
            str[i][j] = 'H'
        elif str[i][j] == '..':
            str[i][j] = 'I'
        elif str[i][j] == '.---':
            str[i][j] = 'J'
        elif str[i][j] == '-.-':
            str[i][j] = 'K'
        elif str[i][j] == '.-..':
            str[i][j] = 'L'
        elif str[i][j] == '--':
            str[i][j] = 'M'
        elif str[i][j] == '-.':
            str[i][j] = 'N'
        elif str[i][j] == '---':
            str[i][j] = 'O'
        elif str[i][j] == '.--.':
            str[i][j] = 'P'
        elif str[i][j] == '--.-':
            str[i][j] = 'Q'
        elif str[i][j] == '.-.':
            str[i][j] = 'R'
        elif str[i][j] == '...':
            str[i][j] = 'S'
        elif str[i][j] == '-':
            str[i][j] = 'T'
        elif str[i][j] == '..-':
            str[i][j] = 'U'
        elif str[i][j] == '...-':
            str[i][j] = 'V'
        elif str[i][j] == '.--':
            str[i][j] = 'W'
        elif str[i][j] == '-..-':
            str[i][j] = 'X'
        elif str[i][j] == '-.--':
            str[i][j] = 'Y'
        elif str[i][j] == 'Z':
            str[i][j] = '--..'
        print('%c' % str[i][j], end = '') #줄이 바뀌지 않도록 end = ' '를 추가해준다
    print('', end = ' ')