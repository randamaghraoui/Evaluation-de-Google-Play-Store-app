
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle
#import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash_html_components as html
from dash.dependencies import Input, Output,ALL
import plotly.express as px
import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
#from app import app

from RatingApp import tab_1_layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv(
    'C:/Users/lenovo/Documents/Google-Play-Store-Rating-master/Data/finaldata.csv')
df = pd.read_csv('C:/Users/lenovo/Documents/Google-Play-Store-Rating-master/Data/googleplaystore_user_reviews.csv')

app.config.suppress_callback_exceptions = True
colors = {"background": "#F3F6FA", "background_div": "white", 'text': '#009999'}
app.config['suppress_callback_exceptions']= True


labels = ['Free','Paid']
values = [92.2,7.8]
labels2 = ['Everyone','Teen','Mature 17+','Everyone10+','Adults only18+','unrated']
values2 = [79.21,11.58,4.93,4.24,0.3,0.1]
labels3 = ['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY',
          'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION',
          'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE',
          'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME',
          'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'GAME', 'FAMILY', 'MEDICAL',
          'SOCIAL', 'SHOPPING', 'PHOTOGRAPHY', 'SPORTS', 'TRAVEL_AND_LOCAL',
          'TOOLS', 'PERSONALIZATION', 'PRODUCTIVITY', 'PARENTING', 'WEATHER',
          'VIDEO_PLAYERS', 'NEWS_AND_MAGAZINES', 'MAPS_AND_NAVIGATION']
values3 = [0.6,0.7,0.2,1.9,3.2,0.4,3.5,2.1,1.7,1.6,0.3,3.5,1.2,3.2,0.7,0.5,3.4,11.7,18.7,3.7,2.5,3.4,3.4,2.4,7.8,3.3,3.7,0.3,0.8,1.7,1.3,1.2]
genres = ['Action', 'Action & Adventure', 'Adventure', 'Arcade', 'Art & Design',
            'Auto & Vehicles', 'Beauty', 'Board', 'Books & Reference',
            'Brain Games', 'Business', 'Card', 'Casino', 'Casual', 'Comics',
            'Communication', 'Creativity', 'Dating', 'Education', 'Educational',
            'Entertainment', 'Events', 'Finance', 'Food & Drink',
            'Health & Fitness', 'House & Home', 'Libraries & Demo', 'Lifestyle',
            'Maps & Navigation', 'Medical', 'Music', 'Music & Audio',
            'Music & Video', 'News & Magazines', 'Parenting', 'Personalization',
            'Photography', 'Pretend Play', 'Productivity', 'Puzzle', 'Racing',
            'Role Playing', 'Shopping', 'Simulation', 'Social', 'Sports',
            'Strategy', 'Tools', 'Travel & Local', 'Trivia',
            'Video Players & Editors', 'Weather', 'Word']
valuesg=[3.8,0.1,0.8,2.2,0.6,0.7,0.5,0.4,1.9,0.1,3.2,0.4,0.4,0.6,3.5,0.1,0.1,5.0,0.3,5.7,0.5,3.5,0.2,3.2,0.8,0.7,3.3,1.3,3.7,0.3,0.2,0.3,2.5,0.4,3.3,3.4
         ,0.2,3.7,1.3,1.0,0.1,2.5,2.1,2.8,3.6,1.1,7.8,2.4,0.1,1.7,0.8,0.1]    
x=['Positive','Neutral','Negative']
y=[64.1,13.8,22.1]                 
rating=[1,1.5,2,2.5,3,3.5,4,4.5,5]

