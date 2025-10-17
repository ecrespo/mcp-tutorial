from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Calculator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/multiply")
def multiply(a: float, b: float) -> dict[str, float]:
    """
    Multiplies two floating-point numbers and returns the result.

    This function takes two floating-point numbers as inputs,
    multiplies them, and returns a dictionary containing the
    result of the multiplication.

    Parameters:
        a: float
            The first floating-point number to be multiplied.
        b: float
            The second floating-point number to be multiplied.

    Returns:
        dict[str, float]: A dictionary containing the result of the
        multiplication with the key "result".
    """
    result = a * b
    return {"result": result}


@app.post("/add")
def add(a: float,b: float) -> dict[str, float]:
    """
    Adds two floating-point numbers and returns the result.
    """
    result = a + b
    return {"result": result}


@app.post("/subtract")
def subtract(a: float,b: float) -> dict[str, float]:
    """
    Subtracts one number from another and returns the result.
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
def div(a: float, b: float) -> dict[str, float]:
    """
    Divides two numbers and returns the result.
    """
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = a / b
    return {"result": result}


mcp = FastApiMCP(
    app,
    name="Calculator",
    description="A simple calculator API using FastAPI and FastApiMCP",
 )
mcp.mount_sse()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)