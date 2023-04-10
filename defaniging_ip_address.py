def defangIPaddr(self, address: str) -> str:
    newadd = ""
    for i in address:
        if i == ".":
            i = "[.]"
        newadd += i
