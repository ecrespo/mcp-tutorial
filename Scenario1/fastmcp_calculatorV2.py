from fastmcp import FastMCP


mcp = FastMCP(name="Calculator")


@mcp.tool(
    name = "add",
    description = "Adds two numbers together and returns the result.",
    tags={"math", "addition"},
)
def add(a: float, b: float)-> float:
    """
    Adds two floating-point numbers and returns the result.

    This function performs the addition of two numbers provided as input and
    returns their sum.

    :param a: The first number to add.
    :type a: float
    :param b: The second number to add.
    :type b: float
    :return: The sum of `a` and `b`.
    :rtype: float
    """
    return a + b

@mcp.tool(
    name = "sub",
    description = "Subtracts one number from another and returns the result.",
    tags={"math", "subtraction"},
)
def sub(a: float, b: float) -> float:
    """
    Subtracts one number from another and returns the result.

    This function takes two floating-point numbers as inputs, subtracts the
    second number from the first, and provides the resulting difference.

    :param a: The first number (minuend).
    :param b: The second number (subtrahend).
    :return: The result of subtracting b from a.
    :rtype: float
    """
    return a - b

@mcp.tool(
    name = "mul",
    description="Multiplies two numbers and returns the result.",
    tags={"math", "multiplication"},
)
def mul(a: float, b: float) -> float:
    """
    Multiplies two numeric values.

    This function takes two numeric arguments and returns their product. It performs
    a basic multiplication operation and supports any numbers provided as input
    within the scope of float type.

    :param a: A floating-point number, representing the first operand.
    :param b: A floating-point number, representing the second operand.
    :return: The product of the two given numbers as a floating-point value.
    """
    return a * b

@mcp.tool(
    name = "div",
    description = "Divides two numbers and returns the result.",
    tags={"math", "division"},
)
def div(a: float, b: float) -> float:
    """
    Divides two numbers and returns the result.

    This function calculates the division of two floating-point numbers.
    It takes two parameters, `a` and `b`, where `a` is divided by `b`.

    :param a: The numerator.
    :type a: float
    :param b: The denominator.
    :type b: float
    :return: The result of the division.
    :rtype: float
    :raises ZeroDivisionError: If the denominator `b` equals zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    return a / b


if __name__ == "__main__":
    mcp.run(transport="http",host="localhost",port=8002)  # STDIO by default
