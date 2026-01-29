import pandas as pd

# Dictionary to map city names to CSV files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# Constants for input validation
VALID_CITIES = ['chicago', 'new york city', 'washington']
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters() -> tuple[str, str, str]:
    """
    Ask the user to specify a city, month, and day to analyze.

    Returns:
        tuple: (city, month, day) filtered by user input
    """
    # Placeholder defaults
    city = 'chicago'
    month = 'all'
    day = 'all'

    # Example validation can be added later
    # while city not in VALID_CITIES:
    #     city = input(f"Enter a city ({', '.join(VALID_CITIES)}): ").lower()

    return city, month, day


def load_data(city: str, month: str, day: str) -> pd.DataFrame:
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        city (str): City to analyze
        month (str): Month to filter by, or "all" for no filter
        day (str): Day of the week to filter by, or "all" for no filter

    Returns:
        pd.DataFrame: Filtered city data
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != 'all':
        month_index = VALID_MONTHS.index(month) + 1
        df = df[df['month'] == month_index]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df


def most_common_stat(df: pd.DataFrame, column: str) -> str:
    """
    Returns the most common value in a DataFrame column.

    Args:
        df (pd.DataFrame): DataFrame to analyze
        column (str): Column name

    Returns:
        str: Most common value
    """
    if column in df:
        return df[column].mode()[0]
    return "N/A"


def time_stats(df: pd.DataFrame):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df (pd.DataFrame): DataFrame containing city bikeshare data
    """
    # Most common month
    print("Most common month:", most_common_stat(df, 'month'))

    # Most common day of the week
    print("Most common day of week:", most_common_stat(df, 'day_of_week'))

    # Most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common start hour:", most_common_stat(df, 'hour'))


def station_stats(df: pd.DataFrame):
    """
    Displays statistics on the most popular stations and trips.

    Args:
        df (pd.DataFrame): DataFrame containing city bikeshare data
    """
    print("Most commonly used start station:", most_common_stat(df, 'Start Station'))
    print("Most commonly used end station:", most_common_stat(df, 'End Station'))

    if 'Start Station' in df and 'End Station' in df:
        df['trip'] = df['Start Station'] + " -> " + df['End Station']
        print("Most frequent combination of stations:", most_common_stat(df, 'trip'))


def trip_duration_stats(df: pd.DataFrame):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df (pd.DataFrame): DataFrame containing city bikeshare data
    """
    if 'Trip Duration' in df:
        print("Total travel time:", df['Trip Duration'].sum())
        print("Mean travel time:", df['Trip Duration'].mean())


def user_stats(df: pd.DataFrame):
    """
    Displays statistics on bikeshare users.

    Args:
        df (pd.DataFrame): DataFrame containing city bikeshare data
    """
    if 'User Type' in df:
        print("User type counts:\n", df['User Type'].value_counts())

    if 'Gender' in df:
        print("Gender counts:\n", df['Gender'].value_counts())

    if 'Birth Year' in df:
        print("Earliest birth year:", int(df['Birth Year'].min()))
        print("Most recent birth year:", int(df['Birth Year'].max()))
        print("Most common birth year:", int(most_common_stat(df, 'Birth Year')))


def main():
    """
    Main function to run the Bikeshare data exploration script.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
<<<<<<< HEAD
import pandas as pd

# Dictionary to map city names to CSV files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        city (str): Name of the city to analyze
        month (str): Name of the month to filter by, or "all" for no filter
        day (str): Name of the day of the week to filter by, or "all" for no filter
    """
    # Prompt user for city input
    # Convert input to lowercase to standardize
    ...

    # Prompt user for month input
    # Convert input to lowercase to standardize
    ...

    # Prompt user for day input
    # Convert input to lowercase to standardize
    ...

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        city (str): City to analyze
        month (str): Month to filter by, or "all" to apply no month filter
        day (str): Day of the week to filter by, or "all" to apply no day filter

    Returns:
        df (DataFrame): Pandas DataFrame containing city data filtered by month and day
    """
    # Load CSV file into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time'
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        ...

    # Filter by day if applicable
    if day != 'all':
        ...

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df (DataFrame): DataFrame containing city bikeshare data
    """
    # Display most common month
    ...

    # Display most common day of the week
    ...

    # Display most common start hour
    ...

def station_stats(df):
    """
    Displays statistics on the most popular stations and trips.

    Args:
        df (DataFrame): DataFrame containing city bikeshare data
    """
    # Display most commonly used start station
    ...

    # Display most commonly used end station
    ...

    # Display most frequent combination of start station and end station
    ...

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df (DataFrame): DataFrame containing city bikeshare data
    """
    # Calculate total travel time
    ...

    # Calculate mean travel time
    ...

def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        df (DataFrame): DataFrame containing city bikeshare data
    """
    # Display counts of user types
    ...

    # Display counts of gender (if available)
    ...

    # Display earliest, most recent, and most common year of birth (if available)
    ...

def main():
    """
    Main function to run the Bikeshare data exploration script.
    Handles user input and calls other functions in order.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
=======
VALID_CITIES = ['chicago', 'new york city', 'washington']
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
def get_filters() -> tuple[str, str, str]:
    city = 'chicago'
    month = 'all'
    day = 'all'
    return city, month, day
def most_common_stat(df: pd.DataFrame, column: str) -> str:
    if column in df:
        return df[column].mode()[0]
    return "N/A"

>>>>>>> refactoring
