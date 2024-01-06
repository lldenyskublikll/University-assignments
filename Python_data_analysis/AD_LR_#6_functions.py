import pandas as pd

# перевірка на можливість  конвертації в int
def is_convertible_to_int(value): 
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False

# перевірка на можливість  конвертації в float
def is_convertible_to_float(value):
    try:
        float_value = int(value)
        return True
    except ValueError:
        return False
    
# Перевірка коректності значень у стовпці "Warehouse_block" 
values_for_warehouse = ['A','B','C','D','F']

def check_warehouse(value):
    if value in values_for_warehouse:
        return value
    else:
        try:
            values_for_warehouse[0] in values_for_warehouse
            return values_for_warehouse[0]
        except:
            return 'A'

# Перевірка коректності значень у стовпці "Mode_of_Shipment"
mode_of_shipment = ['Flight', 'Ship', 'Road']
    
def check_shipment(value):
    if pd.isna(value):
        return value
    elif value in mode_of_shipment:
        return value
    else:
        # Якщо значення не є хибним і не входить у mode_of_shipment, замінюємо його на перший елемент mode_of_shipment
        return mode_of_shipment[0]

# Перевірка коректності значень у стовпці "Product importance"
mode_of_importance = ['high', 'low', 'medium']

def check_importance(value):
    return value in mode_of_importance

# Перевірка коректності значень у стовпці "Gender"
genders =['M', 'F']
def check_gender(value):
    return value in genders
