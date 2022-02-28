"""
Trabajas para una startup en etapa inicial en Alemania. Su equipo ha estado trabajando en un rediseño de la página de
destino. El equipo cree que un nuevo diseño aumentará la cantidad de personas que hacen clic y se unen a su sitio.
Han estado probando los cambios durante algunas semanas y ahora quieren medir el impacto del cambio y necesitan que
usted determine si el aumento puede deberse a una probabilidad aleatoria o si es estadísticamente significativo.

Los datos

El equipo reunió el siguiente archivo:
Rediseñar datos de prueba

     "tratamiento" - "sí" si el usuario vio la nueva versión de la página de destino, no en caso contrario.
     "new_images" - "sí" si la página usó un nuevo conjunto de imágenes, no de lo contrario.
     "convertido": 1 si el usuario se unió al sitio, 0 en caso contrario.

El grupo de control son aquellos usuarios con "no" en ambas columnas: la versión antigua con el conjunto antiguo de imágenes.


Complete las siguientes tareas:

    Analice las tasas de conversión para cada uno de los cuatro grupos: el diseño nuevo/antiguo de la página de
    destino y las imágenes nuevas/antiguas.
    ¿Se pueden explicar los aumentos observados por aleatoriedad? (Sugerencia: Piense en la prueba A/B)
    ¿Qué versión del sitio web deberían usar?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('redesign.csv')
print(df.head())
print(df)

# Calculamos cual es el grupo de control: treatment='no and new_images=no
control_group=df[(df['treatment']=='no')& (df['new_images']=='no')]
print(control_group)

# Analizamos los usuarios en función del treatment
# Si vieron la nueva versión
us_nv=df[df['treatment']=='yes']
print(us_nv.groupby('converted')['treatment'].count())

# Si vieron la versión antigua
us_ov=df[df['treatment']=='no']
print(us_ov.groupby('converted')['treatment'].count())

# Si vieron nuevas imagenes
us_ni=df[df['new_images']=='yes']
print(us_ni.groupby('converted')['new_images'].count())

# Si no vieron nuevas imagenes
us_oi=df[df['new_images']=='no']
print(us_oi.groupby('converted')['new_images'].count())

# Mostramos en gráficos los datos
"""
sns.countplot(x='converted', data=df, hue='treatment')
plt.show()
sns.countplot(x='converted', data=df, hue='new_images')
plt.show()
"""
"""La tasa de conversión o CR, Conversion Rate por sus siglas en inglés, es el porcentaje de usuarios que realizan una
 acción específica ya sea realizar una compra, una descarga, un registro o una reserva. La tasa de conversión se 
 obtiene como resultado de dividir el número de objetivos conseguidos entre los usuarios únicos que visitan la web."""
# Calculamos el CR para los usuarios que vieron la nueva versión
CR_nv=(us_nv[us_nv['converted']==1]['converted'].count()/us_nv['treatment'].count())*100
print("El CR de usuarios que vieron la nueva versión es de: ")
print(CR_nv)
# Calculamos el CR para los usuarios que NO vieron la nueva versión
CR_ov=(us_ov[us_ov['converted']==1]['converted'].count()/us_ov['treatment'].count())*100
print("El CR de usuarios que NO vieron la nueva versión es de: ")
print(CR_ov)
# Calculamos el CR para los usuarios que vieron nuevas imagenes
CR_ni=(us_ni[us_ni['converted']==1]['converted'].count()/us_ni['treatment'].count())*100
print("El CR de usuarios que vieron la nueva versión es de: ")
print(CR_ni)
# Calculamos el CR para los usuarios que NO vieron nuevas imagenes
CR_oi=(us_oi[us_oi['converted']==1]['converted'].count()/us_oi['treatment'].count())*100
print("El CR de usuarios que vieron la nueva versión es de: ")
print(CR_oi)
