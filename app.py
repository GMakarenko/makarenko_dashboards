import os
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
from tools import make_df
import cufflinks as cf
import flask

cf.go_offline()

app = dash.Dash()

JS_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js_files')

scripts = ["https://code.jquery.com/jquery-3.2.1.min.js", "/js_files/executor.js"]

for s in scripts:
    app.scripts.append_script({'external_url': s})
    print("loaded", s)


@app.server.route('/js_files/<resource>')
def serve_static(resource):
    return flask.send_from_directory(JS_FILES_PATH, resource)



colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    id='app-content',
    children=[
        dcc.Graph(id="data-plot"),
        html.Br(),
        html.A(id='start-script',
               children=[html.Button("Click", id='start')])]

)


@app.callback(Output('data-plot', 'figure'), events=[Event('start', 'click')])
def plot_df():
    data = make_df("GUS", 90)
    figure = data.iplot(asFigure=True)
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
