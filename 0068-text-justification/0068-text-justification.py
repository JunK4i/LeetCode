class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rows = [[]]
        char_count = 0
        for word in words:
            char_count+= len(word)
            # print(word, char_count)
            if char_count<maxWidth:
                rows[-1].append(word)
                char_count+=1 #account for space
            elif char_count == maxWidth:
                rows[-1].append(word)
                rows.append([])
                char_count = 0
            elif char_count > maxWidth:
                rows.append([word])
                char_count = len(word)+1
        if rows[-1] == []:
            rows.remove([])
        for i in range(len(rows)):
            char_count = len("".join(rows[i]))
            remainder = maxWidth-char_count
            if i == len(rows)-1:
                temp = " ".join(rows[i])
                rows[i] = temp + " "*(maxWidth-len(temp))
            else:
                spaces = len(rows[i])-1
                if spaces != 0:
                    space = " "*(remainder//spaces)
                    space_list = [space for x in range(spaces)]
                    extra_space =remainder%spaces
                    idx = 0
                    while extra_space >0:
                        space_list[idx] +=" "
                        extra_space-=1
                        idx+=1
                    row=""
                    for j in range(len(space_list)):
                        row += rows[i][j]+space_list[j]
                    row+=rows[i][-1]
                else: 
                    row = rows[i][0] + " "*remainder
                rows[i] = row
        return rows