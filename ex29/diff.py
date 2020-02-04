def diff(file_A, file_B):

    with open(file_A) as a, open(file_B) as b, open("output.txt", "a") as ab:
        # print(a.readlines())
        # print(b.readlines())

        lines_A = [line for line in a.readlines()]
        lines_B = [line for line in b.readlines()]

        len_A = len(lines_A)
        len_B = len(lines_B)

        pa = pb = i = 0

        while pa < len_A + 1 and pb < len_B:
            print(f">>> pa is {pa}.")
            print(f"<<< pb is {pb}.")
            if pa == len_A:
                print(f"[ADD]: {lines_B[pb]}")
                ab.write(f"[+]: {lines_B[pb]}")
                i += 1
                pa = pb = i
            elif lines_A[pa] == lines_B[pb]:
                i += 1
                pa = pb = i
            else:
                pa += 1

        while pb < len_B + 1 and pa < len_A:
            print(f">>> pa is {pa}.")
            print(f"<<< pb is {pb}.")
            if pb == len_B:
                ab.write(f"[-]: {lines_A[pa]}")
                i += 1
                pa = pb = i
            elif lines_B[pb] == lines_A[pa]:
                i += 1
                pa = pb = i
            else:
                pb += 1