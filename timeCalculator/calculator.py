

time = {}

while True:
    def main():
        def ask_hours():
            response_hours = input("How many hours?")
            time['hours'] = float(response_hours)
        ask_hours()

        def ask_minutes():
            response_minutes = input("And how many minutes?")
            time['minutes'] = float(response_minutes)
        ask_minutes()

        def ask_speed():
            response_speed = input("At which speed are you watching the course? Please respond in decimal format, (example: 0.6 or 1.4)")
            time['speed'] = float(response_speed)
        ask_speed()

        import math
        def time_calulator(time):
            
            speed = time.get('speed')
            
            hours = time.get('hours')
            
            minutes = time.get('minutes')
            
            total_minutes = (hours * 60) + minutes

            find_change_of_time = total_minutes / speed

            new_hours = find_change_of_time / 60

            new_minutes = math.modf(new_hours)[0] * 60

            new_seconds = int(math.modf(new_minutes)[0] * 60)

            print("Your new runtime is " + str(math.modf(new_hours)[1]) + " hours, "
            + str(math.modf(new_minutes)[1]) + " minutes, and " + str(new_seconds) + " seconds.")

        time_calulator(time)

    main()