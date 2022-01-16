# Smart Pokedex

:point_right: [The website](https://share.streamlit.io/brice-vergnou/pokedex/name.py)
:point_right: [The article](https://medium.com/@brice.vergnou/how-to-easily-scrap-numerical-data-or-find-an-api-endpoint-3590d26ce4b3)

### Background

As an enthusiast of Pokemon Strategy, I spend a fair amount of time checking stats of Pokemons during a fight to quickly indentify what I could expect from my opponent. The only problem is that I'd have to jump between websites like [Smogon](https://www.smogon.com/dex/ss/formats/ou/) or [PikAnalytics](https://www.pikalytics.com/pokedex/gen8ou), and I wanted to make this process easier for me. 

### Features

The Pokedex is built with Streamlit that does a wonderful job at rendering data in a web browser. Thanks to [a video from Data Professor](https://www.youtube.com/watch?v=hoPvOIJvrb8), I could add a navigation bar to hop between the two pages of this app

#### Name-based

The [first page](https://share.streamlit.io/brice-vergnou/pokedex/name.py) is the most predictable : you give a name and the programs throws at you a bunch of information. 

![image](https://user-images.githubusercontent.com/86613710/149523546-4278abf4-8cd6-44f9-ae46-a452dfcc2b29.png)

The program still had to handle missing data from the API that would make the app crash, or the fact that some API endpoints just didn't exist ( probably because the Pokemon in a certain rank wasn't played enough ). Moreover, you can select which format you want to see the data for, which can be useful if you don't play in the most popular formats



#### Image-based

I couldn't make a Pokedex without adding some computer vision to recognize some Pokemons. I didn't do it for all pokemons ( there are like 800-900+ different species). Plus it was definitely harder as there was not Dataset for what I wanted, so I collected by hand pictures of the 50 most used Pokemons in OverUsed. But even there, I would have some problems : there is barely any picture so the number of images for each class would vary between 15 and 50 images.



Surprisingly enough, I managed to get 85% accuracy with a simple CNN structure ( anything more complex wouldn't have learned anything on such a small dataset ), which made me pretty satisfied.



I also discovered from [this video](https://www.youtube.com/watch?v=9GzfUzJeyi0) that you can actually take the features from a CNN and use it as a random forest feature. I hardly got any better result, but that's something I'll definitely keep in mind



### Conclusion

Nothing impressive, I just wanted to experiment with API's and AI as a newcomer to data science, and would rather learn it from hands-on project that would allow me to discover new things to learn
