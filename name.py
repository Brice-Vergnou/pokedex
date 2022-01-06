import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import pandas as pd


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://github.com/Brice-Vergnou/pokedex" target="_blank">Smart Pokedex</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link disabled" href="https://share.streamlit.io/brice-vergnou/pokedex/image.py">Image-Based Pokedex<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#" >Name-Based Pokedex</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
st.header("Pokemon classifier Analytics")
st.write("\n\n\n\n\n\n\n\n")
st.write("\n:wave:    **Welcome, here you can quickly get some useful informations about a Pokemon for strategy, both in single or VGC. Just provide its name down below**")
st.write("\n\n\n\n\n\n\n")

with open("data_cleaned.json","r") as f:
    dex = json.load(f)

def main():
    pokemon = st.multiselect(
        'Pokemon :',
        dex)
    if pokemon != []:
        working_pokemon = pokemon[0].replace(' ','%20')
        option = st.sidebar.selectbox(
            'Which format are you interested in ?',
            tuple(dex[pokemon[0]]))
        if option == "OverUsed":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8ou-1825/"
        elif option == "VGC" :
            url ="https://www.pikalytics.com/api/p/2021-12/ss-1760/"
        elif option == "Monotype":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8monotype-1760/"
        elif option == "All":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8nationaldexag-1760/"
        elif option == "Ubers":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8ubers-1760/"
        elif option == "UnderUsed":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8uu-1760/"
        elif option == "RarelyUsed":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8ru-1760/"
        elif option == "NeverUsed":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8nu-1760/"
        elif option == "PU":
            url = "https://www.pikalytics.com/api/p/2021-12/gen8pu-1760/"
        get_info(working_pokemon, url)

