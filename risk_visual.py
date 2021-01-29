import pandas as pd
import plotly.express as px
import dash         #(version 1.0.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# ## df 세팅
df_visual = pd.read_excel('./result/mother_file10.xlsx').fillna("")   ## ws_risk_mother 실행 결과인 엑셀 읽어오기

df_visual['R_vector'] = pd.to_numeric(df_visual['R_vector']).fillna(0)

gdf = df_visual.groupby(["대구분","중구분","소구분","부서","WS_ID","WORK_STAND_NM"], as_index=False)[["위험_id개수", "R_vector"]].sum()


# ## 단순 시각화

# fig = px.bar(gdf, x="R_vector", y="부서", color='대구분', orientation='h',
#              hover_data=["대구분", "WORK_STAND_NM", "R_vector"],
#              height=800,
#              title='Test1',
#             category_orders = {"부서":
#                               ["가공소조립부", "판넬조립부", "대조립1부", "대조립2부",
#                               "선행의장부", "의장생산부", "Unit생산부", "선행도장부", "내업공사지원부",
#                               "선실생산부", "건조1부", "건조2부", "건조3부", "의장1부", "의장2부",
#                               "의장3부", "CHS공사부", "기계의장부", "LNG공사부", "도장1부", "도장2부","발판지원부",
#                               "외업공사지원부", "시운전부", "운항관제과", "자재운영부", "조선해양품질경영1부", "조선해양품질경영2부", "작업표준혁신TF"]})
# fig.show()


# ## Plotly Dash Visual

app = dash.Dash(__name__)

app.layout = html.Div([

        html.Div([
            html.Label(['부서'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': '부서', 'value': '부서'},
                         {'label': '대구분', 'value': '대구분'},
                ],
                value='부서',
                style={"width": "50%"}
            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['값'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                         {'label': 'Risk Vector', 'value': 'R_vector'},
                         {'label': 'Risk Count', 'value': '위험_id개수'},
                ],
                value='R_vector',
                style={"width": "50%"}
            ),
        ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])


@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)
def update_graph(x_axis, y_axis):

    dff = gdf
    barchart=px.bar(
            data_frame=dff,
            x= x_axis,
            y= y_axis,
            title="Risk in Working Standard",
            # facet_col='Borough',
            # color='대공정',
            # barmode='group',
            )

    barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,},
                           )

    return (barchart)




if __name__ == '__main__':
    # app.run_server(port = 4040)
    app.run_server(debug=True)
