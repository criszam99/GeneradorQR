import streamlit as st
import qrcode
from io import BytesIO
import re

st.set_page_config(
    page_title="Generador de Código QR",
    page_icon="📱",
    layout="centered"
)

st.title("📱Generador de Código QR diseñado por Cristina Zamorano🍀")
st.write("Para crear códigos QR muy fácilmente.")
datos = st.text_area(
    "📥 Ingresá AQUÍ el enlace que querés convertir en QR 👇🏼👇🏼👇🏼",
    placeholder="Ejemplo: https://escuelaelnacional.com.ar/"
)

nombre_archivo = st.text_input(
    "📝 Dale un nombre a tu nuevo QR 👇🏼👇🏼👇🏼",
    placeholder="Ejemplo: qr_escuela"
)

color_qr = st.color_picker("Color del QR", "#000000")
color_fondo = st.color_picker("Color de fondo", "#FFFFFF")

tamano = st.slider(
    "Tamaño del QR",
    min_value=5,
    max_value=20,
    value=10
)

def limpiar_nombre_archivo(nombre):
    nombre = nombre.strip()
    nombre = re.sub(r'[\\/*?:"<>|]', "", nombre)
    nombre = nombre.replace(" ", "_")
    return nombre

def crear_qr(texto, color, fondo, box_size):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=4
    )

    qr.add_data(texto)
    qr.make(fit=True)

    imagen = qr.make_image(
        fill_color=color,
        back_color=fondo
    ).convert("RGB")

    buffer = BytesIO()
    imagen.save(buffer, format="PNG")
    buffer.seek(0)

    return imagen, buffer

if st.button("Generar QR"):
    if not datos.strip():
        st.warning("⚠️ Por favor, ingresá un texto o enlace.")
    elif not nombre_archivo.strip():
        st.warning("⚠️ Por favor, ingresá un nombre para el archivo.")
    else:
        nombre_limpio = limpiar_nombre_archivo(nombre_archivo)

        imagen_qr, buffer_qr = crear_qr(
            datos,
            color_qr,
            color_fondo,
            tamano
        )

        st.success("✅ Código QR generado correctamente.")

        st.image(
            imagen_qr,
            caption="Vista previa del código QR",
            width=280
        )

        st.download_button(
            label="📥 Descargar QR en PNG",
            data=buffer_qr,
            file_name=f"{nombre_limpio}.png",
            mime="image/png"
        )

st.markdown(
    """
    <h2 style='text-align: center; color: #2E8B57;'>
    🌞✨ ¡Que tengas un hermoso día! 😊📚
    </h2>

    unsafe_allow_html=True
)
