# spacex_dash_app.py
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# --- load data (change path if you downloaded CSV locally) ---
DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv(DATA_URL)

# --- helper: find likely column name among candidates ---
def find_col(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None

LAUNCH_COL   = find_col(spacex_df, ['Launch Site','Launch_Site','LaunchSite'])
CLASS_COL    = find_col(spacex_df, ['class','Class','outcome','Outcome','landing_class'])
PAYLOAD_COL  = find_col(spacex_df, ['Payload Mass (kg)','PayloadMass','Payload Mass','Payload'])
BOOSTER_COL  = find_col(spacex_df, ['Booster Version Category','Booster Version','Booster_Version','BoosterVersion'])

# If any essential column missing, raise readable error
if LAUNCH_COL is None or CLASS_COL is None or PAYLOAD_COL is None:
    raise SystemExit(f"Missing expected column. Available columns: {spacex_df.columns.tolist()}")

# Normalize class to numeric 0/1 (coerce non-numeric to NaN)
spacex_df[CLASS_COL] = pd.to_numeric(spacex_df[CLASS_COL], errors='coerce').fillna(0).astype(int)

# compute slider bounds
min_payload = int(spacex_df[PAYLOAD_COL].min())
max_payload = int(spacex_df[PAYLOAD_COL].max())

# --- build Dash app ---
app = Dash(__name__)
app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={'textAlign':'center'}),

    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=[{'label':'All Sites','value':'ALL'}] + [
                {'label': s, 'value': s} for s in sorted(spacex_df[LAUNCH_COL].unique())
            ],
            value='ALL',
            placeholder='Select a Launch Site here',
            searchable=True,
            style={'width':'70%'}
        )
    ], style={'display':'flex','justifyContent':'center','marginTop':20}),

    html.Div([
        dcc.Graph(id='success-pie-chart', style={'width':'48%','display':'inline-block'}),
        dcc.Graph(id='success-payload-scatter-chart', style={'width':'48%','display':'inline-block'})
    ], style={'display':'flex','justifyContent':'space-around','alignItems':'flex-start','marginTop':20}),

    html.Div([
        html.Label("Payload range (kg)"),
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            step=1000,
            marks={i: str(i) for i in range(0,10001,2000)},
            value=[min_payload, max_payload]
        )
    ], style={'width':'80%','margin':'40px auto'})
])

# --- Callback for pie chart (Task 2) ---
@app.callback(
    Output('success-pie-chart','figure'),
    Input('site-dropdown','value')
)
def update_pie(selected_site):
    if selected_site == 'ALL':
        # sum of successes per site
        df_all = spacex_df.groupby(LAUNCH_COL, as_index=False)[CLASS_COL].sum()
        fig = px.pie(df_all, names=LAUNCH_COL, values=CLASS_COL,
                     title='Total Successful Launches by Site')
        return fig
    else:
        df_site = spacex_df[spacex_df[LAUNCH_COL] == selected_site]
        success = int((df_site[CLASS_COL] == 1).sum())
        failure = int((df_site[CLASS_COL] == 0).sum())
        fig = px.pie(names=['Failure','Success'], values=[failure, success],
                     title=f'Launch Outcomes for site: {selected_site}')
        return fig

# --- Callback for payload vs success scatter (Task 4) ---
@app.callback(
    Output('success-payload-scatter-chart','figure'),
    Input('site-dropdown','value'),
    Input('payload-slider','value')
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    # filter by payload
    dff = spacex_df[(spacex_df[PAYLOAD_COL] >= low) & (spacex_df[PAYLOAD_COL] <= high)]

    if selected_site != 'ALL':
        dff = dff[dff[LAUNCH_COL] == selected_site]

    color_col = BOOSTER_COL if BOOSTER_COL is not None else LAUNCH_COL

    fig = px.scatter(
        dff,
        x=PAYLOAD_COL,
        y=CLASS_COL,
        color=color_col,
        hover_data=[LAUNCH_COL, PAYLOAD_COL],
        title=('Payload vs Outcome' + (f' for {selected_site}' if selected_site!='ALL' else ' for All Sites')),
        labels={PAYLOAD_COL:'Payload Mass (kg)', CLASS_COL:'Class'}
    )
    fig.update_yaxes(tickvals=[0,1], ticktext=['Failure','Success'])
    return fig

# --- run app (Dash v3+) ---
if __name__ == '__main__':
    app.run(debug=True)
