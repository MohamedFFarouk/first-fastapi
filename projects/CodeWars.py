def sort_twisted37(arr):
    def twist_number(n):
        return int(str(n).replace("3", "x").replace("7", "3").replace("x", "7"))

    return sorted(arr, key=twist_number)
