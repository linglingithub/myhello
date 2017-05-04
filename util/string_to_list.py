def string_to_int_list(instr):
    import re
    tokens = re.split(',| |\[|\]', instr)
    result = []
    #tokens = instr.split(",[]")
    for token in tokens:
        if token != "":
            result.append(int(token))
    return result

# a = "[1, 2]"
# b = string_to_int_list(a)
# print b, type(b)