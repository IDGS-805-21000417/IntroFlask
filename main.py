from flask import Flask, render_template, request
from io import open

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "IDGS805"
    lista = ["Pedro", "Juan", "Mario"]
    return render_template("index.html", titulo=titulo, lista=lista)
 

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/Hola")
def hola():
    return "<h1>Holaa mundo</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"el usuario es : {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es {n1 + n2}"

@app.route("/form1")
def form():
    return '''
            <form>
            <label for= "nombre"> Nombre: </label>
            <input type="text" id="nombre" required>
            '''

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/cinepolis")
def cine():
    return render_template("cinepolis.html")

@app.route("/resultado", methods=["GET","POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        resultado = ""
        op = request.form.get("opc")
        if op == "suma":
            resultado = ("La suma de {} + {} = {}".format(num1,num2, str(int(num1)+int(num2))))            
        
        if op == "resta":
            resultado = ("La resta de {} - {} = {}".format(num1,num2, str(int(num1)-int(num2))))            
        
        if op == "multi":
            resultado = ("La multiplicacion de {} * {} = {}".format(num1,num2, str(int(num1)*int(num2))))            
        
        if op == "divi":
            resultado = ("La division de {} / {} = {}".format(num1,num2, str(int(num1)/int(num2)))) 
                    
    return render_template("OperasBas.html", resultado=resultado)       
                


@app.route("/calcular", methods=["GET","POST"])
def operac():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        personas = int(request.form.get("cantCom"))
        boletos = int(request.form.get("cantBol"))
        opciones = request.form.get("Cineco")
        total: float = 0.0
        texto: str = ""  
            
        maxBoletos = (personas *7)
        costo = (boletos * 12)
        
        if boletos <= maxBoletos:
            
            if boletos >= 6:
                costo = (costo - (costo*0.15))                
                # Tarjeta CINECO
                if opciones == "si":
                    costo = (costo - (costo*0.10))
                                                                          
                    nota=open('boletos.txt', 'w')
                    total = total + costo
                    texto = "Nombre: {} costo: {} \nTotal: {}".format(nombre,costo,total)
                    nota.write(texto)
                    nota.close()    
                    
                    salida = ("El costo seria de: {}".format(costo))                        
                    return render_template("cinepolis.html", salida=salida)                                     
                else:
                                     
                    nota=open('boletos.txt', 'w')
                    total = total + costo
                    texto = "Nombre: {} costo: {} \nTotal: {}".format(nombre,costo,total)
                    nota.write(texto)
                    nota.close()    
                    
                    salida = ("El costo seria de: {}".format(costo))                        
                    return render_template("cinepolis.html", salida=salida)                                                                                    
            else:
                
                if boletos >= 3 and boletos <= 5:
                    costo = (costo - (costo*0.10))                    
                
                    if opciones == "si":
                        costo = (costo - (costo*0.10))
                                                                                         
                        nota=open('boletos.txt', 'w')
                        total = total + costo
                        texto = "Nombre: {} costo: {} \nTotal: {}".format(nombre,costo,total)
                        nota.write(texto)
                        nota.close()    
                                 
                        salida = ("El costo seria de: {}".format(costo))                        
                        return render_template("cinepolis.html", salida=salida)                                                         
                    else:                                             
                        nota=open('boletos.txt', 'w')
                        total = total + costo
                        texto = "Nombre: {} costo: {} \nTotal: {}".format(nombre,costo,total)
                        nota.write(texto)
                        nota.close()
                        
                        salida = ("El costo seria de: {}".format(costo))                        
                        return render_template("cinepolis.html", salida=salida)                                            

                else: 
                    # Tarjeta CINECO                               
                    if opciones == "si":
                        costo = (costo - (costo*0.10))                                         
                        nota=open('boletos.txt', '  w')
                        total = total + costo
                        texto = "Nombre: {} costo: {} \nTotal: {}".format(nombre,costo,total)
                        nota.write(texto)
                        nota.close()
                        
                        salida = ("El costo seria de: {}".format(costo))                        
                        return render_template("cinepolis.html", salida=salida)                                                                         
                    else:                    
                        nota=open('boletos.txt', 'w')
                        total = total + costo
                        texto = "Nombre: {} costo: {} \nTotal: {}".format(nombre,costo,total)
                        nota.write(texto)
                        nota.close()
                        
                        salida = ("El costo seria de: {}".format(costo))                        
                        return render_template("cinepolis.html", salida=salida)                                       
                        
                          
        else:        
            salida = ("Demasiados boletos\n Solo se pueden comprar un\nmaximo de 7 boletos por persona")                       
            return render_template("cinepolis.html", salida=salida)
                
if __name__ == "__main__":
    app.run(debug=True, port=3000)