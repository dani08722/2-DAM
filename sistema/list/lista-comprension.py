values ="32,45,11,87,20,48"

int_values=[int(value)for value in values.split(",") if value.startswith("4")] 

print(int_values)