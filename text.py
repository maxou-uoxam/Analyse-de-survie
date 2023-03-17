text = """
# Analyse de survie  
Ce document présente le travail effectué par Maxime Dangelser et Alexis Aulagnier dans le cadre du cours de Projet d’ingénierie des données du Master 1 MIAGE de Polytech Lyon.
Le sujet porte sur l’analyse de survie avec la bibliothèque lifeline en python.

## Présentation du jeu de données :
Nous n’avons pas d’informations sur le jeu de données et nous n’en avons pas trouvé sur internet non plus.
Le jeu de données s’appelle MockPatientDatabaseOscar, « mock patient » voulant dire « faux patient », ce doit être un jeu de données factice représentant une population de personnes en train de se faire soigner.

Le jeu de données contient 52 lignes et nous allons utiliser 3 colonnes :
- Le genre (Homme ou Femme) ~ Genero
- Le temps (entre 10 et 611 qui représente le moment où les données du patient ont été récupérés durant la durée de l’étude) ~ time
- L’évènement (0 : le patient est en vie, 1 : le patient est mort) ~ Evento

## Présentation du langage utilisé :
Lors de ce projet nous avons utilisé le langage de programmation Python.

Python est un langage de programmation interprété, à syntaxe claire et simple, et qui met l'accent sur la lisibilité du code. Il est facile à apprendre et à utiliser pour les débutants en programmation, mais aussi assez puissant pour être utilisé dans des projets complexes.

Python est un langage polyvalent, utilisé dans une grande variété d'applications, notamment pour la science des données, l'apprentissage automatique, la création d'applications web, l'automatisation de tâches, les scripts système, les jeux et bien plus encore.

Il a une grande communauté de développeurs qui ont créé une multitude de bibliothèques et de frameworks, tels que Pandas, Numpy, Matplotlib, Django, Flask, etc., qui facilitent le développement de projets de différentes tailles et complexités.

En outre, Python est un langage open-source, ce qui signifie que tout le monde peut l'utiliser, le modifier et le distribuer librement. C'est un langage très populaire et largement utilisé dans l'industrie, l'éducation et la recherche.


## Présentation des bibliothèques utilisées :
Pour effectuer ce travail nous avons utilisé différentes bibliothèques présentées ci-dessous.

### Pandas :
Pandas est une bibliothèque open-source pour Python qui permet de manipuler et d'analyser des données tabulaires.

Pandas fournit des fonctionnalités pour lire et écrire des données dans différents formats de fichiers, tels que CSV, Excel, JSON, SQL et bien plus encore. Elle permet également de nettoyer et de préparer les données pour l'analyse, notamment en gérant les valeurs manquantes et en effectuant des opérations de fusion, de regroupement et de filtrage.

### LifeLines :
Lifelines est une bibliothèque open-source de Python qui fournit des outils pour l'analyse de données de survie et l'estimation de la durée de vie. Elle est conçue pour les scientifiques des données, les ingénieurs et les chercheurs qui travaillent avec des données de survie dans divers domaines tels que la médecine, l'économie, l'ingénierie, la biologie et bien d'autres encore.

Lifelines permet de modéliser et d'analyser des données de survie à l'aide de techniques telles que l'estimation de la fonction de survie, l'analyse de la durée de vie, les courbes de Kaplan-Meier, les modèles de régression Cox et bien d'autres encore. Elle fournit également des fonctionnalités pour l'analyse des données censurées, telles que les données de survie tronquées, les données de survie avec des valeurs manquantes, les données de survie intervalles et bien d'autres encore.

### Streamlit :
Streamlit est une bibliothèque open-source de Python qui permet de créer facilement des applications web interactives à partir de scripts Python. Elle fournit une interface simple et intuitive pour créer des applications web en utilisant des commandes simples telles que "st.title", "st.write", "st.plot" et bien d'autres encore.

Streamlit permet aux utilisateurs de créer des applications web interactives à partir de scripts Python en quelques minutes, sans avoir à apprendre des langages de programmation web tels que HTML, CSS ou JavaScript. Elle prend également en charge les graphiques interactifs, les cartes, les animations, les widgets, les formulaires et bien d'autres encore.

Streamlit est très populaire dans la communauté des scientifiques des données, car elle permet de créer des tableaux de bord interactifs pour visualiser et explorer des données rapidement et facilement. Elle est également très utile pour la création de prototypes, la démonstration de concepts, la formation et l'enseignement.


### Plotly :
**Plotly** est une bibliothèque de visualisation de données en Python, utilisée pour créer des graphiques interactifs. Elle propose deux interfaces pour créer des graphiques : plotly.express et plotly.graph_objects.

**Plotly.express** est une interface haut niveau pour créer des graphiques rapidement et facilement. Elle est construite sur la base de la bibliothèque pandas et est conçue pour être facile à utiliser pour les débutants en visualisation de données. Elle fournit une grande variété de graphiques prêts à l'emploi pour les types de données les plus courants, tels que les graphiques en barres, les graphiques à secteurs, les graphiques en nuage de points, les diagrammes en boîte, les histogrammes, etc. Il est également possible de personnaliser ces graphiques en ajoutant des options pour la couleur, la taille, les axes, etc.

**Plotly.graph_objects** est une interface bas niveau pour créer des graphiques plus personnalisés. Elle est conçue pour les utilisateurs avancés qui souhaitent un contrôle total sur leur graphique. Cette interface permet de créer des graphiques à partir de zéro en ajoutant des éléments tels que des axes, des titres, des annotations, des légendes, des formes et des images. Elle permet également de créer des graphiques interactifs en ajoutant des événements, des animations et des liens.

### Matplotlib :
Matplotlib est une bibliothèque de visualisation de données en Python qui permet de créer des graphiques statiques. Matplotlib.pyplot, souvent abrégé en plt, est un module de Matplotlib qui fournit une interface de programmation similaire à celle de MATLAB pour créer des graphiques en utilisant des commandes simples.

## Présentation du code :
Le code est trouvable dans le fichier main.py et est commenté.

"""

km_estimator = """
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
"""
plot_hist = """
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
"""

descriptive_stats = """
# Calcul des statistiques descriptives sur la variable "time"
def descriptive_stats():
    stats = data['time'].describe()
    return stats
"""

load_data = """
# Lecture du fichier de données
def load_data():
    data = pd.read_csv("MockPatientDatabaseOscar.csv", sep=";", encoding='latin-1')
    return data


data = load_data()
"""


plot_km_curve = """
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
"""

plot_km_curve_by_sex = """
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
"""
