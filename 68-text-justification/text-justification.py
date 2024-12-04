class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0
        
        while i < len(words):
            if length + len(line) - 1 + len(words[i]) >= maxWidth:
                spaces = maxWidth - length 
                spaces_per_word = spaces//max(1, (len(line) - 1))
                spaces_remained = spaces % max(1, (len(line) - 1))
                
                for j in range(max(1, len(line) - 1)):
                    line[j] += spaces_per_word * " "
                    if spaces_remained:
                        line[j] += " "
                        spaces_remained -= 1
                res.append("".join(line))
                line, length = [], 0
                
            line.append(words[i])
            length += len(words[i])
            i+=1
        
        last_line = " ".join(line)
        spaces = maxWidth - len(last_line)
        last_line += " " * spaces
        res.append(last_line)
        return res
        
# Explanation Video (https://www.youtube.com/watch?v=TzMl4Z7pVh8)