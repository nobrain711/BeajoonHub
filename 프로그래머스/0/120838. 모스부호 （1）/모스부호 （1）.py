def solution(letters):
    # 모스부호 해독표
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    # 정답
    answer = ''
    
    # 1. 리스트로 입력된 문장을 한 개의 부호로 분리
    letters = letters.split(' ')
    
    # 2. 모스부호 해독하기 쉽게 부호 문자로 분리
    morse_sgin = list(morse.keys())
    morse_char = list(morse.values())
    
    # 3. letters를 반복문으로 부호를 매칭
    for letter in letters:
        answer +=  morse_char[morse_sgin.index(letter)]
        
    # 4. 결과 반환
    return answer
    