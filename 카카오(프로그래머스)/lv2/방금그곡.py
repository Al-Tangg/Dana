def solution(m, musicinfos):
    answer = "(None)"
    mlen = 0
    
    m = m.replace("A#", "H").replace("G#", "I").replace("F#", "J").replace("D#", "K").replace("C#", "L").replace("B#","M")
    
    for music in musicinfos:
        start, end, name, melody = music.split(",")
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        melodylen = (e_h - s_h) * 60 + (e_m - s_m)
        
        melody = melody.replace("A#", "H").replace("G#", "I").replace("F#", "J").replace("D#", "K").replace("C#", "L").replace("B#","M")
        melodys = melody * (melodylen // len(melody)) + melody[:(melodylen % len(melody))]
    
        if m in melodys and mlen < melodylen:
            mlen = melodylen
            answer = name
    
    return answer
