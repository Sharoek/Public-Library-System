class helper:
    @staticmethod

    def checknumbers(min, max, txt="Please input your choice:\n"):
        running = True
        while running:
            get_input = input(txt)
            if get_input.isdigit() == False:
                get_input = input("No letters allowed, please input a number:\n")
            if get_input.isdigit() and int(get_input) <= max and int(get_input) >= min:
                running = False
                return get_input
