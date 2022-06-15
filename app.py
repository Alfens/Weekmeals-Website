#Import Python Libraries
import streamlit as st
import pandas as pd
import numpy as np
from packages import *
import joblib
from sklearn.neighbors import KNeighborsRegressor



st.set_page_config(
    page_title="Weekmeals", # => Quick reference - Streamlit
    page_icon="🍽️",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed



st.markdown("""
    # Weekmeals 🍽️

    ## Plan your meals 🗓️  🥘
    ### Easy and customizable! 🤯
""")














st.markdown("""
    ## Select calories level
""")
st.markdown('''
               ### High calorie diet? 🍌🍳🍔
               ''')

st.markdown('''- Extremely active athletes
            - People who need to gain weight. 🚴‍♀️🏊🫃
            ''')

st.markdown('''
               ### Medium calorie diet? 🍗🍝
               ''')

st.markdown('''
                - Person with an average metabolism and activity level 🧍
                ''')

st.markdown('''
               ### Low calorie diet? 🥬🥗
               ''')

st.markdown('''
            - Low metabolism and activity level  🛏️
            - Willing to lose weight''')



calories = st.radio('Calories', ('High', 'Medium', 'Low'))



if calories == 'High':
    st.write('🔼')
    calories = 3
    df = pd.read_csv('data/predict_high2.csv')
    model_calories = joblib.load('models/km_optimo_h.sav')




elif calories == 'Medium':
    st.write('▶️')
    calories = 2
    df = pd.read_csv('data/predict_med2.csv')
    model_calories = joblib.load('models/km_optimomed.sav')





elif calories == 'Low':
    st.write('🔽')
    calories = 1
    df = pd.read_csv('data/predict_low2.csv')
    model_calories = joblib.load('models/km_optimolow.sav')















st.markdown("""
    # Customize your meal plan 💡
""")


st.markdown('''
               ### Put your preferences in a right way! 📝
               ''')
st.markdown('''
            - This sliding bars represent how much of the feature you want in your food! 📊
            - It is a relative value, so you can choose between 0 and 4.
            - The higher the value, the more you want the feature.
            ''')






st.markdown('''
               ## Minutes ⌛
                ''')
st.markdown('''
               ### Pros 👍
                ''')
st.markdown('''
            - More posibilities!
            ''')
st.markdown('''
               ### Cons 👎
               ''')
st.markdown('''
            - Less time you have for other things!
            ''')

a = st.slider('Select minutes', 0, 4, 0)







st.markdown('''
               ## Steps? 🦶
                ''')

st.markdown('''
            ### Pros 👍
            ''')
st.markdown('''
            - More posibilities!
            ''')

st.markdown('''
            ### Cons 👎
            ''')
st.markdown('''
            - More time spent on cooking.
            ''')
b = st.slider('Select number of steps', 0, 4, 0)


st.markdown('## Number of ingredients? 🍅🥚🍚🫐')
st.markdown('''
            ### Pros 👍
            - More diversity of nutrients.
            ''')

st.markdown('''
            ### Cons 👎
            - More time and space to save the ingredients.
            ''')
c = st.slider('Select n_ingredients', 0, 4, 0)



st.markdown('## Fat 🥑')
st.markdown('### Pros 👍')
st.markdown('''
            - Functions as an energy store
            - Cushion for vital organs and a transport system for fat-soluble vitamins.
            ''')
st.markdown('### Cons 👎 ')
st.markdown('- Fat is a concentrated source of calories, eating too much may lead to weight gain and obesity.')
d = st.slider('Select total fat (PDV)', 0, 4, 0)


st.markdown('## Sugar 🧁')
st.markdown('### Pros 👍')
st.markdown('''
            - Stimulates the pleasure centre in our brain 🚀
            - Gives us a dopamine rush and boosts our mood.
            ''')

st.markdown('### Cons 👎')
st.markdown('''
            - Higher blood pressure
            - Inflammation
            - Weight gain
            - Diabetes
            - Fatty liver disease
            ''')
e = st.slider('Select sugar (PDV)', 0, 4, 0)


st.markdown('## Sodium 🧂')

st.markdown('### Pros 👍')
st.markdown('''
            - Body needs a small amount of sodium to function.
            - Vital nutrient.
            - Good source of potassium, which is needed for the body to function properly.
            ''')
st.markdown('### Cons 👎')
st.markdown('''
            - Excess sodium makes your blood pressure too high, a condition called hypertension.
            ''')
f = st.slider('Select sodium', 0, 4, 0)


st.markdown('## Proteins 🥩')

st.markdown('### Pros 👍')
st.markdown('''
            - Important part of a healthy diet.
            - Build and repair muscles and bones.
            - Also be used as an energy source.''')
st.markdown('### Cons 👎')
st.markdown('''
            - Excess protein consumed is usually stored as fat.
            - Weight gain over time.
            ''')
g = st.slider('Select protein', 0, 4, 0)

st.markdown('## Saturated fat? 🥓')

st.markdown('### Pros 👍')
st.markdown('''
            - Provide energy.
            - Support the growth of your cells.
            - Help produce and regulate hormones.
            - Allow you to absorb nutrients.
            ''')
st.markdown('### Cons 👎')
st.markdown('''
            - Too much saturated fat can cause cholesterol to build up in your arteries
            ''')
h = st.slider('Select saturated fat', 0, 4, 0)


st.markdown('## Carbohidrates 🍝')

st.markdown('### Pros 👍')
st.markdown('''
            - Main source of energy.
            - Help fuel your brain, kidneys, heart muscles, and central nervous system.
            ''')
st.markdown('### Cons 👎')
st.markdown('''
            - Can cause high blood sugar and unwanted weight gain.
            ''')
i = st.slider('Select carbohidrates', 0, 4, 0)



st.markdown("""
    ## Lets check your preferences! 🍏🧀🍔🌯
""")
st.markdown("""
    ### What ingredients would you like to avoid?
""")

df = pd.read_csv('data/ss_data_full2.csv')

df2 = df.copy()
if st.checkbox('Gluten 🍞'):
    gluten = 1
    st.write('Gluten removed!')
else:
    gluten = 0

if st.checkbox('Nut 🥜'):
    nut = 1
    st.write('Nuts removed!')
else:
    nut = 0

if st.checkbox('Lactose 🥛'):
    lactose = 1
    st.write('Lactose removed!')
else:
    lactose = 0

if st.checkbox('Egg 🥚'):
    egg = 1
    st.write('Eggs removed!')
else:
    egg = 0


st.markdown("""
    ### Would you like to have a special diet? 👑
""")

if st.checkbox('Vegan 🍅🥬🥗'):
    vegan = 1
    st.write('Going vegan!')
else:
    vegan = 0



if st.checkbox('Veggie 🥚🍅🥛'):
    veggie = 1
    st.write('Going veggie!')
else:
    veggie = 0

if st.checkbox('Pescatarian 🐠'):
    fish = 1
    st.write('Going pescatarian!')
else:
    fish = 0



st.markdown("# Get custom dishes! 🍲")
if st.checkbox(f"""
    Custom dishes
"""):
    import time
    from io import StringIO
    tabla_user  = user_choice(calories, gluten, nut, lactose, egg, vegan, veggie, fish)
    tabla_user_completa = tabla_user.copy()
    @st.cache(hash_funcs={StringIO: StringIO.getvalue})
    def get_table():
        tabla_user2 = tabla_user_completa[['name','steps','ingredients']].sample(10)
        lista = [1,2,3,4,5,6,7,8,9,10]
        tabla_user2.insert(0, 'plate_number', lista)
        return tabla_user2
    st.write(get_table())
    if st.checkbox(f"""
        Select dishes 🤹‍♂️
    """):
        import time

        st.markdown("""
            ### Select your favourite meal!
        """)

        ideal_meal = st.radio('Select your favourite meal!', ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))


        if ideal_meal == '1':
            plato_elegido = 0

        elif ideal_meal == '2':
            plato_elegido = 1


        elif ideal_meal == '3':
            plato_elegido = 2


        elif ideal_meal == '4':
            plato_elegido = 3


        elif ideal_meal == '5':
            plato_elegido = 4


        elif ideal_meal == '6':
            plato_elegido = 5


        elif ideal_meal == '7':
            plato_elegido = 6


        elif ideal_meal == '8':
            plato_elegido = 7


        elif ideal_meal == '9':
            plato_elegido = 8


        elif ideal_meal == '10':
            plato_elegido = 9
        plato = pd.DataFrame(get_table().iloc[plato_elegido]).T
        st.write(plato)


        st.markdown("""
            ### Create your weekmeal plan! 🥘🍱
        """)

        if st.button('Create plan! 🚀'):

            plato_index = int(plato.index[0])

            plato_completo =  pd.DataFrame(tabla_user_completa.iloc[plato_index]).T


            X = tabla_user_completa.drop(columns=['name','steps','ingredients','gluten_free', 'nut_free', 'lactose_free', 'egg_free', 'vegan',
                'veggie', 'fish', 'low_calories', 'normal_calories', 'high_calories']) #Remove non numerical features
            y = tabla_user_completa['calories']

            knn_model = KNeighborsRegressor().fit(X, y) # Instanciate and train model

            ind_list = list(knn_model.kneighbors(plato_completo.drop(columns=['name','steps','ingredients','gluten_free', 'nut_free', 'lactose_free', 'egg_free', 'vegan',
        'veggie', 'fish', 'low_calories', 'normal_calories', 'high_calories']),n_neighbors=14)[1][0])

            recommendation = tabla_user_completa.iloc[ind_list, :].sort_values(by="calories")
            def inv_scaler(df, scaled):
                scaled['minutes'] = (scaled['minutes']*(df['minutes'].std())+ df['minutes'].mean()).round().astype(int)
                scaled['n_steps'] = (scaled['n_steps']*(df['n_steps'].std())+ df['n_steps'].mean()).round().astype(int)
                scaled['n_ingredients'] = (scaled['n_ingredients']*(df['n_ingredients'].std())+ df['n_ingredients'].mean()).round().astype(int)
                scaled['total fat (PDV)'] = (scaled['total fat (PDV)']*(df['total fat (PDV)'].std())+ df['total fat (PDV)'].mean()).round().astype(int)
                scaled['sugar (PDV)'] = (scaled['sugar (PDV)']*(df['sugar (PDV)'].std())+ df['sugar (PDV)'].mean()).round().astype(int)
                scaled['sodium (PDV)'] = (scaled['sodium (PDV)']*(df['sodium (PDV)'].std())+ df['sodium (PDV)'].mean()).round().astype(int)
                scaled['protein (PDV)'] = (scaled['protein (PDV)']*(df['protein (PDV)'].std())+ df['protein (PDV)'].mean()).round().astype(int)
                scaled['saturated fat (PDV)'] = (scaled['saturated fat (PDV)']*(df['saturated fat (PDV)'].std())+ df['saturated fat (PDV)'].mean()).round().astype(int)
                scaled['carbohydrates (PDV)'] = (scaled['carbohydrates (PDV)']*(df['carbohydrates (PDV)'].std())+ df['carbohydrates (PDV)'].mean()).round().astype(int)
                return scaled
            df = pd.read_csv('data/prep_data.csv')
            recommendation = inv_scaler(df, recommendation)
            lista_recomendation = ['Monday lunch', 'Monday dinner', 'Tuesday lunch', 'Tuesday dinner', 'Wednesday lunch', 'Wednesday dinner', 'Thursday lunch', 'Thursday dinner', 'Friday lunch', 'Friday dinner', 'Saturday lunch', 'Saturday dinner', 'Sunday lunch', 'Sunday dinner']
            recommendation.index = lista_recomendation
            st.write(recommendation)
            # st.write(recommendation)
