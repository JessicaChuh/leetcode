#Given an array of characters chars, compress it using the following algorithm:
#Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
#If the group's length is 1, append the character to s.
#Otherwise, append the character followed by the group's length.
#The compressed string s should not be returned separately, but instead, be
#stored in the input character array chars. Note that group lengths that are
#10 or longer will be split into multiple characters in chars.

#After you are done modifying the input array, return the new length of the
#array.

#You must write an algorithm that uses only constant extra space.




#GTP version
def compress(chars):
    write = 0
    read = 0
    count = 0

    while read < len(chars):
        count += 1

        if read == len(chars)-1 or chars[read] != chars[read+1]:
            chars[write] = chars[read]
            write += 1

            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1

            count = 0

        read += 1

    return write

#Other version
def compress(chars):
        i = 1
        j = 1
        mc = chars[0]
        for char in chars[1:]:
            if char == mc:
                del chars[j]
                i+=1
            else:
                mc = char
                if i > 1:
                    for c in reversed(str(i)):
                        chars.insert(j, c)
                    j+=len(str(i))
                j+=1
                i = 1
        if i > 1:
            for c in str(i):
                chars.append(c)
        return len(chars)
