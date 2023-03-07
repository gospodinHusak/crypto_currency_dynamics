from app import app
from dash import Output, Input, State
from utils.totimestamp import totimestamp
from plotly.express import bar
from pandas import DataFrame
from requests import request
from json import loads


@app.callback(
    Output('price-dynamics-graph', 'figure'),
    Input('apply-filters-button', 'n_clicks'),
    State('asset-dropdown', 'value'),
    State('date-from-input', 'value'),
    State('date-to-input', 'value'),
    prevent_initial_call=True
)
def price_dynamics_graph(n_clicks, asset, date_from, date_to):
    d1 = totimestamp(date_from)
    d2 = totimestamp(date_to)

    url = f'http://api.coincap.io/v2/assets/{asset}/history?interval=d1&start={d1}&end={d2}'
    response_raw_data = request("GET", url, headers={}, data={})
    json_data = loads(response_raw_data.text.encode('utf8'))

    data = DataFrame(json_data['data'])
    data['priceUsd'] = data['priceUsd'].astype('float')
    fig = bar(data_frame=data, x='date', y='priceUsd', labels=dict(priceUsd='PRICE', date='DATE'))
    fig.update_layout(
        title={
            'text': 'Cryptocurrency Price Dynamics',
            'xanchor': 'auto',
            'yanchor': 'auto',
            'x': .5,
            'y': .98
        },
        yaxis={'tickformat': "20,.2f"},
        margin={'b': 5, 'l': 5, 'r': 5, 't': 25},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#EBEBF5'},
    )
    return fig
