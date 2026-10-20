def is_anagram_counts(s: str, t: str) -> bool:
    """this is a function to check if two strings are anagrams of each other using character counts"""
    
    if len(s) != len(t):
        return False

    count_s = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        if char not in count_s:
            return False
        else:
            count_s[char] -= 1
            if count_s[char] < 0:
                return False
    return True


def is_anagram_sort(s: str, t: str) -> bool:

    """this is a function to check if two strings are anagrams of each other using sorting"""
    return sorted(s) == sorted(t)


print(is_anagram_counts("listen", "silent"))
print(is_anagram_counts("rat", "car"))
print(is_anagram_counts("a", "ab"))
print(is_anagram_sort("anagram", "nagaram"))
print(is_anagram_counts("aa", "aa"))
print(is_anagram_counts("anagram", "nagaram"))