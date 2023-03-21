def function(y: str, variable: str, x):

    equation = ""

    for i in y:
        if i != variable:
            equation += i
        else:
            equation += "x"

    return eval(equation)

def takeDerivative(y: str, variable: str, x, h):

    equationPlush = ""

    for i in y:
        if i != variable:
            equationPlush += i
        else:
            equationPlush += "(x+h)"

    func = function(y, variable, x)

    derivative = ( eval(equationPlush) - func ) / h

    return derivative

def newtonRaphson(y: str, variable: str, x, h, num_iterations):

    for j in range(num_iterations): 
        
        x -= function(y, variable, x) / takeDerivative(y, variable, x, h)

    return x