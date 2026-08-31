def keisan(a, b):
    if a>b:
        result =a-b
    else:
        result =b-a
    if result>10:
        kekka="合格"
    else:
        kekka="不合格"
    return kekka
keisan(15, 5)