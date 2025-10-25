class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
   
    # def DESCRAIBE (self):
    #     print(f"This pizza contains: {self.ingredients}")

    @classmethod 
    def veg(cls):
        return cls(['mushrooms', 'olives', 'onions'])
   
    @classmethod
    def mar(cls):
        return cls(['mozzarella', 'sauce'])

   
    def __str__(self):
        #! "".JOIN()
        ingredients_str =" and ".join(self.ingredients) #? delet [] in the affichage
        return f"Pizza ingrrdients are : {ingredients_str}"
    

   


# إنشاء كائنات البيتزا
Pizza_1 = Pizza(['tomatoes', 'olives'])
Pizza_2 = Pizza.veg()
Pizza_3 = Pizza.mar()

print(Pizza_1)
print(Pizza_2)
print(Pizza_3)

