import pandas as pd
import matplotlib.pyplot as plt
import extcolors
from colormap import rgb2hex


class colorDisplay():
    def __init__(self,filePath,tolerance,limit):
        self.colors = extcolors.extract_from_path(filePath, tolerance, limit)
        self.filePath = filePath


    def color_to_df(self,input):
        # Gets the rgb color and the percentage of occurrence for each color within the image
        colors_pre_list = str(input).replace('([(', '').split(', (')[0:-1]
        # Seperates the rgb colors into a list
        df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
        # Seperates the percentages into a list
        df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]
        # convert RGB to HEX code
        df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                               int(i.split(", ")[1]),
                               int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]
        #Returns a DataFrame of the Hex codes [c_code} and the percentage occurrence [occurence]
        df = pd.DataFrame(zip(df_color_up, df_percent), columns=['c_code', 'occurence'])
        return df


    def plot(self):
        df_color = self.color_to_df(self.colors)
        #Gets the color list and percentage list out of the DataFrame
        list_color = list(df_color['c_code'])
        list_percent = [int(i) for i in list(df_color['occurence'])]
        #Converts the integer number into a percentage out of 100 and places it in the list
        text_c = [c + ' ' + str(round(p * 100 / sum(list_percent), 1)) + '%' for c, p in zip(list_color,list_percent)]
        #Creates the pie chart to display (matplotlib)
        fig, ax = plt.subplots(figsize=(50, 50), dpi=10)
        wedges, text = ax.pie(list_percent,
                              labels=text_c,
                              labeldistance=1.05,
                              colors=list_color,
                              textprops={'fontsize': 120, 'color': 'black'}
                              )
        plt.setp(wedges, width=0.3)

        # create space in the center
        plt.setp(wedges, width=0.36)

        ax.set_aspect("equal")
        fig.set_facecolor('white')
        plt.show()


"""
        # color palette
        x_posi, y_posi, y_posi2 = 160, -170, -170
        for c in list_color:
            if list_color.index(c) <= 5:
                y_posi += 180
                rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor=c)
                ax2.add_patch(rect)
                ax2.text(x=x_posi + 400, y=y_posi + 100, s=c, fontdict={'fontsize': 190})
            else:
                y_posi2 += 180
                rect = patches.Rectangle((x_posi + 1000, y_posi2), 360, 160, facecolor=c)
                ax2.add_artist(rect)
                ax2.text(x=x_posi + 1400, y=y_posi2 + 100, s=c, fontdict={'fontsize': 190})

        ax2.axis('off')
        fig.set_facecolor('white')
        plt.imshow(bg)
        plt.tight_layout()
"""