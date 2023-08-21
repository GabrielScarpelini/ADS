from flask import Flask, jsonify, request

app = Flask(__name__) 

@app.route("/")
def qnt_primos():
    quantityTotal = 100
    primos = "1,2"
    candPrimo = 3
    qtdFound = 2
    ehPrimo = 1
 
    while qtdFound < quantityTotal:
        for i in range (2, candPrimo):
            if candPrimo % i == 0:
                ehPrimo = 0
                break
        if ehPrimo == 1:
            primos = primos +","+ str(candPrimo)
            qtdFound += 1
        ehPrimo = 1
        candPrimo +=1
        if qtdFound % 10 == 0:
            primos += "\n"
    qtdFound += 1
    return primos

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
