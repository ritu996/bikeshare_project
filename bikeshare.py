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
