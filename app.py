import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Alphacoders",
    page_icon="🚀",
    layout="centered",
)

# Obtener la página desde la URL
pagina = st.query_params.get("page", "inicio")


def mostrar_inicio():
    st.title("🚀 Hola Mundo, soy Alphacoders")
    st.write(
        """
        Bienvenido a **Alphacoders**.
        Creamos soluciones de software, automatización e inteligencia artificial.
        """
    )
    st.divider()
    if st.button("🔒 Ver Política de Privacidad"):
        st.query_params["page"] = "privacidad"
        st.rerun()



def mostrar_privacidad():
    st.title("🔒 Política de Privacidad")

    st.caption(
        f"Última actualización: {date.today().strftime('%d-%m-%Y')}"
    )

    st.markdown("""
## 1. Introducción

Alphacoders reconoce la importancia de proteger la privacidad y los datos personales de sus usuarios, clientes y demás personas que interactúan con nuestros servicios.

La presente Política de Privacidad describe cómo Alphacoders puede recopilar, utilizar, almacenar y proteger la información personal.

## 2. Datos que podemos recopilar

Dependiendo del servicio utilizado, podremos recopilar:

- Nombre y apellidos.
- Dirección de correo electrónico.
- Número de teléfono.
- Información de empresas u organizaciones.
- Información proporcionada voluntariamente mediante formularios.
- Información técnica, como dirección IP, navegador y registros de acceso.

## 3. Finalidad del tratamiento

Los datos podrán ser utilizados para:

- Responder consultas.
- Prestar nuestros servicios.
- Gestionar relaciones comerciales.
- Proporcionar soporte técnico.
- Mejorar nuestros productos y plataformas.
- Cumplir obligaciones legales.
- Prevenir fraudes e incidentes de seguridad.

## 4. Protección de la información

Alphacoders implementará medidas técnicas y organizativas razonables para proteger la información contra accesos no autorizados, pérdida, modificación, divulgación o destrucción.

## 5. Compartición de datos

Alphacoders no venderá datos personales a terceros.

Podremos utilizar proveedores tecnológicos necesarios para operar nuestros servicios, incluyendo servicios de infraestructura, almacenamiento, comunicaciones, analítica o inteligencia artificial.

## 6. Conservación de los datos

La información será conservada únicamente durante el tiempo necesario para cumplir las finalidades para las cuales fue recopilada, salvo que exista una obligación legal o contractual que requiera conservarla por más tiempo.

## 7. Derechos de los usuarios

Los usuarios podrán solicitar, según corresponda:

- Acceso a sus datos.
- Rectificación de información incorrecta.
- Eliminación de sus datos.
- Información sobre el tratamiento realizado.
- Retiro del consentimiento cuando corresponda.

## 8. Uso de Inteligencia Artificial

Algunos servicios desarrollados por Alphacoders pueden utilizar tecnologías de inteligencia artificial.

Cuando estas tecnologías procesen información personal, procuraremos aplicar medidas de seguridad y minimizar el tratamiento de información que no sea necesaria para la prestación del servicio.

## 9. Modificaciones

Alphacoders podrá actualizar esta Política de Privacidad cuando existan cambios legales, tecnológicos u operativos.

La versión vigente estará disponible en este sitio.

## 10. Contacto

Para consultas relacionadas con privacidad y protección de datos, los usuarios podrán contactar a Alphacoders a través de nuestros canales oficiales.

---

**Última actualización:** {}
""".format(date.today().strftime('%d-%m-%Y')))

    st.divider()

    if st.button("🏠 Volver al inicio"):
        st.query_params.clear()
        st.rerun()


# Router
if pagina == "privacidad":
    mostrar_privacidad()
else:
    mostrar_inicio()
