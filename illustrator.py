import matplotlib.pyplot as plt
import numpy as np
import util


def flights_per_months_freq(total_flights, flights):
    fig, ax = plt.subplots(figsize=(15, 7))
    months = ['Jan-2013', 'Feb-2013', 'Mar-2013',
              'Apr-2013', 'May-2013', 'Jun-2013',
              'Jul-2013', 'Aug-2013', 'Sep-2013',
              'Oct-2013', 'Nov-2013', 'Dec-2013']
    # set width of bar
    barWidth = 0.25
    # Set position of bar on X axis
    r1 = np.arange(len(months))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    ax.bar(r1, flights[0], label="EWR", color='b', width=barWidth)
    ax.bar(r2, flights[1], label="JFK", color='r', width=barWidth)
    ax.bar(r3, flights[2], label="LGA", color='g', width=barWidth)
    ax.legend()
    ax.set_xlabel('')
    ax.set_ylabel('Flights')
    the_table = ax.table(cellText=[total_flights],
                         colWidths=[0.2]*12,
                         colLabels=months,
                         loc='bottom')
    plt.subplots_adjust(left=0.2, bottom=0.2)
    ax.set_xticks([]) 
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(0.417, 1)
    fig.patch.set_visible(False)
    ax.axis('tight')
    return fig

def flights_per_months_total(flights):
    fig, ax = plt.subplots(figsize=(15, 7))
    months = ['Jan-2013', 'Feb-2013', 'Mar-2013',
              'Apr-2013', 'May-2013', 'Jun-2013',
              'Jul-2013', 'Aug-2013', 'Sep-2013',
              'Oct-2013', 'Nov-2013', 'Dec-2013']
    # set width of bar
    # Set position of bar on X axis
    r1 = np.arange(len(months))
    ax.bar(r1, flights)
    ax.set_ylabel('Flights')
    ax.set_xticks(r1)
    ax.set_xticklabels(months)
    fig.patch.set_visible(False)
    ax.axis('tight')
    return fig

def flights_per_months_stacked(total_flights, flights):
    fig, ax = plt.subplots(figsize=(15, 7))
    months = ['Jan-2013','Feb-2013','Mar-2013',
                   'Apr-2013','May-2013','Jun-2013',
                   'Jul-2013','Aug-2013','Sep-2013',
                   'Oct-2013','Nov-2013','Dec-2013']
    ax.bar(months, flights[0], label="JFK", color='b')
    ax.bar(months,flights[1], label="EWR", color='r', bottom= flights[0])
    ax.bar(months, flights[2], label="LGA", color='g', bottom=util.add_array( flights[0],flights[1]))
    ax.legend()
    ax.set_xlabel('')
    ax.set_ylabel('Flights')
    the_table = ax.table(cellText=[total_flights],
                         colWidths=[0.2]*12,
                         colLabels=months,
                         loc ='bottom') 
    plt.subplots_adjust(left = 0.2, bottom = 0.2) 
    ax.set_xticks([]) 
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(0.417, 1)
    fig.patch.set_visible(False)
    ax.axis('tight')
    return fig


def flights_per_months_percentage(total_flights, flights):
    sums = util.add_array(util.add_array(flights[0], flights[1]), flights[2])
    per_0 = util.div_array(flights[0],sums)
    per_1 = util.div_array(flights[1],sums)
    per_2 = util.div_array(flights[2],sums)
    fig, ax = plt.subplots(figsize=(15, 7))
    months = ['Jan-2013','Feb-2013','Mar-2013',
                   'Apr-2013','May-2013','Jun-2013',
                   'Jul-2013','Aug-2013','Sep-2013',
                   'Oct-2013','Nov-2013','Dec-2013']
    ax.bar(months,per_0, label="JFK", color='b')
    ax.bar(months,per_1, label="EWR", color='r', bottom= per_0)
    ax.bar(months, per_2, label="LGA", color='g', bottom=util.add_array(per_0,per_1))
    ax.legend()
    ax.set_xlabel('')
    ax.set_ylabel('Flights')
    the_table = ax.table(cellText=[total_flights],
                         colWidths=[0.2]*12,
                         colLabels=months,
                         loc ='bottom') 
    plt.subplots_adjust(left = 0.2, bottom = 0.2) 
    ax.set_xticks([]) 
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(0.417, 1)
    fig.patch.set_visible(False)
    ax.axis('tight')
    return fig

