def get_subgroups(chars):
    if len(chars) == 0:
        return [[]]
    else:
        first = chars[0]
        rest = chars[1:]
        subgroups_without_first = get_subgroups(rest)
        subgroups_with_first = []
        for subgroup in subgroups_without_first:
            subgroups_with_first.append([first] + subgroup)
        return subgroups_with_first + subgroups_without_first

# Example usage
chars = ['a', 'b', 'c']
subgroups = get_subgroups(chars)
print(subgroups)