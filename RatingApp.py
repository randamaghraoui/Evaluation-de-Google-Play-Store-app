
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64
import pickle

from app import app
image_filename = '153-1534763_5-stars-film-rating-clipart-png-download-5.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())



#from flask_ngrok import run_with_ngrok
#from flask import Flask

df = pd.read_csv('googleplaystore.csv')
df.dropna(inplace=True)
types = df['Type'].unique()
contentrating = df['Content Rating'].unique()

data = {'Size': 0.0, 'Type': 0, 'Price': 0.0, 'content_rating': 0, 'Action': 0, 'Action & Adventure': 0, 'Adventure': 0, 'Arcade': 0, 'Art & Design': 0, 'Auto & Vehicles': 0, 'Beauty': 0, 'Board': 0, 'Books & Reference': 0, 'Brain Games': 0, 'Business': 0, 'Card': 0, 'Casino': 0, 'Casual': 0, 'Comics': 0, 'Communication': 0, 'Creativity': 0, 'Dating': 0, 'Education': 0, 'Educational': 0, 'Entertainment': 0, 'Events': 0, 'Finance': 0, 'Food & Drink': 0, 'Health & Fitness': 0, 'House & Home': 0, 'Libraries & Demo': 0, 'Lifestyle': 0, 'Maps & Navigation': 0, 'Medical': 0, 'Music': 0, 'Music & Audio': 0, 'Music & Video': 0, 'News & Magazines': 0, 'Parenting': 0, 'Personalization': 0, 'Photography': 0, 'Pretend Play': 0, 'Productivity': 0, 'Puzzle': 0, 'Racing': 0,
        'Role Playing': 0, 'Shopping': 0, 'Simulation': 0, 'Social': 0, 'Sports': 0, 'Strategy': 0, 'Tools': 0, 'Travel & Local': 0, 'Trivia': 0, 'Video Players & Editors': 0, 'Weather': 0, 'Word': 0, 'Category_ART_AND_DESIGN': 0, 'Category_AUTO_AND_VEHICLES': 0, 'Category_BEAUTY': 0, 'Category_BOOKS_AND_REFERENCE': 0, 'Category_BUSINESS': 0, 'Category_COMICS': 0, 'Category_COMMUNICATION': 0, 'Category_DATING': 0, 'Category_EDUCATION': 0, 'Category_ENTERTAINMENT': 0,
        'Category_EVENTS': 0, 'Category_FAMILY': 0, 'Category_FINANCE': 0, 'Category_FOOD_AND_DRINK': 0, 'Category_GAME': 0, 'Category_HEALTH_AND_FITNESS': 0, 'Category_HOUSE_AND_HOME': 0, 'Category_LIBRARIES_AND_DEMO': 0, 'Category_LIFESTYLE': 0, 'Category_MAPS_AND_NAVIGATION': 0, 'Category_MEDICAL': 0, 'Category_NEWS_AND_MAGAZINES': 0, 'Category_PARENTING': 0, 'Category_PERSONALIZATION': 0, 'Category_PHOTOGRAPHY': 0, 'Category_PRODUCTIVITY': 0, 'Category_SHOPPING': 0, 'Category_SOCIAL': 0, 'Category_SPORTS': 0, 'Category_TOOLS': 0, 'Category_TRAVEL_AND_LOCAL': 0, 'Category_VIDEO_PLAYERS': 0, 'Category_WEATHER': 0}

