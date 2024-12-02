# Guardar este código en un archivo llamado "example.py"
code = '''
def calculate_sum(a,b):
  result=a + b 
  return result 
print(calculate_sum(5,3))
'''
with open("example.py", "w") as file:
    file.write(code)
