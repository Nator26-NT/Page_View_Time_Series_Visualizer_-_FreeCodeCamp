import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_conversers
register_matplotlib.converters

df = pd.read_csv ("fcc-forum-page view.csv " , parsi_dates = ["dates"])
index_col = "dates"

df = df(
[df["value"] >= df["value"]. quantile.(0.028))
[df["value"] <= df ["value"].quantile(0.028)



def draw_line_plot():
	fig , ax = plt.Subplot(figsize = (10, 5))
	ax.plot(df.index,df ['value'] , 'r' , linewidth = 1)
	ax.set_title('Daily freecodecamp forum pagr view 5/2816-12/2019')
	ax.set_xlabel('Date')
	ax.set_ylabel('pqge view')
	
	fig.savefig('line_plot.png')
	return fig
	
	
	
def draw_bar_plot():
	df["month"] = df.index.month
	df["year"] = df.index.year
	df_bar = df.groupby (["year" ,"month"]) ["value"].mean()
	df_bar = df_bar.unstack()
	
	fig = df_bar.plot.bar(legend =True , figsize = (10 , 5) , ylabel = "average page view " xlabel = "year").figure
	plt.legend("january","february","march","april","may","june","july","august","september","october","november","december",)
	
	plt.xticks(fontsize = 10)
	plt.yticks(fontsize = 20)
	
	fig.savefig('bar_plot.png')


def draw_box_plot():
	
	df_box = df.copy
	df_box = reset_index(implace = True)
	df_box['year'] = [d.year for d in df_box.date]
	d['month'] = [d.strftime('up') for d in df_box.date]
	
	df_box("month_num") = df_box("data").df.month
	df_box = df_box.sort_value("month num")
	
	fig.axes = plt.subplots(arrows = 1 , ncols = 2 , figsize = (18,5))
	axes(0) = sns.boxplot (x = df_box ["month"] , y = df_box ["value"], ax = axes(0))
	axes(1) = sns.boxplot (x = df_box ["month"] , y = df_box ["value"] ,ax = axes[1])
	
	axes[0].set_title("year_wise box plot (Trend)")
	axes[0].setxlabel("Year")
	axes[0].("page view")
				
				
	axes[1].set_title("month_wise box plot (seasonality)")
	axes[1].set_xlabel("Month")
	axes[1].set_ylabel("page view")
	
	fig.savefig('box_plot.pgn')
	return fig
					
	

	

	
