import os

# Paso 1: Obtener la ruta absoluta del directorio donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

# Paso 2: Crear la ruta completa al archivo dentro de la subcarpeta "s"
file_path = os.path.join(script_dir, "data.txt")

try:
    # Step 1: Open and read the content of the original file
    with open(file_path, "r") as file:
        data = file.read()  # Read the entire file content
    
    # Step 2: Reverse the content
    reversed_data = data[::-1]  # Reverse the entire string
    
    # Step 3: Write the reversed content to a new file
    file_path_2 = os.path.join(script_dir, "reversed_data.txt")

    with open(file_path_2, "w") as reversed_file:
        reversed_file.write(reversed_data)
        data2 = reversed_file.read()  # Read the entire file content
    
    print(data2)
    
    print("The content has been reversed and written to 'reversed_data.txt'.")
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")
except IOError:
    print("Error: An issue occurred while reading or writing the file.")
    
