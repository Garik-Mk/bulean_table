
def get_variables_positions(string: str) -> list[list]:
    """Returns [[2], [4,6], [8]], for string _ _ a _ b _ b _ c """
    variables_dict = {}

    for i, s in enumerate(string):
        if s not in {'>', '!', '(', ')'}:
            if s in variables_dict.keys():
                variables_dict[s].append(i)
            else:
                variables_dict[s] = [i]

    return list(variables_dict.values())


def get_parentheses_pairs(string: str) -> list[list]:
    """(((a>b)>(c))>(b>!(c))) -> [[2, 6], [8, 10], [1, 11], [17, 19], [13, 20], [0, 21]]"""
    opening_stack = []
    answer = []
    for i, s in enumerate(string):
        if s == '(':
            opening_stack.append(i)
        elif s == ')':
            answer.append([opening_stack.pop(), i])
    
    return answer

def implication(a: bool, b: bool) -> bool:
    return not(a) or b


def main():
    ...


if __name__ == '__main__':
    # print(get_variables_positions('__a_b_b_c'))
    main()