category = ['Category_ART_AND_DESIGN', 'Category_AUTO_AND_VEHICLES', 'Category_BEAUTY',
          'Category_BOOKS_AND_REFERENCE', 'Category_BUSINESS', 'Category_COMICS', 'Category_COMMUNICATION',
          'Category_DATING', 'Category_EDUCATION', 'Category_ENTERTAINMENT', 'Category_EVENTS', 'Category_FINANCE',
          'Category_FOOD_AND_DRINK', 'Category_HEALTH_AND_FITNESS', 'Category_HOUSE_AND_HOME',
          'Category_LIBRARIES_AND_DEMO', 'Category_LIFESTYLE', 'Category_GAME', 'Category_FAMILY', 'Category_MEDICAL',
          'Category_SOCIAL', 'Category_SHOPPING', 'Category_PHOTOGRAPHY', 'Category_SPORTS', 'Category_TRAVEL_AND_LOCAL',
          'Category_TOOLS', 'Category_PERSONALIZATION', 'Category_PRODUCTIVITY', 'Category_PARENTING', 'Category_WEATHER',
          'Category_VIDEO_PLAYERS', 'Category_NEWS_AND_MAGAZINES', 'Category_MAPS_AND_NAVIGATION']
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

contentrating = ['content_rating_Adults only 18+', 'content_rating_Everyone',
                 'content_rating_Everyone 10+', 'content_rating_Mature 17+', 'content_rating_Teen']


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
          

tab_1_layout = html.Div([ 
   # html.Img(
    #        src="/content/drive/MyDrive/Colab Notebooks/images/153-1534763_5-stars-film-rating-clipart-png-download-5.png",
    #        style={
      #          'maxWidth': '100%',
      #          'maxHeight': '100%',
      #          'marginLeft': 'auto',
       #         'marginRight': 'auto'
        #    }
       # ),   
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'maxWidth': '20%',})  ,   
                                             
    html.H1(children='Google Playstore Apps Rating Prediction', style= {'text-align':'center', 'font-family':'Viga','color':'#0d0887'}),
   ], className="row", style={"margin": "1% 3%"}),
    #html.H2(children="Dataset obtained from Lava18 on Kaggle"),
    #html.H2(html.A(children='Dataset Here',
    #href='https://www.kaggle.com/lava18/google-play-store-apps/kernels')),
    #html.Br(),
   # html.Br(),
   # html.Br(),
    html.Div([
    html.H3("Content Rating"),
    dcc.Dropdown(
        id='contentrating',
        options=[{'label': i, 'value': i} for i in contentrating],
        placeholder='Content Rating',
        value='',
        style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}
    ),
     
        ], className="four columns"),
html.Div([
    html.H3("Size of App in bytes (Limit 100 Mb)"),
    dcc.Input(
        id='size',
        placeholder='Size',
        value=0.0,
        style={"margin": "2% 3%","height":"20","verticalAlign":"middle"},
        maxLength=9,
    ),
        ], className="four columns"),
 html.Div([
    html.H3("Free or Paid"),
    dcc.Dropdown(
        id='types',
        options=[{'label': i, 'value': i} for i in types],
        placeholder='Type',
        value='Free',
        style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}
    ),
    ], className="four columns"),
     html.Div([
        html.H3("Price"),
    dcc.Input(
        id='price',
        value=0.0,
        maxLength=3,
        style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}
    ),
        
        ], className="four columns"),
html.Div([
    html.H3("Genre"),
    dcc.Dropdown(
        id='genre',
        options=[{'label': i, 'value': i} for i in genres],
        value='',
        style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}
    ),    ], className="four columns"),
html.Div([
    html.H3("Category"),
    dcc.Dropdown(
        id='category',
        options=[{'label': i, 'value': i} for i in category],
        value='',
        placeholder='Select Category',
        style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}
    ), 
    ], className="four columns"),   
    html.Div([

    html.H3("Predicted Ratings"),
 
    html.Div(id="predictedrating"
    ,style={'font-size':'40px','color':'#F0C300'})
    # generate_table(df)
], className="row", style={"margin": "1% 3%"})
    ])
app.layout = html.Div(style={'backgroundColor': '#F8F9F9'},children=[tab_1_layout])

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
    tree_model = pickle.load(open(
        'DecTreeRegModel.sav', 'rb'))
    tree_result = tree_model.predict(input_data)
    return (' Predicted rating  is {}'.format(tree_result))

#if __name__ == '__main__':
 #   app.run_server(debug=False)
  
