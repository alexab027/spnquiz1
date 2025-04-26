import streamlit as st
import random

# --- Define vocabulary ---
def get_vocab():
    return {
        "capitulo 7: de vacaciones": {
            "travel agency": "la agencia de viajes",
            "room": "la habitacion",
            "hotel": "el hotel",
            "ticket": "el boleto",
            "passport": "el pasaporte",
            "suitcase": "la maleta",
            "sailboat": "el velero"
        },
        "capitulo 7: viajar en avion": {
            "airline": "la aerolinea",
            "airport": "el aeropuerto",
            "airplane": "el avion",
            "security check": "el control de seguridad",
            "boarding pass": "la tarjeta de embarque",
            "window": "la ventanilla",
            "waiting room": "la sala de espera",
            "to board": "abordar",
            "to land": "aterrizar",
            "to take off": "despegar",
            "to check your luggage": "facturar el equipaje"
        },
        "capitulo 7: en el hotel": {
            "elevator": "el ascensor",
            "staircase": "la escalera",
            "ground floor": "la planta baja",
            "key": "la llave",
            "guest": "el huesped",
            "room": "la habitacion",
            "single room": "la habitacion sencilla",
            "double room": "la habitacion doble"
        },
        "capitulo 8: profesiones": {
            "lawyer": "el abogado",
            "actor": "el actor",
            "actress": "la actriz",
            "farmer": "el agricultor",
            "housewife": "el ama de casa",
            "firefighter": "el bombero",
            "singer": "el cantante",
            "counselor": "el consejero",
            "athlete": "el deportista",
            "businessman": "el hombre de negocios",
            "engineer": "el ingeniero",
            "teacher": "el maestro",
            "professor": "el profesor",
            "doctor": "el medico",
            "musician": "el musico",
            "construction worker": "el obrero de la construccion",
            "painter": "el pintor",
            "accountant": "el contador",
            "scientist": "el cientifico",
            "nurse": "el enfermero",
            "software designer": "el disenador de software"
        },
        "capitulo 9: comida": {
            "breakfast": "el desayuno",
            "lunch": "el almuerzo",
            "dinner": "la cena",
            "cereal": "el cereal",
            "toast": "el pan tostado",
            "fried eggs": "los huevos fritos",
            "hamburger": "la hamburguesa",
            "potatoes": "las papas",
            "french fries": "las papas fritas",
            "sandwich": "el sandwich",
            "soup": "la sopa",
            "bread": "el pan",
            "cheese": "el queso",
            "salad": "la ensalada",
            "lettuce": "la lechuga",
            "tomato": "el tomate",
            "vegetables": "las verduras",
            "rice": "el arroz",
            "steak": "el bistec",
            "shrimp": "el camaron",
            "fish": "el pescado",
            "chicken": "el pollo",
            "spaghetti": "los espaguetis",
            "ham": "el jamon",
            "fruit": "la fruta",
            "orange": "la naranja",
            "desserts": "los postres",
            "cake": "el pastel"
        },
        "capitulo 9: bebidas": {
            "orange juice": "el jugo de naranja",
            "milk": "la leche",
            "coffee": "el cafe",
            "tea": "el te",
            "wine": "el vino",
            "beer": "la cerveza",
            "soda": "el refresco",
            "water": "el agua",
            "carbonated water": "el agua con gas",
            "ice water": "el agua fria"
        },
        "capitulo 10: partes del cuerpo": {
            "head": "la cabeza",
            "face": "la cara",
            "hair": "el cabello / el pelo",
            "forehead": "la frente",
            "neck": "el cuello",
            "ear": "la oreja",
            "throat": "la garganta",
            "eye": "el ojo",
            "nose": "la nariz",
            "tongue": "la lengua",
            "mouth": "la boca",
            "lips": "los labios",
            "teeth": "los dientes",
            "back": "la espalda",
            "waist": "la cintura",
            "hip": "la cadera",
            "stomach": "el estomago",
            "arm": "el brazo",
            "shoulder": "el hombro",
            "chest": "el pecho",
            "elbow": "el codo",
            "wrist": "la muneca",
            "hands": "las manos",
            "fingers": "los dedos de la mano",
            "legs": "las piernas",
            "knee": "la rodilla",
            "foot": "el pie",
            "ankle": "el tobillo",
            "brain": "el cerebro",
            "bone": "el hueso",
            "lungs": "los pulmones",
            "heart": "el corazon",
            "muscles": "los musculos",
            "kidneys": "los rinones",
            "liver": "el higado",
            "blood": "la sangre"
        },
        "capitulo 10: problemas de salud": {
            "cold": "el resfriado",
            "fever": "la fiebre",
            "flu": "la gripe",
            "to sneeze": "estornudar",
            "cough": "la tos",
            "to twist an ankle": "torcerse el tobillo",
            "to fall": "caerse",
            "to break": "romperse"
        },
        "capitulo 10: pruebas medicas y medicamentos (no definite articles)": {
            "blood work": "analisis de sangre",
            "to take blood pressure": "tomar la presion",
            "to take temperature": "tomar la temperatura",
            "xrays": "rayos x",
            "mri": "resonancia magnetica",
            "ct scan": "TAC",
            "aspirin": "aspirina",
            "cough syrup": "jarabe para la tos",
            "pills": "pastillas",
            "injection": "inyeccion"
        },
        "capitulo 10: los especialistas (no definite article)": {
            "radiology": "radiologo",
            "cardiology": "cardiologo",
            "urology": "urologo",
            "dermatology": "dermatologo",
            "pediatrics": "pediatria",
            "dentistry": "dentista",
            "surgery": "cirujano"
        },
        "capitulo 11: entrevista de trabajo": {
            "interview": "la entrevista",
            "announcement": "el anuncio",
            "application": "la solicitud",
            "resume": "el curriculum",
            "call": "la llamada",
            "position": "el puesto",
            "company": "la compania",
            "salary": "el salario"
        }
    }

