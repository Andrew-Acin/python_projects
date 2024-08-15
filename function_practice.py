def hello():
    print("Hello User")

hello()


def pack(first_name, last_name , age):
    print(first_name, last_name , age)

pack("andy", "acin", 28)


# def eat_lunch(food):
#     for i in food:
#       print("I ate my " + i)

# snacks = ["apple", "chips", "sandwich"]


# eat_lunch(snacks)

# def eat_lunch(lunch):
#     for i in lunch:
#         print("First i ate my " + i)
#     else:
#         print("My lunchbox is empty")

# snacks = ["apple", "chips", "sandwich"]

# eat_lunch(snacks)
# eat_lunch()
# eat_lunch()

def eat_lunch(snack):
    if len(snack) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(snack)):
            if i == 0:
                print(f"First i ate my {snack[0]}")
            else:
                print(f"Then i ate my {snack[i]}")


eat_lunch(["apple","chips","sandwich"])
eat_lunch([])



