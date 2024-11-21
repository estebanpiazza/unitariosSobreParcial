import ast
from resolucion import analizar_lista_reproduccion

# Métodos nativos restringidos
NATIVE_METHODS = [
    "max", "min", "sum", "len", "sorted", "reversed", "filter",
    "map", "reduce", "zip", "enumerate", "all", "any"
]

# Lista de restricciones
RESTRICCIONES = {
    "Uso de pass": "pass",
    "Uso de continue": "continue",
    "Uso de break": "break",
    "Uso de listas de listas": "nested_list_detected",
    "Uso de variables externas al scope": "global",
    "Bucles infinitos detectados": "infinite_loop_detected",
    "Uso de métodos nativos restringidos": "native_methods_detected"
}


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.issues = {key: False for key in RESTRICCIONES.keys()}
        self.variables_globales = set()

    def visit_Pass(self, node):
        self.issues["Uso de pass"] = True
        self.generic_visit(node)

    def visit_Continue(self, node):
        self.issues["Uso de continue"] = True
        self.generic_visit(node)

    def visit_Break(self, node):
        self.issues["Uso de break"] = True
        self.generic_visit(node)

    def visit_List(self, node):
        if any(isinstance(e, ast.List) for e in node.elts):
            self.issues["Uso de listas de listas"] = True
        self.generic_visit(node)

    def visit_Global(self, node):
        self.issues["Uso de variables externas al scope"] = True
        for name in node.names:
            self.variables_globales.add(name)
        self.generic_visit(node)

    def visit_While(self, node):
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            self.issues["Bucles infinitos detectados"] = True
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in NATIVE_METHODS:
            self.issues["Uso de métodos nativos restringidos"] = True
        self.generic_visit(node)

    def report(self):
        print("\n--- Análisis de Restricciones ---")
        for restriccion, encontrada in self.issues.items():
            print(f"{restriccion}: {'Encontrada' if encontrada else 'No encontrada'}")


def verificar_restricciones(codigo_path):
    with open(codigo_path, "r") as file:
        codigo = file.read()

    try:
        tree = ast.parse(codigo)
        analyzer = CodeAnalyzer()
        analyzer.visit(tree)
        analyzer.report()
    except Exception as e:
        print("Error al analizar el código:", str(e))


def test_analizar_lista_reproduccion():
    errores = {
        "Err1": 0,
        "Err2": 0,
        "Err3": 0,
        "Err4": 0,
        "Err5": 0,
        "Err6": 0,
        "Err7": 0,
        "Err8": 0,
        "Err9": 0,
        "Err10": 0,
        "Otros": 0
    }
    
    puntos_totales = 3

    top5 = ["cancion1", "cancion2", "cancion3", "cancion4", "cancion5"]
    lista_reproduccion = [
        "cancion1", "cancion2", "cancion3", 
        "cancion1", "cancion6", "cancion7", 
        "cancion8", "cancion1"
    ]

    try:
        porcentaje = analizar_lista_reproduccion(top5, lista_reproduccion)
        if porcentaje != 60:
            errores["Err8"] += 0.5
            errores["Err9"] += 0.25
    except Exception as e:
        errores["Err10"] += 3

    total_descuento = sum(errores.values())
    puntos_obtenidos = max(0, puntos_totales - total_descuento)

    print("\nResultados:")
    for error, descuento in errores.items():
        print(f"{error}: {descuento} puntos descontados")
    print(f"Puntos obtenidos: {puntos_obtenidos} / {puntos_totales}")


if __name__ == "__main__":
    print("\n--- Ejecutando Pruebas ---")
    test_analizar_lista_reproduccion()
    
    print("\n--- Verificando Restricciones ---")
    verificar_restricciones("resolucion.py")
