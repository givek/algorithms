from algorithms.data_structures.hash.rolling_hash import RollingHash


def is_sub_string(s, t):
    rs = RollingHash(s)
    rt = RollingHash(t[: len(s)])

    if rs.word_hash == rt.word_hash:
        if rs.word == rt.word:
            return True

    for i in range(len(s), len(t)):
        rt.append(t[i])
        rt.skip()

        if rs.word_hash == rt.word_hash:
            if rs.word == rt.word:
                return True

        print(rt.word, rt.word_hash, rs.word_hash)

    return False


def main():
    s = "hen"
    t = "cade how henlo  you"

    print(is_sub_string(s, t))


if __name__ == "__main__":
    main()
