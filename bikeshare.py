import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Enter city name: ')
    city = str.lower(city)
    
    while (city!='chicago') and (city!='new york city') and (city!='washington'):
        print('Value entered is not valid')
        city = input('Enter city name: ')
        


    # get user input for month (all, january, february, ... , june)
    months = ['All','January', 'February', 'March', 'April', 'May', 'June']
    month = input('Enter specific month or all :')
    month = str.lower(month)
    month = str.capitalize(month)
    
    while month not in months:
        print('Value entered is not valid')
        month = input('Enter specific month or all ')
        
        month = str.capitalize(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = input('Enter specific day or all :')
    day = str.lower(day)
    day = str.capitalize(day)
    
    while day not in days:
        print('Value entered is not valid')
        day = input('Enter specific day or all ')


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
    if (city == 'chicago'):
        df = pd.read_csv("chicago.csv")
    elif (city == 'new york city'):
        df = pd.read_csv("new_york_city.csv")
    else:
        df = pd.read_csv("washington.csv")
        
        
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 5
    display_data = 'no'
    while (view_data == 'yes' and display_data == 'no'):
        print(df.iloc[:start_loc])
        start_loc += 5
        display_data = input("Do you wish to continue?(no if you want more data): ").lower()


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df = pd.DataFrame(df)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month_name()
    print('\nMost Common Month with time of ouccurence: ')
    print(df['month'].value_counts().head(1))
    

    # display the most common day of week
    df['day_name'] = pd.DatetimeIndex(df['Start Time']).day_name()
    print('\nMost Common day with time of ouccurence: ')
    print(df['day_name'].value_counts().head(1))

    # display the most common start hour
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    print('\nMost Common hour with time of ouccurence: ')
    print(df['hour'].value_counts().head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station

    print('\nMost Common start station with how many times used: ')
    print(df['Start Station'].value_counts().head(1))    
    

    # display most commonly used end station

    print('\nMost Common End station with how many times used: ')
    print(df['End Station'].value_counts().head(1))    
    
    # display most frequent combination of start station and end station trip
    print('\nMost Common combination of start station and end stationno with how many times used: ')
    print((df['End Station']+ ' and ' + df['End Station']).value_counts().head(1))  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal Time of Travel(in min): ')
    print(df['Trip Duration'].sum()/60)

    # display mean travel time
    print('\nMean Time of Travel(in min): ')
    print(df['Trip Duration'].mean()/60)     
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\n Count Of User Type: ')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if (city == 'washington'):
        print('\nSorry data for gender is not avaliable')
        print('\nSorry data for date of birth is not avaliable')
    else:
        print('\n Count Of Gender: ')
        print(df['Gender'].value_counts())
    

    # Display earliest, most recent, and most common year of birth
         
        print('\n Earliest year of birth: ')
        print(df['Birth Year'].min())
    
        print('\n Recent year of birth: ')
        print(df['Birth Year'].max())
    
        print('\n most common year of birth: ')
        print(df['Birth Year'].value_counts().head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
