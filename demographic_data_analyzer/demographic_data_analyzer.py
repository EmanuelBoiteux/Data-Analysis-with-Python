import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    total = len(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    cant_bachelors = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = round(cant_bachelors / total * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    total_higher_education = higher_education.shape[0]
    cant_higher_education_salary = higher_education[higher_education['salary'] == '>50K'].shape[0]
    higher_education_rich = round(cant_higher_education_salary / total_higher_education * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    total_lower_education = lower_education.shape[0]
    cant_lower_education_salary = lower_education[lower_education['salary'] == '>50K'].shape[0]
    lower_education_rich = round(cant_lower_education_salary / total_lower_education * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_50 = ((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')).sum()
    total_min_hours = (df['hours-per-week'] == min_work_hours).sum()
    rich_percentage = round(min_hours_50 / total_min_hours * 100, 1)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_totals = df['native-country'].value_counts()
    high_earners_count = df[df['salary'] == '>50K'].groupby('native-country').size()
    percentage_high_earners = round((high_earners_count / country_totals) * 100, 1)
    highest_earning_country = percentage_high_earners.idxmax()
    highest_earning_country_percentage = percentage_high_earners.max()
    

    # Identify the most popular occupation for those who earn >50K in India.
    df_india_high_earners = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = df_india_high_earners['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
