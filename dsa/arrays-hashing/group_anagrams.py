def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Return the words grouped so that anagrams are in the same list."""
    
    groups: dict[str, list[str]] = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print(group_anagrams([]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
print(group_anagrams(["ab", "ba", "ab"]))
print(group_anagrams(["aab", "abb"]))