def top_10_table(dest, total_visits, flights, origins):
    fig, ax = plt.subplots(figsize=(15, 7))
    # set width of bar
    barWidth = 0.25
    # Set position of bar on X axis
    r1 = np.arange(len(dest))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    ax.bar(r1, flights[0], label="JFK", color='b', width=barWidth)
    ax.bar(r2, flights[1], label="EWR", color='r', width=barWidth)
    ax.bar(r3, flights[2], label="LGA", color='g', width=barWidth)
    ax.legend()
    ax.set_xticks(r1)
    ax.set_xticklabels(dest) 
    ax.set_ylabel('Flights')
    col_labels = dest
    table_vals = [dest]
    the_table = ax.table(cellText=[total_visits],
                         colWidths=[0.2]*10,
                         colLabels=dest,
                         rowLabels =["total "],
                         bbox=[-0.01, -0.2, 1, 0.11])
    plt.subplots_adjust(left = 0.2, bottom = 0.2)
    ax.title.set_text('Top 10 Destinations')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    the_table.scale(0.417, 1)
    fig.patch.set_visible(False)
    ax.axis('tight')
    return fig

def temperature_orig(dates_JFK, dates_EWR, dates_LGA, JFK_temps, EWR_temps, LGA_temps, mess_EWR, mess_JFK, mess_LGA):
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.scatter(dates_EWR, EWR_temps, color='b', marker='.', label="EWR")
    ax.scatter(dates_JFK, JFK_temps, color='r', marker='.', label="JFK")
    ax.scatter(dates_LGA, LGA_temps, color='g', marker='.', label="LGA")
    col_labels = ['origin', 'EWR', 'JFK', 'LGA']
    table_vals = [['samples', mess_EWR, mess_JFK, mess_LGA]]
    the_table = ax.table(cellText=table_vals,
                         colWidths=[0.2]*4,
                         colLabels=col_labels,
                         bbox=[0.757, 0.835, 0.24, 0.16])
    ax.title.set_text('Temperature measurements at EWR, JFK and LGA' +
                      ' over 2013\n' +
                      'with number of measurements at each origin')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1, 2)
    every_nth = 30
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    fig.patch.set_visible(False)
    ax.set_xlabel('Date')
    ax.set_ylabel('temperatue in Celsius')
    ax.legend(loc="upper left")
    ax.axis('tight')
    return fig

def all_JFK_temp(JFK_temps, dates_JFK):
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.scatter(dates_JFK, JFK_temps, color='r', marker='.', label="JFK")
    ax.title.set_text('All temperature measurements at JFK' +
                      ' over 2013')
    every_nth = 30
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    fig.patch.set_visible(False)
    ax.set_xlabel('Date')
    ax.set_ylabel('temperatue in Celsius')
    ax.legend(loc="upper left")
    ax.axis('tight')
    return fig

def daily_temps_JFK(JFK_temps, dates_JFK):
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.scatter(dates_JFK, JFK_temps, color='r', marker='.', label="JFK")
    ax.title.set_text('Daily Mean Measurements At JFK in' +
                      ' 2013')
    every_nth = 30
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    fig.patch.set_visible(False)
    ax.set_xlabel('Date')
    ax.set_ylabel('temperatue in Celsius')
    ax.legend(loc="upper left")
    ax.axis('tight')
    return fig

def daily_temps_plot(JFK_temps, EWR_temps, LGA_temps, days):
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.scatter(days, JFK_temps, color='r', marker='.', label='JKF')
    ax.scatter(days, EWR_temps, color='b', marker='.', label='EWR')
    ax.scatter(days, LGA_temps, color='g', marker='.', label='LGA')
    ax.title.set_text('Daily Mean Measurements in' +
                      ' 2013')
    every_nth = 30
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    fig.patch.set_visible(False)
    ax.set_xlabel('Date')
    ax.set_ylabel('temperatue in Celsius')
    ax.legend(loc="upper left")
    ax.axis('tight')
    return fig

def manufac_200(manufact, num_planes):
    fig, ax = plt.subplots(figsize=(15, 4))
    the_table = ax.table(cellText=[num_planes],
                         colWidths=[0.2]*len(manufact),
                         colLabels=manufact,
                         loc ='top') 
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(13)
    the_table.scale(1, 1.3)
    fig.patch.set_visible(False)
    ax.axis('off')
    return fig

def airbus_mod(models, no_of_models):
    data= [[]]
    for i in range(len(models)):
            data.append([models[i], no_of_models[i] ])
    data.remove(data[0])
    fig, ax = plt.subplots(figsize=(15, 4))
    the_table = ax.table(cellText = data,
                         colWidths=[0.2]*2,
                         loc ='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(13)
    the_table.scale(1, 1.3)
    fig.patch.set_visible(False)
    ax.axis('off')
    return fig


def table3(arr_delay, dep_delay):
    data= [[]]
    for i in range(len(arr_delay)):
            data.append([arr_delay[i], dep_delay[i] ])
    data.remove(data[0])
    fig, ax = plt.subplots(figsize=(15, 4))
    the_table = ax.table(cellText = data,
                         rowLabels = ["EWR", "JFK", "LGA"],
                         colLabels = ["Arrival", "Departure"],
                         colWidths=[0.2]*2,
                         loc ='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(13)
    the_table.scale(1, 1.3)
    fig.patch.set_visible(False)
    ax.axis('off')
    return fig