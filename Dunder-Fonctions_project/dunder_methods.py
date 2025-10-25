class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"Order of {self.customer}: {self.cart}"

    def __repr__(self):
        return f"Order(List of items, customer name)"

    # def __bool__(self):
    #     return len(self.cart) > 0 

    def __add__(self, other):
        new_cart =  self.cart.copy()
        new_cart.append(other)
        return Order(new_cart,self.customer)
    
    def __iadd__(self,other):
       self.cart.append(other)
       return self
    
    def __imul__(self,other):
       self.cart.append(other)
       return self
    


# تجربة الكلاس
order = Order(["mouse", "keyboard"], "islam hesham")

order + "BB"
rr =  "monitor" + order 
rr += "chair"
rr *= 3
print(rr.cart)