tab_1_layout1 = html.Div([
            # html.H3('Google Play'),

                html.Div([
                    html.Div([
                        #html.H6('Type', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-1',
                            figure={
                                
                                'data': [go.Pie(labels=labels, values=values),
                
                                ],
                                'layout': {
                                    'title': 'Type'
                                }
                            }
                        )
                    ], className="four columns"),

                    html.Div([
                        #html.H6('Content Rating', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-2',
                            figure={
                                'data': [go.Pie(labels=labels2, values=values2)

                                ],
                                'layout': {
                                    'title': 'Content Rating'
                                }
                            }
                        )
                    ], className="four columns"),

                    html.Div([
                        #html.H6('Sentiment', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-3',
                            figure={
                                'data': [go.Pie(labels=x, values=y)

                                ],
                                'layout': {
                                    'title': 'Sentiment'
                                }
                            }
                        )
                    ], className="four columns")

                ], className="row", style={"margin": "1% 3%"}),

                html.Div([
                    html.Div([
                        #html.H6('Size', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-4',
                            figure={
                                'data': [{'x': data['Size'], 'y': data['Size'],'type': 'histogram', 'name': 'Category'}

                                ],
                                'layout': {
                                    'title': 'Size'
                                }
                            }
                        )
                        ], className="six columns"),

                    html.Div([
                        #html.H6('Category', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-5',
                            figure={
                                'data':  [go.Pie(labels=labels3, values=values3)

                                ],
                                'layout': {
                                    'title': 'Category'
                                }
                            }
                        )
                    ], className="six columns"),
                ], className="row", style={"margin": "1% 3%"}),
                html.Div([
                    html.Div([
                        #html.H6('Genres', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-6',
                            figure={
                                'data': [go.Pie(labels=genres, values=valuesg)
               # {'x': df['Rating'], 'y': df['Rating'],'type': 'histogram', 'name': 'Category'},

                                ],
                                'layout': {
                                    'title': 'Genres'
                                }
                            }
                        )
                    ])
                ], className="row", style={"margin": "1% 3%"}),
                html.Div([
                    html.Div([
                        #html.H6('Rating', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-6',
                            figure={
                                'data': [
                {'x': data['Rating'], 'y': data['Rating'],'type': 'histogram', 'name': 'Category'},

                                ],
                                'layout': {
                                    'title': 'Rating'
                                }
                            }
                        )
                    ])
                ], className="row", style={"margin": "1% 3%"})

            ]
        )
tab_2_layout = html.Div([
            html.Div([
                html.Div([
                    #html.H6('Size Rating'),
                    dcc.Graph(
                        id='med-graph-1',
                        figure={
                            'data': [go.Scatter(x=data['Rating'],y=data['Size'], mode='markers',
                                marker_color=data['Rating'],
                                text=data['Size']),


                            ],
                            'layout': {
                                'title': 'Size Rating'
                            }
                        }
                    )
                ], className="six columns"),

                html.Div([
                   # html.H6('Category Rating '),
                    dcc.Graph(
                        id='med-graph-2',
                        figure={
                            'data': [go.Scatter(x=df['Sentiment_Subjectivity'],y=data['Rating'], mode='markers',
                               # marker_color=data['Category'],
                                text=df['Sentiment']),

                            ],
                            'layout': {
                                'title': 'sentiment  Rating'
                            }
                        }
                    )
                ], className="six columns"),
  
  html.Div([
            html.Div([
                    html.H6('**** ', style={'color': 'white'}),
                    
                    dcc.Graph(
                        id='dem-graph-6',
                        figure={
                             'data': [go.Scatter(x=data['Rating'],y=data['Category'], mode='markers',
                               # marker_color=data['Category'],
                                text=data['Rating']),                               

                            ],
                            'layout': {
                                'title': 'Category Rating'
                            }
                        }
                    )
                ], className="row", style={"margin": "1% 3%"}),  
                          
  ] )            

            ], className="row", style={"margin": "1% 3%"}),
             html.Div([
                    html.Div([
                        #html.H6('Genre Rating', style={'textAlign': 'center'}),
                        dcc.Graph(
                            id='dem-graph-6',
                            figure={
                                'data': [
               go.Scatter(x=data['Genres'],y=data['Rating'], mode='markers',
                               # marker_color=data['Category'],
                                text=data['Rating']),

                                ],
                                'layout': {
                                    'title': 'Genre Rating'
                                }
                            }
                        )
                    ])

                ], className="row", style={"margin": "1% 3%"})
    ])
page_3_layout = html.Div([
    html.H1('Page 2'),
     dcc.Location(id='url'),
    dcc.Link('Go to Page 1', href='/apps/RatingApp'),
     html.Div(id="page-content")
])
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('Google Play Store App Dashboard', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

      dcc.Tabs(id="tabs", className="row", style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}, value='dem_tab', children=[
        dcc.Tab(label='Google Play Store App', value='dem_tab'),
        dcc.Tab(label='Rating ', value='med_tab'),
        dcc.Tab(label='whould y have rating  ', value='/apps/RatingApp'),
        # dcc.Tab(label='Re-admissions', value='readmit_tab')
    ]),
    html.Div(id='tabs-content')
])

from dash.dependencies import Input, Output
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
              #[Input('tabs', 'value')])

  
def render_content(tab):
    if tab == 'dem_tab':
        return tab_1_layout1
    elif tab == 'med_tab':
        return tab_2_layout
    elif tab=='/apps/RatingApp':
        return tab_1_layout
