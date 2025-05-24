import streamlit as st
import pandas as pd


# 📌 Configurar la página con título y diseño amplio
st.set_page_config(page_title="Asesoramiento y Análisis Gastronómico - Tugasa", layout="wide")

# 📌 Configurar la barra lateral con opciones visibles
menu = st.sidebar.radio(
    "📌 Navegación",
    ["🏡 Introducción - Posicionamiento Gastronómico",
     "📊 Análisis de Datos - Optimización y Rentabilidad",
     "👨‍🍳 David Méndez Sánchez - Trayectoria"]
)

# 📌 Página 1: Introducción
if menu == "🏡 Introducción - Posicionamiento Gastronómico":
    # 📌 Mostrar el logo corporativo (corregido con use_container_width)
    st.image("logo_tugasa_portada.jpg", use_container_width=True)
    
    # 📌 Título y presentación estratégica
    st.title("🌿 Posicionamiento Gastronómico de los Restaurantes Tugasa")

    st.markdown("""
    ### 🎯 **Introducción al Proyecto**
    Los restaurantes del grupo **Tugasa** forman parte del **patrimonio gastronómico de la Sierra de Cádiz**.  
    Sin embargo, para **potenciar su posicionamiento y diferenciación**, es necesario **crear estrategias** que optimicen la oferta culinaria, alineándola con los valores de cada restaurante.

    Este análisis tiene **tres objetivos fundamentales**:  
    ✅ **Darle personalidad a cada restaurante**, para que no sean percibidos como una cadena homogénea.  
    ✅ **Apostar por la conexión con el entorno**, potenciando el uso de productos locales y recetas que representen la esencia de la Sierra de Cádiz.  
    ✅ **Posicionar los restaurantes de Tugasa como referentes en la gastronomía gaditana**, haciendo que cada establecimiento tenga una **propuesta gastronómica única** y atractiva.

    ---
    ### 🚀 **Estrategia de Posicionamiento**
    📍 **Cada restaurante debe tener un toque único**  
    📍 **Adaptar la oferta al entorno**  
    📍 **Convertir Tugasa en un referente gastronómico**  

    🔎 **¿Qué sigue?**  
    En la **próxima sección**, analizaremos los datos obtenidos sobre precios, optimización del menú y escandallos, con gráficos potentes para la toma de decisiones.  
    """)

    st.success("¡Listos para analizar los datos y definir estrategias de posicionamiento!")

# 📌 Página 2: Análisis de Datos - Optimización y Rentabilidad
elif menu == "📊 Análisis de Datos - Optimización y Rentabilidad":
    # 📌 Cargar datos
    df = pd.read_csv("Cartas1.csv", encoding="latin1")

    st.title("📊 Optimización Gastronómica en Tugasa")

    st.markdown("""
    ### 📌 **Objetivo del análisis**
    Este estudio busca **optimizar la oferta gastronómica de los restaurantes Tugasa**,  
    mediante un análisis en profundidad de precios, tendencias de platos y costes de escandallo.

    **¿Qué estamos evaluando?**  
    ✅ **Variabilidad de precios** entre los restaurantes.  
    ✅ **Platos más recurrentes** en la carta y su impacto en la oferta.  
    ✅ **Escandallo vs. precio de venta**, buscando mejoras en rentabilidad.  
    """)

    # 📌 Métrica general: Estadísticas básicas sobre los precios
    st.subheader("📌 Datos Generales sobre los Precios")
    st.table(df["Precio"].describe().to_frame())

    st.markdown("""
    📌 **Observaciones:**  
    - La mayoría de los platos están en un rango entre **10€ y 24€**, con algunas excepciones de platos de mayor coste.  
    - La dispersión de precios indica que hay **una variabilidad notable entre restaurantes**, lo que podría impactar la percepción del cliente.  
    """)

    # 📌 Comparación de precios por restaurante en tabla
    st.subheader("💰 Comparación de precios entre restaurantes")
    precio_medio_por_restaurante = df.groupby("Restaurante")["Precio"].mean().reset_index()
    st.table(precio_medio_por_restaurante)

    st.markdown("""
    📌 **Observaciones:**  
    - Algunos restaurantes tienen precios significativamente más altos que otros, lo que **puede impactar la percepción de valor y accesibilidad**.  
    - **¿Oportunidad?** Revisar los precios promedio y ajustar estrategias de marketing para posicionar la oferta.  
    """)

    # 📌 Platos más repetidos en tabla
    st.subheader("🍽️ Platos más repetidos en los restaurantes")
    platos_repetidos = df["Plato"].value_counts().reset_index()
    platos_repetidos.columns = ["Plato", "Repeticiones"]
    st.table(platos_repetidos.head(10))

    st.markdown("""
    📌 **Conclusiones sobre los platos más repetidos:**  
    - **El Secreto Ibérico a la Plancha, la Tarta de Queso con Miel y la Tarta Tres Chocolates están en todos los restaurantes**,  
      lo que los posiciona como platos estrella dentro de la oferta de Tugasa.  
    - **La paella en sus distintas variantes también es un plato recurrente**, lo que refuerza la identidad mediterránea de la gastronomía.  
    """)

    # 📌 KPI: Margen de rentabilidad estimado en tabla
    df["Margen"] = df["Precio"] - df["Precio"] * 0.4  # Simulación de escandallo
    margen_promedio = df["Margen"].mean()
    
    st.subheader("📈 Margen de Rentabilidad Estimado")
    st.table(pd.DataFrame({"Margen Promedio por Plato (€)": [round(margen_promedio, 2)]}))

    st.markdown("""
    📌 **¿Es rentable la oferta actual?**  
    - Un margen promedio de **X€** indica que hay margen de optimización, pero es crucial analizar la relación entre calidad, precio y percepción del cliente.  
    - **Opciones de mejora:**  
      ✔ Diseñar una oferta más equilibrada entre platos de bajo y alto coste.  
      ✔ Crear packs o menús degustación para potenciar el valor percibido sin afectar márgenes.  
    """)

    st.success("Este análisis nos permite **ajustar la oferta gastronómica y mejorar la rentabilidad de los restaurantes de Tugasa**.")


