from plotly.graph_objects import Figure

empty_layout = {
    'margin': {'b': 0, 'l': 0, 'r': 0, 't': 25},
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'xaxis': {
        'showgrid': False,
        'showline': False,
        'showticklabels': False,
        'zeroline': False
    },
    'yaxis': {
        'showgrid': False,
        'showline': False,
        'showticklabels': False,
        'zeroline': False,
    }
}

initial_fig = Figure(layout=empty_layout)