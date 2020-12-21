def randName():
    for i in range(5):
        FirstName = r.choice(first_name)
        SecondName = "".join(r.choice(last_name))
        return FirstName + SecondName