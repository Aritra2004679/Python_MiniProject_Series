import string

def remove_matching_letter(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)

                l = l1 + ['*'] + l2
                return [l, True]

    l = l1 + ['*'] + l2
    return [l, False]


print("=" * 40)
print(" FLAMES Relationship Calculator ")
print("=" * 40)

p1 = input("Enter First Person Name : ")
p1 = p1.lower().replace(" ", "")

p2 = input("Enter Second Person Name : ")
p2 = p2.lower().replace(" ", "")

l1 = list(p1)
l2 = list(p2)

proceed = True

while proceed:
    ret_list = remove_matching_letter(l1, l2)

    con_list = ret_list[0]
    proceed = ret_list[1]

    star_index = con_list.index('*')

    l1 = con_list[:star_index]
    l2 = con_list[star_index + 1:]

count = len(l1) + len(l2)

print("\nRemaining Letter Count :", count)

flames = ["Friends", "Love", "Affection",
          "Marriage", "Enemy", "Sibling"]

while len(flames) > 1:

    split_index = (count % len(flames)) - 1

    if split_index >= 0:

        right = flames[split_index + 1:]
        left = flames[:split_index]

        flames = right + left

    else:

        flames = flames[:len(flames) - 1]

print("\n FLAMES Result ")
print("Relationship Status :", flames[0])
