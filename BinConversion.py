def dec_bin(a_num):
    if a_num <= 1:
        print(int(a_num))
        return
    else:
        bin_num = int(a_num % 2)
        a_num = a_num/2
        print(bin_num)
        dec_bin(a_num)

if __name__ == "__main__":
    dec_bin(255)
        