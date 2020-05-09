from initialAccess import AccessData
from GoogleAccess import gmain


def main():
    obj = AccessData()
    brk_cnd = 1

    # while brk_cnd == 1:
    input_text = obj.getdata()
    indexval = obj.processdata(input_text)
    print(indexval)
    print(input_text)
    if indexval < 5:
        gmain(input_text)
    elif indexval == 5:
        print("PLAY")
    else:
        print("OPEN")


if __name__ == '__main__':
    main()
