# app-runner
from app import app
from layout import layout
from callback import price_dynamics_graph  # has to be imported here


app.layout = layout
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
