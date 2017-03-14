import ast
def calc_pol(pol_str, x = None):
    # your code here
    if (x == None):
        result = "There is no value for x"
        return result
    else:
        node = ast.parse(pol_str, mode='eval')
        code_object = compile(node, filename='<string>', mode='eval')
        result = eval(code_object)
        if result == 0:
            return ('Result = 0, so ' + str(x) + ' ' + 'is a root of ' + pol_str)
        else:
            return ('Result =' + ' ' + str(result))
    #else:
    #    return ('Result = 0, so ' + str(x) + ' ' + 'is a root of ' + pol_str)
    #return result; # see the the cases in the instructions
calc_pol("2*x**2 + 3*x")