# 📌 Página 3: David Méndez Sánchez - Trayectoria y Reconocimientos
elif menu == "👨‍🍳 David Méndez Sánchez - Trayectoria":
   # 📌 Mostrar imagen del chef
    st.image("https://drive.google.com/uc?id=1yaP2fKHfckZiWGvkfLnICbi-euSgmzCa", use_container_width=True)

    
    # 📌 Título con personalidad
    st.title("👨‍🍳 Hola, soy David Méndez Sánchez… y aquí vengo a hablar de lo mío")

    st.markdown("""
    ### 🏆 **¿Quién soy y qué hago aquí?**
    Pues bien, me llamo **David Méndez Sánchez** y, aunque en casa dijeron que estudiara algo con "futuro",  
    yo me metí en la cocina y aquí sigo.  

    No soy chef de televisión ni me paso el día en redes explicando cómo hacer una salsa en 30 segundos.  
    **Soy cocinero. De los que guisan. De los que han aprendido a cocinar con las manos, con el fuego y con las horas**.  

    Me gusta llamarlo **cocina de entrevientos**, porque crecí entre la Sierra y la Bahía,  
    entre la contundencia de la tierra y la frescura del Atlántico. Y mi cocina es justo eso: un punto de encuentro.  

    ---
    ### 🍽️ **Mi cocina: sin tonterías, con identidad**
    📌 Aquí no hay cocina de laboratorio.  
    📌 Aquí no hay platos de moda.  
    📌 Aquí hay **producto bueno**, **técnica**, **historia**, y sobre todo, ganas de que la gente disfrute.  

    Para mí la cocina es **oficio y artesanía**. Se trata de saber tratar un buen pescado, de respetar una buena carne,  
    de darles el punto justo para que sean memorables sin hacer malabares en el plato.  

    ---
    ### 🏅 **Reconocimientos y cosas de esas**  
    No voy a decir que los premios no importan, porque oye, si te reconocen el trabajo, se agradece.  

    - **Bib Gourmand Michelin** (dos años seguidos, así que parece que no ha sido suerte).  
    - **Premio Gurmé a la cocina creativa** (esto suena muy elegante, pero la verdad es que me dieron el premio por hacer lo que me gusta).  
    - **Restaurante seleccionado en la Guía Repsol**.  
    - **Reconocimientos en la Guías de Andalucía** (que no es poco).

    Pero si me preguntas, lo que más me importa es que **mis clientes salgan contentos, que vuelvan,  
    que un plato les recuerde a su infancia o a aquel viaje en el que comieron algo inolvidable**.  

    ---
    ### 🔥 **Mi filosofía**
    _"La cocina no es sólo recetas, es historia, es emoción, es algo que nos representa.  
    No cocino para que me aplaudan, cocino porque es lo que sé hacer y porque me gusta ver a la gente disfrutar.  
    Hay que comer con calma, con alegría y sin postureo. Para comer bien, lo mejor sigue siendo sentarse a la mesa con hambre y ganas."_

    ---
    ### 🚀 **¿Y ahora qué?**
    Pues aquí estoy, asesorando a Tugasa, porque quiero que **cada uno de sus restaurantes tenga personalidad propia**,  
    que no sean sólo "sitios donde se come bien", sino que tengan **alma, carácter y una oferta pensada para el entorno**.  

    📌 **Optimizar el menú, mejorar la rentabilidad y conseguir que la gente quiera volver**.  
    📌 **Hacer de cada restaurante un referente gastronómico dentro de la Sierra de Cádiz**.  

    Vamos a hacerlo bien. Sin cuentos. Con producto, técnica y sentido común.  

    Así que, dicho esto…  
    **¿Nos ponemos a trabajar o seguimos con el discurso? 😄**  
    """)

    st.success("Si has leído hasta aquí, es porque te interesa hacer algo grande. ¡Vamos a por ello!")
