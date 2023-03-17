import streamlit as st
import pandas as pd
from lifelines import KaplanMeierFitter
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import text


def accueil():
    st.write(text.text)


# Lecture du fichier de données
@st.cache_data
def load_data():
    data = pd.read_csv("MockPatientDatabaseOscar.csv", sep=";", encoding='latin-1')
    return data


data = load_data()


# Calcul des statistiques descriptives sur la variable "time"
def descriptive_stats():
    stats = data['time'].describe()
    return stats


# Afficher un histogramme de la durée (variable "time") pour l'ensemble de la population ou par sexe (F/H)
def plot_hist():
    option = st.selectbox('Afficher l\'histogramme pour :', ('Population', 'Hommes', 'Femmes', 'Hommes & Femmes'))
    if option == 'Population':
        fig = px.histogram(data, x='time', color_discrete_sequence=['forestgreen'])
    elif option == 'Hommes':
        fig = px.histogram(data.loc[data['Genero'] == 'M'], x='time', color_discrete_sequence=['deepskyblue'])
    elif option == "Femmes":
        fig = px.histogram(data.loc[data['Genero'] == 'F'], x='time', color_discrete_sequence=['indianred'])
    else:
        fig = px.histogram(
            data,
            y="time",
            x="Genero",
            color_discrete_sequence=['indianred', 'deepskyblue'],
            color='Genero'
        )
    st.plotly_chart(fig)


# Estimer la probabilité de survie et l'intervalle de confiance en utilisant la fonction Kanplan-Meyer.
def km_estimator():
    kmf = KaplanMeierFitter()
    kmf.fit(data['time'], event_observed=data['Evento'])
    surv_prob = kmf.survival_function_
    conf_int = kmf.confidence_interval_survival_function_
    st.write('Tableau des proportions de survivants :')
    st.write(surv_prob)
    st.write('Intervalle de confiance :')
    st.write(conf_int)


# Représenter graphiquement la courbe de survie avec l'intervalle de confiance.
def plot_km_curve():
    kmf = KaplanMeierFitter()
    kmf.fit(data['time'], event_observed=data['Evento'])
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=kmf.timeline,
            y=kmf.survival_function_['KM_estimate'],
            mode='lines',
            name='Probabilité de survie'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=kmf.timeline,
            y=kmf.confidence_interval_['KM_estimate_lower_0.95'],
            mode='lines',
            line=dict(dash='dash'),
            name='Intervalle de confiance inférieure'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=kmf.timeline,
            y=kmf.confidence_interval_['KM_estimate_upper_0.95'],
            mode='lines',
            line=dict(dash='dash'),
            name='Intervalle de confiance supérieure'
        )
    )
    fig.update_layout(title='Courbe de Kaplan-Meier', xaxis_title='Temps', yaxis_title='Probabilité de survie')
    st.plotly_chart(fig)


# Représenter la courbe de Kaplan-Meyer pour chacun des deux groupes (H/F).
def plot_km_curve_by_sex():
    kmf = KaplanMeierFitter()
    fig = go.Figure()
    for name, grouped_df in data.groupby('Genero'):
        kmf.fit(grouped_df['time'], grouped_df['Evento'], label=name)
        fig.add_trace(go.Scatter(x=kmf.timeline, y=kmf.survival_function_[name], mode='lines', name=name))
    fig.update_layout(
        title='Courbe de Kaplan-Meier par groupe',
        xaxis_title='Temps',
        yaxis_title='Probabilité de survie'
    )
    st.plotly_chart(fig)

    fig, ax = plt.subplots()
    kmf = KaplanMeierFitter()
    for name, grouped_df in data.groupby('Genero'):
        kmf.fit(grouped_df['time'], grouped_df['Evento'], label=name)
        kmf.plot(ax=ax)
    st.pyplot(fig)


# Création du menu
st.sidebar.title('Menu')
options = [
    'Accueil',
    'Lecture du fichier de données',
    'Calcul des statistiques descriptives',
    'Afficher un histogramme',
    'Estimer la probabilité de survie et l\'intervalle de confiance',
    'Représenter graphiquement la courbe de survie',
    'Représenter la courbe de Kaplan-Meyer pour chacun des deux groupes'
]
choice = st.sidebar.selectbox('Choisissez une option', options)
show_code = st.sidebar.checkbox(
    label="Montrer le code",
    value=True,
)

# Affichage de l'option sélectionnée
if choice == options[0]:
    accueil()
elif choice == options[1]:
    st.write(load_data())
    if show_code:
        st.code(text.load_data, language='python')
elif choice == options[2]:
    st.write(descriptive_stats())
    if show_code:
        st.code(text.descriptive_stats, language='python')
elif choice == options[3]:
    plot_hist()
    if show_code:
        st.code(text.plot_hist, language='python')
elif choice == options[4]:
    km_estimator()
    if show_code:
        st.code(text.km_estimator, language='python')
elif choice == options[5]:
    plot_km_curve()
    if show_code:
        st.code(text.plot_km_curve, language='python')
elif choice == options[6]:
    plot_km_curve_by_sex()
    if show_code:
        st.code(text.plot_km_curve_by_sex, language='python')
