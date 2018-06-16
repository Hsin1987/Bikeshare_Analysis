import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = {
        '1': 'chicago',
        '2': 'new york city',
        '3': 'washington',
    }
    city_msg = """
    1: Chicago
    2: New YorK
    3: Washington
    """
    print('Choose a city by keying in the number (1~3): ')
    print(city_msg)
    key = str(input())
    while key not in cities.keys():
        print("Please choose the city by keying in  1, 2, or 3.")
        key = str(input())

    city = cities[key]

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
    month_msg = """
        0: All,
        1: January
        2: February,
        3: March,
        4: April,
        5: May,
        6: June,
        """
    print('Chose a the month for analysis by keying in the number (0~6): ')
    print(month_msg)
    key = str(input())
    while key not in months.keys():
        print("Please choose the month by keying in the number (0~6).")
        key = str(input())

    month = months[key].lower()
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
    weekdays_msg = """
        0: All,
        1: Monday
        2: Tuesday,
        3: Wednesday,
        4: Thursday,
        5: Friday,
        6: Saturday,
        7: Sunday
        """
    print('Chose a the weekdays for analysis by keying in the number (0~7): ')
    print(weekdays_msg)
    key = str(input())
    while key not in weekdays.keys():
        print("Please choose the weekdays for analysis by keying in the number (0~7).")
        key = str(input())

    day = weekdays[key]


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
    print("Earliest birth year: ", int(df["Birth Year"].min()))
    print("Most recent birth year: ", int(df["Birth Year"].max()))
    print("Most common year: ", int(df["Birth Year"].value_counts().index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        #df = load_data("chicago", "january", "all")
        time_stats(df)
        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
