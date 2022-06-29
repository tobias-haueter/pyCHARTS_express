import plotly.express as px
import pandas as pd
from art import *
import os
import glob
import sys
import time

# https://plotly.com/python/reference/layout/#layout-modebar-add
# https://plotly.com/chart-studio-help/getting-to-know-the-plotly-modebar/

cwd = str(os.getcwd())
print('------------------------------------------------------------------')
print('pyCHARTs_express                                             v1.02')
print('------------------------------------------------------------------')
print(text2art("pyCHARTs") + '                     2022 by Tobias Haueter')
print('------------------------------------------------------------------')
print('Current Working Directory: ' + cwd)
print('------------------------------------------------------------------')
files = [f for f in glob.glob("**/*.csv", recursive=True)]
for f in files:
    print(f)
print('------------------------------------------------------------------' + '\n')

csvFile_data = input('Choose your CSV data file: ')
# csvFile_data = csvFile_data + '.csv'
if not csvFile_data:
    exit('Input file name = False')
print('---> [%s]' % csvFile_data + '\n')

csvFile_delimiter = input('Choose delimiter character (default = (,): ')
if not csvFile_delimiter:
    csvFile_delimiter = ','
print('---> [%s]' % csvFile_delimiter + '\n')

csvFile_xaxis = input('Name of x-axis column in CSV file: ')
if not csvFile_xaxis:
    exit('Input x-axis name = False')
print('---> [%s]' % csvFile_xaxis + '\n')

print('------------------------------------------------------------------')

config = dict({'scrollZoom': True})


def cli_running():
    n = 0
    p = ['   ', '.', '..', '...']
    while n <= 3:
        sys.stdout.write("\rIn Progress{}".format(p[n]))
        sys.stdout.flush()
        n = n + 1
        time.sleep(0.3)
    print(' ')  # exit dynamic CLI text


try:

    cli_running()

    df = pd.read_csv(csvFile_data, delimiter=csvFile_delimiter)  # <TAB>: delimiter='\t' | comma: ','

    fig = px.line(df, x=csvFile_xaxis, y=df.columns, render_mode="svg")

    fig.update_layout(
        title_text='pyCHARTs [%s]' % csvFile_data,
        title_x=0.5,
        dragmode='zoom',
        newshape_line_color='red',
        newshape_line_width=2,
        newshape_line_dash='solid',
        modebar_add=[
            'drawline',
            'v1hovermode',
            'togglespikelines',
            'togglehover',
            'hovercompare',
            'drawopenpath',
            'drawcircle',
            'drawrect',
            'eraseshape',
            'turntable',
            'orbit',
            'select',
            'lasso',
            'pan'
             ]
    )

    fig.show(config=config)

except:
    exit('Read %s failed!' % csvFile_data)

print('!! pyCHARTs_express is finish with your work !!')
