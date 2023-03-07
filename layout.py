from dash import dcc, html
import dash_bootstrap_components as dbc
from utils.currencies import currencies
from utils.initial_fig import initial_fig
from datetime import date, timedelta

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Label(html.P("Select an asset")),
                        dcc.Dropdown(
                            id="asset-dropdown",
                            value='bitcoin',
                            options=[
                                {'label': k, 'value': v} for k, v in currencies.items()
                            ]
                        )
                    ],
                    className='currency-filter'
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label(html.P('Date from')),
                                dbc.Input(
                                    id='date-from-input',
                                    type='date',
                                    value=date.today() - timedelta(days=30)
                                ),
                            ],
                            className='date-from'
                        ),
                        html.Div(
                            [
                                html.Label(html.P('Date to')),
                                dbc.Input(
                                    id='date-to-input',
                                    type='date',
                                    value=date.today()
                                ),
                            ],
                            className='date-to'
                        )
                    ],
                    className='date-filters'
                ),
                html.Div(
                    dbc.Button('Apply Filters', id='apply-filters-button')
                )
            ],
            className='filters'
        ),
        html.Div(
            dcc.Graph(
                id='price-dynamics-graph',
                figure=initial_fig,
                config={
                    "scrollZoom": True,
                    "modeBarButtonsToRemove": [
                        'zoom2d', 'select2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
                        'lasso2d', 'zoomIn2d', 'zoomOut2d', 'toggleSpikelines'
                    ]
                },
                className='graph'
            ),
            className='graph-window'
        )
    ],
    className='page-body'
)