# TODO : Handle errors
def get_info(pokemon, url):
    try:
        ##### GETTING DATA ######
        pokemon = pokemon.replace(" ", "%20")
        url = url + pokemon
        data = requests.get(url)
        data = data.text
        data = json.loads(data)
        ##### GENERAL DATA
        st.write("## General data")
        _, c1, br1, c2, br2, c3, _ = st.columns(7)
        with c1:
            st.write(f"**{data['percent']}% usage** \t\t")
        with br1:
            st.write("⚡")
        with c2:
            st.write(f"**#{data['ranking']} this month**")
        with br2:
            st.write("⚡")
        with c3:
            st.write(f"**Viability : {data['viability']}**")
        ##### TYPE #####
        st.write("## Types")
        types = data["types"]
        existing_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
                          "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock",
                          "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
        pokemon_types = []
        types_i = []
        for typ in types:
            pokemon_types.append(typ.capitalize())
        for typ in pokemon_types:
            types_i.append(existing_types.index(typ))
        chart = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
            [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
            [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],
            [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
            [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],
            [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
            [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],
            [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],
            [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],
            [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],
            [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],
            [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],
            [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],
            [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],
            [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],
            [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]
        ]
        badges = {
            "Fire": "https://img.shields.io/badge/Fire-FF0000",
            "Grass": "https://img.shields.io/badge/Grass-00FF00",
            "Water": "https://img.shields.io/badge/Water-0000FF",
            "Bug": "https://img.shields.io/badge/Bug-92BC2C",
            "Dark": "https://img.shields.io/badge/Dark-595761",
            "Dragon": "https://img.shields.io/badge/Dragon-0C69C8",
            "Electric": "https://img.shields.io/badge/Electric-F2D94E",
            "Fairy": "https://img.shields.io/badge/Fairy-EE90E6",
            "Fighting": "https://img.shields.io/badge/Fighting-D3425F",
            "Flying": "https://img.shields.io/badge/Flying-A1BBEC",
            "Ghost": "https://img.shields.io/badge/Ghost-5F6DBC",
            "Ground": "https://img.shields.io/badge/Ground-DA7C4D",
            "Ice": "https://img.shields.io/badge/Ice-75D0C1",
            "Normal": "https://img.shields.io/badge/Normal-A0A29F",
            "Poison": "https://img.shields.io/badge/Poison-B763CF",
            "Psychic": "https://img.shields.io/badge/Psychic-FA8581",
            "Rock": "https://img.shields.io/badge/Rock-C9BB8A",
            "Steel": "https://img.shields.io/badge/Steel-5695A3"
        }
        _, c1, mid, c2, _ = st.columns(5)
        if len(pokemon_types) == 1:
            with mid:
                st.write(f"![{pokemon_types[0]}]({badges[pokemon_types[0]]})")
        else:
            with c1:
                st.write(f"![{pokemon_types[0]}]({badges[pokemon_types[0]]})")
            with c2:
                st.write(f"![{pokemon_types[1]}]({badges[pokemon_types[1]]})")
        with st.expander("Weaknesses"):
            st.write("*Doesn't take into account any special ability like levitate or item like Air Balloon*")
            immune = []
            super_weak = []
            weak = []
            res = []
            super_res = []
            for i, typ in enumerate(existing_types):
                status = 1
                for pokemon_tp in types_i:
                    status *= chart[i][pokemon_tp]
                if status == 0:
                    immune.append(typ)
                elif status == 0.25:
                    super_res.append(typ)
                elif status == 0.5:
                    res.append(typ)
                elif status == 2:
                    weak.append(typ)
                elif status == 4:
                    super_weak.append(typ)
            col1, col2, col3 = st.columns(3)
            if immune != []:
                with col1:
                    st.write("### Immune")
                    for typ in immune:
                        st.write(f"![{typ}]({badges[typ]})")
            with col2:
                if super_weak != []:
                    st.write("### Double Weakness")
                    for typ in super_weak:
                        st.write(f"![{typ}]({badges[typ]})")
                if weak != []:
                    st.write("### Weakness")
                    for typ in weak:
                        st.write(f"![{typ}]({badges[typ]})")
            with col3:
                if super_res != []:
                    st.write("### Double Resistance")
                    for typ in super_res:
                        st.write(f"![{typ}]({badges[typ]})")
                if res != []:
                    st.write("### Resistance")
                    for typ in res:
                        st.write(f"![{typ}]({badges[typ]})")
        ##### STATS #####
        st.write("## Stats")
        stats = data["stats"]
        stats = {
            "HP": stats["hp"],
            "Attack": stats["atk"],
            "Spe. Attack": stats["spa"],
            "Defense": stats["def"],
            "Spe. Defense": stats["spd"],
            "Speed": stats["spe"]
        }
        figure = plt.figure()
        y = list(stats.keys())
        width = list(stats.values())
        x_pos = np.arange(len(y))[::-1]
        colors = []
        for stat in width:
            if stat < 60:
                colors.append("red")
            elif 60 <= stat < 75:
                colors.append("orange")
            elif 75 <= stat < 90:
                colors.append("#FAD215")
            elif 90 <= stat < 110:
                colors.append("yellow")
            elif 110 <= stat < 125:
                colors.append("#90EE90")
            elif 125 <= stat < 140:
                colors.append("green")
            else:
                colors.append("cyan")
        plt.barh(x_pos, width, color=colors)
        plt.axis("off")
        plt.style.use('dark_background')
        c1, c2 = st.columns(2)
        with c1:
            for i in range(6):
                st.write(f"\n**{y[i]}** : {width[i]}\n")
        with c2:
            st.pyplot(figure)
        ##### ABILITY #####
        st.write("## Abilities")
        abilities = data["abilities"]
        abilities_name = [x["ability"] for x in abilities]
        abilities_per = [f'{float(x["percent"]):.1f}  %' for x in abilities]
        df_abilities = pd.DataFrame([abilities_per],columns=abilities_name)
        st.write(df_abilities)
        ##### CAPACITIES #####
        st.write("## Moves")
        moves = data["moves"]
        move_name = [x["move"] for x in moves]
        move_per = [f'{float(x["percent"]):.1f}  %' for x in moves]
        df_moves = pd.DataFrame([move_per], columns=move_name)
        st.write(df_moves)
        ##### ITEMS #####
        st.write("## Items")
        items = data["items"]
        item_name = [x["item"] for x in items]
        item_per = [f'{float(x["percent"]):.1f}  %' for x in items]
        df_items = pd.DataFrame([item_per], columns=item_name)
        st.write(df_items)
        ##### TEAM #####
        st.write("## Most Common Teammates")
        teams = data["team"]
        team_name = [x["pokemon"] for x in teams]
        team_per = [f'{float(x["percent"]):.1f}  %' for x in teams]
        df_teams = pd.DataFrame([team_per], columns=team_name)
        st.write(df_teams)
        ##### SPREADS #####
        st.write("## Most Common Spreads")
        spreads = data["spreads"]
        spread_name = [x["nature"] + "   " + x["ev"] for x in spreads[:3]]
        spread_per = [f'{float(x["percent"]):.1f}  %' for x in spreads[:3]]
        df_spreads = pd.DataFrame([spread_per], columns=spread_name)
        st.write(df_spreads)
        ##### CREDITS #####
        st.write("### Credits")
        st.write(f"All the informations have been scrapped from \
                [Pikalitics](https://www.pikalytics.com/pokedex/ss/{pokemon}). You can also find more \
                informations about known sets or check/counters on [Smogon](https://www.smogon.com/dex/ss/pokemon/{pokemon}).")
    except json.JSONDecodeError:
        st.write("#### We don't have data for that Pokemon.😞")
        st.write(" It may be because it doesn't belong to the selected category, or because we're lacking data as it is too rarely used.")
    except :
        st.write("#### Something unexpected happened 😞")
        st.write("Please contact me on Twitter ([@Brice__fr](https://twitter.com/Brice__fr)) so I can fix this bug")

if __name__ == "__main__":
    main()
