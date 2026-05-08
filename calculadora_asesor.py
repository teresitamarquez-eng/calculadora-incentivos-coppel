import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Incentivos Coppel",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp { background-color: #F0F4FF; font-family: 'Segoe UI', sans-serif; }
div.block-container { padding-top: 0.5rem !important; padding-bottom: 1rem !important; }
[data-testid="stSidebar"] { display: none !important; }
button[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarCollapseButton"] { display: none !important; }
div[data-testid="stVerticalBlock"] > div { gap: 0.3rem !important; }

div[data-testid="stExpander"] summary p {
    font-size: 1.05em !important;
    font-weight: bold !important;
    color: #003DA5 !important;
}
div[data-testid="stExpander"] {
    border-left: 5px solid #003DA5 !important;
    border-radius: 12px !important;
    background: white !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
    margin-bottom: 8px !important;
}

.chip-verde    { background-color: #D4EDDA; color: #155724; border-radius: 20px; padding: 3px 10px; font-size: 0.82em; display: inline-block; margin: 2px 0; }
.chip-rojo     { background-color: #F8D7DA; color: #721C24; border-radius: 20px; padding: 3px 10px; font-size: 0.82em; display: inline-block; margin: 2px 0; }
.chip-amarillo { background-color: #FFF3CD; color: #856404; border-radius: 20px; padding: 3px 10px; font-size: 0.82em; display: inline-block; margin: 2px 0; }

.metrica-box { background: #E8F0FF; border-radius: 12px; padding: 8px 10px; text-align: center; margin: 4px 0; }
.metrica-valor { font-size: 1.3em; font-weight: bold; color: #003DA5; }
.metrica-etiqueta { font-size: 0.75em; color: #555; }

.resultado-card {
    background: linear-gradient(135deg, #003DA5, #0056D6);
    border-radius: 16px; padding: 20px; text-align: center;
    color: white; margin-top: 12px; box-shadow: 0 6px 20px rgba(0,61,165,0.4);
}
.resultado-total { font-size: 2.4em; font-weight: bold; color: #FFD100; }
.resultado-label { font-size: 0.95em; color: white; margin-bottom: 6px; }

.divider-azul { border: none; border-top: 1.5px solid #003DA5; opacity: 0.2; margin: 6px 0 8px 0; }

.stSelectbox > div > div {
    border: 2px solid #003DA5 !important;
    border-radius: 12px !important;
}

.stTextInput > div > div > input {
    border: 2px solid #003DA5 !important;
    border-radius: 10px !important;
    font-size: 1.05em !important;
    padding: 8px 12px !important;
}

#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def leer_porcentaje(label, placeholder, key):
    val = st.text_input(label, placeholder=placeholder, key=key)
    try:
        resultado = float(val.replace(",", ".")) if val else 0.0
        return max(0.0, min(200.0, resultado))
    except:
        st.markdown("<span class='chip-rojo'>⚠️ Ingresa un numero valido</span>", unsafe_allow_html=True)
        return 0.0

def leer_monto(label, placeholder, key):
    val = st.text_input(label, placeholder=placeholder, key=key)
    try:
        resultado = float(val.replace(",", "").replace("$", "")) if val else 0.0
        return max(0.0, resultado)
    except:
        st.markdown("<span class='chip-rojo'>⚠️ Ingresa un monto valido</span>", unsafe_allow_html=True)
        return 0.0

def chip(tipo, texto):
    st.markdown("<span class='chip-" + tipo + "'>" + texto + "</span>", unsafe_allow_html=True)

def metrica(etiqueta, valor):
    html = "<div class='metrica-box'><div class='metrica-etiqueta'>" + etiqueta + "</div><div class='metrica-valor'>" + valor + "</div></div>"
    st.markdown(html, unsafe_allow_html=True)

def resultado_final(total, desglose):
    html = "<div class='resultado-card'>"
    html += "<div class='resultado-label'>🏆 TU INCENTIVO TOTAL DEL MES</div>"
    html += "<div class='resultado-total'>$" + "{:,.2f}".format(total) + "</div>"
    html += "<br><div style='font-size:0.82em;color:#cce0ff;'>" + desglose + "</div>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def divider():
    st.markdown("<hr class='divider-azul'>", unsafe_allow_html=True)

def header_azul(titulo, subtitulo):
    if os.path.exists("logo_coppel.png"):
        with open("logo_coppel.png", "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
        st.markdown(
            "<div style='text-align:center;margin-bottom:0px;padding:6px 0px 0px 0px;'>"
            "<img src='data:image/png;base64," + logo_b64 + "' style='height:110px;'>"
            "</div>",
            unsafe_allow_html=True)
    html = "<div style='background:linear-gradient(135deg,#003DA5,#0056D6);"
    html += "padding:16px 20px;border-radius:16px;text-align:center;"
    html += "margin-bottom:12px;margin-top:4px;box-shadow:0 4px 12px rgba(0,61,165,0.3);'>"
    html += "<span style='font-size:1.4em;font-weight:bold;color:#FFD100;'>" + titulo + "</span><br>"
    html += "<span style='color:white;font-size:0.9em;'>" + subtitulo + "</span>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def incentivo_base_asesor(cump):
    if cump < 85:    return 0
    elif cump < 95:  return 700
    elif cump < 100: return 850
    elif cump < 110: return 1150
    elif cump < 120: return 1400
    else:            return 1750

def seccion_comisiones_asesor(cump_equipo, prefix):
    pct_s, pct_m = (0.04, 0.006) if cump_equipo >= 100 else (0.015, 0.004)
    if cump_equipo >= 100:
        chip("verde", "✅ Tasas Cump >= 100%: Seguros 4% | Marketplace 0.6%")
    else:
        chip("amarillo", "⚠️ Tasas Cump < 100%: Seguros 1.5% | Marketplace 0.4%")
    divider()
    st.markdown("**Seguros y Coppel Soluciones**")
    v_club  = leer_monto("🛡️ Seguros Club de Proteccion ($)",  "Ej: 5000", prefix+"_club")
    v_mrc   = leer_monto("🏍️ Seguros Motos RC ($)",            "Ej: 3000", prefix+"_mrc")
    v_mplus = leer_monto("🏍️ Seguros Motos PLUS ($)",          "Ej: 3000", prefix+"_mplus")
    v_cel   = leer_monto("📱 Seguros Celulares ($)",            "Ej: 2000", prefix+"_cel")
    v_gar   = leer_monto("🔧 Garantia Extendida ($)",           "Ej: 1500", prefix+"_gar")
    v_arm   = leer_monto("🔩 Servicio de Armado ($)",           "Ej: 800",  prefix+"_arm")
    v_inst  = leer_monto("🔌 Servicio de Instalacion ($)",      "Ej: 600",  prefix+"_inst")
    divider()
    st.markdown("**Marketplace y Campañas**")
    v_market = leer_monto("🛒 Venta Marketplace (3P) y Campañas ($)", "Ej: 10000", prefix+"_market")
    total_seguros  = (v_club + v_mrc + v_mplus + v_cel + v_gar + v_arm + v_inst) * pct_s
    total_market   = v_market * pct_m
    total_comision = total_seguros + total_market
    col1, col2, col3 = st.columns(3)
    with col1: metrica("🛡️ Seguros",    "$" + "{:,.2f}".format(total_seguros))
    with col2: metrica("🛒 Marketplace", "$" + "{:,.2f}".format(total_market))
    with col3: metrica("📊 Total",       "$" + "{:,.2f}".format(total_comision))
    return total_comision

header_azul("🏆 Incentivos Coppel", "Selecciona tu puesto para calcular tu incentivo")

puesto = st.selectbox("👤 ¿Cual es tu puesto?", options=[
    "🎯 Asesor de Ventas",
    "📱 Asesor Telefonia",
    "👁️ Optometrista",
    "⚙️ Operativos",
    "💰 Cajero Multifuncional",
    "👔 Gerente Titular",
])
divider()

def pantalla_asesor(titulo, prefix):
    header_azul("🏆 Calculadora de Incentivos", titulo + " — Coppel")
    with st.expander("🤝 Paso 1 — Venta de Equipo", expanded=True):
        cump_equipo = leer_porcentaje("% Cumplimiento meta del equipo", "Ej: 95.5", prefix+"_equipo")
        incentivo_base = incentivo_base_asesor(cump_equipo)
        if cump_equipo < 85:    chip("rojo",     "❌ < 85% — Sin incentivo base")
        elif cump_equipo < 100: chip("amarillo", "⚠️ Cumplimiento parcial")
        else:                   chip("verde",    "✅ Meta alcanzada")
        metrica("💰 Incentivo Base", "$" + "{:,.2f}".format(incentivo_base))
    with st.expander("✖️ Paso 2 — Multiplicadores", expanded=True):
        cump_credito = leer_porcentaje("% Cumplimiento Venta a Credito", "Ej: 96.0", prefix+"_credito")
        cump_digital = leer_porcentaje("% Cumplimiento Cliente Digital Avanzado", "Ej: 97.0", prefix+"_digital")
        multiplicador = 1.0
        if cump_credito >= 95:
            multiplicador += 0.20
            chip("verde", "✅ Venta a Credito >= 95% → +0.20")
        else:
            chip("rojo", "❌ Venta a Credito < 95% → +0.00")
        if cump_digital >= 95:
            multiplicador += 0.15
            chip("verde", "✅ Cliente Digital >= 95% → +0.15")
        else:
            chip("rojo", "❌ Cliente Digital < 95% → +0.00")
        incentivo_con_mult = incentivo_base * multiplicador
        col1, col2 = st.columns(2)
        with col1: metrica("✖️ Multiplicador",     "x" + "{:.2f}".format(multiplicador))
        with col2: metrica("💰 Con Multiplicador", "$" + "{:,.2f}".format(incentivo_con_mult))
    with st.expander("💼 Paso 3 — Comisiones por Tipo de Venta", expanded=True):
        total_comisiones = seccion_comisiones_asesor(cump_equipo, prefix)
    with st.expander("🏪 Paso 4 — Bono por Venta de Tienda", expanded=True):
        cump_tienda = leer_porcentaje("% Cumplimiento meta de la tienda", "Ej: 102.0", prefix+"_tienda")
        bono_tienda = 0.20 if cump_tienda >= 100 else 0.0
        if cump_tienda >= 100: chip("verde", "✅ Tienda >= 100% — Bono del 20%")
        else:                  chip("rojo",  "❌ Tienda < 100% — Sin bono")
    subtotal    = incentivo_con_mult + total_comisiones
    bono_extra  = subtotal * bono_tienda
    total_final = subtotal + bono_extra
    desglose  = "Base: $" + "{:,.2f}".format(incentivo_base)
    desglose += " | x" + "{:.2f}".format(multiplicador) + " = $" + "{:,.2f}".format(incentivo_con_mult)
    desglose += "<br>Comisiones: $" + "{:,.2f}".format(total_comisiones)
    desglose += " | Bono Tienda: $" + "{:,.2f}".format(bono_extra)
    resultado_final(total_final, desglose)

if   puesto == "🎯 Asesor de Ventas": pantalla_asesor("Asesor de Ventas", "av")
elif puesto == "📱 Asesor Telefonia": pantalla_asesor("Asesor Telefonia",  "at")
elif puesto == "👁️ Optometrista":     pantalla_asesor("Optometrista",      "opt")

elif puesto == "⚙️ Operativos":
    header_azul("🏆 Calculadora de Incentivos", "Operativos — Coppel")
    with st.expander("🏪 Paso 1 — Venta de Tienda", expanded=True):
        cump_tienda = leer_porcentaje("% Cumplimiento meta de la tienda", "Ej: 95.5", "ope_tienda")
        def incentivo_operativo(c):
            if c < 89:    return 0
            elif c < 95:  return 200
            elif c < 100: return 350
            elif c < 110: return 650
            else:         return 1000
        incentivo_base = incentivo_operativo(cump_tienda)
        if cump_tienda < 89:    chip("rojo",     "❌ < 89% — Sin incentivo base")
        elif cump_tienda < 100: chip("amarillo", "⚠️ Cumplimiento parcial")
        else:                   chip("verde",    "✅ Meta alcanzada")
        metrica("💰 Incentivo Base", "$" + "{:,.2f}".format(incentivo_base))
    with st.expander("💼 Paso 2 — Comisiones por Tipo de Venta", expanded=True):
        pct_s, pct_m = (0.04, 0.006) if cump_tienda >= 100 else (0.015, 0.004)
        if cump_tienda >= 100: chip("verde",    "✅ Tasas Cump >= 100%: 4% | Marketplace 0.6%")
        else:                  chip("amarillo", "⚠️ Tasas Cump < 100%: 1.5% | Marketplace 0.4%")
        divider()
        st.markdown("**Seguros y Coppel Soluciones**")
        v_club  = leer_monto("🛡️ Seguros Club de Proteccion ($)",  "Ej: 5000", "ope_club")
        v_mrc   = leer_monto("🏍️ Seguros Motos RC ($)",            "Ej: 3000", "ope_mrc")
        v_mplus = leer_monto("🏍️ Seguros Motos PLUS ($)",          "Ej: 3000", "ope_mplus")
        v_cel   = leer_monto("📱 Seguros Celulares ($)",            "Ej: 2000", "ope_cel")
        v_gar   = leer_monto("🔧 Garantia Extendida ($)",           "Ej: 1500", "ope_gar")
        v_arm   = leer_monto("🔩 Servicio de Armado ($)",           "Ej: 800",  "ope_arm")
        v_inst  = leer_monto("🔌 Servicio de Instalacion ($)",      "Ej: 600",  "ope_inst")
        divider()
        st.markdown("**Marketplace y Campañas**")
        v_market = leer_monto("🛒 Venta Marketplace (3P) y Campañas ($)", "Ej: 10000", "ope_market")
        total_seguros  = (v_club + v_mrc + v_mplus + v_cel + v_gar + v_arm + v_inst) * pct_s
        total_market   = v_market * pct_m
        total_comision = total_seguros + total_market
        col1, col2, col3 = st.columns(3)
        with col1: metrica("🛡️ Seguros",    "$" + "{:,.2f}".format(total_seguros))
        with col2: metrica("🛒 Marketplace", "$" + "{:,.2f}".format(total_market))
        with col3: metrica("📊 Total",       "$" + "{:,.2f}".format(total_comision))
    desglose = "Base: $" + "{:,.2f}".format(incentivo_base) + " | Comisiones: $" + "{:,.2f}".format(total_comision)
    resultado_final(incentivo_base + total_comision, desglose)

elif puesto == "💰 Cajero Multifuncional":
    header_azul("🏆 Calculadora de Incentivos", "Cajero Multifuncional — Coppel")
    with st.expander("💳 Paso 1 — Cobranza", expanded=True):
        cump_cobranza = leer_porcentaje("% Cumplimiento meta de cobranza", "Ej: 92.0", "caj_cobranza")
        def incentivo_cajero(c):
            if c < 89:    return 0
            elif c < 95:  return 200
            elif c < 100: return 350
            elif c < 110: return 650
            else:         return 1000
        incentivo_base = incentivo_cajero(cump_cobranza)
        if cump_cobranza < 89:    chip("rojo",     "❌ < 89% — Sin incentivo base")
        elif cump_cobranza < 100: chip("amarillo", "⚠️ Cumplimiento parcial")
        else:                     chip("verde",    "✅ Meta alcanzada")
        metrica("💰 Incentivo Base", "$" + "{:,.2f}".format(incentivo_base))
    with st.expander("✖️ Paso 2 — Multiplicadores", expanded=True):
        cump_credito      = leer_porcentaje("% Cumplimiento Venta a Credito",  "Ej: 65.0", "caj_credito")
        cump_venta_centro = leer_porcentaje("% Cumplimiento Venta del Centro", "Ej: 101.0", "caj_centro")
        multiplicador = 1.0
        if cump_credito >= 60:
            multiplicador += 0.15
            chip("verde", "✅ Venta a Credito >= 60% → +0.15")
        else:
            chip("rojo", "❌ Venta a Credito < 60% → +0.00")
        if cump_venta_centro >= 100:
            multiplicador += 0.15
            chip("verde", "✅ Venta Centro >= 100% → +0.15")
        else:
            chip("rojo", "❌ Venta Centro < 100% → +0.00")
        incentivo_con_mult = incentivo_base * multiplicador
        col1, col2 = st.columns(2)
        with col1: metrica("✖️ Multiplicador",     "x" + "{:.2f}".format(multiplicador))
        with col2: metrica("💰 Con Multiplicador", "$" + "{:,.2f}".format(incentivo_con_mult))
    with st.expander("💼 Paso 3 — Comisiones por Servicios", expanded=True):
        pct_s = 0.04 if cump_venta_centro >= 100 else 0.015
        if cump_venta_centro >= 100: chip("verde",    "✅ Tasas Cump >= 100%: 4%")
        else:                        chip("amarillo", "⚠️ Tasas Cump < 100%: 1.5%")
        divider()
        v_seguros  = leer_monto("🛡️ Seguros ($)",  "Ej: 5000", "caj_seguros")
        v_posventa = leer_monto("🔧 Posventa ($)", "Ej: 3000", "caj_posventa")
        total_comision = (v_seguros + v_posventa) * pct_s
        col1, col2 = st.columns(2)
        with col1: metrica("🛡️ Seguros",  "$" + "{:,.2f}".format(v_seguros  * pct_s))
        with col2: metrica("🔧 Posventa", "$" + "{:,.2f}".format(v_posventa * pct_s))
        metrica("📊 Total Comisiones", "$" + "{:,.2f}".format(total_comision))
    desglose  = "Base: $" + "{:,.2f}".format(incentivo_base)
    desglose += " | x" + "{:.2f}".format(multiplicador) + " = $" + "{:,.2f}".format(incentivo_con_mult)
    desglose += "<br>Comisiones: $" + "{:,.2f}".format(total_comision)
    resultado_final(incentivo_con_mult + total_comision, desglose)

elif puesto == "👔 Gerente Titular":
    header_azul("🏆 Calculadora de Incentivos", "Gerente Titular — Coppel")
    with st.expander("⚠️ Requisito — Cumplimiento Minimo de Tienda", expanded=True):
        cump_tienda = leer_porcentaje("% Cumplimiento meta de venta de la tienda", "Ej: 95.0", "ger_tienda")
        if cump_tienda < 89: chip("rojo",  "❌ < 89% — No se genera incentivo en ningun rubro")
        else:                chip("verde", "✅ Requisito minimo cumplido (>= 89%)")
    if cump_tienda >= 89:
        with st.expander("📊 Paso 1 — Productividad (Venta Tienda)", expanded=True):
            def incentivo_gerente(c):
                if c < 95:    return 0
                elif c < 100: return 2000
                elif c < 105: return 3000
                elif c < 110: return 4200
                else:         return 6000
            incentivo_base = incentivo_gerente(cump_tienda)
            if cump_tienda < 95:    chip("amarillo", "⚠️ < 95% — Sin incentivo de productividad")
            elif cump_tienda < 100: chip("amarillo", "⚠️ Cumplimiento parcial")
            else:                   chip("verde",    "✅ Meta alcanzada")
            metrica("💰 Incentivo Base", "$" + "{:,.2f}".format(incentivo_base))
        with st.expander("📋 Paso 2 — Evaluacion Objetiva", expanded=True):
            eval_obj = leer_porcentaje("% Resultado de Evaluacion Objetiva", "Ej: 97.0", "ger_eval")
            def mult_eval_fn(e):
                if e >= 98:   return 1.7
                elif e >= 96: return 1.5
                elif e >= 90: return 1.2
                else:         return 1.0
            mult_eval = mult_eval_fn(eval_obj)
            if mult_eval == 1.7:   chip("verde",    "✅ 98-100% → x1.70")
            elif mult_eval == 1.5: chip("verde",    "✅ 96-97%  → x1.50")
            elif mult_eval == 1.2: chip("amarillo", "⚠️ 90-95%  → x1.20")
            else:                  chip("rojo",     "❌ 0-89%   → x1.00")
            metrica("✖️ Multiplicador Evaluacion", "x" + "{:.2f}".format(mult_eval))
        with st.expander("📦 Paso 3 — Faltante de Tienda", expanded=True):
            pct_faltante = leer_porcentaje("% Faltante de tienda", "Ej: 0.8", "ger_faltante")
            def mult_falt_fn(f):
                if f < 1:      return 1.20
                elif f <= 1.5: return 1.10
                elif f <= 2:   return 1.00
                else:          return 0.80
            mult_falt = mult_falt_fn(pct_faltante)
            if mult_falt == 1.20:   chip("verde",    "✅ < 1%     → x1.20")
            elif mult_falt == 1.10: chip("verde",    "✅ 1%-1.5%  → x1.10")
            elif mult_falt == 1.00: chip("amarillo", "⚠️ 1.5%-2%  → x1.00")
            else:                   chip("rojo",     "❌ > 2%     → x0.80")
            metrica("✖️ Multiplicador Faltante", "x" + "{:.2f}".format(mult_falt))
        total_final = incentivo_base * mult_eval * mult_falt
        desglose  = "Base: $" + "{:,.2f}".format(incentivo_base)
        desglose += " | xEval " + "{:.2f}".format(mult_eval)
        desglose += " | xFaltante " + "{:.2f}".format(mult_falt)
        resultado_final(total_final, desglose)
    else:
        resultado_final(0, "Cumplimiento minimo no alcanzado (89%)")

st.markdown("<br>", unsafe_allow_html=True)
st.caption("Calculadora Interna Coppel - v1.0 - Solo para uso interno")
