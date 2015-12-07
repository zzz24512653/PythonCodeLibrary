def get_next(p):
    next_val = [-1]
    i = 0
    j = next_val[i]
    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            if p[i] != p[j]:
                next_val.append(j)
            else:
                next_val.append(next_val[j])
        else:
            j = next_val[j]
    return next_val


def kmp(s, p):
    if s is None or p is None or len(p) > len(s):
        return None
    next_val = get_next(p)
    i = 0
    j = 0
    while i < len(s):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_val[j]
        if j == len(p):
            return i - len(p)
    return -1


if __name__ == "__main__":
    # print get_next("abaabcac")
    print kmp("baacddaa", "da")