@app.callback(
    Output('predictedrating', 'children'),
    [Input('price', 'value'), Input(
        'contentrating', 'value'), Input('size', 'value'), Input('types', 'value'), Input('genre', 'value'),
        Input('category', 'value')]
)
def update_output(price, contentrating, size, types, genre, category):
    data = {'Size': 0.0, 'Type': 0, 'Price': 0.0, 'Action': 0, 'Action & Adventure': 0, 'Adventure': 0, 'Arcade': 0, 'Art & Design': 0, 'Auto & Vehicles': 0, 'Beauty': 0, 'Board': 0, 'Books & Reference': 0, 'Brain Games': 0, 'Business': 0, 'Card': 0, 'Casino': 0, 'Casual': 0, 'Comics': 0, 'Communication': 0, 'Creativity': 0, 'Dating': 0, 'Education': 0, 'Educational': 0, 'Entertainment': 0, 'Events': 0, 'Finance': 0, 'Food & Drink': 0, 'Health & Fitness': 0, 'House & Home': 0, 'Libraries & Demo': 0, 'Lifestyle': 0, 'Maps & Navigation': 0, 'Medical': 0, 'Music': 0, 'Music & Audio': 0, 'Music & Video': 0, 'News & Magazines': 0, 'Parenting': 0, 'Personalization': 0, 'Photography': 0, 'Pretend Play': 0, 'Productivity': 0, 'Puzzle': 0, 'Racing': 0,
            'Role Playing': 0, 'Shopping': 0, 'Simulation': 0, 'Social': 0, 'Sports': 0, 'Strategy': 0, 'Tools': 0, 'Travel & Local': 0, 'Trivia': 0, 'Video Players & Editors': 0, 'Weather': 0, 'Word': 0, 'Category_ART_AND_DESIGN': 0, 'Category_AUTO_AND_VEHICLES': 0, 'Category_BEAUTY': 0, 'Category_BOOKS_AND_REFERENCE': 0, 'Category_BUSINESS': 0, 'Category_COMICS': 0, 'Category_COMMUNICATION': 0, 'Category_DATING': 0, 'Category_EDUCATION': 0, 'Category_ENTERTAINMENT': 0,
            'Category_EVENTS': 0, 'Category_FAMILY': 0, 'Category_FINANCE': 0, 'Category_FOOD_AND_DRINK': 0, 'Category_GAME': 0, 'Category_HEALTH_AND_FITNESS': 0, 'Category_HOUSE_AND_HOME': 0, 'Category_LIBRARIES_AND_DEMO': 0, 'Category_LIFESTYLE': 0, 'Category_MAPS_AND_NAVIGATION': 0, 'Category_MEDICAL': 0, 'Category_NEWS_AND_MAGAZINES': 0, 'Category_PARENTING': 0, 'Category_PERSONALIZATION': 0, 'Category_PHOTOGRAPHY': 0, 'Category_PRODUCTIVITY': 0, 'Category_SHOPPING': 0, 'Category_SOCIAL': 0, 'Category_SPORTS': 0, 'Category_TOOLS': 0, 'Category_TRAVEL_AND_LOCAL': 0, 'Category_VIDEO_PLAYERS': 0, 'Category_WEATHER': 0, 'content_rating_Adults only 18+': 0, 'content_rating_Everyone': 0, 'content_rating_Everyone 10+': 0, 'content_rating_Mature 17+': 0, 'content_rating_Teen': 0}
    for x in data:
        if(x == genre):
            data[x] = 1
        elif(x == category):
            data[x] = 1
        elif(x == contentrating):
            data[x] = 1
        elif(x == 'Type'):
            if(types == 'Free'):
               data[x] = 0
            elif(types=='Paid'):
               data[x] = 1
        elif(x =='Size'):
            data[x] = size
        elif(x =='Price'):
            data[x] = price
            # if (price>0):
            #     data['Type'] = 0
            # else:
            #     data['Type'] = 1
#app = dash.Dash(__name__)
    input_data = pd.DataFrame(data, index=[0])
    svr_model = pickle.load(open(
        'C:/Users/lenovo/Documents/Google-Play-Store-Rating-master/Models/DecTreeRegModel.sav', 'rb'))
    svr_result = svr_model.predict(input_data)
    return (' Predicted rating  is {}'.format(svr_result))        
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8050', proxy=None, debug=False, dev_tools_ui=None, dev_tools_props_check=None, dev_tools_serve_dev_bundles=None, dev_tools_hot_reload=None, dev_tools_hot_reload_interval=None, dev_tools_hot_reload_watch_interval=None, dev_tools_hot_reload_max_retry=None, dev_tools_silence_routes_logging=None, dev_tools_prune_errors=None)

    #app.run_server(debug=True)
    #port="8017"