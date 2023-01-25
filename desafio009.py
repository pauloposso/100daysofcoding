def rainwater_traper(heights):
    base = 0
    water = 0
    for height in heights:
        if height > base:
            base = height
        elif height <= base:
            water += base - height

    print(water)


def main():
   heights1 = [0, 4, 2, 0, 1, 4, 3, 4]
   heights2 = [1, 0, 1, 0, 1, 0, 1]
   heights3 = [1, 0, 10, 0, 5, 0, 11]
   rainwater_traper(heights1)
   rainwater_traper(heights2)
   rainwater_traper(heights3)

if __name__ == '__main__':
    main()