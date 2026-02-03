# def greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [1, 3, 5, 7 ,8 ,110 ,23 ,45 ,89]

new = list(filter(lambda x: x>9, a))
print(new)  