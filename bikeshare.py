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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("Which city you want to explore?,chicago,new york city or washington:")
        city=city.lower()
        if city in['chicago','new york city','washington']:
            break
        else:
            print("City u entered in the invalid city")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("if you want deatils of specfic month then type month name from first six months or  else type 'all':")
        month=month.lower()
        if month in['january','febuary','march','april','may','june','all']:
            break
        else:
            print("Invaild input.please put the right month")
               

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("if you want details of specfic days then please enter the any day from a week or else type 'all':")
        day=day.lower()
        if day in['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            break
        else:
            print("invaild input. please put the right day")

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
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.index(month)+1
    
        # filter by month to create the new dataframe
        df =df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    print("The most commom month",df['month'].mode()[0])

    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday_name
    print('The most common day of week is',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print("The most commom hour",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is ',df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df["Combination"]=df['Start Station']+" " +df['End Station']
    print("The most frequent combination of start station and end station trip is :",df['Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total time travel is:",df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('The mean travel time is:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print(user_type)

    # TO DO: Display counts of gender
  #  if user_type in df['new york city','chicago']:
    try:
        gender_type=df['Gender'].value_counts()
        print(gender_type)
        
    except:
        print("ONly chicago and new york city data for gender in avaiable")
    # TO DO: Display earliest, most recent, and most common year of birth
  #  if city != 'washington':
    try:
        min_year_birth=min(df['Birth Year'])
        print("The earliest year of birth is",int(min_year_birth))
        max_year_birth=max(df['Birth Year'])
        print("The most recent year of birth is",max_year_birth)
        common_year=df['Birth Year'].mode()[0]
        print(common_year)
    except:
        print("Only aviable for the new york city and chicago cities")
                                 
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data=input("Would u like to view 5 individual trip data? Enter yes or no ")
    start_loc=0
    while True:
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display.lower()!= "yes":
            break
                             

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
