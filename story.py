print(
'''
you woke up in a dark forest, and birds are chirping around you
with a hint of sunlight coming through the trees. You get up
and walk around, and you see a little cottage in the distance.
'''
)
def main():
    cottage = input("do you want to go inside the cottage? (yes or no)")
    answer(cottage)
def answer():
    if cottage == "yes":
        print("okay let's go inside, and see whos there")
    else:
        print(
        '''
        are you sure? you'll be stuck outside in the dark forest..
        oh wait.. you see a crow on the rock near by and its trying to talk to you
        '''
        )

if __name__ == "__main__":
    main()
