import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def input_mod(input_print, error_print, enterable_list):
    print(input_print)
    ret = str(input())
    while ret not in enterable_list:
        print(error_print)
        ret = str(input())
    return ret


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Stage 1:
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = {
        '1': 'chicago',
        '2': 'new york city',
        '3': 'washington'}

    city_msg = ''
    for k, v in sorted(cities.items()):
        city_msg += '{}: {}\n'.format(k, v)

    input_print = 'Choose a city by keying in the number (1~3): \n' + city_msg
    error_print = 'Please choose the city by keying in  1, 2, or 3.'
    enterable_list = cities.keys()

    city = cities[input_mod(input_print, error_print, enterable_list)]

    # Stage 2:
    # get user input for month (all, january, february, ... , june)
    months = {
        '0': "All",
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June'
    }

    month_msg = ''
    for k, v in sorted(months.items()):
        month_msg += '{}: {}\n'.format(k, v)

    input_print = 'Chose a the month for analysis by keying in the number (0~6): \n' + month_msg
    error_print = 'Please choose the month by keying in the number (0~6).'
    enterable_list = months.keys()
    month = months[input_mod(input_print, error_print, enterable_list)].lower()

    # Stage 3:
    # get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays = {
        '0': "All",
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Saturday',
        '7': 'Sunday'
    }

    weekdays_msg = ''
    for k, v in sorted(weekdays.items()):
        weekdays_msg += "{}: {}\n".format(k, v)

    input_print = 'Chose a the weekdays for analysis by keying in the number (0~7): \n' + weekdays_msg
    error_print = 'Please choose the weekdays for analysis by keying in the number (0~7).'
    enterable_list = weekdays.keys()
    day = weekdays[input_mod(input_print, error_print, enterable_list)]

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    popular_weekday = df['day_of_week'].mode()[0]
    print('Most Popular Weekday:', popular_weekday)

    # display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
    print('Most Popular Weekday:', popular_weekday)

    # 3.display the most common start hour:
    # 3-1 convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # 3-2 extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # 3-3 find the most popular hour.
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", pop_start_station)
    # display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", pop_end_station)
    # display most frequent combination of start station and end station trip
    df['route'] = df["Start Station"] + " to " + df["End Station"]
    popular_route = df['route'].mode()[0]
    print("The most popular route: From ", popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time: ", "%.2f" % (df["Trip Duration"].sum()/3600), " hours.")

    # display mean travel time
    print("Mean travel time: ", "%.2f" % (df["Trip Duration"].mean()/60), " minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("# Display counts of user types: ")
    print(df["User Type"].value_counts())

    # Display counts of gender
    print("# Display counts of Gender: ")
    print(df["Gender"].value_counts())

    # Display earliest, most recent, and most common year of birth
    try:
        print("Earliest birth year: ", int(df["Birth Year"].min()))
        print("Most recent birth year: ", int(df["Birth Year"].max()))
        print("Most common year: ", int(df["Birth Year"].value_counts().index[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print("The raw data does not include user's birth year.")

    print('-'*40)

def raw_data_display(df):
    choose = {
        '1': True,
        "2": False
    }
    input_print = '\nWant see raw data? \n Type 1 for "yes". \n Type 2 for "no". \n '
    error_print = 'Please type 1 for "yes" or 2 for "no" '
    enterable_list = choose.keys()
    display_raw_data = choose[input_mod(input_print, error_print, enterable_list)]
    counter = 0
    while display_raw_data:
        print("Data from No.{} to No.{}: ".format(counter+1, counter+10))

        with pd.option_context('display.max_rows', None, 'display.max_columns', 1000):
            print(df.iloc[counter: counter+10])
        counter += 11
        input_print = '\nWant see raw more data? \n 6 Type 1 for "yes". \n Type 2 for "no". \n'
        display_raw_data = choose[input_mod(input_print, error_print, enterable_list)]
    return


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)
        raw_data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
