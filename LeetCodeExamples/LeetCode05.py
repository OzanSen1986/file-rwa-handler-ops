'''You are given a list of strings.
Group the strings that are anagrams (words formed using the same letters in the same counts).
Return a list of groups, where each group is a list of anagram strings.'''

word_list= ["pipe", "pine", "nipe", "pepi", "peip", "pineapp", "apppine", "pien"]
def groupAnagrams(strs: list[str]):
    result={}
    for word in strs:
        sorted_word=''.join(sorted(word))
        if sorted_word not in result:
            result[sorted_word] = []
        result[sorted_word].append(word)
    return list(result.values())


print(groupAnagrams(word_list))