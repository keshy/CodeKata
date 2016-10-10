# coding=utf-8
# Input  : str = “()())()”
# Output : ()()() (())()
# There are two possible solutions
# "()()()" and "(())()"
#
# Input  : str = (v)())()
# Output : (v)()()  (v())()


def is_valid(invalid_string):
    st = []
    i = 0
    for k in invalid_string:
        if k == '(':
            st.append(k)
            i += 1
        if k == ')':
            try:
                st.remove('(')
                i -= 1
            except Exception:
                return False
    if len(st) == 0:
        return True
    else:
        return False


def valid_strings(invalid_string, hide, results=set(), ejected=set()):

    if hide == len(invalid_string):
        return results, ejected

    altered = [x for x in invalid_string]
    altered.pop(hide)
    if is_valid(altered):
        ejected.add(hide)
        results.add(''.join(altered))
    # some memoization should be possible here
    return valid_strings(invalid_string, hide + 1, results, ejected)

##################
# Bug: this does not work for cases where there are more than one parenthesis to be removed
##################
if __name__ == '__main__':
    str = '()))'
    print(valid_strings(str, 0))