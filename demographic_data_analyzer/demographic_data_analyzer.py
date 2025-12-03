import pandas as pd

def demographic_data_analyzer(print_info = True):

    df = pd.read_csv("adult.data.csv")
    total = len(df)

    # How many people of each race are represented in this dataset?
    cant_race = df['race'].value_counts()

    # What is the average age of men?
    avg_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    cant_bachelors = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = round(cant_bachelors / total * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    total_advanced_education = advanced_education.shape[0]
    cant_advanced_education_salary = advanced_education[advanced_education['salary'] == '>50K'].shape[0]
    percentage_advanced_education = round(cant_advanced_education_salary / total_advanced_education * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    no_advanced_education = df[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    total_no_advanced_education = no_advanced_education.shape[0]
    cant_no_advanced_education_salary = no_advanced_education[no_advanced_education['salary'] == '>50K'].shape[0]
    percentage_no_advanced_education = round(cant_no_advanced_education_salary / total_no_advanced_education * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_50 = ((df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')).sum()
    total_min_hours = (df['hours-per-week'] == min_hours).sum()
    min_hour_50_per = round(min_hours_50 / total_min_hours * 100, 1)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_totals = df['native-country'].value_counts()
    high_earners_count = df[df['salary'] == '>50K'].groupby('native-country').size()
    percentage_high_earners = round((high_earners_count / country_totals) * 100, 1)
    highest_percentage = percentage_high_earners.max()
    country_with_highest_percentage = percentage_high_earners.idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    df_india_high_earners = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    most_popular_occupation = df_india_high_earners['occupation'].value_counts().index[0]

    if print_info:
        print("Number of each race:\n", cant_race) 
        print("Average age of men:", avg_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_advanced_education}%")
        print(f"Percentage without higher education that earn >50K: {percentage_no_advanced_education}%")
        print(f"Min work time: {min_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {min_hour_50_per}%")
        print("Country with highest percentage of rich:", country_with_highest_percentage)
        print(f"Highest percentage of rich people in country: {highest_percentage}%")
        print("Top occupations in India:", most_popular_occupation)

    return {
        'race_count': cant_race,
        'average_age_men': avg_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': percentage_advanced_education,
        'lower_education_rich': percentage_no_advanced_education,
        'min_work_hours': min_hours,
        'rich_percentage': min_hour_50_per,
        'highest_earning_country': country_with_highest_percentage,
        'highest_earning_country_percentage': highest_percentage,
        'top_IN_occupation': most_popular_occupation
    }
