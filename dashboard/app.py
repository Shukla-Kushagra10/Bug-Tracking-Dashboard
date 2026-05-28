import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from reports.data_processor import get_bug_data

app = dash.Dash(__name__)

def load_data():
    df = get_bug_data()
    # Dummy data fallback for empty local databases to demonstrate functionality
    if df.empty:
        df = pd.DataFrame({
            'bug_id': [1, 2, 3], 'severity': ['High', 'Medium', 'Low'],
            'status': ['Open', 'In Progress', 'Closed'], 'developer': ['Alice', 'Bob', 'Alice'],
            'sprint': ['Sprint 1', 'Sprint 1', 'Sprint 2'], 'resolution_time_days': [None, None, 4],
            'module': ['Checkout', 'Login', 'API']
        })
    return df

app.layout = html.Div([
    html.H1("🐞 Bug Tracking Dashboard"),
    
    # Filters: By module, severity, sprint, developer[cite: 11].
    dcc.Dropdown(
        id='sprint-filter',
        options=[{'label': s, 'value': s} for s in load_data()['sprint'].unique()],
        multi=True,
        placeholder="Filter by Sprint"
    ),

    html.Div([
        # Pie chart: Bug severity distribution 
        dcc.Graph(id='severity-pie', style={'display': 'inline-block', 'width': '48%'}),
        # Line graph: Defect trend over sprints 
        dcc.Graph(id='trend-line', style={'display': 'inline-block', 'width': '48%'}),
    ]),
    
    html.Div([
        # Bar chart: Average resolution time per developer 
        dcc.Graph(id='resolution-bar', style={'display': 'inline-block', 'width': '48%'}),
        html.Div([
            html.H3("Table: Open vs Closed bugs"), # Table: Open vs Closed bugs 
            dash_table.DataTable(id='bug-table')
        ], style={'display': 'inline-block', 'width': '48%', 'verticalAlign': 'top'})
    ])
])

@app.callback(
    [Output('severity-pie', 'figure'), Output('trend-line', 'figure'),
     Output('resolution-bar', 'figure'), Output('bug-table', 'data')],
    [Input('sprint-filter', 'value')]
)
def update_charts(selected_sprints):
    df = load_data()
    if selected_sprints:
        df = df[df['sprint'].isin(selected_sprints)]
        
    fig_pie = px.pie(df, names='severity', title='Severity Distribution')
    
    trend_data = df.groupby('sprint').size().reset_index(name='count')
    fig_line = px.line(trend_data, x='sprint', y='count', title='Defect Trend')
    
    res_data = df.dropna(subset=['resolution_time_days'])
    fig_bar = px.bar(res_data, x='developer', y='resolution_time_days', title='Resolution Time')
    
    table_data = df[['bug_id', 'module', 'severity', 'status']].to_dict('records')
    
    return fig_pie, fig_line, fig_bar, table_data

if __name__ == '__main__':
    app.run_server(debug=True)
    