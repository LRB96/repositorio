def fibonacci(n):
	
	if n == 0 or n == 1:
		return 1

	return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)



# def f(n):
# 	for i in range(n):
# 		for j in range(n):
# 			print(i, j)

# f(5)


# def funcion_decoradora(funcion):
# 	def wrapper():
# 		print("Este es el último mensaje...")
# 		funcion()
# 		print("Este es el primer mensaje ;)")
# 	return wrapper

# def zumbido():
# 	print("Buzzzzzz")

# zumbido = funcion_decoradora(zumbido)



# def funcion_mayor():
# 	print("Esta es una función mayor y su mensaje de salida.")

# 	def librerias():
# 		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

# 	def frameworks():
# 		print("Algunos frameworks de Python son: Django, Dash y Flask.")

# 	frameworks()
# 	librerias()

if __name__ == "__main__":
    # funcion_mayor()
    # zumbido()
	# f()
	fibonacci()