# --- Initialize session state ---
default_state = {
    "quiz_started": False,
    "vocab_items": [],
    "index": 0,
    "score": 0,
    "last_result": "",
    "input_submitted": False,
    "direction": "English to Spanish"
}

for key, value in default_state.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --- Title & Intro ---
st.title("📘 Spanish Vocabulary: SPN 1121")
st.markdown("""
**Welcome!**  
This is a study tool for all vocab in SPN 1121 class at SJR state.  

- 👉 *Do NOT include accent marks*  
- 👉 *Assume masculine forms for gendered words*
- 👉 *Keep in mind: some words have multiple definitions but the program only knows one*
""")

# --- Start screen ---
if not st.session_state.quiz_started:
    vocab = get_vocab()
    chapter = st.selectbox("Choose a chapter:", list(vocab.keys()))
    direction = st.radio("Choose direction:", ["English to Spanish", "Spanish to English"])
    num_terms = st.slider("How many terms do you want to practice?", 1, len(vocab[chapter]))

    if st.button("Start Quiz"):
        items = list(vocab[chapter].items())
        random.shuffle(items)
        st.session_state.vocab_items = items[:num_terms]
        st.session_state.direction = direction
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.last_result = ""
        st.session_state.input_submitted = False
        st.session_state.quiz_started = True
        st.rerun()

# --- Quiz Mode ---
else:
    vocab_items = st.session_state.vocab_items
    index = st.session_state.index
    total = len(vocab_items)
    direction = st.session_state.direction

    if index < total:
        en, sp = vocab_items[index]
        question = en if direction == "English to Spanish" else sp
        answer = sp if direction == "English to Spanish" else en

        st.write(f"Word {index + 1} of {total}")
        st.subheader(f"Translate: **{question}**")

        user_input = st.text_input("Your answer:", key=f"input_{index}")

        if user_input and not st.session_state.input_submitted:
            if user_input.strip().lower() == answer.lower():
                st.session_state.last_result = "✅ Correct!"
                st.session_state.score += 1
            else:
                st.session_state.last_result = f"❌ Wrong! The correct answer is: **{answer}**"
            st.session_state.input_submitted = True
            st.rerun()

        if st.session_state.input_submitted:
            st.info(st.session_state.last_result)
            if st.button("Next Word"):
                st.session_state.index += 1
                st.session_state.input_submitted = False
                st.rerun()

    else:
        st.success(f"🎉 Quiz complete! You scored {st.session_state.score} out of {total}")
        if st.button("Start over"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

