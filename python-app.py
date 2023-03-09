from dash import Dash, html


app = Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.H1('Vitej, vole!')
app.title = "GUI for BCK Automation Tool"
app.run(debug=True)
