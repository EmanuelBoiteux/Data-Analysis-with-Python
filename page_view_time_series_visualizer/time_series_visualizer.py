import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

df = df[(df['value'] > lower_bound) & (df['value'] < upper_bound)]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(16, 5))
    plt.plot(df,color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped.reindex(columns=month_order)
    
    ax = df_grouped.plot(kind='bar', figsize=(15, 13))
    ax.set_xlabel('Years', fontsize=25)
    ax.set_ylabel('Average Page Views', fontsize=25)
    ax.tick_params(axis='x', labelsize=20, rotation=90)
    ax.tick_params(axis='y', labelsize=20)

    legend = ax.legend(
        title='Months',
        fontsize=20,
        title_fontsize=20,
        loc='upper left',
        shadow=True
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.5)

    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]


    fig, axes = plt.subplots(1, 2, figsize=(28.8, 10.8))

    y_ticks = range(0, 220000, 20000)

    sns.boxplot(
        x='year', 
        y='value', 
        data=df_box, 
        ax=axes[0],
        hue='year',
        legend=False,
        palette='tab10'
    )
    
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize=25)
    axes[0].set_xlabel("Year", fontsize=20)
    axes[0].set_ylabel("Page Views", fontsize=20)
    axes[0].tick_params(axis='both', labelsize=20)
    axes[0].set_yticks(y_ticks)
    
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    sns.boxplot(
        x='month', 
        y='value', 
        data=df_box, 
        order=month_order, 
        ax=axes[1],
        hue='month',
        legend=False,
        palette='husl'
    )
    
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize=25)
    axes[1].set_xlabel("Month", fontsize=20)
    axes[1].set_ylabel("Page Views", fontsize=20)
    axes[1].tick_params(axis='both', labelsize=20)
    axes[1].set_yticks(y_ticks)

    fig.tight_layout(pad=3.0)
    fig.subplots_adjust(wspace=0.15)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig