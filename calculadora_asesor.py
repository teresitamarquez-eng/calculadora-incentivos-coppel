import streamlit as st

# ─────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Incentivos Coppel",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────
# CSS PERSONALIZADO — COLORES COPPEL + MÓVIL
# ─────────────────────────────────────────
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background-color: #F0F4FF;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Header principal */
    .header-coppel {
        background: linear-gradient(135deg, #003DA5, #0056D6);
        color: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,61,165,0.3);
    }
    .header-coppel h1 { font-size: 1.6em; margin: 0; color: #FFD100 !important; }
    .header-coppel p  { margin: 5px 0 0 0; font-size: 0.95em; color: white; }
    /* Tarjetas de sección */
    .seccion-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        border-left: 5px solid #003DA5;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .seccion-titulo { color: #003DA5; font-size: 1.1em; font-weight: bold; margin-bottom: 12px; }
    /* Tarjeta resultado final */
    .resultado-card {
        background: linear-gradient(135deg, #003DA5, #0056D6);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        color: white;
        margin-top: 20px;
        box-shadow: 0 6px 20px rgba(0,61,165,0.4);
    }
    .resultado-total { font-size: 2.5em; font-weight: bold; color: #FFD100; }
    .resultado-label { font-size: 1em; color: white; margin-bottom: 8px; }
    /* Chips de estado */
    .chip-verde  { background-color: #D4EDDA; color: #155724; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; display: inline-block; margin: 4px 0; }
    .chip-rojo   { background-color: #F8D7DA; color: #721C24; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; display: inline-block; margin: 4px 0; }
    .chip-amarillo { background-color: #FFF3CD; color: #856404; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; display: inline-block; margin: 4px 0; }
    /* Métricas */
    .metrica-box { background: #E8F0FF; border-radius: 12px; padding: 12px; text-align: center; margin: 8px 0; }
    .metrica-valor { font-size: 1.4em; font-weight: bold; color: #003DA5; }
    .metrica-etiqueta { font-size: 0.8em; color: #555; }
    /* Inputs más grandes para móvil */
    .stNumberInput input { font-size: 1.1em !important; padding: 10px !important; border-radius: 10px !important; }
    /* Ocultar menú Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ── HEADER ──────────────────────────────
st.markdown("""
    <div class="header-coppel">
        <h1>🏆 Calculadora de Incentivos</h1>
        <p>Asesor de Ventas — Coppel</p>
    </div>
""", unsafe_allow_html=True)

# ── SECCIÓN 1 — VENTA DE EQUIPO ─────────
st.markdown('<div class="seccion-card">', unsafe_allow_html=True)
st.markdown('<div class="seccion-titulo">📦 Venta de Equipo</div>', unsafe_allow_html=True)

cump_equipo = st.number_input("% Cumplimiento meta del equipo",
    min_value=0.0, max_value=200.0, step=0.01, format="%.2f")

def calcular_incentivo_base(cump):
    if cump < 85:    return 0
    elif cump < 95:  return 700
    elif cump < 100: return 850
    elif cump < 110: return 1150
    elif cump < 120: return 1400
    else:            return 1750

incentivo_base = calcular_incentivo_base(cump_equipo)

if cump_equipo < 85:
    st.markdown('<span class="chip-rojo">❌ < 85% — Sin incentivo base</span>', unsafe_allow_html=True)
elif cump_equipo < 100:
    st.markdown('<span class="chip-amarillo">⚠️ Cumplimiento parcial</span>', unsafe_allow_html=True)
else:
    st.markdown('<span class="chip-verde">✅ Meta alcanzada</span>', unsafe_allow_html=True)

st.markdown(f"""
    <div class="metrica-box">
        <div class="metrica-etiqueta">💰 Incentivo Base</div>
        <div class="metrica-valor">${incentivo_base:,.2f}</div>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── SECCIÓN 2 — MULTIPLICADORES ──────────
st.markdown('<div class="seccion-card">', unsafe_allow_html=True)
st.markdown('<div class="seccion-titulo">✖️ Multiplicadores</div>', unsafe_allow_html=True)

cump_credito = st.number_input("% Cumplimiento Venta a Crédito",
    min_value=0.0, max_value=200.0, step=0.01, format="%.2f")
cump_digital = st.number_input("% Cumplimiento Cliente Digital Avanzado",
    min_value=0.0, max_value=200.0, step=0.01, format="%.2f")

multiplicador = 1.0
if cump_credito >= 95:
    multiplicador += 0.20
    st.markdown('<span class="chip-verde">✅ Venta a Crédito ≥ 95% → +0.20</span>', unsafe_allow_html=True)
else:
    st.markdown('<span class="chip-rojo">❌ Venta a Crédito < 95% → +0.00</span>', unsafe_allow_html=True)

if cump_digital >= 95:
    multiplicador += 0.15
    st.markdown('<span class="chip-verde">✅ Cliente Digital ≥ 95% → +0.15</span>', unsafe_allow_html=True)
else:
    st.markdown('<span class="chip-rojo">❌ Cliente Digital < 95% → +0.00</span>', unsafe_allow_html=True)

incentivo_con_mult = incentivo_base * multiplicador
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="metrica-box"><div class="metrica-etiqueta">✖️ Multiplicador</div><div class="metrica-valor">×{multiplicador:.2f}</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metrica-box"><div class="metrica-etiqueta">💰 Con Multiplicador</div><div class="metrica-valor">${incentivo_con_mult:,.2f}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── SECCIÓN 3 — COMISIONES ───────────────
st.markdown('<div class="seccion-card">', unsafe_allow_html=True)
st.markdown('<div class="seccion-titulo">💼 Comisiones por Tipo de Venta</div>', unsafe_allow_html=True)

venta_seguros     = st.number_input("💊 Monto — Seguros y Coppel Soluciones ($)", min_value=0.0, step=100.0, format="%.2f")
venta_marketplace = st.number_input("🛒 Monto — Marketplace (3P) y Campañas ($)", min_value=0.0, step=100.0, format="%.2f")

if cump_equipo >= 100:
    pct_seguros, pct_marketplace = 0.04, 0.006
    st.markdown('<span class="chip-verde">✅ Tasas Cump ≥ 100%: Seguros 4% | Marketplace 0.6%</span>', unsafe_allow_html=True)
else:
    pct_seguros, pct_marketplace = 0.015, 0.004
    st.markdown('<span class="chip-amarillo">⚠️ Tasas Cump < 100%: Seguros 1.5% | Marketplace 0.4%</span>', unsafe_allow_html=True)

comision_seguros     = venta_seguros * pct_seguros
comision_marketplace = venta_marketplace * pct_marketplace
total_comisiones     = comision_seguros + comision_marketplace

col3, col4, col5 = st.columns(3)
with col3:
    st.markdown(f'<div class="metrica-box"><div class="metrica-etiqueta">💊 Seguros</div><div class="metrica-valor">${comision_seguros:,.2f}</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="metrica-box"><div class="metrica-etiqueta">🛒 Marketplace</div><div class="metrica-valor">${comision_marketplace:,.2f}</div></div>', unsafe_allow_html=True)
with col5:
    st.markdown(f'<div class="metrica-box"><div class="metrica-etiqueta">📊 Total</div><div class="metrica-valor">${total_comisiones:,.2f}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── SECCIÓN 4 — VENTA DE TIENDA ──────────
st.markdown('<div class="seccion-card">', unsafe_allow_html=True)
st.markdown('<div class="seccion-titulo">🏪 Bono por Venta de Tienda</div>', unsafe_allow_html=True)

cump_tienda = st.number_input("% Cumplimiento meta de la tienda",
    min_value=0.0, max_value=200.0, step=0.01, format="%.2f")

bono_tienda = 0.0
if cump_tienda >= 100:
    bono_tienda = 0.20
    st.markdown('<span class="chip-verde">✅ Tienda ≥ 100% — Bono adicional del 20%</span>', unsafe_allow_html=True)
else:
    st.markdown('<span class="chip-rojo">❌ Tienda < 100% — Sin bono adicional</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── RESULTADO FINAL ──────────────────────
subtotal    = incentivo_con_mult + total_comisiones
bono_extra  = subtotal * bono_tienda
total_final = subtotal + bono_extra

st.markdown(f"""
    <div class="resultado-card">
        <div class="resultado-label">🏆 TU INCENTIVO TOTAL DEL MES</div>
        <div class="resultado-total">${total_final:,.2f}</div>
        <br>
        <div style="font-size:0.85em; color:#cce0ff;">
            Base: ${incentivo_base:,.2f} &nbsp;|&nbsp; ×{multiplicador:.2f} = ${incentivo_con_mult:,.2f}<br>
            Comisiones: ${total_comisiones:,.2f} &nbsp;|&nbsp; Bono Tienda: ${bono_extra:,.2f}
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("Calculadora Interna Coppel • Asesor de Ventas v1.0 • Solo para uso interno")
