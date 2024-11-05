# THE BIO FUNCTION
def bio(name,born,pronoun):
    age = 2024 - born
    FutureAge = 2051 - born
    print(name.title(), "was born in", born)
    print("He will turn", age, "years old this year")
    print("He will be", FutureAge, "in the year 2051")
    print(" ")

# PRINT BIOS
bio("stephen", 1984, "he")
bio("mary", 1990, "she")
bio("jane", 2000, "she")


# EXIT
quit()