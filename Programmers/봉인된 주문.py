# [프로그래머스] 2025 프로그래머스 코드챌린지 2차 예선 > 봉인된 주문

def solution(n, bans):
    
    def convert_to_spell(n) :
        spell_idx = []
        idx = n % 26
        while n >= 26 :
            idx = n % 26
            if idx == 0 : idx = 26 # 0을 Z로 취급
            if len(spell_idx) != 0 and spell_idx[-1] == 26 : 
                idx -= 1 # 이전 문자가 Z이면 처리.. 사실 아직도 이해 안감
                if idx == 0 : idx = 26 # 0을 Z로 취급
            spell_idx.append(idx)
            
            n = n // 26
        
        if spell_idx[-1] == 26 : 
            if n != 1 : spell_idx.append(n-1)
        else : spell_idx.append(n)
        
        # 문자로 변환
        string = ''
        
        for i in spell_idx :
            string += chr(i+96)
        return string[::-1]
    
    og = convert_to_spell(n)
    bans.sort(key=lambda x: (len(x), x))

    for ban in bans :
        if len(ban) < len(og) :
            n += 1
            og = convert_to_spell(n) # 비교할 문자열을 업데이트
        elif len(ban) == len(og) and ban <= og :
            n += 1
            og = convert_to_spell(n) # 비교할 문자열을 업데이트
    return convert_to_spell(n)