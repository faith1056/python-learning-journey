single_item = ("vanilla",)
print(single_item)
print(type(single_item))


signature_blend = ("vanilla","caramel","hazelnut")
print(signature_blend[1])
print(signature_blend[-1])

signature_blend = ("vanilla","caramel","hazelnut")
print(f"To make the House Blend,use:{signature_blend[0]} and {signature_blend[1]}")


signature_recipe = ("vanilla","chocolate","hazelnut")
left_pump,center_pump,right_pump = signature_recipe
print(left_pump)
print(center_pump)
print(right_pump)


dimensions = (12, 8)
width,height = dimensions
print(width)
print(height)


foods = ("rice", "beans", "yam")
print(foods[-1])
print(foods[0])
print(foods[1])
print(foods[2])


foods = ("rice", "beans", "yam")
print(len(foods))


foods = ("rice", "beans", "yam")
for food in foods:
    print(food)

