# def multiple_args(snt,*num):
#     print(snt, num)


# if __name__ == "__main__":
#     multiple_args("write",1,2,3)


def name_likes_colors(name, *colors):
    print(f"A {name} likes the following colors:")
    for c in colors:
        print(f"- {c}")


if __name__ == '__main__':
    print(name_likes_colors("Max", "azul"))
    print(name_likes_colors("Tomas", "azul", "verde"))
    print(name_likes_colors("Clark", "azul", "verde", "rojo"))