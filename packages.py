import pandas as pd
import numpy as np

def df_read(path = 'data/ss_data_full2.csv'):
    import pandas as pd
    df = pd.read_csv(path)
    return df.reset_index(drop=True)

# Predict ranking -------------------------------------------------------------------------------------------
def prediccion(a,b,c,d,e,f,g,h,i,predict_df, modelo):

    values = []
    values.append(predict_df.sort_values('minutes')['minutes'][a])
    values.append(predict_df.sort_values('n_steps')['n_steps'][b])
    values.append(predict_df.sort_values('n_ingredients')['n_ingredients'][c])
    values.append(predict_df.sort_values('total fat (PDV)')['total fat (PDV)'][d])
    values.append(predict_df.sort_values('sugar (PDV)')['sugar (PDV)'][e])
    values.append(predict_df.sort_values('sodium (PDV)')['sodium (PDV)'][f])
    values.append(predict_df.sort_values('protein (PDV)')['protein (PDV)'][g])
    values.append(predict_df.sort_values('saturated fat (PDV)')['saturated fat (PDV)'][h])
    values.append(predict_df.sort_values('carbohydrates (PDV)')['carbohydrates (PDV)'][i])
    pred = modelo.predict(np.array([values]))
    print(pred)

    return pred

def user_choice(calories, gluten, nut, lactose, egg, vegan, veggie, fish):
    df = pd.read_csv('data/ss_data_full2.csv')
    df2 = df.copy()
    if calories == 1:
        df2= df2[df2['low_calories'] == 1.0]
    elif calories == 2:
        df2= df2[df2['normal_calories'] == 1.0]
    elif calories == 3:
        df2= df2[df2['high_calories'] == 1.0]
    if gluten == 1:
        df2 = df2[df2['gluten_free'] == gluten]
    if nut == 1:
        df2 = df2[df2['nut_free'] == nut]
    if lactose == 1:
        df2 = df2[df2['lactose_free'] == lactose]
    if egg == 1:
        df2 = df2[df2['egg_free'] == egg]
    if vegan == 1:
        df2 = df2[df2['vegan'] == vegan]
    if veggie == 1:
        df2 = df2[df2['veggie'] == veggie]
    if fish == 1:
        df2 = df2[df2['fish'] == fish]
    return df2.reset_index(drop=True)
