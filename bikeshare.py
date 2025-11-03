import pandas as pd

# بيانات الملفات حسب المدينة
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# قوائم ثابتة
CITIES = ["chicago", "new york city", "washington"]
MONTHS = ["january", "february", "march", "april", "may", "june", "all"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_user_choice(prompt, valid_options):
    """
    تطلب من المستخدم اختيار قيمة من قائمة الخيارات المتاحة.
    
    Parameters:
        prompt (str): الرسالة التي تظهر للمستخدم.
        valid_options (list): قائمة القيم المسموح بها.
        
    Returns:
        str: الخيار الذي اختاره المستخدم (بحروف صغيرة).
    """
    valid_options = [option.lower() for option in valid_options]
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        print("Invalid input. Please enter a valid option.")

def get_city():
    """
    تطلب من المستخدم اختيار مدينة من قائمة المدن المتاحة.
    
    Returns:
        str: اسم المدينة كـ string بالحروف الصغيرة.
    """
    return get_user_choice("Choose a city (Chicago, New York City, Washington): ", CITIES)

def get_month():
    """
    تطلب من المستخدم اختيار الشهر أو 'all' لجميع الأشهر.
    
    Returns:
        str: اسم الشهر أو 'all'.
    """
    return get_user_choice("Choose a month (January to June) or 'all' for no filter: ", MONTHS)

def get_day():
    """
    تطلب من المستخدم اختيار يوم الأسبوع أو 'all' لجميع الأيام.
    
    Returns:
        str: اسم اليوم أو 'all'.
    """
    return get_user_choice("Choose a day of the week or 'all' for no filter: ", DAYS)

def load_data(city, month='all', day='all'):
    """
    تحميل بيانات المدينة المختارة وتطبيق الفلاتر حسب الشهر واليوم.
    
    Parameters:
        city (str): اسم المدينة.
        month (str): اسم الشهر أو 'all' لجميع الأشهر.
        day (str): اسم اليوم أو 'all' لجميع الأيام.
        
    Returns:
        DataFrame: بيانات مفلترة أو None إذا لم يوجد ملف.
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"Error: File for {city} not found.")
        return None

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    """
    حساب وعرض أكثر الأوقات شيوعًا لبدء الرحلات.
    """
    print("\n=== Most Frequent Times of Travel ===")
    if df.empty:
        print("No data available.")
        return
    month_names = MONTHS[:-1]  # حذف 'all'
    common_month = df['month'].mode()[0]
    print("Most common month:", month_names[common_month - 1].title())
    common_day = df['day_of_week'].mode()[0]
    print("Most common day of week:", common_day)
    common_hour = df['hour'].mode()[0]
    print("Most common start hour:", common_hour)

def station_stats(df):
    """
    حساب وعرض أكثر المحطات استخدامًا والرحلات الشائعة.
    """
    print("\n=== Most Popular Stations and Trip ===")
    if df.empty:
        print("No data available.")
        return
    print("Most common start station:", df['Start Station'].mode()[0])
    print("Most common end station:", df['End Station'].mode()[0])
    df['trip'] = df['Start Station'] + " -> " + df['End Station']
    print("Most common trip:", df['trip'].mode()[0])

def trip_duration_stats(df):
    """
    حساب وعرض مدة الرحلات الإجمالية والمتوسط.
    """
    print("\n=== Trip Duration ===")
    if df.empty:
        print("No data available.")
        return
    total_time = df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()
    print(f"Total travel time (hours): {total_time / 3600:.2f}")
    print(f"Mean travel time (minutes): {mean_time / 60:.2f}")

def user_stats(df, city):
    """
    عرض إحصائيات عن مستخدمي الدراجة (النوع، الجنس، سنة الميلاد إذا متاحة).
    
    Parameters:
        df (DataFrame): بيانات الرحلات.
        city (str): اسم المدينة.
    """
    print("\n=== User Info ===")
    if df.empty:
        print("No data available.")
        return
    print("\nCounts of user types:\n", df['User Type'].value_counts())
    if 'Gender' in df.columns:
        print("\nCounts of gender:\n", df['Gender'].value_counts(dropna=True))
    else:
        print("\nNo gender data available for", city.title())
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year'].dropna()
        if not birth_year.empty:
            print("\nEarliest year of birth:", int(birth_year.min()))
            print("Most recent year of birth:", int(birth_year.max()))
            print("Most common year of birth:", int(birth_year.mode()[0]))
        else:
            print("No valid birth year data available.")
    else:
        print("No birth year data available for", city.title())

def display_raw_data(df):
    """
    عرض 5 صفوف من البيانات الخام عند الطلب.
    """
    i = 0
    while True:
        show_data = input("\nDo you want to see 5 rows of raw data? (yes/no): ").lower()
        if show_data != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print("No more data to display.")
            break

def main():
    """
    الدالة الرئيسية لتشغيل البرنامج. 
    تقوم بتكرار جميع الخطوات إذا أراد المستخدم إعادة التشغيل.
    """
    print("Hello! Let's explore US bikeshare data!")
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)
        if df is None:
            continue  # إذا لم يوجد الملف، نطلب اختيار مدينة أخرى
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        
        restart = input("\nDo you want to restart? Enter yes or no: ").lower()
        if restart != 'yes':
            print("\nThank you for exploring bikeshare data!")
            break

if __name__ == "__main__":
    main()
