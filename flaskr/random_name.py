import random

names_list = ["Rhona", "Creola", "Damian", "Breann", "Mohamed", "Karima", "Xiao",
             "Delsie", "Loris", "Betsy", "Lashon", "Kareem", "Ebony",
             "Mary", "Cherlyn", "Jerrie", "Claretta", "Ailene", "Christeen",
             "Leann", "Carmina", "Odilia", "Maurine", "Cary", "Burton",
             "Virgil", "Carolynn", "Keitha", "Eveline", "Somer", "Paulina",
             "Katherina", "Cecile", "Rosamaria", "Jenise", "Lory", "Bernice",
             "Dewitt", "Evan", "Porfirio", "Timika", "Wilford", "Lilian",
             "Deneen", "Vania", "Sunni", "Karie", "Kenisha", "Shanae",
             "Oneida", "Janessa", "Loria", "Lakiesha", "Josie", "Palmira",
             "Rina", "Cassie", "Zada", "Deane", "Bethany", "Tonja",
             "Heather", "Burl", "Drucilla", "Chanelle", "Taina", "Palma",
             "Carmine", "Sharee", "Franklin", "Isidra", "Belen", "Gisela",
             "Sharlene", "Vonnie", "Perry", "Jeromy", "Esmeralda",
             "Letha", "Brianne", "Bennie", "Nancy", "Shaina", "Kelvin"]


def random_name():
    index = random.randint(0, len(names_list)-1)    # nosec
    return str(names_list[index])
